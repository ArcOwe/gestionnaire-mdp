import click
import getpass
from core.verif import save_mdp

@click.command()
def newmdp():
    service = input("Entrez le service correspondant : ")
    nom_utilisateur = input("Entrez le nom d'utilisateur : ")
    password = getpass.getpass("Entrez un mot de passe : ")
   
    save_mdp(password, service, nom_utilisateur)
    click.echo("Nouveau mot de passe enregistré")

