#!/bin/bash

if [ -z "$DIGITAL_OCEAN_IP_ADDRESS"]
then
    echo "DIGITAL_OCEAN_IP_ADDRESS is not set"
    exit 0
fi

git archive --format tar --output ./project.tar main

echo 'Uploading project...'
rsync ./project.tar root@DIGITAL_OCEAN_IP_ADDRESS:/tmp/project.tar

echo 'Building the image...'

ssh -o StrictHostKeyChecking=no root@DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
    mkdir -p /app
    rm -rf /app/* && tar -xf /tmp/project.tar -C /app
    docker compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH

echo 'Building complete as successfully.'