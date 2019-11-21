MQTTHOST = "tailor.cloudmqtt.com"
MQTTPORT = "17195"
MQTTCLIENT = "ABCDEF"
MQTTTOPIC = "FFF"
MQTTPROTOCOLNAME = "MQIsdp"
MQTTLVL = 3
MQTTFLAGS = 0xC2
MQTTKEEPALIVE = 60
MQTTUSERNAME = "httfjvkw"
MQTTPASSWORD = "bbtf2s5efMsp"
MQTTOS = 0
MQTTPACKETID = 1

dataOutput = ""

def stringToHex(str):
	x = len(str)
	sstr = ""
	for i in range(x):
		sstr += hex(ord(str[i])).lstrip("0x").rstrip("L") or "0"
	return sstr

def intToHex(Int):
	return hex(Int).lstrip("0x").rstrip("L") or "0"
	
def connectionPacket():
	global dataOutput
	dataOutput += "10"
	#+len(MQTTCLIENT)
	X = len(MQTTUSERNAME)+len(MQTTPASSWORD)+len(MQTTPROTOCOLNAME)+len(MQTTCLIENT)+12
	
	while True:
		encodeByte = X % 128
		
		X = X / 128
		if X >= 1:
			encodeByte = encodeByte | 128
		c = "{}".format(hex(encodeByte).lstrip("0x").rstrip("L") or "0")
		dataOutput += c
		if X < 1:
			break
	a = intToHex((len(MQTTPROTOCOLNAME) & 0xF000) >> 16)
	b = intToHex((len(MQTTPROTOCOLNAME) & 0x0F00) >> 8)
	c = intToHex((len(MQTTPROTOCOLNAME) & 0x00F0) >> 4)
	d = intToHex((len(MQTTPROTOCOLNAME) & 0x000F))
	e = "{}{}{}{}{}".format(a,b,c,d,stringToHex(MQTTPROTOCOLNAME))
	dataOutput += e
	c = "{}{}".format(intToHex((MQTTLVL & 0xF0) >> 4), intToHex(MQTTLVL  & 0x0F))
	dataOutput += c	
	c = "{}{}".format(intToHex((MQTTFLAGS & 0xF0) >> 4), intToHex(MQTTFLAGS  & 0x0F))
	dataOutput += c	
	a = intToHex((MQTTKEEPALIVE& 0xF000) >> 16)
	b = intToHex((MQTTKEEPALIVE & 0x0F00) >> 8)
	c = intToHex(48>> 4)
	d = intToHex((MQTTKEEPALIVE& 0x000F))
	print(MQTTKEEPALIVE & 0x00F0)
	e = "{}{}{}{}".format(a,b,c,d)
	dataOutput += e
	print(dataOutput)
		

connectionPacket()