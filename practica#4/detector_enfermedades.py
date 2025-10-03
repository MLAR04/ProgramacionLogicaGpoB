import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests 
import io       

# BASE DE CONOCIMIENTO 

ENFERMEDADES = {
    "Gripe": ["tos", "dolor de cabeza"],
    "Covid": ["fiebre", "tos", "cansancio", "pérdida del olfato"],
    "Migraña": ["dolor de cabeza", "náuseas"],
    "Resfriado": ["congestión nasal", "fiebre", "tos"]
}

SINTOMAS_DISPONIBLES = sorted(list(set(s for sintomas in ENFERMEDADES.values() for s in sintomas)))

# Función para diagnosticar
def diagnosticar_enfermedad(sintomas_ingresados):
    diagnosticos_posibles = []
    if not sintomas_ingresados:
        return "Si no tienes sistomas, estas sano"
    for enfermedad, sintomas_requeridos in ENFERMEDADES.items():
        if all(sintoma in sintomas_ingresados for sintoma in sintomas_requeridos):
            diagnosticos_posibles.append(enfermedad)
    if not diagnosticos_posibles:
        return "No se pudo diagnosticar una enfermedad específica. Por favor, consulta a un médico."
    elif len(diagnosticos_posibles) == 1:
        return f"Diagnóstico: **{diagnosticos_posibles[0]}**"
    else:
        return f"Diagnóstico Múltiple: Podría ser **{', '.join(diagnosticos_posibles)}**. Por favor, consulta a un médico."


# Interfaz para diagnostico 
class DeteccionEnfermedadesApp:
    def __init__(self, master):
        self.master = master
        master.title("Clinica del Dr. Mario")
        master.geometry("800x600")
        master.resizable(False, False)
        
      
        try:
            # Imagen de fondo 
            response = requests.get("https://www.nintendo.com/eu/media/images/10_share_images/games_15/nintendo_3ds_download_software_7/SI_3DSDS_DrMarioMiracleCure_image1600w.jpg")
            response.raise_for_status() 
            image_data = response.content
            image_stream = io.BytesIO(image_data)
            original_image = Image.open(image_stream)
            
            #  Redimensionar y preparar para Tkinter 
            resized_image = original_image.resize((800, 600), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(resized_image)

            # Crear Canvas y Frame
            self.canvas = tk.Canvas(master, width=800, height=600)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
            
            self.content_frame = tk.Frame(self.canvas, bg="lightblue", padx=10, pady=10, highlightthickness=2, highlightbackground="darkblue")
           
            self.content_frame_id = self.canvas.create_window(400, 300, window=self.content_frame, anchor="center") 
            self.canvas.bind("<Configure>", self.on_canvas_resize)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de Red", f"No se pudo descargar la imagen de la URL: {e}")
            self.content_frame = tk.Frame(master, padx=10, pady=10, bg="lightgray")
            self.content_frame.pack(fill="both", expand=True)
        except Exception as e:
            messagebox.showerror("Error de Imagen", f"Error al cargar la imagen: {e}")
            self.content_frame = tk.Frame(master, padx=10, pady=10, bg="lightgray")
            self.content_frame.pack(fill="both", expand=True)

        self.vars = {}  
        
       
        tk.Label(self.content_frame, text="Selecciona tus Síntomas:", font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue").grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        
        row_num = 1
        col_num = 0
        for i, sintoma in enumerate(SINTOMAS_DISPONIBLES):
            var = tk.IntVar()
            self.vars[sintoma] = var
           
            cb = tk.Checkbutton(self.content_frame, text=sintoma.capitalize(), variable=var, bg="white", font=("Arial", 10), relief="flat")
            cb.grid(row=row_num, column=col_num, sticky="w", padx=5, pady=2)
            
            if i % 5 == 4:
                row_num += 1
                col_num = 0
            else:
                col_num += 1
                
     
        tk.Button(self.content_frame, text="Diagnosticar", command=self.obtener_diagnostico, 
                  font=("Arial", 12, "bold"), bg="red", fg="white", padx=10, pady=5).grid(row=row_num + 1, column=0, columnspan=2, pady=20)

        # Área de Resultados
        tk.Label(self.content_frame, text="Resultado:", font=("Arial", 12, "italic"), bg="lightblue").grid(row=row_num + 2, column=0, sticky="w")
        self.resultado_label = tk.Label(self.content_frame, text="", font=("Arial", 12), bg="white", wraplength=350, justify="left", fg="black")
        self.resultado_label.grid(row=row_num + 3, column=0, columnspan=2, sticky="ew")

    def on_canvas_resize(self, event):
        self.canvas.coords(self.content_frame_id, event.width / 2, event.height / 2)

    def obtener_diagnostico(self):
        sintomas_seleccionados = [sintoma for sintoma, var in self.vars.items() if var.get() == 1]
        resultado = diagnosticar_enfermedad(sintomas_seleccionados)
        self.resultado_label.config(text=resultado.replace('**', ''))

        
# aqui arrnca todo
if __name__ == "__main__":
    root = tk.Tk()
    app = DeteccionEnfermedadesApp(root)
    root.mainloop()
