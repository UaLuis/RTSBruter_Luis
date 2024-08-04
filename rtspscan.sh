#!/bin/bash

echo "Masscan-RTSP"

masscan -iL target.txt -p554 --rate 10000 >> out.txt
sed 's/Discovered open port [0-9]*\/tcp on //g' out.txt > masmap.txt

sleep 1
echo "Scan complete."


