import click #module pour CLI
import getpass

@click.group() #permet d'introduire plusieurs commandes
def cli():
    """Gestionnaire de mot de passe""" #nom du CLI
    pass

if __name__ == "__main__":
    cli()