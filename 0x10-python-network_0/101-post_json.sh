#!/bin/bash
# a script that sends a JSON POST request to URL passed as the firat argument and display the response
curl -s -H Content-Type: application/json" -d "$(cat "$2")" "$1"
