#------------------------------------------------------------------------------------------------------
# INICIO DE LA CLASE Flight
#------------------------------------------------------------------------------------------------------
class Flight:
    """_summary_ Una clase que representa un vuelo

    ATRIBUTOS:
        - _number: El numero de vuelo
        - _aircraft: El modelo de la aeronave
        - _seating: Una lista de diccionarios que representa el seating plan

    METODOS:
        - get_aircraft_model(): Muestra el modelo de la aeronave
        - get_number(): Muestra el numero de vuelo
        - allocate_passenger(): Asigna un asiento a un pasajero
        - reallocate_passenger(): Reasigna un asiento a un pasajero
        - num_available_seats(): Calcula el numero de asientos disponibles
        - print_seating(): Muestra el seating plan
        - print_boarding_tarjetas(): Muestra las tarjetas de embarque
        - parse_seat(): Parsea un asiento
        - passenger_seats(): Calcula los asientos ocupados por un pasajero
    """
    #-----------------------------------------
    def __init__(self, number, aircraft):
        """_summary_ Inicializa un vuelo

        Args:
            number (string): El numero de vuelo
            aircraft (Aircraft): El modelo de la aeronave

        Raises:
            ValueError: Si el numero de vuelo no tiene un formato valido

        Info:
            - number[:2].isalpha() Comprueba si los dos primeros caracteres son letras
            - number[:2].isupper() Comprueba si los dos primeros caracteres son mayusculas
            - number[2:].isdigit() Comprueba si los caracteres restantes son numeros
            - int(number[2:]) <= 9999 Comprueba si el numero de vuelo es menor o igual a 9999

        Devuelve:
            None
        """
        if not number[:2].isalpha():
            raise ValueError(f"Los dos primeros caracteres no son letras: '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Los dos primeros caracteres no son mayusculas: '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Los caracteres restantes no son numeros o el numero de vuelo es mayor que 9999: '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
    #-----------------------------------------

    #-----------------------------------------
    def get_aircraft_model(self):
        """_summary_ Muestra el modelo del avion

        Devuelve:
            model: El modelo del avion
        """
        return f"{self._aircraft.model()}"
    #-----------------------------------------

    #-----------------------------------------
    def get_number(self):
        """_summary_ Muestra el numero de vuelo

        Devuelve:
            number: El numero de vuelo
        """
        return f"{self._number}"
    #-----------------------------------------
    
    #-----------------------------------------
    def allocate_passenger(self, seat, passenger):
        """_summary_ Aloja a un pasajero en un asiento determinado

        Args:
            seat (string): El asiento designado por un numero de fila y una letra (p.e. '12C' o '21F')
            passenger (string): El nombre del pasajero

        Raises:
            ValueError: Si el asiento esta ocupado

        Devuelve:
            None
        """
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"El asiento {seat} ya esta ocupado")
        self._seating[row][letter] = passenger
    #-----------------------------------------

    #-----------------------------------------
    def reallocate_passenger(self, from_seat, to_seat):
        """_summary_ Realojamos a un pasajero en un asiento diferente

        Args:
            from_seat (string): El asiento designado por un numero de fila y una letra (p.e. '12C' o '21F')
            to_seat (string): El asiento designado por un numero de fila y una letra (p.e. '12C' o '21F')

        Raises:
            ValueError: Si el asiento esta vacio
            ValueError: Si el asiento esta ocupado

        Devuelve:
            None
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No hay nadie sentado en el asiento {from_seat}")
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"El asiento {to_seat} ya esta ocupado")
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
    #-----------------------------------------

    #-----------------------------------------
    def num_available_seats(self):
        """_summary_ Obtiene el numero de asientos disponibles

        Devuelve:
            num_available_seats: El numero de asientos disponibles

        Info:
            - sum(1 for s in row.values() if s is None) Comprueba si el asiento esta ocupado
        """
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)
    #-----------------------------------------
    
    #-----------------------------------------
    def print_seating(self):
        """_summary_  Imprime por consola el seating plan
            Ejemplo:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    
        Devuelve:
            None
        """
        from pprint import pprint
        pprint(self._seating, width=200)
    #-----------------------------------------

    #-----------------------------------------
    def print_boarding_cards(self):
        """_summary_ Imprime por consola las tarjetas de embarque de cada pasajero
            Tarjeta de embarque:
            ----------------------------------------------------------
            |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
            ----------------------------------------------------------
        
        Devuelve:
            None

        Info:
            - sorted(self._passenger_seats()) Ordena los pasajeros por asiento
            - f"| Nombre: {passenger[0]}" \ Concatena el nombre del pasajero
            - f"  Apellidos: {passenger[1]}" \ Concatena los apellidos del pasajero
            - f"  DNI: {passenger[2]}" \ Concatena el DNI del pasajero
            - f"  Asiento: {seat}" \ Concatena el asiento del pasajero
            - f"  Numero de vuelo: {self._number}" \ Concatena el numero de vuelo
            - f"  Modelo de aeronave: {self._aircraft.get_model()}" \ Concatena el modelo de aeronave
            - " |" Concatena el final de la tarjeta de embarque
            - esquinasYlaterales = '+' + '-'*(len(output)-2) + '+' Calcula el numero de caracteres de la tarjeta de embarque
            - lineas = [esquinasYlaterales, output, esquinasYlaterales] Crea una lista con las lineas de la tarjeta de embarque
            - tarjeta = '\n'.join(lineas) Une las lineas de la tarjeta de embarque
            - print(tarjeta) Imprime la tarjeta de embarque
        """
        import passenger
        for passenger, seat in sorted(self._passenger_seats()):
            output = f"| Nombre: {passenger[0]}" \
                    f"  Apellidos: {passenger[1]}" \
                    f"  DNI: {passenger[2]}" \
                    f"  Asiento: {seat}" \
                    f"  Numero de vuelo: {self._number}" \
                    f"  Modelo: {self._aircraft.get_model()}" \
                    " |"
            esquinasYlaterales = '+' + '-'*(len(output)-2) + '+'
        
            lineas = [esquinasYlaterales, output, esquinasYlaterales]
            tarjeta = '\n'.join(lineas)
            print(tarjeta)
            print()
    #-----------------------------------------

    #-----------------------------------------
    def _parse_seat(self, seat):
        """_summary_ Analiza un numero de asiento para asegurarse de que es valido

        Args:
            seat (string): El asiento designado por un numero de fila y una letra (p.e. '12C' o '21F')

        Raises:
            ValueError: Si el asiento no tiene el formato correcto
            ValueError: Si el numero de fila o la letra del asiento no son validos

        Devuelve:
            row: El numero de fila
            letter: La letra del asiento

        Info:
            - rows, seat_letters = self._aircraft.seating_plan() Obtiene el numero de filas y las letras de los asientos
            - letter = seat[-1] Obtiene la letra del asiento
            - if letter not in seat_letters: Comprueba si la letra del asiento es válida
            - raise ValueError(f"La letra del asiento no es válida {letter}") Lanza una excepción si la letra del asiento no es válida
            - row_text = seat[:-1] Obtiene el numero de fila
            - try: \ Intenta convertir el numero de fila a entero
            - except ValueError: \ Si no se puede convertir a entero
            - raise ValueError(f"El numero de fila no es valido {row_text}") Lanza una excepción si el numero de fila no es valido
            - if row not in rows: Comprueba si el numero de fila es valido
            - raise ValueError(f"La fila no existe {row}") Lanza una excepción si el numero de fila no es valido
            - return row, letter Devuelve el numero de fila y la letra del asiento

        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"La letra del asiento no es válida {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"El numero de fila no es valido {row_text}")
        if row not in rows:
            raise ValueError(f"La fila no existe {row}")
        return row, letter
    #-----------------------------------------
    
    #-----------------------------------------
    def _passenger_seats(self):
        """_summary_ Genera una secuencia de tuplas de pasajeros y asientos

        Yields:
            passenger: El nombre del pasajero
            seat: El asiento del pasajero

        Info:
            - row_numbers, seat_letters = self._aircraft.seating_plan() Obtiene el numero de filas y las letras de los asientos
            - for row in row_numbers: Recorre las filas
            - for letter in seat_letters: Recorre las letras de los asientos
            - passenger = self._seating[row][letter] Obtiene el nombre del pasajero
            - if passenger is not None: Comprueba si el asiento esta ocupado
            - yield (passenger, f"{row}{letter}") Devuelve el nombre del pasajero y el asiento
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")
    #-----------------------------------------

#------------------------------------------------------------------------------------------------------
# FIN DE LA CLASE Flight
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
# Llamada con help para ver la documentacion de la clase y metodos
help(Flight)
