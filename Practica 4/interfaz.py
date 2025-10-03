import tkinter as tk
from diagnosticar import diagnostico


def guardar_sintomas():
    sintomas = []
    for i, var in enumerate(variables):
        if var.get():
            sintomas.append(opciones[i])
    enfermedad = diagnostico(sintomas)
    if enfermedad is False:
        resultado_label.config(text="No se puede diagnosticar ninguna enfermedad")
    else:
        resultado_label.config(text=f"Esta enfermo de {enfermedad}")


opciones = ["congestion nasal", "fiebre", "tos", "dolor de cabeza", "nauseas", "cansancio", "perdida de olfato"]
root = tk.Tk()
root.geometry('500x500')
root.title('Diagnostico')

tk.Label(root, text="Seleccione sus Sintomas", font=("Arial", 14)).pack(pady=10)

variables = []
for sintoma in opciones:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=sintoma, variable=var)
    chk.pack(anchor='w')
    variables.append(var)

btn_guardar = tk.Button(root, text='Guardar', command=guardar_sintomas)
btn_guardar.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 10))
resultado_label.pack(pady=20)

root.mainloop()
