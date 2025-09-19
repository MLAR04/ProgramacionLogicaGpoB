# Primer Caso. Saber si un número es multiplo de 6

def multiplo6(div2: bool, div3: bool) -> bool:
    return div2 and div3

if __name__ == "__main__":
    print("Rg | R1 | R2 \n-----------")
    for _ in range(2):
        for i in range(2):
            print(f"{multiplo6(_, i)}  | {_}  | {i}")
            print("----------")