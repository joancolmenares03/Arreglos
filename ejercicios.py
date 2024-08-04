def promedioArray():
    arreglo = input().split()
    x = 0
    for i in arreglo:
        arreglo[arreglo.index(i)] = float(i)
    for i in arreglo:
        x += i
    return x/len(arreglo)

def lista():
    w = input().split()
    v = input().split()
    resultado = 0
    for i in w:
        w[w.index(i)] = float(i)
    for i in v:
        v[v.index(i)] = float(i)
    
    for x in w:
        resultado += x*v[w.index(x)]
    return resultado

def producto():
    w = input().split()
    v = input().split()
    resultado = []
    for i in w:
        w[w.index(i)] = float(i)
    for i in v:
        v[v.index(i)] = float(i)

    for x in w:
        resultado.append(x*v[w.index(x)])
    return resultado

def main():
    print(promedioArray())
    print(producto())
    print(lista())

if __name__ == "__main__":
    main()
