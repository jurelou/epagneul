# -*- coding: utf-8 -*-
from typing import Optional
from pathlib import Path, PosixPath

from loguru import logger

from epagneul.common import exceptions
from epagneul.artifacts import ALL_ARTIFACTS

ARTIFACTS = {artifact.name: artifact() for artifact in ALL_ARTIFACTS}


def get_artifact_type(filepath: PosixPath) -> Optional[str]:
    logger.info(f"Get artifact type for {filepath}")
    filepath = filepath
    if not filepath.is_file():
        return None
    for artifact_name, artifact in ARTIFACTS.items():
        if artifact.is_valid(filepath):
            return artifact_name
    return None


# def add_machine(machine: Machine):
#     logger.info(f"Add machine {machine.name}")
#     if arango.get("machines", machine.name):
#         logger.debug(f"Machine {machine.name} already exists")
#         raise exceptions.MachineAlreadyExists(machine.name)
#     machine_data = machine.dict()
#     machine_data["_key"] = machine.name
#     return arango.insert("machines", machine_data)

# def add_observable(o: BaseObservable):
#     logger.info(f"Add observable {o.model_name}")
#     observable_key = o.unique_key()
#     observable_data = o.dict(exclude={"type"})
#     modified, inserted_document = arango.upsert(collection=o.model_name(),key=observable_key, document=observable_data)
#     if modified:
#         history_collection = f"{o.model_name()}_history"
#         inserted_document.pop("detection_key", None)
#         old_id = inserted_document.pop("_id")
#         old_key = inserted_document.pop("_key")

#         if arango.exists(history_collection, inserted_document):
#             logger.info(f"Observable {old_id} : {old_key} is already in history")
#             return old_id
#         inserted_document["_source_key"] = old_key
#         logger.info(f"Add observable {old_id} to history")
#         arango.insert(history_collection, inserted_document)
#         return old_id
#     return inserted_document["_id"]

# def collect_artifact(artifact_type, file_path):
#     logger.info(f"Collect artifact ({artifact_type}) {file_path}")
#     file_path = Path(file_path)
#     relations = ARTIFACTS[artifact_type].parse(file_path)
#     if not relations:
#         logger.warning(f"Artifact {file_path} does not contains any relationships")
#         return
#     for relation in relations:
#         # Store all observables


#         relation.source.detection_key = relation.key
#         source = add_observable(relation.source)

#         relation.target.detection_key = relation.key
#         target = add_observable(relation.target)

#         # Store the relationship
#         attributes = relation.dict(exclude={"target", "source", "type"})
#         attributes["type"] = relation.type.name
#         arango.insert_edge("observables",
#             edge={
#                 '_from': source,
#                 '_to': target,
#                 **attributes
#             })


# def add_evidence(evidence: Evidence):
#     logger.info(f"Add evidence {evidence.file_path} for machine {evidence.machine.name}")
#     if not arango.get("machines", evidence.machine.name):
#         raise exceptions.MachineNotFound(evidence.machine.name)
#     artifact_type = get_artifact_type(evidence.file_path)
#     if not artifact_type:
#         raise exceptions.UnsupportedEvidenceType(evidence.file_path)

#     collect_artifact(artifact_type, evidence.file_path)
#     arango.insert("evidences", evidence.dict())


def analyze_artifact(file_path: PosixPath, artifact_type: Optional[str] = None):
    if not artifact_type:
        artifact_type = get_artifact_type(file_path)

    if not artifact_type:
        raise exceptions.UnsupportedEvidenceType(file_path.name)

    file_path = file_path
    logger.info(f"Collect artifact ({artifact_type}) {file_path}")
    relations = ARTIFACTS[artifact_type].parse(file_path)
    if not relations:
        logger.warning(f"Artifact {file_path} does not contains any relationships")
        return []

    return relations
