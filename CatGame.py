import tkinter as tk
from tkinter import messagebox

class gato:
    def __init__(self,tk, root):
        """
        Inicializa la clase 'gato'.

        Args:
            root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("3 EN RAYA")  # Título de la ventana
        self.matriz = [[None for _ in range(3)] for _ in range(3)]  # Matriz para los botones
        self.turno = "X"  # Jugador inicial
        
        self.crear_botones()  # Llama a la función para crear los botones

    def crear_botones(self):
        """
        Crea una cuadrícula de botones para el juego.
        Cada botón corresponde a una celda en el tablero.
        """
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.root, text='', width=5, height=2,
                                  command=lambda i=i, j=j: self.cambiar_valor(i, j))
                boton.grid(row=i, column=j)  # Coloca el botón en la cuadrícula
                self.matriz[i][j] = boton  # Guarda el botón en la matriz

    def cambiar_valor(self, i, j):
        """
        Cambia el valor del botón en la posición (i, j) y verifica el estado del juego.

        Args:
            i (int): Fila del botón.
            j (int): Columna del botón.
        """
        if self.matriz[i][j]['text'] == '':
            self.matriz[i][j]['text'] = self.turno  # Asigna el valor del turno actual
            if self.verificar_ganador():
                messagebox.showinfo("¡Ganaste!", f"El jugador {self.turno} ha ganado!")
                self.resetear()  # Reinicia el juego
            elif self.tablero_lleno():
                messagebox.showinfo("Empate", "El juego ha terminado en empate.")
                self.resetear()  # Reinicia el juego
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'  # Cambia el turno

    def verificar_ganador(self):
        """
        Verifica si hay un ganador en el juego.

        Returns:
            bool: True si hay un ganador, False en caso contrario.
        """
        # Combinaciones ganadoras
        combinaciones = [
            [(0, 0), (0, 1), (0, 2)],  # Fila 1
            [(1, 0), (1, 1), (1, 2)],  # Fila 2
            [(2, 0), (2, 1), (2, 2)],  # Fila 3
            [(0, 0), (1, 0), (2, 0)],  # Columna 1
            [(0, 1), (1, 1), (2, 1)],  # Columna 2
            [(0, 2), (1, 2), (2, 2)],  # Columna 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal
            [(0, 2), (1, 1), (2, 0)]   # Diagonal inversa
        ]
        for combinacion in combinaciones:
            if self.matriz[combinacion[0][0]][combinacion[0][1]]['text'] == self.turno and \
               self.matriz[combinacion[1][0]][combinacion[1][1]]['text'] == self.turno and \
               self.matriz[combinacion[2][0]][combinacion[2][1]]['text'] == self.turno:
                return True  # Se encontró un ganador
        return False  # No hay ganador

    def tablero_lleno(self): 
        """
        Verifica si el tablero está lleno.

        Returns:
            bool: True si el tablero está lleno, False en caso contrario.
        """
        for fila in self.matriz:
            for boton in fila:
                if boton['text'] == '':
                    return False  # Hay al menos una celda vacía
        return True  # Todas las celdas están llenas

    def resetear(self):
        """
        Reinicia el juego, limpiando el tablero y restableciendo el turno.
        """
        for fila in self.matriz:
            for boton in fila:
                boton['text'] = ''  # Limpia el texto de cada botón
        self.turno = "X"  # Restablece el turno a 'X'

# Crear la ventana principal
root = tk.Tk()
app = gato(root)  # Inicializa la aplicación
root.mainloop()  # Inicia el bucle de eventos