def multiplo(x):
    if x%2 == 0:
        r1 = True
    else:
         r1 =False
    if x%3==0:
            r2= True
    else: r2 =False
    print (r1, r2, r1 and r2)

if __name__ == '__main__':
    print("  r1   r2   s")
    multiplo(12)
    multiplo(8)
    multiplo(9)
    multiplo(1)