from argon2 import PasswordHasher #importe le module permettant de hash le mdp maitre
import getpass #permet d'entrer et de stocker temporairement un mdp sans l'afficher à l'écran
from argon2.exceptions import VerifyMismatchError #permet de gerer les exceptions et de vérifier les mdp
import os

ph = PasswordHasher() #fonction pour hash et salt

if not os.path.exists("master.hash"): #vérifie si le fichier qui stock le hash existe déjà
    password = getpass.getpass("Veuillez saisir votre mot de passe maitre")
    hash = ph.hash(password) #hash le mdp
    with open("master.hash", "w") as f: #crée un fichier texte pour stocker uniquement le hash
       f.write(hash)
    print("Mot de passe maitre enregistré")

with open("master.hash", "r") as f:
    stored_hash = f.read()

password2 = getpass.getpass("Entrer votre mot de passe: ") #variable pour stocker le mot de passe en clair (uniquement en mémoire,donc temporairement)

try:
    ph.verify(stored_hash, password2) #vérification du mdp
except VerifyMismatchError: #gestion de l'erreur mdp incorrect
    print("Mot de passe incorrect")
    
