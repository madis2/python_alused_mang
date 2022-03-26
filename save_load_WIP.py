# Roger Niils
# IT-21


import pickle
import os

# Teeme listi
asjad = ["health", "kuld", "attack", "defense", "relv"]

# Prindime listi
print("Elus")
print(asjad)

# Salvestame listi
pickle.dump(asjad, open("asjad.txt", "wb"))

# Muudame
asjad.remove("health")
asjad.remove("kuld")
asjad.remove("attack")
asjad.remove("defense")

# Prindime listi
print("Surnud")
print(asjad)

# Laeme save data
asjad = pickle.load(open("asjad.txt", "rb"))

# Prindime listi
print("Elus")
print(asjad)
