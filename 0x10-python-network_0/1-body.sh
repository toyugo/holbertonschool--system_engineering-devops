#!/bin/bash
# Get the byte size
code=$(curl -sL -w "%{http_code}" -I "$1" -o /bin/null)
if [ $code -eq 200 ]
then
    curl -sL "$1"
fi