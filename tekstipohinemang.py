# Matis Russi
# IT-21

# Moodulid

import random

# Damage

health = 100
kuld = 10
attack = 1
defense = 1
relv = 1

peasant_health = 0
peasant_kuld = 0
peasant_attack = 0
peasant_defense = 0

def peasant():
    global peasent_health
    global peasant_kuld
    global peasant_attack
    global peasant_defense
    
    peasant_health = 50
    peasant_kuld = 8
    peasant_attack = 1
    peasant_defense = 1

mook_dmg = random.randint(5,15)

print('Kohtad kurja talupoega kes tahab rünnata sind.')

def valikud():
    print('[1] Ründa vastast.')
    print('[2] Bloki (30% tõenäosus). ')
    print('[3] Ravi end 10 elu võrra.')
    
    valik = int(input('Vali enda tegevus: '))
    return valik

def kaklus(peasant_health, peasant_kuld, peasant_attack, peasant_defense):
    global health
    global kuld
    global attack
    global defense
    global relv
    
    while peasant_health >= 0:
        valik = valikud()
        
        dmg = random.randint(5,15) # Kahju mis teed vastasele
        peasant_dmg = random.randint(1,10) # Kahju mis tehakse sulle 
        protsent = 30
        
        print('─────────────────────────────────────')
        
        if valik == 1:
            if relv == None:
                if dmg >= 12:
                    peasant_health -= dmg
                    health -= peasant_dmg
                    print(f'Kriitiline löök. Tegid {dmg} kahju')
                    print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                    print(f'Sinu elud: {health}')
                    print(f'Vastase elud: {peasant_health}')
                    print('─────────────────────────────────────')
                elif dmg in range(7,11):
                    peasant_health -= dmg
                    health -= peasant_dmg
                    print(f'Hea löök. Tegid {dmg} kahju')
                    print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                    print(f'Sinu elud: {health}')
                    print(f'Vastase elud: {peasant_health}')
                    print('─────────────────────────────────────')
                else:
                    peasant_health -= dmg
                    health -= peasant_dmg
                    print(f'Halb löök. Tegid {dmg} kahju')
                    print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                    print(f'Sinu elud: {health}')
                    print(f'Vastase elud: {peasant_health}')
                    print('─────────────────────────────────────')
            else:
                peasant_health -= mook_dmg
                health -= peasant_dmg
                print(f'Tegid mõõgaga {mook_dmg} kahju.')
                print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
        elif valik == 2:
            if random.randint(0,100) > protsent:
                health -= peasant_dmg
                print(f'Vastane tegi sulle {peasant_dmg}.')
                print(f'Sinu elud: {health}')
                print('─────────────────────────────────────')
            else:
                blokk = random.randint(0,3)
                peasant_health -= blokk
                print(f'Blokeerides löögi tegid vastasele {blokk} kahju.')
                print('─────────────────────────────────────')
        else:
            health += 10
            peasant_dmg = random.randint(1,10) # Kahju mis tehakse sulle
            health -= peasant_dmg
            print(f'Vastane tegi sulle {peasant_dmg} kahju.')
            print(f'Sinu elud: {health}')
            print('─────────────────────────────────────')
            
kaklus(150, 10, 10)
