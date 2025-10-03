import tkinter as tk
from tkinter import messagebox
from motor_inferencia import diagnosticar, BASE_CONOCIMIENTO

def crear_interfaz():
    root = tk.Tk()
    root.title("Sistema de Diagnóstico Médico")
    root.geometry("750x600")
    root.resizable(False, False)
    root.configure(bg="#EAF2F8")

    # Paleta de azules
    COLOR_PRIMARIO = "#3498DB"
    COLOR_SECUNDARIO = "#5DADE2"
    COLOR_FONDO = "#EAF2F8"
    COLOR_TEXTO = "#1B2631"
    COLOR_BOTON = "#2E86C1"
    COLOR_BOTON_HOVER = "#2874A6"
    COLOR_BORDE = "#AED6F1"

    # Marco principal
    marco_principal = tk.Frame(root, bg=COLOR_FONDO, relief="flat", bd=0)
    marco_principal.pack(fill="both", expand=True, padx=15, pady=15)

    # Título
    titulo = tk.Label(
        marco_principal,
        text="Sistema de Diagnóstico de Enfermedades",
        font=("Arial", 16, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Panel izquierdo
    panel_izquierdo = tk.Frame(marco_principal, bg=COLOR_FONDO, relief="flat")
    panel_izquierdo.grid(row=1, column=0, padx=(0, 10), sticky="nsew")
    marco_principal.grid_columnconfigure(0, weight=1)

    frame_instrucciones = tk.Frame(panel_izquierdo, bg=COLOR_FONDO)
    frame_instrucciones.pack(fill="x", pady=(0, 10))

    instrucciones = tk.Label(
        frame_instrucciones,
        text="Ingrese los síntomas separados por coma:",
        font=("Arial", 12, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO,
        wraplength=400,
        justify="left"
    )
    instrucciones.pack(anchor="w")

    ejemplo_pequeno = tk.Label(
        frame_instrucciones,
        text="Ej: tos, fiebre, dolor de cabeza",
        font=("Arial", 10),
        bg=COLOR_FONDO,
        fg=COLOR_SECUNDARIO,
        justify="left"
    )
    ejemplo_pequeno.pack(anchor="w", pady=(2, 0))

    entrada_sintomas = tk.Text(
        panel_izquierdo,
        width=45,
        height=12,
        font=("Arial", 11),
        bg="white",
        fg=COLOR_TEXTO,
        relief="solid",
        bd=1,
        padx=10,
        pady=10,
        wrap=tk.WORD
    )
    entrada_sintomas.pack(pady=5, fill="both", expand=True)
    entrada_sintomas.config(highlightbackground=COLOR_BORDE, highlightcolor=COLOR_SECUNDARIO, highlightthickness=1)

    # Resultado
    frame_resultado = tk.Frame(panel_izquierdo, bg=COLOR_FONDO)
    frame_resultado.pack(fill="x", pady=10)

    titulo_resultado = tk.Label(
        frame_resultado,
        text="Resultado del Diagnóstico:",
        font=("Arial", 12, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO,
        justify="left"
    )
    titulo_resultado.pack(anchor="w")

    resultado_frame = tk.Frame(
        frame_resultado,
        bg="#D6EAF8",
        relief="solid",
        bd=1,
        height=60
    )
    resultado_frame.pack(fill="x", pady=(5, 0))
    resultado_frame.pack_propagate(False)

    resultado_label = tk.Label(
        resultado_frame,
        text="",
        font=("Arial", 12),
        fg=COLOR_PRIMARIO,
        bg="#D6EAF8",
        wraplength=400,
        justify="left",
        padx=10,
        pady=10
    )
    resultado_label.pack(fill="both", expand=True)

    # Función diagnóstico
    def diagnosticar_paciente():
        texto = entrada_sintomas.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Atención", "Por favor, escriba al menos un síntoma.")
            return
        sintomas = [s.strip() for s in texto.split(",") if s.strip()]
        resultado = diagnosticar(sintomas, BASE_CONOCIMIENTO)
        resultado_label.config(text=f"{resultado}")

    # Botón
    frame_boton = tk.Frame(panel_izquierdo, bg=COLOR_FONDO)
    frame_boton.pack(fill="x", pady=15)

    def on_enter_boton(e):
        boton.config(bg=COLOR_BOTON_HOVER, cursor="hand2")

    def on_leave_boton(e):
        boton.config(bg=COLOR_BOTON, cursor="")

    boton = tk.Button(
        frame_boton,
        text="Realizar Diagnóstico",
        font=("Arial", 13, "bold"),
        command=diagnosticar_paciente,
        bg=COLOR_BOTON,
        fg="white",
        activebackground=COLOR_PRIMARIO,
        activeforeground="white",
        bd=0,
        padx=25,
        pady=12,
        relief="flat"
    )
    boton.pack(pady=5)
    boton.bind("<Enter>", on_enter_boton)
    boton.bind("<Leave>", on_leave_boton)

    # Panel derecho: ejemplos
    panel_derecho = tk.Frame(
        marco_principal,
        bg="white",
        relief="solid",
        bd=1,
        width=250
    )
    panel_derecho.grid(row=1, column=1, padx=(10, 0), sticky="ns")
    panel_derecho.grid_propagate(False)
    panel_derecho.config(height=450)

    titulo_ejemplo = tk.Label(
        panel_derecho,
        text="Ejemplos de Entrada",
        font=("Arial", 13, "bold"),
        bg="white",
        fg=COLOR_TEXTO,
        pady=15
    )
    titulo_ejemplo.pack(fill="x")

    contenido_ejemplo = tk.Label(
        panel_derecho,
        text="• tos, dolor de cabeza\n\n• fiebre, tos, cansancio, pérdida del olfato\n\n• dolor de cabeza, nauseas\n\n• congestion nasal, fiebre, tos",
        font=("Arial", 11),
        bg="white",
        fg=COLOR_TEXTO,
        justify="left",
        wraplength=220,
        padx=15
    )
    contenido_ejemplo.pack(anchor="w", pady=10)

    info_frame = tk.Frame(panel_derecho, bg="#D6EAF8", relief="solid", bd=1)
    info_frame.pack(side="bottom", fill="x", pady=10, padx=10)

    info_text = tk.Label(
        info_frame,
        text="💡 Separe cada síntoma con comas\n💡 Sea específico con los síntomas\n💡 Incluya todos los síntomas relevantes",
        font=("Arial", 9),
        bg="#D6EAF8",
        fg=COLOR_TEXTO,
        justify="left",
        padx=10,
        pady=8
    )
    info_text.pack(anchor="w")

    root.mainloop()
