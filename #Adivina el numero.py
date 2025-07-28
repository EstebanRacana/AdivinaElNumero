import random
numeroRandom=random.randint(1,100)
cont=3;
#print(f"Random integer: {numeroRandom}")
print("Estoy pensando en un numero del 1 al 100...")
while(cont!=0):
    numeroUsuario=int(input("Ingrese un numero para adivinar que numero piensa la maquina, tenes 3 intentos"))
    if(numeroUsuario==numeroRandom):
        print("Lo lograste! Acertado.")
        cont=0
    elif(numeroUsuario>numeroRandom):
            print("Te fuiste muy lejos, intenta un numero mas bajo")
            cont=cont-1
    elif(numeroUsuario<numeroRandom):
            print("Te fuiste muy lejos, intenta un numero mas alto")
            cont=cont-1
    if(cont==0):
        print("Juego finalizado, el numero era: ",numeroRandom)
        
