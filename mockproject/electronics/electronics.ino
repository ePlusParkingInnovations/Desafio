

void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT);

}

void loop() {
  int prev = 0;
  int current = digitalRead(8);
  while(1){
    if(prev != current){
      Serial.println( current );
      prev = current;
    }
    current = digitalRead(8);
    
  }
}
