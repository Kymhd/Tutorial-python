"""
Un entier naturel de trois chiffres est dit cubique s'il est égale
à la somme des cubes de ses trois chiffres.
exemple : 153 est cubique car 153 = 1**3 + 5**3 + 3**3
"""
for i in range(100, 999):
    a = i // 100     #centaine
    b = (i % 100) // 10 #dizain
    c = i % 10 #un
    if (a**3) + (b**3) + (c**3) == i:
        print(i)
        
# 153
# 370
# 371
# 407