#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me, and ge a You got me! response
curl -sL -X "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
