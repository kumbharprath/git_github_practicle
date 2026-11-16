#!/usr/bin/env bash
# Usage: bash scripts/check_service.sh http://127.0.0.1:8000/health
URL="${1:-http://127.0.0.1:8000/health}"
ATTEMPTS=3

for ((i=1; i<=ATTEMPTS; i++)); do
    echo "Attempt $i at $(date '+%Y-%m-%d %H:%M:%S')"
    if curl --silent --fail --max-time 3 "$URL" > /dev/null; then
        echo "SUCCESS: service is responding"
        exit 0
    fi
    echo "Service not ready; retrying..."
    sleep 1
done

echo "ERROR: service did not respond after $ATTEMPTS attempts"
exit 1
