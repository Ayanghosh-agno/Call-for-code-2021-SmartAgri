import wiotp.sdk.device
import pytz
from datetime import datetime
import json
import time
import RPi.GPIO as GPIO
from boltiot import Sms
# Import SMS class from boltiot library
# Credentials required to send SMS
SID = 'Enter SID from Twilo dashboard' 
AUTH_TOKEN = 'Enter auth token from twilo dashboard' 
FROM_NUMBER = 'enter twilo number here'
TO_NUMBER = 'enter your mobile number here'
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER) # Create object to send SMS
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.output(15, True)
GPIO.output(32, True)
GPIO.output(33, True)
GPIO.output(35, True)
GPIO.output(37, True)
GPIO.output(36, True)
GPIO.output(38, True)



myConfig={
"identity":{
"orgId":"86xw9r",
"typeId":"Relay_alarm",
"deviceId":"relay"
    },
"auth":
{
    "token":"Relay123"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
i=0
j=0

s2=":50"
def myCommandCallback(cmd):
    s=cmd.data['Alarm']['alarm']
    s=str(s)
    s1=cmd.data['Alarm']['alarm2']
    s1=str(s1)
    i=int(s[0:2])
    j=int(s1[0:2])
    if (i>=5 and i <= 11):
        s4="Good Morning Farmer"
    if (i>=12 and i <= 16):
        s4="Good Afternoon Farmer"
    if (i>=17 and i <= 23 or i>=0 and i<=4):
        s4="Good Evening Farmer"
        
    if (j>=5 and j<= 11):
        s5="Good Morning Farmer"
    if (i>=12 and j <= 16):
        s5="Good Afternoon Farmer"
    if (j>=17 and j <= 23 or j>=0 and j<=4):
        s5="Good Evening Farmer"

    s=s+s2
    s1=s1+s2
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    time_now=str(datetime_ist.strftime('%H:%M:%S'))
    if (s==time_now):
        seperator= '\r\n \r\n'
        s=seperator.join(cmd.data['Noti_fi'])
        a="\r\n\r\n The follwing are the details of your field and surrroundings,\r\n Do have a look,\r\n Be asure we are taking care of every thing.\r\n\r\n\r\n\r\n\r\n"
        c="\r\n\r\n You can also click the below link to get the details or go to your SmartAgri App"
        d="\r\n\r\nsmartagri2021.eu-gb.mybluemix.net/ui\r\n"
        e="\r\n Thank You!"
        sms.send_sms("\r\n\r\n"+s4+a+s+c+d+e) # Call function to send SMS!'
    if (s1==time_now):
        seperator= '\r\n \r\n'
        s=seperator.join(cmd.data['Noti_fi'])
        a="\r\n\r\n The follwing are the details of your field and surrroundings,\r\n Do have a look,\r\n Be asure we are taking care of every thing.\r\n\r\n"
        c="\r\n\r\n You can also click the below link to get the details or go to your SmartAgri App"
        d="\r\n\r\nsmartagri2021.eu-gb.mybluemix.net/ui\r\n"
        e="\r\n Thank You!"
        sms.send_sms("\r\n\r\n"+s5+a+s+c+d+e) # Call function to send SMS!'

 
while True:
    rel1=GPIO.input(15)
    rel2=GPIO.input(32)
    rel3=GPIO.input(33)
    rel4=GPIO.input(35)
    rel5=GPIO.input(37)
    rel6=GPIO.input(36)
    rel7=GPIO.input(38)

    myData={'relay-1':rel1,'relay-2':rel2,'relay-3':rel3,'relay-4':rel4,'relay-5':rel5,'relay-6':rel6,'relay-7':rel7}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,onPublish=None)
    time.sleep(5)

    client.commandCallback=myCommandCallback
