import click
from commands.init import init
from commands.unlock import unlock
from commands.newmdp import newmdp

@click.group()
def cli():
    """Gestionnaire de mot de passe"""
    pass

cli.add_command(init)
cli.add_command(unlock)
cli.add_command(newmdp)

if __name__ == "__main__":
    cli()