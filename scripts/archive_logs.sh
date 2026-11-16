#!/usr/bin/env bash
# Safe sample: archive log files in ./logs (never deletes original logs)
mkdir -p logs archives
STAMP=$(date '+%Y%m%d_%H%M%S')

if compgen -G 'logs/*.log' > /dev/null; then
    tar -czf "archives/logs_$STAMP.tar.gz" logs/*.log
    echo "Created archives/logs_$STAMP.tar.gz"
else
    echo "No .log files found in logs/"
fi

df -h .
