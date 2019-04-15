import itertools
country=['America','German','England','Franch','Russa','Italy']
name=['A','B','C','D','E','F']

pos=itertools.permutations(name)

for i in list(pos):
    if i[0] in 'ACE' or i[1] in 'ACE' or i[4] in 'ACE':
        continue
    if i[1] in 'BF':
        continue
    if i[3] == 'A' or i[5] == 'C':
        continue
    if i[0] == 'B' or i[3] == 'C':
        continue
    print(list(zip(country,i)))
    print(sorted(zip(country,name), key=lambda t: t[1])) #sorted, lambda


#_ = [print(i) for p in __import__('itertools').permutations('美俄德法意英') if all([p[0] not in "美俄德法", p[1] not in "德美", p[2] not in "美俄德意法", p[4] not in "美俄德", p[5] not in "德"]) for i in zip('ABCDEF', p)] #solve in one line