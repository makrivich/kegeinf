k=0
for s in open('9.txt'):
    a=[int(x) for x in s.split()]
    if a==sorted(a) and sum(x%2==0 for x in a)>3:
        k+=1
print(k)
