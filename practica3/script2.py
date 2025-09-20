"""
Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal

Rg → Una persona puede votar
R1 → tiene más de 18 años
R2 → tiene credencial de elector
R3 → está en la lista nominal
"""
def puede_votar(r1, r2, r3):
    return (r1 and (r2 and r3))

if __name__ == "__main__":
    print("R1 | R2 | R3 | Rg")
    for i in reversed(range(2)):
        for j in reversed(range(2)):
            for h in reversed(range(2)):
                print(i, " | ", j, " | ", h, " | ", puede_votar(i, j, h))