# ==============================================================
#  lista_pasajeros.py  ·  Lista enlazada de pasajeros
#  ✍ ESTE ES EL ARCHIVO DONDE TRABAJAS TÚ
# --------------------------------------------------------------
#        head
#         |
#         v
#    +----------+---+    +----------+---+    +----------+---+
#    | #1005    | o-+--->| #1002    | o-+--->| #1009    | o-+---> None
#    | Diana 3C |   |    | Ana 1A   |   |    | Luis 7D  |   |
#    +----------+---+    +----------+---+    +----------+---+
#       data    next        data    next        data    next
#
#  Los pasajeros quedan en ORDEN DE LLEGADA (el orden en que reservaron).
#
#  ✅ Ya funcionan: la clase Nodo, el constructor __init__ y ingresar.
#  ✍ Tú implementas los otros 9 métodos. Reglas:
#     1. Recorre SIEMPRE con el patrón de la Unidad 3:
#            actual = self.head
#            while actual is not None:
#                ...
#                actual = actual.next
#     2. NO conviertas la lista enlazada en una list de Python para
#        buscar, modificar o eliminar (nada de list(), in, index, sort).
#     3. La ÚNICA list de Python permitida es el RESULTADO de listar()
#        y de filtrar_por_clase(): es la "caja" que Flask envía al navegador.
#     4. La clase NUNCA hace print() ni input(): RETORNA valores.
#     5. Para empezar un método, BORRA su línea  raise NotImplementedError(...)
#        y escribe tu código en su lugar.
# ==============================================================

from pasajero import Pasajero


class Nodo:
    """Un vagón del tren: lleva un pasajero (data) y el enganche al siguiente (next)."""

    def __init__(self, data):
        self.data = data          # el Pasajero que viaja en este vagón
        self.next = None          # al nacer no está enganchado a nadie


class ListaPasajeros:
    """Lista enlazada simple con todas las reservas del vuelo."""

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 1: el constructor
    # ----------------------------------------------------------
    def __init__(self):
        self.head = None          # la cabeza: el primer nodo (None = avión vacío)
        self.cantidad = 0         # cuántas reservas (nodos) hay

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 2: ingresar (= insertar_final de la Unidad 3)
    #    Engancha un pasajero NUEVO al final del tren.
    # ----------------------------------------------------------
    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)                # 1. creo el vagón con el pasajero

        if self.head is None:                 # 2a. Lista vacía:
            self.head = nuevo                 #     el nuevo es la cabeza
        else:                                 # 2b. Lista con nodos:
            actual = self.head                #     pongo el dedo en la cabeza
            while actual.next is not None:    #     mientras NO sea el último...
                actual = actual.next          #     ...avanzo un vagón
            actual.next = nuevo               #     el último ahora apunta al nuevo

        self.cantidad = self.cantidad + 1     # 3. hay una reserva más
        return True

    # ==========================================================
    # ✍ TAREA · implementa estos métodos (en este orden te será más fácil)
    # ==========================================================

    def esta_vacia(self):
        """Retorna True si no hay ninguna reserva; False si hay al menos una."""
        return self.head is None              # sin cabeza = nadie en el tren

    def longitud(self):
        """Retorna cuántas reservas hay."""
        return self.cantidad                  # ingresar/eliminar ya llevan la cuenta

    def listar(self):
        """Retorna una list con TODOS los Pasajero, de head al último."""
        resultado = []                        # la "caja de envío" para Flask
        actual = self.head                    # dedo en el primer vagón
        while actual is not None:             # mientras haya vagón
            resultado.append(actual.data)     # guardo el pasajero (no el nodo)
            actual = actual.next              # avanzo al siguiente vagón
        return resultado

    def buscar(self, numero):
        """Búsqueda lineal por número de reserva. Retorna Pasajero o None."""
        actual = self.head
        while actual is not None:
            if actual.data.numero == numero:  # ¿es la reserva buscada?
                return actual.data            # sí: retorno el Pasajero
            actual = actual.next
        return None                           # recorrí todo y no estaba

    def buscar_por_asiento(self, asiento):
        """Retorna el Pasajero sentado en ese asiento o None si está libre."""
        actual = self.head
        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_cedula(self, cedula):
        """Retorna el Pasajero con esa cédula o None."""
        actual = self.head
        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next
        return None

    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Cambia nombre, edad y asiento. True si lo modificó, False si no existe."""
        pasajero = self.buscar(numero)        # reutilizo buscar()
        if pasajero is None:                  # no existe esa reserva
            return False
        pasajero.nombre = nuevo_nombre        # el nodo no se mueve: solo cambia su carga
        pasajero.edad = nueva_edad
        pasajero.asiento = nuevo_asiento
        return True

    def eliminar(self, numero):
        """Desengancha el nodo con ese número. Retorna el Pasajero eliminado o None."""
        if self.head is None:                 # caso 1: lista vacía
            return None

        if self.head.data.numero == numero:   # caso 2: es la cabeza
            eliminado = self.head.data
            self.head = self.head.next        # la cabeza pasa al segundo vagón
            self.cantidad = self.cantidad - 1
            return eliminado

        anterior = self.head                  # caso 3: está en medio o al final
        actual = self.head.next
        while actual is not None:
            if actual.data.numero == numero:
                anterior.next = actual.next   # el anterior salta al vagón eliminado
                self.cantidad = self.cantidad - 1
                return actual.data
            anterior = actual                 # avanzo los dos dedos
            actual = actual.next

        return None                           # caso 4: no existe

    def filtrar_por_clase(self, clase):
        """Retorna una list con los pasajeros de esa clase, en el orden de la lista."""
        resultado = []
        actual = self.head
        while actual is not None:
            if actual.data.clase() == clase:  # "Ejecutiva" o "Económica"
                resultado.append(actual.data)
            actual = actual.next
        return resultado
