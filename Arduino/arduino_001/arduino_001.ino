int speakerPin = 9;
int length = 26;
char notes[] = "eeeeeeegcde fffffeeeeddedg";
int beats[] = {1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2};
int tempo = 300;

void playTone(int tone, int duration){
  for (long i = 0; i < duration * 1000L; i+=tone*2){
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration){

  char names[] = {'c', 'd', 'e', 'f'}
}