# -*- coding: utf-8 -*-
import docker

from epagneul.common import exceptions

_CLIENT = docker.from_env()


def run_container(
    image: str,
    detach=False,
    remove=True,
    *args,
    **kwargs,
):
    """Run a docker container.

    TODO: Bufferize stdout / stderr
    """
    try:
        res = _CLIENT.containers.run(
            image,
            detach=detach,
            auto_remove=True,
            *args,
            **kwargs,
        )
    except docker.errors.ImageNotFound as err:
        raise exceptions.DockerImageNotFound(image) from err
    except docker.errors.ContainerError as err:
        raise exceptions.DockerContainerRuntimeError(image) from err
    except docker.errors.APIError as err:  # pragma: no cover
        raise exceptions.DockerImageNotFound(image) from err
    return res.decode()
