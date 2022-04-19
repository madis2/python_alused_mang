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
algus = int(input("[1] Start [2] Exit [3] Load "))
print()
if algus == 2:
    exit()
    
elif algus == 1:
    user_name = input("Mis on teie karakteri nimi?  ")
elif algus == 3:
    with open(f"SAVE.txt", "r")as f:
        for rida in f:
            a = rida.split(" ")
            user_name = a[0]
            health = int(a[1])
            kuld = int(a[2])
            attack = float(a[3])
            defense = int(a[4])
            protsent = int(a[5])
            level = int(a[6])

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

# Funktsioon menu tasemete vahel.

def menu():
    print('[1] Jätka mängu.')
    print('[2] Lahku mängust (AUTOSAVE).')
    
    valik2 = int(input('Vali enda tegevus: '))
    
    if valik2 == 2:
        with open(f"SAVE.txt", "w+")as f: # Siin autosaveib mäng statid.
            f.write(f"{user_name} ")
            f.write(f"{health} ")
            f.write(f"{kuld} ")
            f.write(f"{attack} ")
            f.write(f"{defense} ")
            f.write(f"{protsent} ")
            f.write(f"{level} ")
        
        exit()

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
        peasant_dmg = random.randint(3,10) # Kahju mis tehakse sulle
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
        
        with open(f"SAVE.txt", "w+")as f: # Siin autosaveib mäng statid.
            f.write(f"{user_name} ")
            f.write(f"{health} ")
            f.write(f"{kuld} ")
            f.write(f"{attack} ")
            f.write(f"{defense} ")
            f.write(f"{protsent} ")
            f.write(f"{level} ")
             
    else:
        print('Muutusid pedeks ja sind tapeti koha peal!')
        print('The end!')
        time.sleep(3)
        exit()

# Mäng algab.

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
    print()
    time.sleep(2)
    
    kaklus(50, random.randint(7,10), 1, 0.05, 1)
    print('Talupoeg on koomas ja sa otsustad jätkata enda seiklust.')
    print()
    print('+0.05 ATTACK')
    print('+1% DEFENSE')
    level += 1
    time.sleep(3)
    menu()
    print()
    
    
if level == 1:
    print('TASE 2')
    print('─────────────────────────────────────')
    print(f'Läbisid {random.randint(50,150)} kilomeetrit')
    time.sleep(2)
    print('Liikusid edasi läände ja leidsid vanatädi. \nVanatädi soovitas liikuda edasi läände. \nEnda nime ta ei avaldanud.')
    time.sleep(5)
    print(f'Liikusid läände ning avastasid maja.')
    time.sleep(2)
    print('Majas sees oli kaks piraati.')
    print('Alustad võitlust ühe piraadiga. Teine vaatab pealt.')
    print()
    
    kaklus(60, random.randint(10,15), 1.5, 0.03, 2)
    
    print('Piraat Tõnu on teadvusetu.')
    time.sleep(2)
    print('Piraat Pets ründab sind.')
    print('Ta tundub tugevam kui Tõnu.')
    print()
    time.sleep(2)
    
    kaklus(70, random.randint(15,20), 2, 0.04, 2)
    
    print('Oled mõlemad piraadid hukanud')
    time.sleep(2)
    print('Jätkad oma seiklust läände.')
    level += 1
    
    print('+0.07 ATTACK')
    print('+4% DEFENSE')
    time.sleep(3)
    menu()
    print()
    
if level == 2:
    print('TASE 3')
    print('─────────────────────────────────────')
    print(f'Läbisid {50,150} kilomeetrit.')
    time.sleep(2)
    print('Oled pikalt liikunud läände ja edusamme nähtaval ei ole.')
    time.sleep(2)
    print('Teed väikse puhkepausi et süüa ja taastada energia ja tervis.')
    health += 20
    time.sleep(5)
    print()
    print('Taastasid 20 elu.')
    print()
    time.sleep(2)
    print('Puhkepausi tehes äkiliselt rünnatakse sind seljatagant.')
    print('Vastane lõi mööda ning valmistud sõdimiseks.')
    
    kaklus(85, random.randint(20,25), 3, 0.1, 3)
    print('Võitsid vastase kuid siiamaani ei saa aru kes või mis see on.')
    time.sleep(2)
    print('Sind ei huvita ning jätkad seiklust')
    print()
    time.sleep(2)
    print('+0.1 ATTACK')
    print('+3% DEFENSE')
    time.sleep(3)
    menu()
    print()
    level += 1

if level == 3:
    print('TASE 4')
    print('─────────────────────────────────────')
    print(f'Läbisid {random.randint(50,150)} kilomeetrit.')
    time.sleep(2)
    print('Leiad posteri kus tuleb välja, et oled pärast eelnevaid mõrvu \nkuulutatud tagaotsitavaks')
    time.sleep(3)
    print(f'Sinu mõrvamise autasu on {kuld}')
    time.sleep(2)
    print('Kõnnid edasi mitte midagi arvates sellest.')
    time.sleep(2)
    print('Sulle tuleb vastu rüütel.')
    print('Räägid temaga juttu ja siis ta avastab, et oled tagaotsitav.')
    time.sleep(2)
    print('"Vabandust {user_name} oli tore vestelda aga \nkahjuks ei jää mul muud üle kui tappa sind."')
    print()
    time.sleep(3)
    print('Alustad võitlust rüütliga.')
    print('Rüütlil on raudrüü seljas kuid oled piisavalt tugev et võita.')
    
    kaklus(100, random.randint(20,30), 5, 0.5, 7)
    
    time.sleep(2)
    print('Sul vedas, et võitsid.')
    time.sleep(2)
    print('Mõtled endaviisi, et hakkad lähemale jõudma kalevipojale.')
    print('+0.5 ATTACK')
    print('+7% DEFENSE')
    time.sleep(3)
    menu()
    print()
    
if level == 4:
    print('TASE 5')
    print('─────────────────────────────────────')
    print(f'Läbisid {random.randint(50,150)} kilomeetrit.')
    time.sleep(2)
    print('Näed kaugelt suurt mehikest kuid ')
    time.sleep(3)
    print('Sulle tuleb vastu kalevipoja alluv.')
    time.sleep(2)
    print('"Kes sa selline oled?"')
    print()
    print('"Soovin kalevipojaga rääkida."')
    time.sleep(3)
    print('Keegi ei räägi temaga peale minu.')
    print('"Pead ennem minust läbi saama."')
    time.sleep(3)
    print('Alustad võitlust kalevipoja alluvaga.')
    print('Ta alluv tundub tugev. Eeldan, et kalevipoeg on veel tugevam.')
    
    kaklus(120, random.randint(30,50), 10, 1.0, 10)
    
    time.sleep(2)
    print('"Oled minust tugevam. Austan seda."')
    time.sleep(2)
    print('Oled valmistunud kalevipoja saladust lahti arutama.')
    print('+1 ATTACK')
    print('+10% DEFENSE')
    time.sleep(3)
    menu()
    print()

if level == 5:
    print('TASE 6')
    print('─────────────────────────────────────')
    print(f'Oled jõudnud sihtpunkti.')
    time.sleep(2)
    print("Lähed vestled kalevipojaga.")
    time.sleep(3)
    print("Ta ei ole nõus saladust väljastama ennem kui temaga võitled.")
    time.sleep(3)
    print('Alustad poolsõbralikku kaklust kalevipojaga.')
    kaklus(175, random.randint(50,100), 15, 5, 20)
    
    time.sleep(3)
    print('"Hah. Tegelikult polegi mul saladust."')
    time.sleep(3)
    print('Olen lihtsalt saavutanud tugevuse sünnist alates kakeldes ja töö tegemisega.')
    time.sleep(3)
    print('Kalevipoja "saladus" valmistab sulle pettumust ning lahkud.')
    time.sleep(3)
    
    
    
    print()
    print("--------------------")
    print("MÄNG LÄBI!")
    print("--------------------")
    print(f'SKOOR: {kuld}')
    print("--------------------")
    print()
    print("Credits: Roger Niils, Matis Russi")
    print() 
