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

unsigned char getchar0() {
	while (!(UCSR0A & (1 << RXC0))); // RXC0 비트를 확인하여 데이터 수신 대기
	return UDR0;
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

void init(){
	UBRR0H = 0;
	UBRR0L = 8;

	UCSR0B = (1 << RXEN0) | (1 << TXEN0); // RXEN0, TXEN0 비트를 설정하여 송수신 활성화
	UCSR0C = (1 << UCSZ01) | (1 << UCSZ00); // UCSZ01, UCSZ00 비트를 설정하여 프레임 포맷 설정

	DDRA = 0xff; // 포트 A를 출력으로 설정
	
	DDRB = 0xFF;
	DDRE = 0xcf;
	PORTB = 0x00;
	
	timer_init();
	
	EICRB = 0x0A; // INT4 = falling edge
	EIMSK = 0x30; // INT4 interrupt enable
	SREG |= 1<<7;
}

int main(void) {
	unsigned char c;
	unsigned char buffer[10];
	unsigned int i = 0;

	init();

	while (1) {
		c = getchar0();

		buffer[i] = c;
		i++;

		if (c == '\r') {
			i = 0;
			if (buffer[0] == 'o' && buffer[1] == 'p' && buffer[2] == 'e' && buffer[3] == 'n' && buffer[4] == '\r') {
				moveMotor(true);
				} else {
				moveMotor(false);
			}
		}
	}
}
