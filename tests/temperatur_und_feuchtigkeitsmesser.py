import time
import random
import board
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

# GPIO-Modus für RPLCD zurücksetzen/initialisieren
GPIO.setwarnings(False)

# Initialisiert LCD (welches Kabel liegt wo)
lcd = CharLCD(pin_rs=22, pin_e=18, pins_data=[25, 24, 23, 26],
              numbering_mode=GPIO.BCM, cols=16, rows=2)


sim_temp = 22.0
sim_feucht = 55.0

print("LCD und Sensor starten...")
lcd.clear()
lcd.write_string("Lager-Monitor\nBooting...")
time.sleep(3)

try:
    while True:
        # Simulation von Messschwankungen
        
        sim_temp += random.uniform(-0.2, 0.2)
        sim_feucht += random.uniform(-0.5, 0.5)
        
        # Werte auf 1 Nachkommastelle runden
        
        sim_temp = round(sim_temp, 1)
        sim_feucht = round(sim_feucht, 1)
        
        lcd.clear()
        
        if sim_temp >= 25.0:
            # Kritische Temparatur
            lcd.write_string(f"!! ALARM !!\nTemp zu hoch: {sim_temp}C")
            print(f"[ALERT] Kritische Temparatur im Lager: {sim_temp}C!")
        else:
            #Normalzustand
            lcd.write_string(f"Temp: {sim_temp} C\n")
            lcd.write_string(f"Feucht: {sim_feucht} %")
            print(f"Simulierte Werte: {sim_temp}C, {sim_feucht}%")
        
        
        time.sleep(2.5)
        
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("System Off")
    GPIO.cleanup()
    print("\nProgramm sauber beendet.")
        