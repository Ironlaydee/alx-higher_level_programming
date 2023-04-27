#!/bin/bash
# a script that send a POST request to a passed URL and displays the responds
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
