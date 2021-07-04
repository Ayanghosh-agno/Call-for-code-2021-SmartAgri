import credentials
import cv2
import wiotp.sdk.device
from imutils.video import VideoStream
import imutils
import time
import datetime
myConfig={
"identity":{
"orgId":"86xw9r",
"typeId":"Cam_Noti",
"deviceId":"rasp"
    },
"auth":
{
    "token":"Camera_Rasp"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
camera=0
def myCommandCallback(cmd):
    if (cmd.data['camera']==1):
        picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        picname=picname+".jpg"
        print(picname)
        cv2.imwrite(picname,frame)
        credentials.multi_part_upload("agnobucket", picname,picname)
        myData={"URL":picname}
        client.publishEvent(eventId="status",msgFormat="json",data=myData,onPublish=None)

c = VideoStream(usePiCamera=True).start()       #For Raspberry Pi Camera module, comment it if using webcam
time.sleep(2.0)
while True:
    frame = c.read()
    frame = imutils.resize(frame, width=450)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    client.commandCallback=myCommandCallback

