###############################################################################
# Želimo definirati pivotiranje na mestu za tabelo [a]. Ker bi želeli
# pivotirati zgolj dele tabele, se omejimo na del tabele, ki se nahaja med
# indeksoma [start] in [end].
#
# Primer: za [start = 0] in [end = 8] tabelo
#
# [10, 4, 5, 15, 11, 2, 17, 0, 18]
#
# preuredimo v
#
# [0, 2, 5, 4, 10, 11, 17, 15, 18]
#
# (Možnih je več različnih rešitev, pomembno je, da je element 10 pivot.)
#
# Sestavi funkcijo [pivot(a, start, end)], ki preuredi tabelo [a] tako, da bo
# element [ a[start] ] postal pivot za del tabele med indeksoma [start] in
# [end]. Funkcija naj vrne indeks, na katerem je po preurejanju pristal pivot.
# Funkcija naj deluje v času O(n), kjer je n dolžina tabele [a].
#
# Primer:
#
#     >>> a = [10, 4, 5, 15, 11, 2, 17, 0, 18]
#     >>> pivot(a, 1, 7)
#     3
#     >>> a
#     [10, 2, 0, 4, 11, 15, 17, 5, 18]
###############################################################################

# def pivot(a, start, end):
#    pivot = a[start]
#    for i in range(start + 1, end):
#        x = a[i]
#        if x < pivot:
#            a[start] = x
#            a[i] = pivot
#        else:
#            for j in range(end, i):
#                y = a[j]
#                if y < pivot:
#                    a[j] = pivot
#                    a[i] = y
#                else:


def pivot(table, start, end):
    # a = table[start: end+1]
    left_i = start + 1 #start + 0
    right_i = end #start + end
    pivot = table[start]
    while left_i < right_i:
        if table[left_i] < pivot:
            left_i += 1
        elif table[right_i] >= pivot:
            right_i -= 1
        else:
            table[left_i], table[right_i] = table[right_i], table[left_i]
    
    table[start] = table[right_i]
    table[right_i] = pivot
    return right_i

            


###############################################################################
# V tabeli želimo poiskati vrednost k-tega elementa po velikosti.
#
# Primer: Če je
#
#     >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#
# potem je tretji element po velikosti enak 5, ker so od njega manši elementi
#  2, 3 in 4. Pri tem štejemo indekse od 0 naprej, torej je "ničti" element 2.
#
# Sestavite funkcijo [kth_element(a, k)], ki v tabeli [a] poišče [k]-ti
# element po velikosti. Funkcija sme spremeniti tabelo [a]. Cilj naloge je, da
# jo rešite brez da v celoti uredite tabelo [a].
###############################################################################
def kth_element(table, k, start=0, end=None):
    if end is None:
        end = len(table) - 1
    i = pivot(table, start, end)
    if i == k:
        return table[i]
    elif i > k:
        return kth_element(table, k, start, i - 1)
    else:
        return kth_element(table, k - i, i + 1, end)

###############################################################################
# Tabelo a želimo urediti z algoritmom hitrega urejanja (quicksort).
#
# Napišite funkcijo [quicksort(a)], ki uredi tabelo [a] s pomočjo pivotiranja.
# Poskrbi, da algoritem deluje 'na mestu', torej ne uporablja novih tabel.
#
# Namig: Definirajte pomožno funkcijo [quicksort_part(a, start, end)], ki
#        uredi zgolj del tabele [a].
#
#     >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
#     >>> quicksort(a)
#     [2, 3, 4, 5, 10, 11, 15, 17, 18]
###############################################################################
def quicksort(a, start=0, end=None):
    if end is None:
        end = len(a) - 1
    if start >= end:
        return
    else:
        i = pivot(a, start, end)
        quicksort(a, start, i-1)
        quicksort(a, i+1, end)


        # qs1 = q(lower)
        # qs2 = q(upper)
        # qs1 @ [x] @ qs2



###############################################################################
# Če imamo dve urejeni tabeli, potem urejeno združeno tabelo dobimo tako, da
# urejeni tabeli zlijemo. Pri zlivanju vsakič vzamemo manjšega od začetnih
# elementov obeh tabel. Zaradi učinkovitosti ne ustvarjamo nove tabele, ampak
# rezultat zapisujemo v že pripravljeno tabelo (ustrezne dolžine).
# 
# Funkcija naj deluje v času O(n), kjer je n dolžina tarčne tabele.
# 
# Sestavite funkcijo [zlij(target, begin, end, list_1, list_2)], ki v del 
# tabele [target] med start in end zlije tabeli [list_1] in [list_2]. V primeru, 
# da sta elementa v obeh tabelah enaka, naj bo prvi element iz prve tabele.
# 
# Primer:
#  
#     >>> list_1 = [1,3,5,7,10]
#     >>> list_2 = [1,2,3,4,5,6,7]
#     >>> target = [-1 for _ in range(len(list_1) + len(list_2))]
#     >>> zlij(target, 0, len(target), list_1, list_2)
#     >>> target
#     [1,1,2,3,3,4,5,5,6,7,7,10]
#
###############################################################################
def zlij(target, start, end, list_1, list_2):
    i1 = 0
    i2 = 0
    while i1 < len(list_1) and i2 < len(list_2):
        if list[i1] <= list2[i2]:
            target[start + i1 + i2] = list_1[i1]
            i1 += 1
        else:
            target[start + i1 + i2] = list_2[i2]
            i2 += 1
    while i1 < len(list_1):
        target[start + i1 + i2] = list_1[i1]
        i1 += 1
    while i2 < len(list_2):
        target[start + i1 + i2] = list_1[i2]
        i2 += 1

#sortirni algoritem je stabilen, če enaki stvari pusti pri miru; mergesort je, če je merge, quicksort pa ne
#vse delaj z INDEKSI, so praktično zastonj

#V ocamlu bi dal pa inf na konc Num = NumI Int
#                                    | Inf 

###############################################################################
# Tabelo želimo urediti z zlivanjem (merge sort). 
# Tabelo razdelimo na polovici, ju rekurzivno uredimo in nato zlijemo z uporabo
# funkcije [zlij].
#
# Namig: prazna tabela in tabela z enim samim elementom sta vedno urejeni.
#
# Napišite funkcijo [mergesort(a)], ki uredi tabelo [a] s pomočjo zlivanja.
# Za razliko od hitrega urejanja tu tabele lahko kopirate, zlivanje pa je 
# potrebno narediti na mestu.
#
# >>> a = [10, 4, 5, 15, 11, 3, 17, 2, 18]
# >>> mergesort(a)
# [2, 3, 4, 5, 10, 11, 15, 17, 18]
###############################################################################


def mergesort(a):
    n = len(a) // 2
    a1 = a[0:n]
    a2 = a[n:len(a)]
    zlij(a, 0, len(a), mergesort(a1), mergesort(a2))