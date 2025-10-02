import tkinter as tk
from tkinter import messagebox
from Enfermedades import Enfermedades, generar_diagnostico

sintomas = sorted({sintoma for sintomas in Enfermedades.values() for sintoma in sintomas})
#funcion boton
def confirmar():
    seleccion = [sintoma for sintoma, var in checkbox_vars.items() if var.get() == 1]
    diagnostico = generar_diagnostico(seleccion)
    messagebox.showinfo("Resultado", diagnostico)

root = tk.Tk()
root.title("Diagnóstico")
root.geometry("300x400")  
titulo = tk.Label(root, text="Diagnóstico", font=("Arial", 18, "bold"))
titulo.pack(pady=15)

subtitulo = tk.Label(root, text="Seleccione sus síntomas:", font=("Arial", 12))
subtitulo.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

checkbox_vars = {}
#checkbox
for sintoma in sintomas:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(frame, text=sintoma, variable=var, font=("Arial", 11))
    checkbox.pack(anchor="w", padx=20)
    checkbox_vars[sintoma] = var
#boton
btn = tk.Button(root, text="Confirmar", command=confirmar, font=("Arial", 12, "bold"), bg="lightblue")
btn.pack(pady=20)

root.mainloop()
