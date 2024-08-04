# RTSBruter_Luis
Bruter for RTSP

Use:

1. ```git clone https://github.com/UaLuis/RTSBruter_Luis.git && cd RTSBruter_Luis```
2. ```pip3 install -r requirements.txt```
3. ```sudo chmod +x rtspscan.sh```
4. Make a file target.txt with IP or IP range
5. For Brute1 use command: ```sudo ./rtspscan.sh && sudo python3 Brute1.py -t ./target.txt -u ./user.txt -password admin run```
6. For Brute2 use command: ```sudo ./rtspscan.sh && sudo python3 Brute2.py```
