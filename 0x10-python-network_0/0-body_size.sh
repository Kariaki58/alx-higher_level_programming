#!/bin/bash
#comment
echo "$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')"
