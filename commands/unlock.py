import click
import getpass
from core.verif import verify_master, master_exist

@click.command()
def unlock():
    password = getpass.getpass("Entrez votre mot de passe maître: ")
    if verify_master(password):
        click.echo("Accès autorisé")
    else:
        click.echo("Mot de passe incorrect")
