# RaspPi-Notification-System

## Desciption
The system uses curl command and PushBullet to send boot info to your phone when the Raspberry pi boots and even after it boots to send more info about the system status. PushBullet makes getting things on and off your phone easy and fast.

## Get Started
* Create an account at [PushBullet](https://www.pushbullet.com/)
* Go to your settings then click on "Create Access Token" button
* Put your token in the a_1 variable

```Python

a_1 = "curl -u [Your_PushBullet_Token_Here]: https://api.pushbullet.com/v2/pushes -d type=note -d title='Raspberry Pi' -d body='"

```
