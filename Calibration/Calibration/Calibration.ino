#include "SPI.h"
#include "ILI9341_t3.h"
#include "font_Arial.h"
#include "HX711.h"
#include <Bounce.h>
#include <Encoder.h>
#include <SD.h>

//Encoder objects/variables
Encoder encoder(8,9);
int encoder_position = 0;

//Load cell objects/variables
HX711 scale;
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;
long load_cell_reading;

//Display objects/variables
#define TFT_DC      20
#define TFT_CS      21
#define TFT_RST    255  // 255 = unused, connect to 3.3V
#define TFT_MOSI     7
#define TFT_SCLK    14
#define TFT_MISO    12
ILI9341_t3 tft = ILI9341_t3(TFT_CS, TFT_DC, TFT_RST, TFT_MOSI, TFT_SCLK, TFT_MISO);
const int chipSelect = 6;

//Common 16-bit color values:
#define BLUE      0x001F
#define TEAL      0x0438
#define GREEN     0x07E0
#define CYAN      0x07FF
#define RED       0xF800
#define MAGENTA   0xF81F
#define YELLOW    0xFFE0
#define ORANGE    0xFC00
#define PINK      0xF81F
#define PURPLE    0x8010
#define GREY      0xC618
#define WHITE     0xFFFF
#define BLACK     0x0000

void setup()
{

  // Start serial communication
  Serial.begin(256000);
  
  //Start load cell ADC communication
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

  //Start LCD
  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(BLACK);
  tft.setCursor(10, 10);
  tft.setTextColor(WHITE);  
  tft.setTextSize(1);

  // See if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) 
  {
    Serial.println("Card failed, or not present");
    tft.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  tft.setCursor(110, 120);
  tft.println("Card initialized");
  Serial.println("card initialized");
  delay(1000);
  
  tft.fillScreen(BLACK);
  tft.setCursor(80, 120);
  tft.setTextSize(2);
  tft.println("SPORT ANALYZER");
  Serial.println("SPORT ANALYZER");
  delay(1000);
  tft.fillScreen(BLACK);

//  Serial.println("CLEARDATA");
//  Serial.println("LABEL,Realtime,Encoder,Load cell,Time(ms)");

  // Open the txt. file and add labels on each column
  File dataFile = SD.open("cal.txt", FILE_WRITE);
  
  if (dataFile) 
    {
      dataFile.print("Encoder");
      dataFile.print(";");
      dataFile.print("Load cell");
      dataFile.print(";");
      dataFile.println("Time");
      dataFile.flush();
    }  
    // if the file isn't open, pop up an error:
    else 
    {
      Serial.println("error opening datalog.txt");
    } 
}

void loop()
{     

  //Read the encoder and the load cell
  encoder_position = -1*(encoder.read());
  load_cell_reading = scale.read();
  
  // Display values on the screen
  display_show();
  //Save data on the SD card
  save_sd_card();
}

void display_show()
{
  tft.setTextColor(WHITE, BLACK);
  tft.setCursor(22, 100);
  tft.setTextSize(2);
  tft.print("ENCODER:");
  tft.println(encoder_position);
  tft.setCursor(10, 140);
  tft.print("LOADCELL:");
  tft.println(load_cell_reading);
}

void save_sd_card()
{
  File dataFile = SD.open("cal.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) 
   {
     //dataFile.println(dataString);
     dataFile.print(encoder_position);
     dataFile.print(";");
     dataFile.print(load_cell_reading);
     dataFile.print(";");
     dataFile.println(millis());
     //dataFile.flush();
     dataFile.close();
   }  
   // if the file isn't open, pop up an error:
   else 
   {
     Serial.println("error opening datalog.txt");
   } 
  
}

void serial_print()
{
    Serial.print("DATA,TIME,");
    Serial.print(encoder_position);
    Serial.print(","); 
    Serial.print(load_cell_reading);
    Serial.print(","); 
    Serial.print(millis());
}
