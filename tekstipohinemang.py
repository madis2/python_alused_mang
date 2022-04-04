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

print(f"Sinu nimi on {user_name}. \nOled otsimas kalevipoega, et leida tema saladus tugevusele.")
time.sleep(3)
print()


#### Stats ####

health = 100
kuld = 10     # Kulda kasutame me skoorina mida näitame mängu lõpus     
attack = 1    # Attack muutuja korrutab su damageit ehk kahju, et teeksid rohkem viga vastasele mängu jooksul.
defense = 0   # See muutuja lisatakse juurde protsendile.
protsent = 30 # Protsent tõstab bloki õnnestumist.
level = 0     # Muutuja mitmendal tasemel mängija on.

km = random.randint(50,150) # Lambine muutuja 

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
        print(f'Õnnitlen {user_name}!')
        kuld += peasant_kuld          # Siin lisatakse kõik statid juurde karakterile.
        peasant_kuld -= peasant_kuld
        attack += xp_attack           # Siin lisatakse juurde vastaselt saadud attack level
        defense += xp_defense         # Siin lisatakse juurde vastaseld saadud defense level
        protsent += defense           # Saadud defense level listakase juurde protsendile
        time.sleep(3)
    else:
        print('Muutusid pedeks ja sind tapeti koha peal!')
        print('The end!')
        time.sleep(3)
        exit()

if level == 0:
    print('TASE 1')
    print('─────────────────────────────────────')
    print('Alustad oma seiklust kalevipoja otsinguga.')
    time.sleep(2)
    print('Tee peal tuleb vastu kuri talupoeg.')
    time.sleep(2)
    print('"Sina varastasid mu kanamunad!"')
    print()
    time.sleep(2)
    print('Alustad võitlust talupojaga kanamunade üle. \nMida soovid teha?')
    
    kaklus(50,10,1,0.05,5)
    print('Talupoeg on koomas ja sa otsustad jätkata enda seiklust.')
    level += 1
if level == 1:
    print('TASE 2')
    print('─────────────────────────────────────')
    print(f'Läbisid {km} kilomeetrit')
    time.sleep(2)
    print('Liikusid edasi läände ja leidsid vanatädi. \nVanatädi soovitas liikuda edasi läände. \nEnda nime ta ei avaldanud.')
    time.sleep(5)
    print(f'Liikusid läände ning avastasid maja.')
    time.sleep(2)
    print('Majas sees oli kaks piraati.')
    print('Alustad võitlust ühe piraadiga. Teine vaatab pealt.')
    print()
    
    kaklus(60,15,1,0.1,2.5)
    
    print('Piraat Tõnu on teadvusetu.')
    time.sleep(2)
    print('Piraat Pets ründab sind.')
    print('Ta tundub tugevam kui Tõnu.')
    print()
    time.sleep(2)
    
    kaklus(70,20,1.25,0.2,2.5)
    kaklus()
