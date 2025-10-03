from base_conocimiento import Enfermedades


def diagnostico(x):
    for i in Enfermedades:
        if Enfermedades[i] == x:
            return i
    return False




