from functools import lru_cache

# Cilj: izračunajte vrednosti Fibonaccijevega zaporadja za 100, 500, 1000,
# 10**5, and 10**6 člen.
# Za vsako definicijo preizkusite kako pozne člene lahko izračuante in poglejte
# zakaj se pojavi problem (neučinkovitost, pregloboka rekurzija,
# premalo spomina ...).

# Definirajte naivno rekurzivno različico.
# Omejitev: Prepočasno.
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# Z uporabo dekoratorja izboljšajte naivno različico.
# Omejitev: Preseže največjo dovoljeno globino rekurzija za ~350.
@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 2:
        return 1
    return fib_cache(n-1) + fib_cache(n-2)


# Nariši drevo klicov za navadno rekurzivno fib funkcijo pri n=5 in
# ugotovi kateri podproblemi so klicani večkrat.

# Definirajte rekurzivno memoizirano funkcijo fib brez uporabe dekoratorja.
# Omejitev: Preseže največjo dovoljeno globino rekurzija za ~1000.
def fib_memo_rec(n):
    memo = {}
    def fib_inner(i):
        if i <= 2:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = fib_inner(i-1) + fib_inner(i-2)
        return memo[i]

    return fib_inner(n)

# Na katere podprobleme se direktno sklicuje rekurzivna definicija fib?

# Definirajte fib ki gradi rezultat od spodaj navzgor (torej računa in si zapomni
# vrednosti od 1 proti n.)
def fib_memo_iter(n):
    memo = {1: 1, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

# Izboljšajte prejšnjo različico tako, da hrani zgolj rezultate, ki jih v
# nadaljevanju nujno potrebuje.
def fib_iter(n):
    pp = 0
    p = 1
    for i in range(3, n+2):
        pp, p = p, pp+p
    return p

print(fib_iter(50))