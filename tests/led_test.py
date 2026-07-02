from gpiozero import LED
from time import sleep

warn_led = LED(17)

print("LED-Test startet... Schalte LED ein.")
warn_led.on()
sleep(3)

print("Schalte LED aus.")
warn_led.off()