#include <Ultrasonic.h>
#define pino_trigger 4
#define pino_echo 2
Ultrasonic ultrasonic(pino_trigger, pino_echo);

#define A 12 //
#define B 13 // define o pino respectivo
#define C  7 // a cada led
#define D  8 //
#define E  9 //
#define F 11 //
#define G 10 //
#define QTD_SEG   7 //quantidade de leds
#define QTD_CHAR 10 //quantidade de dígitos
int seg[] = {A, B, C, D, E, F, G}; //vetor referente aos pinos
int contador; //usado para definir qual dígito será mostrado
bool num[][10] = { {1, 1, 1, 1, 1, 1, 0},   // mapeia
                   {0, 1, 1, 0, 0, 0, 0},   // cada
                   {1, 1, 0, 1, 1, 0, 1},   // dígito
                   {1, 1, 1, 1, 0, 0, 1},   // à respectiva
                   {0, 1, 1, 0, 0, 1, 1},   // combinação
                   {1, 0, 1, 1, 0, 1, 1},   // de leds
                   {1, 0, 1, 1, 1, 1, 1},   // acesos
                   {1, 1, 1, 0, 0, 0, 0},   //
                   {1, 1, 1, 1, 1, 1, 1},   //
                   {1, 1, 1, 1, 0, 1, 1} }; //
         
void setup() {
  Serial.begin(9600);
  Serial.println("Lendo dados do sensor...");
  
  contador = 0; //inicia o contador
  for(int i = 0; i < QTD_SEG; i ++)
  pinMode(seg[i], OUTPUT); //inicia os pinos
  
}
void loop() {
  float cmMsec, inMsec;
  long microsec = ultrasonic.timing();
  cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
  int i = 0;
  int atual = 0;
  int antiga = 0;
  
  if (cmMsec <= 20){
     atual = 1;
  }
  else {atual = 0;}

  if (atual == 1 && antiga == 0){
    contador++;
    if (contador > 9){
    contador = 0;
    
  }
    for(int i = 0; i < QTD_SEG; i ++)
    digitalWrite(seg[i], num[contador][i]); //exibe os dígitos
    delay(1000);
   antiga == atual;
  }
  
  
  delay(500);
}
