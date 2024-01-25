#!/bin/bash
# this sends a JSON POST request to a URL which is passed as the first argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
