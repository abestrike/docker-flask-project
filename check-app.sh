#!/bin/bash

if curl -s -f http://localhost:8080/health > /dev/null; then
    echo "✅ Flask app is running!"
else
    echo "❌ Flask app is not running!"
    exit 1
fi
