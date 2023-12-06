#!/usr/bin/env bash

url=$1
size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')
echo "$size"
