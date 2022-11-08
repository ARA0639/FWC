#include<Arduino.h>
int X,Y,Z,FN;

void setup()
{
	pinMode(2,INPUT);
	pinMode(3,INPUT);
	pinMode(4,INPUT);
	pinMode(6,OUTPUT);
}
void loop()
{
	X =digitalRead(2);
	Y =digitalRead(3);
	Z =digitalRead(4);
	FN =(!X||Y||!Z)&&(X||!Y)&&(!Y||Z);
	if(FN ==1)
		digitalWrite(6,HIGH);
	else
		digitalWrite(6,LOW);
}

