import datetime
import re
from typing import Any

import numpy as np
from epagneul.core.changefinder import ChangeFinder
from epagneul.core.store import Datastore
from evtx import PyEvtxParser
from loguru import logger
from lxml import etree
from pydantic import BaseModel

from epagneul.core.evtx_events.basic_logon_events import parse_basic_logons
from epagneul.core.evtx_events.event_3 import parse_3
from epagneul.core.evtx_events.event_4648 import parse_4648
from epagneul.core.evtx_events.event_4672 import parse_4672
from epagneul.core.evtx_events import group_events


class Event(BaseModel):
    event_id: int
    timestamp: datetime.datetime
    data: Any


supported_events = {
    3: parse_3,
    4648: parse_4648,
    4624: parse_basic_logons,
    4625: parse_basic_logons,
    4672: parse_4672,
    4768: parse_basic_logons,
    4769: parse_basic_logons,
    4771: parse_basic_logons,
    4776: parse_basic_logons,

    4728: group_events.parse_add_group,
    4732: group_events.parse_add_group,
    4756: group_events.parse_add_group,

    #5140: test,
    #4729: test,
    #4733: test,
    #4757: test,
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


def parse_evtx(file_data):
    logger.info(f"Parsing evtx file: {file_data}")
    evtx = PyEvtxParser(file_data)

    store = Datastore()

    for r in evtx.records():
        data = r["data"]
        if not re.search(USEFULL_EVENTS_STR, data):
            continue

        event = get_event_from_xml(data)
        store.add_timestamp(event.timestamp)

        if event.event_id in supported_events:
            supported_events[event.event_id](store, event)

    return store


def adetection(counts, users, starttime, tohours):
    count_array = np.zeros((6, len(users), tohours + 1))
    count_all_array = []
    result_array = []
    cfdetect = {}
    for _, event in counts.iterrows():
        column = int(
            (
                datetime.datetime.strptime(event["dates"], "%Y-%m-%d  %H:%M:%S")
                - starttime
            ).total_seconds()
            / 3600
        )
        row = users.index(event["username"])
        # count_array[row, column, 0] = count_array[row, column, 0] + count
        if event["eventid"] == 4624:
            count_array[0, row, column] = event["count"]
        elif event["eventid"] == 4625:
            count_array[1, row, column] = event["count"]
        elif event["eventid"] == 4768:
            count_array[2, row, column] = event["count"]
        elif event["eventid"] == 4769:
            count_array[3, row, column] = event["count"]
        elif event["eventid"] == 4776:
            count_array[4, row, column] = event["count"]
        elif event["eventid"] == 4648:
            count_array[5, row, column] = event["count"]
    count_sum = np.sum(count_array, axis=0)
    count_average = count_sum.mean(axis=0)
    num = 0
    for udata in count_sum:
        cf = ChangeFinder(r=0.04, order=1, smooth=6)
        ret = []
        for i in count_average:
            cf.update(i)

        for i in udata:
            score = cf.update(i)
            ret.append(round(score[1], 2))
        result_array.append(ret)

        cfdetect[users[num]] = max(ret)

        count_all_array.append(udata.tolist())
        for var in range(0, 6):
            con = []
            for i in range(0, tohours + 1):
                con.append(count_array[var, num, i])
            count_all_array.append(con)
        num += 1

    return count_all_array, result_array, cfdetect


if __name__ == "__main__":
    from epagneul.api.core.neo4j import get_database

    db = get_database()
    db.bootstrap()
    db.rm()
    # store = parse_evtx("/data/files/")
    # store.finalize()

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
