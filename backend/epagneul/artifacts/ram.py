# -*- coding: utf-8 -*-
import pathlib

import ujson
from loguru import logger

from epagneul.common import docker, settings, exceptions
from epagneul.artifacts.base import BaseArtifact
from epagneul.models.observables import Process


class RamArtifact(BaseArtifact):
    name = "Raw RAM (Random-access memory)"

    _profile: str

    def is_valid(self, filepath: pathlib.PosixPath) -> bool:
        input_file = f"/tmp/{filepath.name}"
        try:
            stdout = docker.run_container(
                image=settings.tools.rekall.docker_image,
                command=["-f", input_file, "imageinfo"],
                volumes={filepath.absolute(): {"bind": input_file, "mode": "ro"}},
            )
        except exceptions.BaseDockerError as err:
            logger.debug(
                f"File {input_file} is not a valid RAM artifact: docker_error {err}",
            )
            return False
        if not stdout:
            logger.debug(f"File {input_file} is not a valid RAM artifact: empty result")
            return False
        is_valid = all(
            s in stdout
            for s in ["Kernel DTB", "NT Build Ex", "NtSystemRoot", "Signed Drivers"]
        )
        if is_valid:
            logger.info(f"File {input_file} is a valid RAM artifact")
        else:
            logger.debug(
                f"File {input_file} is not a valid RAM artifact: insufficient infos",
            )
        return is_valid

    # @staticmethod
    # def _run_pstree(filepath: pathlib.PosixPath) -> str:
    #     input_file = f"/tmp/{filepath.name}"
    #     return docker.run_container(
    #         image=settings.tools.volatility261.docker_image,
    #         command=[
    #             "-f",
    #             input_file,
    #             "pslist"
    #         ],
    #         volumes={
    #             filepath.absolute(): {"bind": input_file, "mode": "ro"}
    #         },
    #     )

    # @staticmethod
    # def _run_handles(filepath: pathlib.PosixPath, pid: str) -> str:
    #     input_file = f"/tmp/{filepath.name}"
    #     command = f"-f {input_file} handles -p 1676 -t Process"
    #     return docker.run_container(
    #         image=settings.tools.rekall.docker_image,
    #         command=command,
    #         volumes={
    #             filepath.absolute(): {"bind": input_file, "mode": "ro"}
    #         },
    #     )

    def parse(self, filepath: pathlib.PosixPath) -> bool:
        """Parses processes from RAM using rekall

        Relationships:
            * Process -> CREATE -> Process
        """
        logger.debug(f"Parsing ram {filepath}")
        # stdout = self._run_pstree(filepath)
        # Read output line by line, skipping header
        # Header:
        # _EPROCESS name pid ppid thread_count handle_count session_id wow64 process_create_time process_exit_time
        # depth = 1
        # for out in stdout.splitlines()[2:]:
        #     row = out.split()
        #     line_depth = len(row[0])
        #     handles = self._run_handles(filepath, pid=int(row[2]))
