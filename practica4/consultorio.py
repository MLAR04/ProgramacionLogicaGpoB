from universo import universo

def diagnostico ():
    mapasintomas = {
    "1": "cansansio",
    "2": "congestionnasal",
    "3": "dolordecabeza",
    "4": "fiebre",
    "5": "nauseas",
    "6": "perdidadelolfato",
    "7": "tos"
    }
    print("INGRESE CON EL NUMERO DE OPCION LOS SINTOMAS QUE TIENE \nSI TIENE MAS DE UN SINTOMA SOLAMENTE SEPARE CON UN ESPACIO ENTRE CADA NUMERO\nDECIR UN EJEMPLO SI TIENE TOS Y DOLOR DE CABEZA USTED ESCRIBIRA 7,3 \n1. cansancio \n2. congestion nasal \n3. dolor de cabeza \n4. fiebre \n5. nauseas \n6. perdida del olfato \n7. tos \n")
    captura = input()
    nums = captura.split()
    sintomass = []
    for x in nums:
        if x in mapasintomas:
            sintomass.append(mapasintomas[x])
        else:
            print("opcion no valida, vuelva a intentarlo")
            diagnostico() 
    for enfermedad in universo:
        encontrado = True
        for sintoma in sintomass:
            if sintoma not in universo[enfermedad]["sintomas"] or len(sintomass) != len(universo[enfermedad]["sintomas"]) :
                encontrado = False

        if encontrado :
            print(f'tienes {enfermedad}')
    if not encontrado:
        print("con la informacion que nos brindas no podemos diagnosticarte")            


            
            


if __name__ == '__main__':
    diagnostico()