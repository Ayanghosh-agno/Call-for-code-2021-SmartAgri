import wiotp.sdk.device
import json
import time
import RPi.GPIO as GPIO
servoPIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)                    
GPIO.setup(29, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

Upper = GPIO.output(40,True)
Lower=GPIO.output(29,True)

myConfig={
"identity":{
"orgId":"86xw9r",
"typeId":"New",
"deviceId":"12345"
    },
"auth":
{
    "token":"Ayaniot123"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
a=0
def myCommandCallback(cmd):
    Upper = GPIO.input(40)
    Lower=GPIO.input(29)
    
    n=len(cmd.data)
    if(n==8):
        nn=cmd.data['Roof']
        if(nn==0):
            a=1
        if(nn==1):
            a=2
        if(cmd.data['Cooling-System']==0):
            GPIO.output(15, True)
        if(cmd.data['Cooling-System']==1):
            GPIO.output(15, False)
        if(cmd.data['Led']==0):
            GPIO.output(32, True)
        if(cmd.data['Led']==1):
            GPIO.output(32, False)
        if(cmd.data['Heater']==0):
            GPIO.output(33, True)
        if(cmd.data['Heater']==1):
            GPIO.output(33, False)
        if(cmd.data['Field Pump']==0):
            GPIO.output(35, True)
        if(cmd.data['Field Pump']==1):
            GPIO.output(35, False)
        if(cmd.data['Submersible pump']==0):
            GPIO.output(37, True)
        if(cmd.data['Submersible pump']==1):
            GPIO.output(37, False)
        if(cmd.data['Water Cooler']==0):
            GPIO.output(36, True)
        if(cmd.data['Water Cooler']==1):
            GPIO.output(36, False)
        if(cmd.data['Water Heater']==0):
            GPIO.output(38, True)
        if(cmd.data['Water Heater']==1):
            GPIO.output(38, False)
            
        if(Upper==0 and Lower==1 and nn==0):
            p.ChangeDutyCycle(10)
            print('down')
            a=1
        elif(Upper==1 and Lower==0 and nn==1):
            p.ChangeDutyCycle(5)
            print('up')
            a=2
        elif(a==2 and Upper==0 and Lower==1):
            p.ChangeDutyCycle(0)
            a=0
        elif(a==1 and Upper==1 and Lower==0):
            p.ChangeDutyCycle(0)
            a=0
            

        

        
        
    



while True:
    client.commandCallback=myCommandCallback
