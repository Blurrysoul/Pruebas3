label islas:
    window hide
    $ isla = renpy.imagemap("mapa.jpg","mapa2.jpg",[
        (50, 200, 500, 530,"isla1"),
        (90, 490, 570, 1020,"isla2"),
        (550, 120, 1190, 340,"isla3"),#Dos islas
        (1210, 210, 1650, 390,"isla4"),
        (1050, 840, 1350, 1050,"isla5")
    ])

    if isla == "isla1":
        scene isla1
        "bienvenido a isla1"

    elif isla == "isla2":
        scene isla2
        "bienvenido a isla2"

    elif isla == "isla3":
        scene isla3
        "bienvenido a isla3"

    elif isla == "isla4":
        scene isla4
        "bienvenido a isla4"

    elif isla == "isla5":
        scene isla5
        "bienvenido a isla5"
        
    return