def conexion(r1,r2,r3):
    if (r1 or r2) and r3:
        print(r1,r2,r3,True)
    else:print(r1,r2,r3,False)

if __name__ == "__main__":
    print("r1 r2 r3   s")
    for i in range(2):
        for j in range(2):
            for k in range(2):
                conexion(i, j, k)
                

