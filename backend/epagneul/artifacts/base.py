# -*- coding: utf-8 -*-
import pathlib
from abc import ABC, abstractmethod
from typing import Iterator


class BaseArtifact(ABC):
    """Base Artifact class.
    This class should be used to create file based forensic artifacts.

    Params:
        scope (str): Artifacts are groupped together using a scope.
                     Unique values are unique whithin the scope

    Attributes:
        name (str): Each artifact is represented by a unique (human readable) name
    """

    def __init__(self, scope: str = ""):
        self._scope = scope

    @property
    def scope(self) -> str:
        """Artifact's scope."""
        return self._scope

    @property
    @abstractmethod
    def name(self) -> str:
        """Artifact human readable name."""

    '''
    @abstractmethod
    def is_valid(self, filepath: pathlib.PosixPath) -> bool:
        """Checks whether or not a given filepath is a valid artifact.

        This is usefull for automatic mapping between files and artifacts.
        You may check for file signatures or magic codes.
        """
    '''
    @abstractmethod
    def parse(self, filepath: pathlib.PosixPath):
        """Parses an artifact from a given filepath.

        It should not be necessary to check if the given file is a valid artifact.
        """
