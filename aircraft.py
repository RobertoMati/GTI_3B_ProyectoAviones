"""
CLASES A IMPLEMENTAR EN ESTE FICHERO:
    - Clase Aircraft: Representa un avión. Contiene información del avion.
    - Clase Airbus: Representa un avión Airbus. Hereda de la clase Aircraft.
    - Clase Boeing: Representa un avión Boeing. Hereda de la clase Aircraft.
"""
#------------------------------------------------------------
class Aircraft:
    """_summary_ Representa un avion. Contiene informacion del avion.

    ATRIBUTOS:
        - registration (string)
        - model (string)
        - num_rows (int)
        - num_seats_per_row (int)

    METODOS:
        - get_model()
        - get_registration()
        - seating_plan()
        - num_seats()
    """
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """_summary_ Constructor de la clase Aircraft

        Args:
            registration (string): El registro del avion
            model (string): El modelo del avion
            num_rows (int): El numero de filas del avion
            num_seats_per_row (int): El numero de asientos por fila del avion

        Devuelve:
            None
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """_summary_ Muestra los datos del registro

        Devuelve:
            registration: El registro del avion
        """
        return self.__registration
    
    def get_model(self):
        """_summary_ Muestra los datos del modelo

        Devuelve:
            model: El modelo del avion
        """
        return self.__model
    
    def seating_plan(self):
        """_summary_ Genera un plan de asientos para el numero de filas y asientos por fila

        Devuelve:
            rows: Una lista de filas: None, 1, 2, etc. 
        
            seats: Una cadena de letras como 'ABCDEF'

        Info:
            - range(1, self.__num_rows + 1) genera una lista de numeros de 1 a self.__num_rows
            - "ABCDEFGHJK"[:self.__num_seats_per_row] Representa las letras de los asientos disponibles en cada fila.
            - Ejemplo: "ABCDEFGHJK"[:6] devuelve "ABCDEF"
        """
        return (range(1, self.__num_rows + 1), "ABCDEFGHJK"[:self.__num_seats_per_row])
    
    def num_seats(self):
        """_summary_ Calcula el numero de asientos

        Devuelve:
            seats: El numero de asientos

        Info:
            Multiplica el numero de filas por el numero de asientos por fila, consiguiendo el numero total de asientos
        """
        return self.__num_rows * self.__num_seats_per_row
    
    
#------------------------------------------------------------

#------------------------------------------------------------
class Airbus(Aircraft):
    """_summary_ Representa un avion Airbus. Contiene informacion del avion.

    Args:
        Aircraft (class): La clase padre de la clase Airbus

    ATRIBUTOS:
        - model: "Airbus A319"
        - num_rows: 23
        - num_seats_per_row: 6
        - variant: string

    METODOS:
        - get_variant()

    HERENCIA:
        - __init__(self, variant, registration)
            Constructor de la clase Airbus
            Args:
                variant (string): La variante del avion
                registration (string): El registro del avion
            Devuelve:
                None

    Info:
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
        Llama al constructor de la clase padre (Aircraft) y le pasa los parametros necesarios
    """

    def get_variant(self):
        """_summary_ Muestra los datos de la variante

        Devuelve:
            variant: La variante del avion
        """
        return self.__variant

    def __init__(self, variant, registration):
        """_summary_ Constructor de la clase Airbus

        Args:
            variant (string): La variante del avion
            registration (string): El registro del avion

        Devuelve:
            None

        Info:
            self.__model = "Airbus A319"
            self.__num_rows = 23
            self.__num_seats_per_row = 6
            Estos atributos son privados y solo pueden ser accedidos desde la clase Airbus
        """
        self.__model = "Airbus A319"
        self.__num_rows = 23
        self.__num_seats_per_row = 6
        self.__variant = variant
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
#------------------------------------------------------------

#------------------------------------------------------------
class Boeing(Aircraft):
    """_summary_ Representa un avion Boeing. Contiene informacion del avion.

    Args:
        Aircraft (class): La clase padre de la clase Boeing

    ATRIBUTOS:
        - model: "Boeing 777"
        - num_rows: 56
        - num_seats_per_row: 9
        - airline: string

    METODOS:
        - get_airline()

    HERENCIA:
        - __init__(self, airline, registration)
            Constructor de la clase Boeing
            Args:
                airline (string): La aerolinea del avion
                registration (string): El registro del avion
            Devuelve:
                None

    Info:
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
        Llama al constructor de la clase padre (Aircraft) y le pasa los parametros necesarios

    """

    def get_airline(self):
        """_summary_ Muestra los datos de la aerolinea

        Devuelve:
            airline: La aerolinea del avion
        """
        return self.__airline
    
    def __init__(self,airline, registration):
        """_summary_ Constructor de la clase Boeing

        Args:
            airline (string): La aerolinea del avion
            registration (string): El registro del avion

        Devuelve:
            None

        Info:
            self.__model = "Boeing 777"
            self.__num_rows = 56
            self.__num_seats_per_row = 9
            Estos atributos son privados y solo pueden ser accedidos desde la clase Boeing
        """
        self.__model = "Boeing 777"
        self.__num_rows = 56
        self.__num_seats_per_row = 9
        self.__airline = airline
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)

#------------------------------------------------------------
#------------------------------------------------------------
help(Aircraft)
help(Airbus)
help(Boeing)


    
