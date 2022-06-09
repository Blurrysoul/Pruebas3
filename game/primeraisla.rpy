label primeraisla:
    window hide

    screen prueba:


    scene primeraisla

    show screen visor1


    $ posi = renpy.random.randint(0,9)
    $ zona = renpy.imagemap("images/primer-mapa/primer-mapax.jpg","images/primer-mapa/primer-mapa2.jpg",[
    (50, 240, 835, 1040,"1"),
    (120, 10, 790, 250,"2"),
    (650, 15, 1650, 370,"3"),
    (760, 210, 1850, 770,"4")
    ])
    
    default hierro = 0
    default oro = 0
    default pieles = 0
    default embarazos = 0
    default sexo = 0
    default carne = 0

    if posi == 0:
        $evt = "Recolectar oro"
        $oro += 1

    if posi == 1:
        $evt = "Recolectar oro"
        $oro += 1    

    if posi == 2:
        $evt = "Recolectar hierro"
        $hierro += 1

    if posi == 3:
        $evt = "Recolectar hierro"  
        $hierro += 1

    if posi == 4:
        $evt = "Recolectar piel de ciervo"
        $pieles += 1

    if posi == 5:
        $evt = "Recolectar piel de ciervo"  
        $pieles += 1
            
    if posi == 6:
        $evt = "Recolectar carne de conejo"
        $carne += 1

    if posi == 7:
        $evt = "Recolectar carne de conejo" 
        $carne += 1 

    if posi == 8:
        $evt = "Escena Sexo"
        $sexo += 1
        if sexo == 3:
            $embarazos += 1
            $sexo = sexo-3

    if posi == 9:
        $evt = "Escena Sexo"
        if sexo == 3:
            $embarazos += 1
            $sexo = sexo-3



    if zona == "1":
        scene zona1i1
        "Buscando en el terreno... {w=3} Zona 1 {b}[evt]{/b} > {b}[posi]{/b}"

    
    elif zona == "2":
        "Zona 2 {b}[evt]{/b} > {b}[posi]{/b}"

    elif zona == "3":
        "Zona 3 {b}[evt]{/b} > {b}[posi]{/b}"

    elif zona == "4":
        "Zona 4 {b}[evt]{/b} > {b}[posi]{/b}"

    jump primeraisla
        
return