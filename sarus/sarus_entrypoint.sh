#!/bin/bash

# Put any commands here that you want to run before your application,
# then put this between container image and application command
echo "[sarus-entrypoint] Running this before the actual application $@"

exec "$@"
