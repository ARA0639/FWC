#include <avr/io.h>

 int main (void)
{

  DDRD  = DDRD |(1 << 6);
  unsigned char i,x,y,z,o;
  while (1) {
	  i = PIND;
          x = 0b00000100;
	  y = 0b00001000;
	  z = 0b00010000;
	  x = x&i;
	  y = y&i;
	  z = z&i;
	  x = x>>2;
	  y = y>>3;
	  z = z>>4;
	  o =(~x|y|~z)&(x|~y)&(~y|z);
	  o = o<<6;
          PORTD=o;
  }


  return 0;

}
