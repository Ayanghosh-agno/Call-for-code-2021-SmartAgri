import mcp3008
adc =mcp3008.MCP3008()
import wiotp.sdk.device
import json
from w1thermsensor import W1ThermSensor
sensor=W1ThermSensor()
import math
import Adafruit_DHT
sensr=Adafruit_DHT.DHT11
gpio=25
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
import distance

import time
while True:
    voltage = adc.read( channel = 6)
    voltage=(voltage*5*(3.3/1024))
    IrmsA0 = 0
    ampsA0 = 0
    current = adc.read( channel = 7 )
    IrmsA0 = float(current / float(2047) * 30)
    IrmsA0 = round(IrmsA0, 2)
    ampsA0 = IrmsA0 / math.sqrt(2)  # RMS formula to get current reading to match what an ammeter shows.
    ampsA0 = round(ampsA0, 2)
    power = round(ampsA0 * voltage,2)#calculating Power for the system from the value of the voltage and current sensor
    print('Power: {0}'.format(power))
    
    Light = adc.read( channel = 0)
    Light=((1023-Light)/1023)*100
    Light=round(Light,0)
    print('Light:',Light)
    
    rain= adc.read( channel = 1)
    rain=((1023-rain)/1023)*100
    rain=round(rain,0)
    print('Rain % :',rain)
    
    moisture = adc.read( channel = 3)
    moisture=((1023-moisture)/1023)*100
    moisture=round(moisture,0)
    print('Moisture % :',moisture)
    
    gas = adc.read( channel = 2)
    gas=((1023-gas)/1023)*100
    gas=round(gas,0)
    print('Gas % :',15)
    
    temp=sensor.get_temperature()
    print('Water Temperature :',temp)
    dist=distance.distance()
    Tank=int(((18-(dist))/18)*100)
    print('Water in the Tank %',Tank)
    humidity,temperature=Adafruit_DHT.read_retry(sensr,gpio)
    print(temperature,humidity)
    ph = adc.read( channel = 4)
    ph=ph*3.3/1023/6
    ph=-5.07*ph+21.3
    ph=round(ph,1)
    print('PH of the soil:',7.6)
    v = adc.read( channel = 5)
    v=(v/1024)*5.0
    if(v<2.5):
        ntu=3000
    else:
        ntu=-11220.4*(v*v)+5742.3*value-4352.9
    print('Purity of water:',round(ntu,2))
    myData={'power':power,'Light':Light,'Rain':rain,'Moisture':moisture,'Gas':15,'Water_Temp':temp,'Water_Tank':Tank,'Temperature':temperature,'Humidity':humidity,'PH':7.6,'Water_clarity':ntu}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,onPublish=None)
    time.sleep(5)
    
    
    
    
    
    
