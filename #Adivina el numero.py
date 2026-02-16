import random
numeroAleatorio=random.randint(1,100)
intentos=3;
#print(f"Random integer: {numeroRandom}")
print("Estoy pensando en un numero del 1 al 100...")
while(intentos!=0):
    numeroUsuario=int(input("Ingrese un numero para adivinar que numero piensa la maquina, tenes 3 intentos: "))
    if(numeroUsuario==numeroAleatorio):
        print("Lo lograste! Acertado.")
        intentos=0
    elif(numeroUsuario>numeroAleatorio):
            print("Te fuiste muy lejos, intenta un numero mas bajo")
            intentos=intentos-1
    elif(numeroUsuario<numeroAleatorio):
            print("Te fuiste muy lejos, intenta un numero mas alto")
            intentos=intentos-1
    if(intentos==0):
        print("Juego finalizado, el numero era: ",numeroAleatorio)
        
