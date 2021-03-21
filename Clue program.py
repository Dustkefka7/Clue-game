# -*- coding: utf-8 -*-
"""

@author: Elian Aguilar Moreno 18310428

5 personajes con nombres y profesiones:

Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario 
Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)
Kimberly es vendedora de mostrador en la plaza de la tecnologia 
Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes)
Bryan vende tenis y gorras en san juan de dios 

5 localizaciones:
    
Mercado de San Jhony (san juan de dios)
La Frikiplaza
Club nocturno Lola Lolita
Centro comercial Andares 
Estadio Jalisco

5 armas:
    
Filero(navaja)
heavy machine gun
Desodorante y encendedor
bate de beisbol
motosierra
"""






from random import choice

input("Bienvenido jugador estas a punto de entrar a la experiencia Clue.\nPress enter to continue")
input("El juego consiste en que hay un asesino y tendras que ir adivinando a partir de deducciones quien es, con que arma cometio el asesinato y en donde lo hizo\nPress enter to continue")
input("Comenzemos...\nPress enter to continue")
input("A continuacion se te mostrara el listado de los 5 posibles asesinos,las 5 posibles armas y las 5 posibles localizaciones.\nPress enter to continue")
print("\n\n5 personajes con nombres y profesiones: \n\nKevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \nJonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\nKimberly es vendedora de mostrador en la plaza de la tecnologia \nKaren Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \nBryan vende tenis y gorras en san juan de dios ")
print("\n\n5 localizaciones:\n\nMercado de San Jhony (san juan de dios)\nLa Frikiplaza\nClub nocturno Lola Lolita\nCentro comercial Andares \nEstadio Jalisco")
print("\n\n5 armas:\n\nFilero(navaja)\nheavy machine gun\nDesodorante y encendedor\nbate de beisbol\nmotosierra")

input("\n\nAhora se generara el evento de asesinato de manera aleatoria.\nHay un asesino que utilizo un arma y lo hizo en algun lugar de la ciudad de Guadalajara\nPress enter to continue")
input("Encuentralo!\nPress enter to continue")


nombre=["1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario",
"2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)",
"3.Kimberly es vendedora de mostrador en la plaza de la tecnologia",
"4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes)",
"5.Bryan vende tenis y gorras en san juan de dios" ]

localizacion=["1.Mercado de San Jhony (san juan de dios)",
"2.La Frikiplaza",
"3.Club nocturno Lola Lolita",
"4.Centro comercial Andares",
"5.Estadio Jalisco" ]

arma=["1.Filero(navaja)",
"2.heavy machine gun",
"3.Desodorante y encendedor",
"4.bate de beisbol",
"5.motosierra" ]

asesino_aleatorio=choice(nombre)
localizacion_aleatorio=choice(localizacion)
arma_aleatorio=choice(arma)

def comparacionacusado(tuacusado):
    if tuacusado=='1':
        if"1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario"==asesino_aleatorio:
            input("Has acertado! El es el asesino.\nPress enter to continue")
        else:
            input("Te has equivocado el no es el asesino\nPress enter to continue")
    
    if tuacusado=='2':
        if"2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)"==asesino_aleatorio:
            input("Has acertado! El es el asesino.\nPress enter to continue")
        else:
            input("Te has equivocado el no es el asesino\nPress enter to continue")

    if tuacusado=='3':
        if"3.Kimberly es vendedora de mostrador en la plaza de la tecnologia"==asesino_aleatorio:
            input("Has acertado! El es el asesino.\nPress enter to continue")
        else:
            input("Te has equivocado el no es el asesino\nPress enter to continue")

    if tuacusado=='4':
        if"4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes)"==asesino_aleatorio:
            input("Has acertado! El es el asesino.\nPress enter to continue")
        else:
            input("Te has equivocado el no es el asesino\nPress enter to continue")

    if tuacusado=='5':
        if"5.Bryan vende tenis y gorras en san juan de dios"==asesino_aleatorio:
            input("Has acertado! El es el asesino.\nPress enter to continue")
        else:
            input("Te has equivocado el no es el asesino\nPress enter to continue")
            
def comparacionarma(tuarma):
    if tuarma=='1':
        if"1.Filero(navaja)"==arma_aleatorio:
            input("Has acertado! Esa es el arma.\nPress enter to continue")
        else:
            input("Te has equivocado esa no es el arma.\nPress enter to continue")
            
    if tuarma=='2':
        if"2.heavy machine gun"==arma_aleatorio:
            input("Has acertado! Esa es el arma.\nPress enter to continue")
        else:
            input("Te has equivocado esa no es el arma.\nPress enter to continue")
            
    if tuarma=='3':
        if"3.Desodorante y encendedor"==arma_aleatorio:
            input("Has acertado! Esa es el arma.\nPress enter to continue")
        else:
            input("Te has equivocado esa no es el arma.\nPress enter to continue")
            
    if tuarma=='4':
        if"4.bate de beisbol"==arma_aleatorio:
            input("Has acertado! Esa es el arma.\nPress enter to continue")
        else:
            input("Te has equivocado esa no es el arma.\nPress enter to continue")
            
    if tuarma=='5':
        if"5.motosierra"==arma_aleatorio:
            input("Has acertado! Esa es el arma.\nPress enter to continue")
        else:
            input("Te has equivocado esa no es el arma.\nPress enter to continue")

input("Se ha cometido un asesinato en algun lugar de GDL!\nPress enter to continue")
input("Quien es el responsable!?\nPress enter to continue")
input("\nEres el detective Rorschach buscas siempre hacer el bien.\nUn dia en la ciudad de guadalajara estabas en busca del asesino de tu hija.\nCuando decides entrar a un lugar.\nA que lugar entraste?\nPress enter to continue")


print("El asesisno es:", asesino_aleatorio)
print("Lo hizo en:",localizacion_aleatorio)
print("Con el arma:",arma_aleatorio)


opcion=0
def menu():
    opc=int(input("A que lugar quieres entrar?\n"+
        "1.Mercado San Juan de Dios\n" +
        "2.Friki plaza\n" +
        "3.Club nocturno Lola lolita\n" +
        "4.Centro comercial andares\n" + 
        "5.Estadio Jalisco\n" +
        "6.Regresar a tu oficina con las pistas que tienes y hacer un veredicto final\n" +
        "Elige una opcion:"))

    return opc

while opcion !=6:
    opcion=menu()
    if opcion==1:
        input("\n\nEl mercado de San juan de dios uno de los tantos lugares fuera de la vista de dios, puedes encontrar la gente mas generosa y humilde y al mismo tiempo la peor escoria de la ciudad...\nPress enter to continue")
        tuacusado=input("Haz una acusacion!\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        comparacionacusado(tuacusado)
        tuarma=input("Haz una acusacion!\nCon que arma fue?\nEscoge con que crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        comparacionarma(tuarma)
        if localizacion_aleatorio=='1.Mercado de San Jhony (san juan de dios)':
            input("El asesinato se realizo aqui!")
        else:    
            input("El asesinato no se hizo aqui")
            
    if opcion==2:
        input("\n\nLa frikiplaza un lugar tipico de reunion para otakus,aun puedes oler en el aire un olor bastante desagradable y ves a personas que estan sentadas jugando yugi oh ...\nPress enter to continue")
        tuacusado=input("Haz una acusacion!\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        comparacionacusado(tuacusado)
        tuarma=input("Haz una acusacion!\nCon que arma fue?\nEscoge con que crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        comparacionarma(tuarma)
        if localizacion_aleatorio=='2.La Frikiplaza':
            input("El asesinato se realizo aqui!")
        else:    
            input("El asesinato no se hizo aqui")
        
    if opcion==3:
        input("\n\nEl club nocturno Lola lolita un lugar de trafico de drogas muchas jovencitas van a este lugar a pasar el rato, pero este tiene mala fama, es un peligro para estas chicas y ellas lo saben...\nPress enter to continue")
        tuacusado=input("Haz una acusacion!\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        comparacionacusado(tuacusado)
        tuarma=input("Haz una acusacion!\nCon que arma fue?\nEscoge con que crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        comparacionarma(tuarma)
        if localizacion_aleatorio=='3.Club nocturno Lola Lolita':
            input("El asesinato se realizo aqui!")
        else:    
            input("El asesinato no se hizo aqui")
        
    if opcion==4:
        input("El centro comercial andares en general se trata de un lugar bastante tranquilo en comparacion con el rsto de lugares que se le ocurrio al tipo que desarrollo este juego. Las familias hacen sus compras aqui...\nPress enter to continue")
        tuacusado=input("Haz una acusacion!\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        comparacionacusado(tuacusado)
        tuarma=input("Haz una acusacion!\nCon que arma fue?\nEscoge con que crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        comparacionarma(tuarma)
        if localizacion_aleatorio=='4.Centro comercial Andares':
            input("El asesinato se realizo aqui!")
        else:    
            input("El asesinato no se hizo aqui")
        
    if opcion==5:
        input("Un lugar de mala muerte el estadio Jalisco,tienes que tener cuidado ya que pueden robarte no solo tus pertenencias si no la vida misma. Puedes encontrar de las personas mas curiosas, darian su vida con tal de defender sus ideales(el equipo al que le van)...\nPress enter to continue")
        tuacusado=input("Haz una acusacion!\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        comparacionacusado(tuacusado)
        tuarma=input("Haz una acusacion!\nCon que arma fue?\nEscoge con que crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        comparacionarma(tuarma)
        if localizacion_aleatorio=='5.Estadio Jalisco':
            input("El asesinato se realizo aqui!")
        else:    
            input("El asesinato no se hizo aqui")
        
    if opcion==6:
        input("Haz tu veredicto final.\nCon todo lo que recabaste realiza tu acusacion final.\nPress enter to continue")
        vfase=input("\nQuien fue?\nEscoge la opcion de la persona que crees que es el asesino\n\n1.Kevin Alexis se gana la vida consiguiendo y vendiedo muestras de medicina en el santuario \n2.Jonathan Iker es dueno de su propio negocio ,esta en ventas, tiene mente de tiburon (sin miedo al exito)\n3.Kimberly es vendedora de mostrador en la plaza de la tecnologia \n4.Karen Andrea Nayeli es vendedora de catalogo(Avon,Price shoes) \n5.Bryan vende tenis y gorras en san juan de dios\n\nEscoge: ")
        vfarm=input("\nCon que arma fue?\nEscoge con que arma crees que se cometio el asesinato\n\n1.Filero(navaja)\n2.heavy machine gun\n3.Desodorante y encendedor\n4.Bate de beisbol\n5.motosierra\n\nEscoge:")
        vflug=input("\nEn que lugar se hizo?\nEscoge en que lugar crees que se hizo el asesinato\n\n1.Mercado de San Jhony (san juan de dios)\n2.La Frikiplaza\n3.Club nocturno Lola Lolita\n4.Centro comercial Andares \n5.Estadio Jalisco\n\nEscoge:")
        
        if vfase==asesino_aleatorio:
            if vfarm==arma_aleatorio:
                if vflug==localizacion_aleatorio:
                    input("H A S  E N C O N T R A D O\nA L  A S E S I N O")
                    input("FELICIDADES HAS ECHO JUSTICIA")
        else:
            input("HAS FALLADO NO HAS DADO CON EL ASESINO\nPress enter to continue")
            print("\nEl asesisno era:", asesino_aleatorio)
            print("\nLo hizo en:",localizacion_aleatorio)
            print("\nCon el arma:",arma_aleatorio)
            input("\nPress enter to continue")










