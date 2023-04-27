#!/bin/bash
# a script that takes in URL and display HTTP methods
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
