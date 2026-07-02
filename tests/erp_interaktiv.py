from gpiozero import TonalBuzzer
from gpiozero import LED
from time import sleep


led_rot = LED(17)
led_gruen = LED(27)
buzzer = TonalBuzzer(21)

def spiele_erfolg_melodie():
    noten = ['C5', 'E5', 'G5']
    for note in noten:
        buzzer.play(note)
        sleep(0.15)
        buzzer.stop()
    
def spiele_fehler_melodie():
    noten = ['C5', 'E5', 'F5']
    for note in noten:
        buzzer.play(note)
        sleep(0.25)
        buzzer.stop()

def check_lagerbestand(artikel_name):
    name_clean = artikel_name.strip().lower()
    
    if name_clean == "ritterburg":
        return 5
    elif name_clean == "feuerwehr":
        return 0
    elif name_clean == "exit":
        return -99
    else:
        return -1
    
print("=======================================")
print(" KLEMMBAUSTEINE GMBH - INTERAKTIVES ERP")
print("=======================================")
print("Verfuegbare Artikel: 'ritterburg', 'feuerwehr' ")
print("Tippe 'exit' zum Beenden. \n")

while True:
    led_rot.off()
    led_gruen.off()
    
    
    eingabe = input("\nWelchen Artikel moechtest du pruefen? ")
    
    if eingabe.strip().lower() == "exit":
        print ("Programm beendet.")
        break
    

    bestand = check_lagerbestand(eingabe)
    
    if bestand > 0:
        print("--> Bestand da! Fröhliche Melodie.")
        led_gruen.on()
        spiele_erfolg_melodie()
        sleep(1)
        
    elif bestand == 0:
        print("--> AUSVERKAUFT! Warn-Melodie ertönt.")
        led_rot.on()
        spiele_fehler_melodie()
        sleep(1)
        
    else:
        print("--> Unbekannter Artikel! Bitte erneut versuchen.")
        
        buzzer.play('A5')
        sleep(0.5)
        buzzer.stop()
        