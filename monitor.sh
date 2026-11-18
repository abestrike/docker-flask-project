#!/usr/bin/env bash

status=$(curl -sS --max-time 3 -o /dev/null -w '%{http_code}' http://localhost:8080/health)
echo "$(date '+%F %T') HTTP=$status" >> monitor.log

if [[ "$status" == "200" ]]; then
    echo "✅ HEALTHY"
elif [[ "$status" == "000" ]]; then
    echo "❌ No HTTP response (timeout or connection failure)"
else
    echo "⚠️ Something is wrong: $status"
fi
