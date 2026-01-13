import getpass
import click
from core.verif import master_exist, create_master

@click.command()
def init():
    if master_exist():
        click.echo("Mot de passe maître déjà existant")
        return
    
    password = getpass.getpass("Entrez votre mot de passe maître: ")
    confirm = getpass.getpass("Confirmez votre mot de passe: ")
    if confirm != password:
        click.echo("Les mots de passe ne correspondent pas.")
        return
    
    create_master(password)
    click.echo("Mot de passe créé avec succès !")