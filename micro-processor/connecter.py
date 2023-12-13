import time

import serial

# COM9 포트 설정
ser_read = serial.Serial('COM9', 9600, timeout=1)

# COM8 포트 설정
ser_write = serial.Serial('COM8', 115200, timeout=1)

try:
    while True:
        # COM9로부터 데이터 읽기
        data = ser_read.readline().decode('utf-8').strip()

        if (data):
        # 읽은 데이터를 출력
            print("Received data from COM9:", data)

            # 읽은 데이터를 COM8로 전송
            ser_write.write(data.encode('utf-8') + b'\r')
        time.sleep(30)
except KeyboardInterrupt:
    # Ctrl+C를 누르면 종료
    ser_read.close()
    ser_write.close()
