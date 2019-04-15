#!/usr/bin/env bash

VERSION=1

docker login

docker build . -t marcohoyer/zcan:$VERSION
docker push marcohoyer/zcan:$VERSION
