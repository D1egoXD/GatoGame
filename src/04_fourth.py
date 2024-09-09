import tkinter as tk

def button_click(x, y):
    print(f"Button clicked at position: ({x}, {y})")

# Crear la ventana principal
root = tk.Tk()
root.title("Buttons")

# Crear una cuadrícula de botones
for i in range(3):
    for j in range(3):
        button = tk.Button(root, width=10, height=3, command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j)

# Iniciar el bucle principal de la aplicación
root.mainloop()
