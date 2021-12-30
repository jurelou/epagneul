# -*- coding: utf-8 -*-
class EpagneulException(Exception):
    """Base Epagneul exceptions class."""


########################################
# Docker related exceptions
########################################
class BaseDockerError(EpagneulException):
    """Base errors for docker API."""

    def __init__(self, image):
        self.image = image


class DockerImageNotFound(BaseDockerError):
    """Docker image not found."""

    def __str__(self):
        return f"Docker image {self.image} not found"


class DockerContainerRuntimeError(BaseDockerError):
    """Docker container runtime error."""

    def __str__(self):
        return f"Docker container {self.image} runtime error"


########################################
# Machine related exceptions
########################################
# class BaseMachineError(EpagneulException):
#     """Base errors for machine related exceptions."""

#     def __init__(self, machine):
#         self.machine = machine

# class MachineAlreadyExists(BaseMachineError):
#     """Duplicate machine found."""

#     def __str__(self):
#         return f"Machine {self.machine} already exists"

# class MachineNotFound(BaseMachineError):
#     """Machine not found."""

#     def __str__(self):
#         return f"Machine {self.machine} does not exists"

########################################
# Evidence related exceptions
########################################


class BaseEvidenceError(EpagneulException):
    """Base errors for evidence related exceptions."""

    def __init__(self, evidence):
        self.evidence = evidence


class UnsupportedEvidenceType(BaseEvidenceError):
    """Evidence type is invalid or not supported."""

    def __str__(self):
        return f"Evidence type for {self.evidence} is invalid or not supported"
