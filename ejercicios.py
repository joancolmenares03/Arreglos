def promedioArray():
    arreglo = input().split() #Crea uns variable tipo cadena que se convierte en lista con el metodo split

    x = 0                     #Variable auxiliar

    for i in arreglo:         #Debido a los elementos de la lista son de tipo cadena se usa este ciclo for para convertilos en flotantes
        arreglo[arreglo.index(i)] = float(i)

    for i in arreglo:         #Ciclo for para sumar el valor de cada elemento de la lista a la variable auxiliar
        x += i

    return x/len(arreglo)     #Retorna el valor de x dividido en la cantidad de elementos de la lista para dar el promedio

def lista():
    w = input().split()       #Crea uns variable tipo cadena que se convierte en lista con el metodo split
    v = input().split()       #Crea uns variable tipo cadena que se convierte en lista con el metodo split

    resultado = 0             #Variable auxiliar

    if len(w)==len(v):        #Condicional para comparar la longitud de las listas

        for i in w:           #Debido a los elementos de la lista son de tipo cadena se usa este ciclo for para convertilos en flotantes
            w[w.index(i)] = float(i)
        for i in v:           #Debido a los elementos de la lista son de tipo cadena se usa este ciclo for para convertilos en flotantes
            v[v.index(i)] = float(i)
    
        for x in w:           #Ciclo for para tomar los elementos de las listas por su indice comun y sumar el producto de estos elementos
            resultado += x*v[w.index(x)]
        return resultado

    else:                     #Else en caso de que la longitud de las listas no coincida
        print("La cantidad de elementos en los arreglos no coinciden")

def producto():
    w = input().split()       #Crea uns variable tipo cadena que se convierte en lista con el metodo split
    v = input().split()       #Crea uns variable tipo cadena que se convierte en lista con el metodo split

    resultado = []            #Variable auxiliar tipo lista

    if len(w) == len(v):      #Condicional para comparar la longitud de las listas

        for i in w:           #Debido a los elementos de la lista son de tipo cadena se usa este ciclo for para convertilos en flotantes
            w[w.index(i)] = float(i)
        for i in v:           #Debido a los elementos de la lista son de tipo cadena se usa este ciclo for para convertilos en flotantes
            v[v.index(i)] = float(i)

        for x in w:           #Ciclo for para agregar a la lista auxiliar el producto de dos elementos de igual indice
            resultado.append(x*v[w.index(x)])
        return resultado

    else:                     #Else en caso de que la longitud de las listas no coincida
        print("La cantidad de elementos en los arreglos no coinciden")

def main():
    print(promedioArray())
    print(lista())
    print(producto())

if __name__ == "__main__":
    main()
