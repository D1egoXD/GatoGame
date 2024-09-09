import tkinter as tk
from tkinter import messagebox

class MatrizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Matriz 3x3")
        self.matriz = [[None for _ in range(3)] for _ in range(3)]
        self.turno = "X"
        
        self.crear_botones()

    def crear_botones(self):
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.root, text='', width=5, height=2,
                                  command=lambda i=i, j=j: self.cambiar_valor(i, j))
                boton.grid(row=i, column=j)
                self.matriz[i][j] = boton

    def cambiar_valor(self, i, j):
        if self.matriz[i][j]['text'] == '':
            self.matriz[i][j]['text'] = self.turno
            if self.verificar_ganador():
                messagebox.showinfo("¡Ganaste!", f"El jugador {self.turno} ha ganado!")
                self.resetear()
            elif self.tablero_lleno():
                messagebox.showinfo("Empate", "El juego ha terminado en empate.")
                self.resetear()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_ganador(self):
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
                return True
        return False

    def tablero_lleno(self):
        for fila in self.matriz:
            for boton in fila:
                if boton['text'] == '':
                    return False
        return True

    def resetear(self):
        for fila in self.matriz:
            for boton in fila:
                boton['text'] = ''
        self.turno = "X"

# Crear la ventana principal
root = tk.Tk()
app = MatrizApp(root)
root.mainloop()