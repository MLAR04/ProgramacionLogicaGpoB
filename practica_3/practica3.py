"""
Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.
r1: divisible entre 2
r2: divisible entre 3
multiplode6 <-> r1 && r2
r1 - r2 - s
v  -  v  - v
v  -  f  - f
f  -  v  - f
f  -  f  - f 
"""
def multiplo6(x):
    if x%2==0 and x%3==0:
        print(x,"es multiplo de 6")
    else: (x,"no es multiplo de 6")
    print("r1\t\tr2\t\tS ")
    print("--------------------")
    for r1 in [True, False]:
        for r2 in [True, False]:
            resultado = r1 and r2
            print(f"{r1}\t{r2}\t{resultado}")


"""
Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal.
r1: si tiene más de 18 años
r2: tiene credencial de elector
r3: está en la lista nominal
puedeVotar <-> r1 && r2 && r3
r1 - r2 - r3 - s
v  - v  - v  - v
v  - f  - v  - f
v  - v  - f  - f
f  - v  - v  - f
f  - f  - v  - f
f  - v  - f  - f
v  - f  - f  - f
f  - f  - f  - f
"""
def puedeVotar(x,y,z):
    print('votar')
    if(x=='si' and y=='si' and z=='si'):
        print("puedes votar")
    else: print("no puede votar")
    print("r1\t\tr2\t\tr3\t\tS ")
    print("----------------------")
    for r1 in [True, False]:
        for r2 in [True, False]:
            for r3 in [True, False]:
                resultado = r1 and r2 and r3
                print(f"{r1}\t{r2}\t{r3}\t{resultado}")

"""
Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona.
r1: tiene Wi-Fi activado
r2: cable Ethernet conectado,
r3: además el módem funciona
conectarseInternet <-> (r1 || r2) && r3
r1 - r2 - r3 - s
v  - v  - v  - v
v  - v  - f  - f
v  - f  - v  - v
f  - v  - v  - v
v  - f  - f  - f
f  - v  - f  - f
f  - f  - v  - f
f  - f  - f  - f
"""
def conectarInternet(x,y,z):
    print('Internet')
    if ((x=="si" or y=="si") and z =='si'):
        print("se puede conectar a internet")
    else: print("no se puede conectar a internet")
    print("r1\t\tr2\t\tr3\t\tS ")
    print("----------------------")
    for r1 in [True, False]:
        for r2 in [True, False]:
            for r3 in [True, False]:
                resultado = (r1 or r2) and r3
                print(f"{r1}\t{r2}\t{r3}\t{resultado}")


if __name__ == '__main__':
    # #1
    multiplo6(24)

    # #2
    puedeVotar('si','no','si')

    # #3
    conectarInternet('si', 'si', 'no')

