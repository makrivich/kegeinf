a=[int(x) for x in open('17.txt')]
m=min(x for x in a if abs(x)%10==3)
r=[]
for x,y in zip(a,a[1:]):
    if abs(min(x,y))%10==3 and x**2+y**2<m**2:
        r.append(x**2+y**2)
print(len(r),max(r))
