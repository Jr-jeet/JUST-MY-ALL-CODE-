# JUST-MY-ALL-CODE-
# NOT A PROJECT 
MY LAPTOP IS NOT IN GOOD CONTION , SO I AM CREATING  A NEW REPOSITORY FOR MY CODE  WHICH IS ALSO MY NOTE   "HERE IS MY ALL CODE WHICH IS VERY CLOSE TO ME"   
HERE I SAVE MY CODE 
BEACUSE I HAVE NO IDEA WHEN MY LAPTOP STOP WORKING 
AND WHEN MY ALL DATA GIES INTO TRUST 


String command;

void setup() {
  Serial.begin(115200);
  Serial.println("Offline Study Watch");
  Serial.println("Type: gst, python, income tax");
}

String think(String question) {
  question.toLowerCase();
  question.trim();

  if (question == "gst") {
    return "GST return filing is the process of submitting tax information to the government.";
  }

  if (question == "python") {
    return "Python is a programming language.";
  }

  if (question == "income tax") {
    return "Income tax is a tax paid on earnings and income.";
  }

  return "Topic not found.";
}

void loop() {

  if (Serial.available()) {

    command = Serial.readStringUntil('\n');

    String answer = think(command);

    Serial.println(answer);
  }
}