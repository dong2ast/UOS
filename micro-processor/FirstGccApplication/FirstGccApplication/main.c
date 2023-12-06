#define __DELAY_BACKWARD_COMPATIBLE__
#define F_CPU 16000000UL

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdbool.h>

#define SERVO_DEG_P60 500
#define SERVO_DEG_M60 250

volatile bool trigger = false;

void timer_init()
{
	TCCR1A = 0x82;
	TCCR1B = 0x1B;
	ICR1 = 4999;
	OCR1A = 375;
}

SIGNAL(INT4_vect)
{
	trigger = true;
}

SIGNAL(INT5_vect)
{
	trigger = false;
}

void moveMotor(bool trigger){
	if (trigger) {
		OCR1A = SERVO_DEG_M60;
		_delay_ms(300);
	} else {
		OCR1A = SERVO_DEG_P60;
		_delay_ms(300);
	}
}


int main(void)
{
	
	DDRB = 0xFF;
	DDRE = 0xcf;
	PORTB = 0x00;
	
	timer_init();
	
	EICRB = 0x0A; // INT4 = falling edge
	EIMSK = 0x30; // INT4 interrupt enable
	SREG |= 1<<7;
	
	while (1)
	{
		moveMotor(trigger);
	}
}
