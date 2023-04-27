#!/bin/bash
# takes in a header as argument, GET request to the URL
curl -sH "X-School-User-Id: 98" "${1}"
