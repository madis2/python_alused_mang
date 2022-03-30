# Matis Russi
# Roger Niils
# IT-21

# Moodulid
import time
import random

#### Menu ####

print()
print("--------------------")
print("Kalevipoja otsingud")
print("--------------------")
print()
print()
print("Credits: Roger Niils, Matis Russi")
print()
print("Versioon: 0.5")
print()
print()
algus = int(input("[1] Start [2] Exit  "))
print()
if algus == 2:
    exit()
    
elif algus == 1:
    user_name = input("Mis on teie karakteri nimi?  ")
elif algus == 2:
    exit()

time.sleep(1)
print("Siin on sinu seikluse algus")
print()

#### Stats ####

health = 100
kuld = 10
attack = 1
defense = 1
relv = 0
mook_dmg = random.randint(15,20)
protsent = 30

# Funktsioon valikud võitluse jaoks.

def valikud():
    print('[1] Ründa vastast.')
    print('[2] Bloki (30% tõenäosus). ')
    print('[3] Ravi end 10 elu võrra.')
    
    valik = int(input('Vali enda tegevus: '))
    return valik

# Funktsioon kaklus võitluste jaoks. 

def kaklus(peasant_health, peasant_kuld, peasant_attack):
    global health
    global kuld
    global attack
    global defense
    global relv
    global mook_dmg
    global protsent
    
    while peasant_health >= 0 and health >= 0:
        valik = valikud()
        
        dmg = random.randint(5,10) # Kahju mis teed vastasele
        dmg = dmg*attack
        peasant_dmg = random.randint(1,5) # Kahju mis tehakse sulle
        peasant_dmg = peasant_dmg
        
        print('─────────────────────────────────────')
        
        if valik == 1:
            if relv == 0:
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
                mook_dmg = mook_dmg
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
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
            else:
                print(f'Blokk õnnestus')
                print('─────────────────────────────────────')
        else:
            health += 10
            peasant_dmg = random.randint(1,10) # Kahju mis tehakse sulle
            health -= peasant_dmg
            print(f'Vastane tegi sulle {peasant_dmg} kahju.')
            print(f'Sinu elud: {health}')
            print('─────────────────────────────────────')
            
    if peasant_health <= 0:
        print('Õnnitlen kunn, oled tapnud oma vastase!')
        kuld += peasant_kuld
        peasant_kuld -= peasant_kuld
    else:
        print('Muutusid pedeks ja sind tapeti koha peal!')
        print('The end!')

# Võitlus algab
        
print('Kohtad kurja talupoega kes tahab rünnata sind.') 
kaklus(50, random.randint(5,15), 1.5)