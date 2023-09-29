import random
estado1 = True

while estado1 == True:
    no = random.randint(1,6)
    # uno 
    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
    # dos 
    if no == 2:
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
    # tres 
    if no == 3:
        print("[-----]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[-----]")
    # cuatro
    if no == 4:
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
    # cinco 
    if no == 5:
        print("[-----]")
        print("[-0-0-]")
        print("[--0--]")
        print("[-0-0-]")
        print("[-----]")
    # seis
    if no == 6:
        print("[-----]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-----]")
    print("numero random:", no)
    estado = input("presiona y para girar otra vez, y n para salir: ");
    if estado == "y":
        estado1 = True
    if estado == "n":
        estado1 = False
    
    
