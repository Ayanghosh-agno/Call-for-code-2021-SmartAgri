<div align="center">
<img src="https://i.postimg.cc/nLR310L8/greenhouse.png">
</div>
<h1 align="center">SMART AGRI <a name="project-name"></a> </h1>
<div align="center">
  
  >Lets begin a smart farming revolution because agriculture is not a farming, it's a FEEDING !
  
</div>

## What is SMART-AGRI?

Smart-Agri is a smart farming evolution system integrated with both hardware and software part to make a smart green-house system to help to increase the productivity of the food production process as well as the profit of the farmers in this time of climate change. Basically our system is a complete package that a farmer needs for the best farming conditions inside the Green-house connecting with a water tank which is further equipped with several sensors and appliances to manage the water nutrients and temperature. We also tried to use the renewable resources as far as possible, like storing the rain water or opening the roof the greenhouse automatically to let the rain water shower on the plants whenever need saving both the water and electricity with accessing the solar power fitted in the greenhouse roof. Further it can also help the unskilled farmers with some important factors of farming like, Crop yield prediction, profit prediction, best crop that should be grown under that soil with that particular environmental conditions and also with fertilizers prediction. Each of these is designed under a single user friendly app with about 10+ Indian local understandable languages by the farmer.

## Contents 
- [SMART AGRI](#project-name)
  01. [Short Description](#Short-Description)
      - [What's the problem?](#whats-the-problem)
      - [Proposed Solution](#Proposed-Solution)
  2. [Demo Video](#Demo-Video)
  3. [Architecture](#Architecture)
  4. [Long Description](#Long-Description)
      - [More about the UI](#More-about-the-UI)
      - [About the hardware setup](#hardware-part)
  5. [Hardware Requirements](#Hardware-Requirements)
  6. [Software/Access Requirements](#Software/Access-Requirements)
  7. [Project Roadmap](#Project-Roadmap)
  8. [Circuit Setup](#Circuit-Setup)
  9. [Development/Code Setup](#Development/Code-Setup)
  10. [APP URL](#APP-URL)
  11. [Planned for Future](#Planned-for-Future)
  12. [Authors](#Authors)

<h2 align="center"> Short Description <a name="Short-Description"></a> </h2>

### What's the problem? <a name="whats-the-problem"></a>

Agriculture is one of the professions that is been practiced for decades, but by years passing, the people are losing faith from this because of the lack of productivity and lack of farming knowledge and due to this unpredictable weather because of this rapid climate change. As a result farmer's condition from different parts of the world are getting worse day by day making them to face huge losses due to which they are choosing suicide as their only option. Maximum family farming lacks the knowledge to deal with this climate change and to overcome the issues caused in the plants from different insects and due to lack of nutrients which finally results in their production. 
Though some of the products which are available focus on huge area basis and also with some limited features, with manuals and operating procedures only found in ENGLISH as the only language, making it very hard for most of the farmers in the world to understand easily.

### Proposed Solution <a name="Proposed-Solution"></a>

Making a Smart Greenhouse prototype with the latest technology and IBM cloud integration to make the farming condition favourable for healthy production through out the year. It can intelligently monitor and can take actions, eliminating the manual interaction. Many sensors are deployed to measure the environmental parameters and to take action accordingly.

SMART-AGRI contains the following features:-

* Real-time weather monitoring with WEATHER API.
* Date when the crop was planted with CLOUDANT DB.
* Best fertilizer to be used for better and healthy growth with IBM AUTO AI associated with ML model.
* Crop selection based on the Soil, and current environmental conditions with IBM AUTO AI associated with ML model.
* Rain fall prediction with IBM AUTO AI associated with ML model.
* Crop Yield prediction of the particular crop in a particular region with the help of 10 years dataset and IBM AUTO AI associated with ML model.
* Plant disease Prediction, either the farming plant or other plant selected through the app by the farmer and the way to cure them using IBM VISUAL RECOGNITION.
* Farmer can choose the information he wants get notified in two desired times among the given 7 parameters using TWILLO.
* Getting the Sensors value from the greenhouse and to control the appliances such as the Cooler, Heater, LEDs, Roof, Water Pump etc through IBM IOT.
* Historical data access on desired sensor value using CLOUDANT DB.
* Storing the Greenhouse plants image taken by the Greenhouse Camera in the OBJECT STORAGE to access for future use and to analyse it.
* With more than 7+ Indian local languages along with English is deployed with IBM WATSON LANGUAGE TRANSLATION API to make it easy for the farmers to understand   their farming conditions. 
* Making a user friendly and easy to access UI with the help of NODE RED SERVICES on IBM further implementing it to the MIT-APP-Inventor to make an APP out of it.
* Live feed coming directly from the Greenhouse to the farmer for extra security and safety.

<h2 align="center">Demo Video</h1><a name="Demo-Video"></a>

[![Demo Video](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Thumbnail.JPG)](https://www.youtube.com)

<h2 align="center">Architecture</h1><a name="Architecture"></a>

![Architecture Image](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/project%20architecture.png)


## Long Description <a name="Long-Description"></a>
[Long Description Document Link](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Documentation/Smart%20Agri.pdf)

### More about the UI <a name="More-about-the-UI"></a>
*Sample of the APP UI:*
<div align="center">

<img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Home.png">
  <br>
    <br>
   <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/line.png">
      <br>
        <br>
  <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Field_Data.png">
    <br>
     <br>
   <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/line.png">
      <br>
        <br>     
  <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Restpart.png">
      <br>
     <br>
   <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/line.png">
</div>

### About the hardware setup <a name="hardware-part"></a>
<div align="center">
  <img src="https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Hardware.jpg">
</div>

## Hardware Requirements <a name="Hardware-Requirements"> </a> 

* Voltage Sensor
* Gas Sensor
* Light Sensor
* Current Sensor
* Moisture Sensor
* Ph-Sensor
* Turbidity Sensor
* Rain Sensor
* Dh11 Sensor
* LM2596 voltage regulator
* Ultrasonic Sensor
* DS18b20 Temperature Sensor
* Limit Switch
* Raspberry Pi model-3
* Night Vision camera module
* 8-channel relay module
* Water Pump
* Peltier plate with heat sink
* Cooling Fan
* Led Lights
* Nichrome Wire(Heater)
* Servo

![Hardware](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Hardware.png)




## Software/Access Requirements<a name="Software/Access-Requirements"></a> 
 * [IBM developer account](https://cloud.ibm.com/login)
 * [IBM Visual recognition service](https://cloud.ibm.com/login)
 * [IBM Watson Services(Auto AI, machine learning, IoT)](https://cloud.ibm.com/login)
 * [Node Red](https://cloud.ibm.com/login)
 * [IBM Language Translator](https://cloud.ibm.com/login)
 * [IBM Cloudant DB](https://cloud.ibm.com/login)
 * [IBM Object Storage](https://cloud.ibm.com/login)
 * [Twlio](https://www.twilio.com/) API access- for SMS notifications.
 * [OpenWeather](https://openweathermap.org/api) API access- To retrieve weather information
 * [Python3](https://www.python.org)- for programming the raspberry pi.




## Project Roadmap <a name="Project-Roadmap"></a>
![picture alt](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/Roadmap.png)



## Circuit Setup <a name="Circuit-Setup"></a>
 ![picture alt](https://github.com/Ayanghosh-agno/Call-for-code-2021-SmartAgri/blob/main/Image/FULL-1.jpg)


## Development/Code-Setup <a name="Development/Code-Setup"></a>


## APP URL <a name="APP-URL"></a>
[URL](https://smartagri2021.eu-gb.mybluemix.net/ui/)

## Planned for Future <a name="Planned-for-Future"></a>

* Future rain prediction for saving more water and energy.
* Helping the farmers to predict the current value of the crops.
* Helping the farmers to calculate profit about any particular crop in the particular region.
* To make a water and soil Ph neutralizing system.
* The threshold for autonomous operation is pre-set, and can only be changed by programming experts, more flexibility can be given to the farmers to set the threshold values.
* Implementing the SMART-AGRI in a large scale basis and to take feedback from local farmers to do any chances or addition of any features if needed.

## Contributor<a name="Authors"></a>
* Ayan Ghosh- 3rd Year Under-Graduate Student in University Institute of Technology, Burdwan [*See Linkedin*](https://www.linkedin.com/in/ayan-ghosh-4743841a1/)
