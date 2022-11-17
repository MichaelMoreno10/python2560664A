from re import U


def main():
    print("Divisor de dos números ")
    j=int(input("Escriba el dividendo"))
    u=int(input("Escriba el divisor"))
    if j %u==0:
        print(f"La división es exacta. Cociente :{u // j}")
    else:
        print(f"La división es exacta . Cociente: {u//j}"
        f"Resto: {j%u}"
        )
if __name__=="__main__":
    main()