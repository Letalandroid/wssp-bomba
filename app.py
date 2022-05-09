from pyautogui import write, press
from time import sleep

mensaje = str(input("Escriba el mensaje a enviar: "))
numMensajes = int(input("Escriba cuántos mensajes desea enviar: "))

print("\nEsperando que abra WhatsApp...")
sleep(1)
input("Una vez tenga el WhatsApp abierto, presione la tecla Enter...\n")

i = 5

while i > 0:
    print(f"Enviando mensajes bomba en {i}")
    i = i - 1
    sleep(1)

print(" ")

for i in range (numMensajes):
    print(f"Enviando mensaje bomba num{i}")
    write(mensaje)
    press("Enter")