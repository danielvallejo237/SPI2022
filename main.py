import garambubot as gb

clasificador=gb.ClasificadorInt

if __name__=="__main__":
    while True:
        peticion = input("Tú: ")
        Opc=clasificador(peticion)
        if Opc == 1:
            print("Garambullo Bot: Hola, te puedo ayudar a encontrar una receta con ciertos ingredientes. Por favor,  pídela poniendo los ingredientes con #. Por ejemplo: Quiero una receta con #cebolla y #tomate ")
        if Opc == 2:
            print("Garambullo Bot: Hasta luego.")
            break
        if Opc == 4:
            receta=gb.Ask(peticion)
            if receta!="":
                print("Garambullo Bot: \n" +receta)
                repetir = input("Garambullo Bot: Fue un gusto ayudarte. Si quieres pedir otra receta ingresa si y si no ingresa no: ")
                if repetir.lower() == "si":
                    print("Garambullo Bot: Por favor, solicita tu nueva receta poniendo los ingredientes con #")
                    continue
                elif repetir.lower() == "no":
                    print("Garambullo Bot: Hasta luego.")
                    break
            else:
                print("No encontramos recetas con esos ingredientes en nuestra base de datos")
        if Opc == 3:
            print("No puedo entender tu mensaje. Por favor, pide una receta poniendo los ingredientes con #. Por ejemplo: Quiero una receta con #cebolla y #tomate")