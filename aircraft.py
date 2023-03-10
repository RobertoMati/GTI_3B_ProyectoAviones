"""
CLASES A IMPLEMENTAR EN ESTE FICHERO:
    - Clase Aircraft: Representa un avión. Contiene información de la aeronave.
    - Clase Airbus: Representa un avión Airbus. Hereda de la clase Aircraft.
    - Clase Boeing: Representa un avión Boeing. Hereda de la clase Aircraft.
"""

"""
CONSIDERACIONES:
    - Cada clase se implementará en un fichero con el mismo nombre. Los nombres de las clases serán los mismos que se ven 
      en el diagrama de clases, siguiendo el convenido de nomenclatura (sólo la primera letra en mayúscula), 
      mientras que los nombres de los ficheros serán en minúscula.
    
    - Los nombres de los parámetros de los __init__ serán los mismos que los atributos de la clase que definen.
    
    - Las clases Airbus y Boing se implementarán en el fichero de la superclase Aircraft.
    
    - Los atributos de cada clase serán privados. Su nomenclatura empezará por __ y se utilizarán los getters para acceder a su valor.
"""

"""
La clase Aircraft contiene información de la aeronave. De esta clase, cabe mencionar el método seating_plan() que genera una tupla con dos valores. 
El primero es una lista de los números de filas (p.e. del 1 al 23, siendo None el primer elemento de la lista) y el segundo es un string de letras (p.e. 'ABCDEF'). 
Estos valores representan las filas de asientos disponibles y su nomenclatura para una misma fila, respectivamente. El método num_seats simplemente devuelve el número 
total de asientos que tiene la aeronave. A continuación, puedes ver la descripción de ambos métodos:
"""

"""
ATRIUBUTOS DE LA CLASE AIRCRAFT:
    - __registration: string
        El registro de la aeronave

    - __model: string
        El modelo de la aeronave

    - __num_rows: int
        El numero de filas de la aeronave

    - __num_seats_per_row: int
        El numero de asientos por fila de la aeronave
"""

"""
MÉTODOS DE LA CLASE AIRCRAFT:
    - get_model()
        Muestra los datos del modelo
        Devuelve:
        model: El modelo de la aeronave

    - get_registration()
        Muestra los datos del registro
        Devuelve:
        registration: El registro de la aeronave

    - seating_plan()
        Generates a seating plan for the number of rows and seats per row
        Devuelve:
        rows: A list of rows: None, 1, 2, etc.
        seats: A string of letters such as 'ABCDEF'
        
    - num_seats()
        Calculates the number of seats
        Devuelve:
        seats: The number of seats
"""

"""
ATRIBUTOS DE LA CLASE AIRBUS:
    - __model: "Airbus A319"
        El modelo de la aeronave

    - __num_rows: 23
        El numero de filas de la aeronave

    - __num_seats_per_row: 6
        El numero de asientos por fila de la aeronave

    - __variant: string
"""

"""
MÉTODOS DE LA CLASE AIRBUS:
    - get_variant()
        Muestra los datos de la variante
        Devuelve:
        variant: La variante de la aeronave
"""

"""
ATRIBUTOS DE LA CLASE BOEING:
    - __model: "Boeing 777"
        El modelo de la aeronave

    - __num_rows: 56
        El numero de filas de la aeronave

    - __num_seats_per_row: 9
        El numero de asientos por fila de la aeronave

    - __airline: string
"""

"""
MÉTODOS DE LA CLASE BOEING:
    - get_airline()
        Muestra los datos de la aerolinea
        Devuelve:
        airline: La aerolinea de la aeronave
"""
#------------------------------------------------------------
class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self.__registration
    
    def get_model(self):
        return self.__model
    
    def seating_plan(self):
        # range(1, self.__num_rows + 1) genera una lista de números de 1 a self.__num_rows
        # "ABCDEFGHJK"[:self.__num_seats_per_row] Crea una cadena de texto que representa las letras de los asientos disponibles en cada fila.
        # Ejemplo: "ABCDEFGHJK"[:6] devuelve "ABCDEF"
        return (range(1, self.__num_rows + 1), "ABCDEFGHJK"[:self.__num_seats_per_row])
    
    def num_seats(self):
        # Multiplico el número de filas por el número de asientos por fila
        return self.__num_rows * self.__num_seats_per_row
#------------------------------------------------------------

#------------------------------------------------------------
class Airbus(Aircraft):

    def get_variant(self):
        return self.__variant

    def __init__(self, variant, registration):
        self.__model = "Airbus A319"
        self.__num_rows = 23
        self.__num_seats_per_row = 6
        self.__variant = variant
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
#------------------------------------------------------------

#------------------------------------------------------------
class Boeing(Aircraft):

    def get_airline(self):
        return self.__airline
    
    def __init__(self,airline, registration):
        self.__model = "Boeing 777"
        self.__num_rows = 56
        self.__num_seats_per_row = 9
        self.__airline = airline
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)


    
