import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

# GPIO-Modus vorbereiten
GPIO.setwarnings(False)

lcd = CharLCD(pin_rs=22, pin_e=18, pins_data=[25, 24, 23, 26],
              numbering_mode=GPIO.BCM, cols=16, rows=2)

print("Fließband-Zähler startet...")
lcd.clear()
lcd.write_string("Klemmbausteine\nGmbH - System")
time.sleep(3)

paket_zähler = 0

try:
    while True:
        # Ein neues Paket wird verpackt
        paket_zähler += 1
        
        lcd.clear()
        
        lcd.write_string("Status: Aktiv\n")
        
        lcd.write_string(f"Pakete: {paket_zähler}")
        
        print(f"[INFO] Paket verarbeitet. Gesamt: {paket_zähler}")
        
        time.sleep(2.0)
        
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("Band gestoppt\nSystem Off")
    GPIO.cleanup()
    print("\nAnlage sicher heruntergefahren.")