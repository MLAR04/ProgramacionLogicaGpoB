from itertools import product

# Rules and stuff
def div_by_2(n) -> bool:
    return n % 2 == 0

def div_by_3(n) -> bool:
    return n % 3 == 0

def mult_of_6(n) -> bool:
    return div_by_2(n) and div_by_3(n)

def older_than_18(n) -> bool:
    return n > 18

def can_vote(person: dict) -> bool:
    # person = {"age": int, "credencial": bool, "lista": bool}
    return older_than_18(person["age"]) and person["credencial"] and person["lista"]

def connect_internet(comp: dict) -> bool:
    # comp = {"wifi": bool, "ethernet": bool, "modem": bool}
    return (comp["wifi"] or comp["ethernet"]) and comp["modem"]

# Table Templates
def table1(n: int = None, full: bool = True):
    header = ["D2", "D3", "M6 = D2 AND D3"]
    if full or n is None:
        rows = [[D2, D3, D2 and D3] for D2, D3 in product([True, False], repeat=2)]
    else:
        D2, D3 = div_by_2(n), div_by_3(n)
        rows = [[D2, D3, D2 and D3]]
    return header, rows

def table2(person: dict = None, full: bool = True):
    header = ["A", "C", "L", "V = A AND C AND L"]
    if full or person is None:
        rows = [[A, C, L, A and C and L] for A, C, L in product([True, False], repeat=3)]
    else:
        A = older_than_18(person["age"])
        C = person["credencial"]
        L = person["lista"]
        rows = [[A, C, L, A and C and L]]
    return header, rows

def table3(comp: dict = None, full: bool = True):
    header = ["W", "E", "M", "C = (W OR E) AND M"]
    if full or comp is None:
        rows = [[W, E, M, (W or E) and M] for W, E, M in product([True, False], repeat=3)]
    else:
        W, E, M = comp["wifi"], comp["ethernet"], comp["modem"]
        rows = [[W, E, M, (W or E) and M]]
    return header, rows

# Base Table
def show_table(header, rows):
    widths = [max(len(str(x)) for x in [h] + [r[i] for r in rows]) for i, h in enumerate(header)]
    def fmt(row):
        return " | ".join(str(v).ljust(widths[i]) for i, v in enumerate(row))
    print(fmt(header))
    print("-+-".join("-"*w for w in widths))
    for row in rows:
        print(fmt(row))

# Print em individually
def example_table1(n: int):
    header, rows = table1(n=n, full=False)
    show_table(header, rows)
    M6 = rows[0][2]  # result value
    print(f"Conclusión: {n} {"es" if M6 else "NO es"} múltiplo de 6.\n")

def example_table2(person: dict):
    header, rows = table2(person=person, full=False)
    show_table(header, rows)
    V = rows[0][3]  # result value
    print(f"Conclusión: La persona {"puede" if V else "NO puede"} votar.\n")

def example_table3(comp: dict):
    header, rows = table3(comp=comp, full=False)
    show_table(header, rows)
    C = rows[0][3]  # result value
    print(f"Conclusión: La computadora {"puede" if C else "NO puede"} conectarse a Internet.\n")

# How its used
example_table1(12)
example_table1(14)

example_table2({"age": 20, "credencial": True, "lista": True})
example_table2({"age": 16, "credencial": True, "lista": True})
example_table2({"age": 25, "credencial": False, "lista": True})

example_table3({"wifi": True, "ethernet": False, "modem": True})
example_table3({"wifi": False, "ethernet": True, "modem": False})
example_table3({"wifi": False, "ethernet": False, "modem": True})
