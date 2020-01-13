#v ocamlu imamo slovarje iz stvari, ki jih znamo primerjat
#v pythonu pa (hash tabele), notr ne mormo dat seznama, ker nima hasha, od
#tega lahko lru faila: seznam pretvorimo v (immutable) tuple, ali frozen?set
# ki je tudi immutable 
#ocaml: seznam je zelo drugo kot tuple
#napiši dumb verzijo in daš čez @lru_cache

from functools import lru_cache

test_matrix = [[1, 2, 0],
               [2, 4, 5],
               [7, 0, 1]]

#def najpot(m, i, j):    ---- dobro je vključiti lokacijo, ker so indexi zastonj, gledamo od zunaj
#    if len(m) == i + 1:
#        return sum(m[i])
#    elif len(m[i]) == j + 1:
#        s = 0
#        for x in range(len(m)):
#            s += m[x]
#        return s
#    else:
#        return m[i][j] + max(naj_pot(m,i+1,j), naj_pot(m,i,j+1))

def max_sir(matrix):
    max_row = len(matrix)
    max_col = len(matrix[0])

    @lru_cache(maxsize=None)                    #(lru je last recent use, max je kolk za nazaj)
    def max_index(row, col):                    #pomožna funkcija samo z lokacijo
        if row == max_row or col == max_col:
            return 0
        return matrix[row][col] + max(max_index(row+1, col), max_index(row, col+1))
    
    return max_index(0, 0)

print(max_sir(test_matrix))
print(max_sir([[j for j in range(200)] for _ in range(200)]))