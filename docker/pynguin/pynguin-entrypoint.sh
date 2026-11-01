#!/usr/bin/env bash
# Install the target project's requirements from /package/package.txt (when the
# mount is provided), then exec Pynguin with all arguments.  Mirrors the
# CodaMOSA pynguin-docker.sh contract: /input:ro, /output, /package:ro.
set -e

if [ -f /package/package.txt ]; then
    echo "Installing project dependencies from /package/package.txt"
    pip install -q -r /package/package.txt || echo "WARNING: partial dependency install" >&2
fi

exec pynguin "$@"