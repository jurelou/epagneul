from neo4j import GraphDatabase
from epagneul.common import settings
from datetime import datetime

from uuid import uuid4
from epagneul.models.folders import Folder, FolderInDB
from epagneul.models.files import File
from epagneul.models.graph import Edge, Node, EdgeData, NodeData


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


class DataBase:
    def __init__(self):
        self._driver = GraphDatabase.driver(settings.neo4j.endpoint, auth=(settings.neo4j.username, settings.neo4j.password))

    def bootstrap(self):
        print("bootstrap db")
        """
        with self._driver.session() as session:
            session.run("CREATE CONSTRAINT machine_id ON (n:Machine) ASSERT n.identifier IS UNIQUE")
            session.run("CREATE CONSTRAINT user_id ON (n:User) ASSERT n.identifier IS UNIQUE")
        """

    def close(self):
        self._driver.close()
        print("close db")

    def rm(self):
        with self._driver.session() as session:
            session.run("MATCH (n) " "DETACH DELETE n")

    def get_graph(self, folder: str):
        nodes = {}
        edges = []


        def  _get_or_add_node(node):
            if node["identifier"] in nodes:
                return nodes[node["identifier"]].data.id

            new_node = Node(data=NodeData(**node, id=node["identifier"]))
            new_node.data.width = 10 + (len(new_node.data.label) * 11)

            compound_id = f"compound-{node['algo_lpa']}"
            if compound_id not in nodes:
                nodes[compound_id] = Node(data=NodeData(id=compound_id, category="compound", bg_color="grey", bg_opacity=0.33))
            new_node.data.parent = compound_id
            nodes[node["identifier"]] = new_node

            return new_node.data.id

        with self._driver.session() as session:
            res = session.run(
                "MATCH (source {folder: $folder})-[rel:LogonEvent]->(target {folder: $folder}) "
                "return source, PROPERTIES(rel) as rel, target",
                folder=folder
            )
            for item in res:
                source_id = _get_or_add_node(item["source"])
                target_id = _get_or_add_node(item["target"])
                rel = item["rel"]
                rel["source"] = source_id
                rel["target"] = target_id
                edges.append(Edge(data=EdgeData(**rel, id=uuid4().hex)))

        return list(nodes.values()), edges
        
    def create_folder(self, folder: Folder):
        with self._driver.session() as session:
            session.run(
                "CREATE (folder: Folder) SET folder += $data",
                data=folder.dict()
            )

    def get_folders(self):
        with self._driver.session() as session:
            result = session.run("MATCH (folder: Folder) return folder")
            return [ Folder(**folder["folder"]) for folder in result.data()]

    def get_folder(self, folder_id):
        with self._driver.session() as session:
            folder = session.run(
                "MATCH (folder: Folder {identifier: $folder_identifier}) return folder",
                folder_identifier=folder_id
            )
            files = session.run(
                "MATCH (file: File)-[r]->(folder: Folder {identifier: $folder_identifier}) return collect(file)",
                folder_identifier=folder_id
            )
            folder_data = folder.single()
            if not folder_data:
                print(f"FOLDER NOT FOUND {folder_id}")
                return None

            files_documents = []
            start_time = end_time = None
            for f in files.single().data()["collect(file)"]:
                file_document = File(**f)
                if not start_time or file_document.start_time < start_time:
                    start_time = file_document.start_time
                if not end_time or file_document.end_time > end_time:
                    end_time = file_document.end_time
                files_documents.append(file_document)

            return FolderInDB(
                **folder_data.data()["folder"],
                start_time=start_time,
                end_time=end_time,
                files=files_documents
            )

    def remove_folder(self, folder_id):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (folder: Folder {identifier: $identifier}) DETACH DELETE folder",
                identifier=folder_id
            )
            return result

    def add_folder_file(self, folder_id, file: File):
        with self._driver.session() as session:
            session.run(
                "MATCH (folder: Folder {identifier: $folder_identifier}) "
                "CREATE (file: File) "
                "SET file += $data "
                "CREATE (file)-[:DEPENDS]->(folder) ",
                data=file.dict(),
                folder_identifier=folder_id
            )

    def add_evtx_store(self, store, folder: str):
        print("ADD STORE NOW")
        timeline, detectn, cfdetect = store.get_change_finder()

        users = [
            {
                "identifier": f"user-{u.identifier}",
                "label": u.username,
                "tip": f"id: {u.identifier}<br>Username: {u.username}<br>SID: {u.sid}<br>Role: {u.role}<br>Domain: {u.domain}",
                "border_color": "#e76f51" if u.is_admin else "#e9c46a",
                "bg_opacity": 0.0,
                "shape": "ellipse",
                "category": "user",
                "timeline": timeline[i],
                "algo_change_finder": cfdetect[u.identifier],
            } for i, u in enumerate(store.users.values())    
        ]
        
        machines = [{
            "identifier": f"machine-{m.identifier}",
            "label": m.hostname or m.ip,
            "tip": f"id: {m.identifier}<br>Hostname: {m.hostname}<br>IP: {m.ip}",
            "border_color": "#2a9d8f",
            "bg_opacity": 0.0,
            "shape": "rectangle",
            "category": "machine"
        } for m in store.machines.values() ]

        events = [{
            "source": f"user-{e.source}",
            "target": f"machine-{e.target}",
            "label": e.event_id,
            "logon_type": e.logon_type,
            "timestamps": [datetime.timestamp(ts) for ts in e.timestamps],
            #"tip": f"Event ID: {e.event_id}<br>Logon type: {e.logon_type}<br>Logon status: {e.status}<br>Timestamp: {e.timestamp}",
        } for e in store.logon_events.values() ]

        print("DONE FMT")
        with self._driver.session() as session:
            print("Adding users")
            session.run(
                "UNWIND $users as row "
                "MERGE (user: User {folder: $folder, identifier: row.identifier}) "
                "ON CREATE SET user += row ",
                users=users,
                folder=folder,
            )
            print("Adding machines")
            session.run(
                "UNWIND $machines as row "
                "MERGE (machine: Machine {folder: $folder, identifier: row.identifier}) "
                "ON CREATE SET machine += row",
                machines=machines,
                folder=folder,
            )
            print("Adding events")
            for chunk in chunker(events, 10000):
                session.run(
                    "UNWIND $events as row "
                    "MATCH (user: User {identifier: row.source, folder: $folder}), (machine: Machine {identifier: row.target, folder: $folder}) "
                    "CREATE (user)-[rel: LogonEvent]->(machine) "
                    "SET rel += row",
                    events=chunk,
                    folder=folder,
                )
            print("done")

    def make_lpa(self, folder: str):
        with self._driver.session() as session:
            query = f"""CALL gds.labelPropagation.write({{
                    nodeQuery: 'MATCH (u {{ folder: "{folder}" }}) RETURN id(u) AS id',
                    relationshipQuery: 'MATCH (n: User {{ folder: "{folder}" }})-[r: LogonEvent]-(m: Machine {{ folder: "{folder}" }}) RETURN id(n) AS source, id(m) AS target, type(r) as type',
                    writeProperty: 'algo_lpa'
                }})
            """
            r = session.run(query)
    
    def make_pagerank(self, folder: str):
        with self._driver.session() as session:
            query = f"""CALL gds.pageRank.write({{
                    nodeQuery: 'MATCH (u {{ folder: "{folder}" }}) RETURN id(u) AS id',
                    relationshipQuery: 'MATCH (n: User {{ folder: "{folder}" }})-[r: LogonEvent]-(m: Machine {{ folder: "{folder}" }}) RETURN id(n) AS source, id(m) AS target, type(r) as type',
                    dampingFactor: 0.85,
                    writeProperty: 'algo_pagerank'
                }})
            """
            r = session.run(query)
db = DataBase()

def get_database():
    return db