int step_time=60*10; // en secondes
void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);

}
void loop() {
  int valeur_brute = analogRead(A0);

  float temperature_celcius = valeur_brute * (5.0 / 1023.0 * 100.0);

  Serial.println(temperature_celcius);
  delay(1000);
}
