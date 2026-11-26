from itertools import product
k=0
for p in product('СОВЕСТЬ',repeat=7):
    if p.count('С')==2 and all(p.count(c)==1 for c in 'ОВЕИЬ'):
        s=''.join('Г' if c in 'ОЕИЬ' else 'С' for c in p)
        if not('ГГ' in s and 'СС' in s):
            k+=1
print(k)
