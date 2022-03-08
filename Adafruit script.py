#Impoterer bibliotek
import time
from Adafruit_IO import Client, Feed, RequestError, ThrottlingError 
import pyfirmata 
  

#Sette opp brukernamn og key til og være klienten
ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY =  ""
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY) 
  
board = pyfirmata.Arduino('COM4') 
pyfirmata.util.Iterator(board).start() 
  
#spesifisera portane som skal brukast på arduinoen
digital_output = board.get_pin('d:8:o')
analog_input = board.get_pin('a:0:i') 

while True: 
    #Prøver koden, om det skjer ein throttling error venta den 65 sek før den starta igjen. 
    try: 
        #Lese av analog og digitalt input
        print("running") 
        data = aio.receive(aio.feeds('digital').key) 
        data2 = aio.send(aio.feeds('analog').key, analog_input.read()) 
  
        #Lyset på arduinoen av og på
        if data.value == "1": 
            digital_output.write(1) 
            print("LED ON") 
        else: 
            digital_output.write(0) 
            print("LED OFF") 
  
        time.sleep(3) 
        
    except ThrottlingError: 
        print("*dies*") 
        time.sleep(65) 
