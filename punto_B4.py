#Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico, 
#donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.

opcion = input('''Seleccione el tipo de robot para su informackon basica
    1. Cilindrico
    2. Cartesiano
    3. Esferico
    \n''')

match opcion:
    case "1":
        print('''este robot cuenta con una articulacion rotacional y una tipo prismatico "RPP"\n''')

    case "2":
        print('''este tipo de robot tiene 3 movimientos de tipo lineal perpendiculares entre si X,Y,Z "PPP"\n''')

    case "3":
        print('''este tipo de robot cuenta con 2 articulaciones rotacionales y una tipo prismatica "RRP"\n''')
    
