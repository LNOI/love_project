EXPOSE_PORT=8200 \
    CONTAINER_IMAGE=internal-server \
    CONFIG_SET=prod \
    BUILD_IMAGE_TAG=latest \
    CONTAINER_NAME=internal-tool-$EXPOSE_PORT \
    docker-compose down --remove-orphans

EXPOSE_PORT=8200 \
    CONTAINER_IMAGE=internal-server \
    CONFIG_SET=prod \
    BUILD_IMAGE_TAG=latest \
    CONTAINER_NAME=internal-tool-$EXPOSE_PORT \
    docker-compose build --force-rm

EXPOSE_PORT=8200 \
    CONTAINER_IMAGE=internal-server \
    CONFIG_SET=prod \
    BUILD_IMAGE_TAG=latest \
    CONTAINER_NAME=internal-tool-$EXPOSE_PORT \
    docker-compose up -d 
