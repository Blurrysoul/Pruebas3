# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:


define e = Character("")
define sara = Character("")
image sara ="sara.png"
image int_barco ="interior-barco.jpg" 
image mapa = "mapa.jpg"
image primermapa = "primer-mapa.jpg"
image isla1 = "isla1.jpg"
image isla2 = "isla2.jpg"
image isla3 = "isla3.jpg"
image isla4 = "isla4.jpg"
image isla5 = "isla5.jpg"
image primeraisla = "images/primer-mapa/primer-mapa.jpg"
image zona1i1 = "images/isla1/zona1.jpg"
# El juego comienza aquí.

label start:


    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    "Sara es una chica Ingeniera en el año x la cual se embarcó a una expedición hacia una isla del pacifico"
    "Todo parecía perfecto, con este trabajo por fin podría lograr lo que siempre ha deseado, estudiar un raro material con potenciales enorme"
    scene int_barco
    show sara
    sara "Que bien!"
    "Y lo mejor de todo, todo pagado en una isla paradisiaca del pacifico ¿Qué más podría pedir?"
    "Pero en medio del trayecto comenzó a formarse una tormenta eléctrica misteriosa"
    "Esta tormenta era inusual, tenía color purpura, sus rayos parecían surgir a diestra y siniestra"
    "Poco a poco el barco se adentró en ella e inevitablemente el barco entre ola y ola finalmente naufraga"
    "Al despertarse se da cuenta que está en una playa de una isla que no es la que estaban buscando"
    sara "´Dios, mi cabeza...´"

    jump primeraisla

    # Finaliza el juego: