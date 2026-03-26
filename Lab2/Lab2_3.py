print('Докажите (путем перебора возможных значений), что для любых величин А, В, С типа Boolean следующие пары логических выражений имеют одинаковые значения (эквивалентны): ')
print('а) (A or B) и (B or A);')
print('б) (A and (B or C)) и ((A and B) or (A and C)).')
print('\na)')

bool_val = [False,True]
print('|   A   |   B   | A + B | B + A | is equal? |')
print('|-------|-------|-------|-------|-----------|')
CountAny=0
CountTrue=0
for A in bool_val:
    for B in bool_val:
        print(f'|{A:^7}|{B:^7}|{A or B:^7}|{B or A:^7}|{(A or B) == (B or A):^11}|')
        CountAny+=1
        if (A or B) == (B or A) :
            CountTrue+=1
print('|-------|-------|-------|-------|-----------|')

if (CountAny==CountTrue):
    print('ALL RIGHT!')
else:
    print('Oh, crap')

print('\nб)')
CountAny=0
CountTrue=0
print('| A | B | C |   A & (B + C)   |(A & B) + (A & C)| is equal? |')
print('|---|---|---|-----------------|-----------------|-----------|')
for A in bool_val:
    for B in bool_val:
        for C in bool_val:
            print(f'|{A:^3}|{B:^3}|{C:^3}|{A and (B or C):^17}|{(A and B)or(A and C):^17}|{(A and (B or C)) == ((A and B)or(A and C)):^11}|')
            CountAny += 1
            if (A and (B or C)) == ((A and B)or(A and C)):
                CountTrue += 1
print('|---|---|---|-----------------|-----------------|-----------|')

if (CountAny==CountTrue):
    print('ALL RIGHT!')
else:
    print('Oh, crap')