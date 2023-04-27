#!/bin/bash
# takes and sends a request to URL, displays rge size of response
curl -s "$1" | wc -c
