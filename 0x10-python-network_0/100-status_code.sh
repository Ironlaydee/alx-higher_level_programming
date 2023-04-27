#!/bin/bash
# a script that request URL passed as argument, and display the status of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
