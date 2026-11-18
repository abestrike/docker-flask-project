#!/usr/bin/env bash

healthy=$(grep -c 'HTTP=200' monitor.log)
failed=$(grep -c 'HTTP=000' monitor.log)

echo "=== Flask Monitoring Report ==="
echo "Healthy checks: $healthy"
echo "Failed checks: $failed"
