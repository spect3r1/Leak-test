import os
import logging

from verda.containers import (
    Deployment,
    Container,
    ComputeResource,
    ContainerRegistrySettings,
    DockerHubCredentials,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

registry_creds = DockerHubCredentials(
    name="prod-registry",
    username=os.environ["DOCKERHUB_USERNAME"],
    access_token=os.environ["DOCKERHUB_TOKEN"],
)

deployment = Deployment(
    name="prod-api",
    containers=[
        Container(
            image="docker.io/acme/private-api:latest",
            exposed_port=8080,
            name="api",
        )
    ],
    compute=ComputeResource(
        name="cpu",
        size=2,
    ),
    container_registry_settings=ContainerRegistrySettings(
        is_private=True,
        credentials=registry_creds,
    ),
)

logger.info("Creating deployment: %s", deployment)
