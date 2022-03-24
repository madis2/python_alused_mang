# Matis Russi
# IT-21

# Moodulid

import random

# Damage

health = 100
kuld = 10
attack = 1
defense = 1
relv = None

peasant_health = 50
peasant_kuld = 8
peasant_attack = 1
peasant_defense = 1

print('Kohtad kurja talupoega kes tahab rünnata sind.')

def valikud():
    print('[1] Ründa vastast')
    print('[2] Ravi end')
    
    valik = int(input('Vali enda tegevus: '))
    return valik

valik = valikud()

while peasant_health >= 0:
    
    if option == 1:
            