#include <ESP8266WiFi.h>
#include <time.h>
#include <ESP8266HTTPClient.h>
#include <Arduino.h>
#include <U8g2lib.h>
 
const char* ssid = "********";                          
const char* password = "********";                       
char baseDate[10]; 
char baseTime[10]; 

String url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey=vaHuhGQ%2FEk%2FTnn43WDRuw3gAbPLxDgvdLIjGtReWvN8KiOTLvBezmYurECebWPpiodu4IrccnwH%2BCljQ9pKLmw%3D%3D&pageNo=1&numOfRows=8&dataType=XML&";
String pmUrl = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=vaHuhGQ%2FEk%2FTnn43WDRuw3gAbPLxDgvdLIjGtReWvN8KiOTLvBezmYurECebWPpiodu4IrccnwH%2BCljQ9pKLmw%3D%3D&returnType=xml&numOfRows=1&pageNo=1&stationName=%EB%8F%99%EB%8C%80%EB%AC%B8%EA%B5%AC&dataTerm=DAILY&ver=1.0";
U8G2_SSD1306_128X64_NONAME_1_SW_I2C u8g2(U8G2_R0, /* clock=*/ 14, /* data=*/ 12, /* reset=*/ U8X8_PIN_NONE);

String printTime = "";
int count = 0;

char* weatherString[8] = {"맑음", "비", "비/눈", "눈", "소나기", "빗방울", "빗방울눈날림", "눈날림"};
char* pmString[5] = {"측정중","좋음", "보통", "나쁨", "매우나쁨"};

bool toggle = false;

void printOLED(String text1, String text2, String text3){
  u8g2.firstPage();
  do {
    u8g2.setCursor(0, 15);
    u8g2.print(text1);
    u8g2.setCursor(0, 40);
    u8g2.print(text2);		
    u8g2.setCursor(0, 55);
    u8g2.print(text3);
  } while ( u8g2.nextPage() );
}

void printOLED(String text1, String text2){
  u8g2.firstPage();
  do {
    u8g2.setCursor(0, 15);
    u8g2.print(text1);
    u8g2.setCursor(0, 40);
    u8g2.print(text2);
  } while ( u8g2.nextPage() );
}

void printOLED(String text){
  u8g2.firstPage();
  do {
    u8g2.setCursor(0, 15);
    u8g2.print(text);
  } while ( u8g2.nextPage() );
}

void printConnectingStatus(){
    u8g2.firstPage();
    do {
        u8g2.setCursor(0, 15);
        u8g2.print("인터넷 연결 중");
        for (int i=0; i<=count; i = i + 8){
          u8g2.setCursor(i, 40);
          u8g2.print(".");	
        }
    } while ( u8g2.nextPage() );

    count = (count==16) ? 0 : count+8;
}

void printConnectingSuccess(){
  printOLED("연결 성공!!");
  delay(300);
  printOLED("");
  delay(150);
  printOLED("연결 성공!!");
  delay(300);
  printOLED("");
}

void setWiFi() { 
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    printConnectingStatus();
  }

  printConnectingSuccess();  
} 

int parse(String payload) {
  for(int i=0; i<7; i++) {
    int end_point = payload.indexOf("</item>");
    payload = payload.substring(end_point+6,payload.length());
  }

  int start_point = payload.indexOf("<fcstValue>");
  int end_point = payload.indexOf("</fcstValue>");
  
  payload = payload.substring(start_point+11, end_point);
  
  return payload.toInt();
}

int parsePM(String payload) {
  int start_point = payload.indexOf("<pm10Grade>");
  int end_point = payload.indexOf("</pm10Grade>");
  
  payload = payload.substring(start_point+11, end_point);
  
  return payload.toInt();
}
 

void setup() {
  Serial.begin(115200);

  u8g2.begin();
  u8g2.enableUTF8Print();

  u8g2.setFont(u8g2_font_unifont_t_korean2);  
  u8g2.setFontDirection(0);
  u8g2.firstPage();

  setWiFi();
  
  configTime(9*3600, 0, "pool.ntp.org", "time.nist.gov");
  while (!time(nullptr)) delay(500);
}
 
void loop() {
  time_t now = time(nullptr);
  struct tm *t;
  t = localtime(&now);

  u8g2.setFont(u8g2_font_unifont_t_korean2);  
  u8g2.setFontDirection(0);

  sprintf(baseDate, "%04d%02d%02d", t->tm_year+1900, t->tm_mon+1, t->tm_mday);
  sprintf(baseTime,"%02d%02d", (t->tm_hour != 0) ? (t->tm_hour -1) : 23, t->tm_min);

  if (t->tm_year != 70) {
    if (WiFi.status() == WL_CONNECTED) // 와이파이가 접속되어 있는 경우
    {
      WiFiClient client; // 와이파이 클라이언트 객체
      HTTPClient http; // HTTP 클라이언트 객체

      String target = url + "base_date=" + baseDate + "&base_time=" + baseTime + "&nx=62&ny=127";
      String printTime = printTime + (t->tm_year+1900) + "/" + (t->tm_mon+1) + "/" + (t->tm_mday) + " " + (t->tm_hour) + ":" + baseTime[2] + baseTime[3];

      int pmCode = 0;

      if (http.begin(client, pmUrl)) {  // HTTP PM
        // 서버에 연결하고 HTTP 헤더 전송
        int httpCode = http.GET();
        
        // httpCode 가 음수라면 에러
        if (httpCode > 0) { // 에러가 없는 경우
          if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
            String payload = http.getString(); // 받은 XML 데이터를 String에 저장
            
            pmCode = parsePM(payload);
            // pmCode = 3; //시연용
          }
        } else {
          printOLED("PM GET실패", http.errorToString(httpCode).c_str());
        }
        http.end();
      } 

      if (http.begin(client, target)) {  // HTTP 일기예보
        // 서버에 연결하고 HTTP 헤더 전송
        int httpCode = http.GET();

        // httpCode 가 음수라면 에러
        if (httpCode > 0) { // 에러가 없는 경우
          if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
            String payload = http.getString(); // 받은 XML 데이터를 String에 저장
            int result = parse(payload);
            // int result = 0; //시연용

            printOLED(printTime, String("날씨: ") + weatherString[result], String("미세먼지: ") + pmString[pmCode]);
            
            //result가 0이 아닌 경우 + 미세먼지가 나쁨 이상일 경우 창문 close하게 시리얼 통신
            Serial.print((((result!=0) || (pmCode>2)) ? "close\r" : "open\r"));
            delay(59000);

            //시연용
            // Serial.print(toggle ? "close\r" : "open\r");
            // toggle = toggle ? false : true;
            // delay(9000);
          }
        } else {
          printOLED("[HTTP] GET실패", http.errorToString(httpCode).c_str());
        }
        http.end();
      } else {
        printOLED("[HTTP] 접속불가");
      }
    } else {
      printOLED("Lose Connection", "인터넷 상태를", "확인해주세요.");
    }
  } else {
    printOLED("Time error", "시간대 정보를", "받아오는중입니다.");
  }
  delay(1000);
}
