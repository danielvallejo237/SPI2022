import garambubot as gb
from termcolor import colored, cprint
tu = colored('Tú: ', 'blue',attrs=['bold'])
gbot=colored('Garambullo Bot: ', 'blue', attrs=['bold'])
clasificador=gb.ClasificadorInt

if __name__=="__main__":
    while True:
        peticion = input(tu)
        Opc=clasificador(peticion)
        if Opc == 1:
            print(gbot+" Hola, te puedo ayudar a encontrar una receta con ciertos ingredientes. Por favor,  pídela poniendo los ingredientes con #. Por ejemplo: Quiero una receta con #cebolla y #tomate ")
        if Opc == 2:
            print(gbot+" Hasta luego.")
            break
        if Opc == 4:
            receta=gb.Ask(peticion)
            if receta!="":
                print(gbot+" \n" +receta)
                repetir = input(gbot+" Fue un gusto ayudarte. Si quieres pedir otra receta ingresa si y si no ingresa no: ")
                if repetir.lower() == "si":
                    print(gbot+" Por favor, solicita tu nueva receta poniendo los ingredientes con #")
                    continue
                elif repetir.lower() == "no":
                    print(gbot+" Hasta luego.")
                    break
            else:
                print(gbot+" No encontramos recetas con esos ingredientes en nuestra base de datos")
        if Opc == 3:
            print(gbot+ " No puedo entender tu mensaje. Por favor, pide una receta poniendo los ingredientes con #. Por ejemplo: Quiero una receta con #cebolla y #tomate")