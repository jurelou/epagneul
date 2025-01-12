import datetime
import re
from typing import Any
import json
from epagneul.core.store import Datastore
from evtx import PyEvtxParser
from loguru import logger
from lxml import etree
from pydantic import BaseModel


from epagneul.core.evtx_events import basic_logon_events
from epagneul.core.evtx_events.event_3 import parse_3
from epagneul.core.evtx_events.event_4648 import parse_4648
from epagneul.core.evtx_events.event_4672 import parse_4672
from epagneul.core.evtx_events.event_4768 import parse_4768
from epagneul.core.evtx_events import group_events


class Event(BaseModel):
    event_id: int
    timestamp: datetime.datetime
    data: Any


supported_events = {
    3: parse_3,
    4648: parse_4648,
    4624: basic_logon_events.parse_logon_successfull,
    4625: basic_logon_events.parse_logon_failed,
    4672: parse_4672,

    4768: parse_4768,
    4769: basic_logon_events.parse_tgs,
    4771: basic_logon_events.parse_tgt_failed,

    4776: basic_logon_events.parse_ntlm_request,

    4728: group_events.parse_add_group,
    4732: group_events.parse_add_group,
    4756: group_events.parse_add_group,

    # 5140: test,
    # 4729: test,
    # 4733: test,
    # 4757: test,
}


USEFULL_EVENTS_STR = re.compile(
    f'<EventID>({"|".join([str(i) for i in supported_events.keys()])})<', re.MULTILINE
)


def to_lxml(record_xml):
    rep_xml = record_xml.replace(
        'xmlns="http://schemas.microsoft.com/win/2004/08/events/event"', ""
    )
    fin_xml = rep_xml.encode("utf-8")
    parser = etree.XMLParser(resolve_entities=False)
    return etree.fromstring(fin_xml, parser)


def convert_logtime(logtime, tzone=1):
    tzless = re.sub("[^0-9-:\s]", " ", logtime.split(".")[0]).strip()
    try:
        return datetime.datetime.strptime(
            tzless, "%Y-%m-%d %H:%M:%S"
        ) + datetime.timedelta(hours=tzone)
    except:
        return datetime.datetime.strptime(
            tzless, "%Y-%m-%dT%H:%M:%S"
        ) + datetime.timedelta(hours=tzone)


def get_event_from_xml(raw_xml_event):
    xml_event = to_lxml(raw_xml_event)
    return Event(
        event_id=int(xml_event.xpath("/Event/System/EventID")[0].text),
        # computer_name=xml_event.xpath("/Event/System/Computer")[0].text,
        timestamp=convert_logtime(
            xml_event.xpath("/Event/System/TimeCreated")[0].get("SystemTime")
        ),
        data=xml_event.xpath("/Event/EventData/Data"),
    )


def parse_evtx_jsonl(file_data):
    """
    Parses a .jsonl file containing EVTX data and processes it into a Datastore.

    Args:
        file_data: A file-like object containing JSONL data.

    Returns:
        Datastore: The processed datastore object.
    """
    logger.info(f"Parsing JSONL file: {file_data}")
    store = Datastore()

    try:
        # Iterate over the file data
        for line in file_data if isinstance(file_data, list) else file_data.readlines():
            line = line.strip()  # Ensure no trailing newline or spaces
            if not line:  # Skip empty lines
                continue

            try:
                # Parse the JSON line
                event_json = json.loads(line)

                # Safely extract EventID
                event_id = int(event_json.get("Event", {})
                                        .get("System", {})
                                        .get("EventID", 0))

                # Safely extract SystemTime
                system_time = (event_json.get("Event", {})
                                        .get("System", {})
                                        .get("TimeCreated", {})
                                        .get("#attributes", {})
                                        .get("SystemTime", None))
                timestamp = convert_logtime(system_time)

                # Extract EventData
                event_data = event_json.get("Event", {}).get("EventData")

                if event_id in supported_events:
                    
                    # Create the event and process it
                    event = Event(event_id=event_id, timestamp=timestamp, data=event_data)
                    store.add_timestamp(event.timestamp)
                    supported_events[event_id](store, event)

            except json.JSONDecodeError as json_err:
                logger.error(f"JSON decode error in line: {line}. Error: {json_err}")
            except Exception as e:
                logger.error(f"Error parsing line: {line}. Error: {e}")

    except Exception as e:
        logger.critical(f"Failed to process file data. Error: {e}")

    return store
    
    
def parse_evtx(file_data):
    logger.info(f"Parsing EVTX JSON file: {file_data}")
    evtx = PyEvtxParser(file_data)

    store = Datastore()

    try:
        # Process each record in JSON format
        for record_json in evtx.records_json():
            try:
                # Convert the string in record_json["data"] to a Python dictionary
                parsed_data = json.loads(record_json["data"])
                # Safely parse the JSON data
                event_id = int(
                    parsed_data.get("Event", {})
                    .get("System", {})
                    .get("EventID", 0)
                )
                # Safely extract SystemTime
                system_time = (
                    parsed_data.get("Event", {})
                                .get("System", {})
                                .get("TimeCreated", {})
                                .get("#attributes", {})
                                .get("SystemTime", None)
                )
                timestamp = convert_logtime(system_time)
                # Extract EventData
                event_data = parsed_data.get("Event", {}).get("EventData")
                # Process supported events
                if event_id in supported_events:
                    event = Event(event_id=event_id, timestamp=timestamp, data=event_data)
                    store.add_timestamp(event.timestamp)
                    supported_events[event_id](store, event)

            except json.JSONDecodeError as json_err:
                logger.error(f"JSON decode error in record: {parsed_data}. Error: {json_err}")
            except Exception as e:
                logger.error(f"Error processing record: {parsed_data}. Error: {e}")

    except Exception as e:
        logger.critical(f"Failed to process EVTX JSON data. Error: {e}")

    return store


if __name__ == "__main__":
    from epagneul.core.neo4j import get_database

    db = get_database()
    db.bootstrap()
    db.rm()
    store = parse_evtx("/data/filtered.evtx")
    store.finalize()

    print(store.users)

    """
    #a, b, c = store.get_change_finder()
    #start_day = datetime.datetime(*store.start_time.timetuple()[:3]).strftime("%Y-%m-%d")
    start_day = datetime.datetime.strptime("2021-12-09", "%Y-%m-%d") #temp
    learn_hmm(ml_frame, users, start_day)
    predictions = predict_hmm(ml_frame, users, start_day)
    print(predictions)
    db.add_evtx_store(store, folder="a")

    db.make_lpa("a")
    db.make_pagerank("a")
    """


"""
def predict_hmm(frame, users, start_day):
    detections = []
    model = joblib.load("multinomial_hmm.pkl")

    while True:
        start_day_str = start_day.strftime("%Y-%m-%d")
        for user in users:
            hosts = np.unique(frame[(frame["user"] == user)].host.values)
            for host in hosts:
                udata = []

                for _, data in frame[(frame["date"].str.contains(start_day_str)) & (frame["user"] == user) & (frame["host"] == host)].iterrows():
                    id = data["id"]
                    if id == 4776:
                        udata.append(0)
                    elif id == 4768:
                        udata.append(1)
                    elif id == 4769:
                        udata.append(2)
                    elif id == 4624:
                        udata.append(3)
                    elif id == 4625:
                        udata.append(4)
                    elif id == 4648:
                        udata.append(5)

                if len(udata) > 2:
                    data_decode = model.predict(np.array([np.array(udata)], dtype="int").T)
                    unique_data = np.unique(data_decode)
                    if unique_data.shape[0] == 2:
                        if user not in detections:
                            detections.append(user)


        start_day += datetime.timedelta(days=1)
        if frame.loc[(frame["date"].str.contains(start_day_str))].empty:
            break
    return detections


def learn_hmm(frame, users, start_day):
    lengths = []
    data_array = np.array([])
    emission_probability = np.array([[0.09,   0.05,   0.35,   0.51],
                                     [0.0003, 0.0004, 0.0003, 0.999],
                                     [0.0003, 0.0004, 0.0003, 0.999]])

    while True:
        start_day_str = start_day.strftime("%Y-%m-%d")
        for user in users:
            hosts = np.unique(frame[(frame["user"] == user)].host.values)
            for host in hosts:
                udata = np.array([])
                for _, data in frame[(frame["date"].str.contains(start_day_str)) & (frame["user"] == user) & (frame["host"] == host)].iterrows():
                    udata = np.append(udata, data["id"])

                if udata.shape[0] > 2:
                    data_array = np.append(data_array, udata)
                    lengths.append(udata.shape[0])
        start_day += datetime.timedelta(days=1)
        if frame.loc[(frame["date"].str.contains(start_day_str))].empty:
            break

    data_array[data_array == 4776] = 0
    data_array[data_array == 4768] = 1
    data_array[data_array == 4769] = 2
    data_array[data_array == 4624] = 3
    data_array[data_array == 4625] = 4
    data_array[data_array == 4648] = 5

    model = hmm.MultinomialHMM(n_components=3, n_iter=10000)
    #model.emissionprob_ = emission_probability
    model.fit(np.array([data_array], dtype="int").T, lengths)
    joblib.dump(model, "./multinomial_hmm.pkl")
"""
