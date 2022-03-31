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

print("Siin on sinu seikluse algus")
time.sleep(1)
print()


#### Stats ####

health = 100
kuld = 10     # Kulda kasutame me skoorina mida näitame mängu lõpus     
attack = 1    # Attack muutuja korrutab su damageit ehk kahju, et teeksid rohkem viga vastasele mängu jooksul.
defense = 0   # See muutuja lisatakse juurde protsendile.
protsent = 30 # Protsent tõstab bloki õnnestumist.

# Funktsioon valikud võitluse jaoks.

def valikud():
    print(f'[1] Ründa vastast. (Kahju korrutaja {attack}%)')
    print(f'[2] Bloki ({protsent}% tõenäosus). ')
    print('[3] Ravi end 10 elu võrra.')
    
    valik = int(input('Vali enda tegevus: '))
    return valik

# Funktsioon kaklus võitluste jaoks. 

def kaklus(peasant_health, peasant_kuld, peasant_attack, xp_attack, xp_defense):
    global health
    global kuld
    global attack
    global defense
    global relv
    global mook_dmg
    global protsent
    global user_name
    
    while peasant_health >= 1 and health >= 1:
        valik = valikud()
        
        dmg = random.randint(5,10) # Kahju mis teed vastasele
        booster = dmg*attack
        peasant_dmg = random.randint(1,5) # Kahju mis tehakse sulle
        peasant_dmg = peasant_dmg
        
        print('─────────────────────────────────────')
        
        if valik == 1:
            if dmg >= 12:
                peasant_health -= dmg
                health -= peasant_dmg
                print(f'Kriitiline löök. Tegid {dmg} kahju')
                print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
                time.sleep(0.5)
            elif dmg in range(7,11):
                peasant_health -= dmg
                health -= peasant_dmg
                print(f'Hea löök. Tegid {dmg} kahju')
                print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
                time.sleep(0.5)
            else:
                peasant_health -= dmg
                health -= peasant_dmg
                print(f'Halb löök. Tegid {dmg} kahju')
                print(f'Vastane tegi sulle {peasant_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
                time.sleep(0.5)
        elif valik == 2:
            if random.randint(0,100) > protsent:
                health -= peasant_dmg
                print(f'Vastane tegi sulle {peasant_dmg}.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
                time.sleep(0.5)
            else:
                blokk = random.randint(1,3)
                peasant_health -= blokk
                print(f'Blokiga tegid {blokk} kahju.')
                print(f'Blokk õnnestus')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {peasant_health}')
                print('─────────────────────────────────────')
                time.sleep(0.5)
        else:
            health += 10
            peasant_dmg = random.randint(1,10) 
            health -= peasant_dmg
            print(f'Vastane tegi sulle {peasant_dmg} kahju.')
            print(f'Sinu elud: {health}')
            print('─────────────────────────────────────')
            time.sleep(0.5)
            
    if peasant_health <= 0:
        print(f'Õnnitlen {user_name}, oled tapnud oma vastase!')
        kuld += peasant_kuld          # Siin lisatakse kõik statid juurde karakterile.
        peasant_kuld -= peasant_kuld
        attack += xp_attack       
        defense += xp_defense
        protsent += defense
        time.sleep(3)
    else:
        print('Muutusid pedeks ja sind tapeti koha peal!')
        print('The end!')
        time.sleep(3)



# Seiklus algab
