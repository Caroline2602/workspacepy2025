# S(n) = 1+2+3+4+5 .... n
# S(n) = n + S(n-1)
# S(n) = n + n-1 + S(n-2)
## ...
## S(n) = n + n-1 +n-2 ...... +1
def sumarN(n):
    if n==1:
        return 1
    else:
        return n+sumarN(n-1)
def sumarNV2(n):
    if n!=1:
        return n+sumarNV2(n-1)
    else:
        return 1
print(sumarN(1000))
print(sumarNV2(1000))