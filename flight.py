"""
La clase Flight representa la información de un vuelo. Posiblemente, la parte más complicada es la representación de los asientos, 
que puedes encontrar en el atributo seating. Esto se representa mediante una lista de diccionarios, donde cada posición de la lista 
hace referencia a una fila de asientos (1, 2, etc.). Para cada fila, habrá un diccionario donde las claves serán las letras de los 
asientos ('A', 'B', etc.) y los valores serán los datos del pasajero (nombre, apellido e id). Como la numeración de las filas empieza 
en 1, introduciremos un valor None en la posición 0. De esta forma, la posición 1 de la lista se corresponderá con la fila 1, la posición
2 con la fila 2, etc. A continuación, puedes ver la descripción de los métodos de la clase Flight:
"""

"""
En la función __init__ se inicializará el atributo seating, mediante llamada al método seating_plan() del atributo aircraft. A continuación 
puedes ver los métodos que nos permiten gestionar los asientos:

    - allocate_passenger()
        Aloja a un pasajero en un asiento determinado
        Args:
        seat: Un asiento designado por un número de fila y una letra (p.e. '12C' o '21F')
        passenger: Información del pasajero ('Jack', 'Shephard', '85994003S')
        
    - reallocate_passenger()
        Realojamos a un pasajero en un asiento diferente
        Args:
        from_seat: El exisitente asiento designado por un número de fila y una letra (p.e. '12C')
        to_seat: El nuevo asiento designado por un número de fila y una letra (p.e. '21F')
        
    - num_available_seats()
        Obtiene el número de asientos disponibles
        Devuelve:
        El número de asientos disponibles
"""

"""
Además, también tenemos dos métodos que nos permiten imprimir información por consola. El método print_seating() mostrará el listado de asientos por consola. 
Para mostrar las filas una detrás de otra, puedes importar la función pprint() del módulo pprint:

from pprint import pprint

pprint(seating)
"""

"""
También tenemos el método print_boarding_cards() que mostrará por pantalla las tarjetas de embarque de todos los pasajeros. 
A continuación tienes la definición de estos métodos:

    - print_seating()
        Imprime por consola el seating plan
        Ejemplo:
        {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    
    - print_boarding_cards()
        Imprime por consola las tarjetas de embarque de cada pasajero
        Tarjeta de embarque:
        ----------------------------------------------------------
        |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
        ----------------------------------------------------------
"""

"""
MÉTODOS DE LA CLASE FLIGHT:
    - get_aircraft_model()
        Muestra los datos del modelo de la aeronave
        Devuelve:
        aircraft_model: El modelo de la aeronave

    - get_number()
        Muestra los datos del número de vuelo
        Devuelve:
        number: El número de vuelo

    - allocate_passenger()
        Aloja a un pasajero en un asiento determinado

    - reallocate_passenger()
        Realojamos a un pasajero en un asiento diferente

    - num_available_seats()
        Obtiene el número de asientos disponibles

    - print_seating()
        Imprime por consola el seating plan

    - print_boarding_cards()
        Imprime por consola las tarjetas de embarque de cada pasajero

    - _parse_seat()
        Parsea un asiento designado por un número de fila y una letra (p.e. '12C' o '21F')

    - _passenger_seats()
        Genera una secuencia de asientos ocupados por un pasajero
"""

class Flight: