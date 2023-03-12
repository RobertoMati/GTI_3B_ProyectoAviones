"""
CLASE A IMPLEMENTAR EN ESTE FICHERO:
    - Clase Passenger: Representa un pasajero. Contiene informacion del pasajero.
"""

#------------------------------------------------------------------------------------------------------
# INICIO DE LA CLASE Passenger
#------------------------------------------------------------------------------------------------------
class Passenger:
    """_summary_ La clase Passenger se utiliza para almacenar la informacion de cada pasajero: nombre, apellido e id. 
                Esta clase tiene un metodo passenger_data() que devuelve una tupla con los tres valores:        

    ATRIBUTOS:
        - name: string
        - surname: string
        - id_card: int

    METODOS:
        - passenger_data()
    """ 
    #-----------------------------------------
    def __init__(self, name, surname, id_card):
        """_summary_ Constructor de la clase Passenger

        Args:
            name (string): El nombre del pasajero
            surname (string): El apellido del pasajero
            id_card (int): El id de embarque del pasajero

        Devuelve:
            None
        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card
    #-----------------------------------------
    
    #-----------------------------------------
    def passenger_data(self):
        """_summary_ Obtiene los datos del pasajero

        Args:
            None

        Devuelve:
            name: El nombre del pasajero, p.e. 'Jack'
            family_name: El apellido del pasajero, p.e. 'Shepard'
            id_card: El id de embarque del pasajero, p.e. '859940003S'
        """
        return self.__name, self.__surname, self.__id_card
    #-----------------------------------------
#------------------------------------------------------------------------------------------------------
# FIN DE LA CLASE Passenger
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
# Llamada con help para ver la documentacion de la clase y metodos
help(Passenger)
