def shellsort(arreglo, criterio):
    n = len(arreglo)
    brecha = n // 2
    while brecha > 0:
        for i in range(brecha, n):
            temp = arreglo[i]
            j = i
            while j >= brecha and arreglo[j - brecha][criterio] > temp[criterio]:
                arreglo[j] = arreglo[j - brecha]
                j -= brecha
            arreglo[j] = temp
        brecha //= 2
    return arreglo

def merge_sort(arreglo, criterio):
    if len(arreglo) > 1:
        medio = len(arreglo) // 2
        mitad_izq = arreglo[:medio]
        mitad_der = arreglo[medio:]

        merge_sort(mitad_izq, criterio)
        merge_sort(mitad_der, criterio)

        i = j = k = 0
        while i < len(mitad_izq) and j < len(mitad_der):
            if mitad_izq[i][criterio] < mitad_der[j][criterio]:
                arreglo[k] = mitad_izq[i]
                i += 1
            else:
                arreglo[k] = mitad_der[j]
                j += 1
            k += 1

        while i < len(mitad_izq):
            arreglo[k] = mitad_izq[i]
            i += 1
            k += 1

        while j < len(mitad_der):
            arreglo[k] = mitad_der[j]
            j += 1
            k += 1
    return arreglo
