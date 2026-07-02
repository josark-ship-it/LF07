from gpiozero import LED
from time import sleep


led_rot = LED(17)
led_gruen = LED(27)

def check_lagerbestand(artikel_name):
    
    if artikel_name == "Große Ritterburg":
        return 5
    elif artikel_name == "Feuerwehrauto Mini":
        return 0
    else:
        return -1
    
print("--- Klemmbausteine Gmbh - Lager-Ampel ---")

gesuchter_artikel = "Große Ritterburg"
bestand = check_lagerbestand(gesuchter_artikel)

print(f"Pruefe Bestand fuer: {gesuchter_artikel}...")
print(f"Gefundener Bestand: {bestand}")


if bestand > 0:
    print("Status: Genug Bestand da. Gruene LED leuchtet.")
    led_gruen.on()
    led_rot.off()
elif bestand == 0:
    print("WARNUNG: Artikel ausverkauft! Rote LED leuchtet.")
    led_rot.on()
    led_gruen.off()
else:
    print("FEHLER: Artikel nicht im System! Beide LEDs blinken als Warnung.")
    
    for _ in range(3):
        led_rot.on()
        led_gruen.on()
        sleep(0.5)
        led_rot.off()
        led_gruen.off()
        sleep(0.5)
        
        
sleep(5)
led_rot.off()
led_gruen.off()
print("Programm beendet.")