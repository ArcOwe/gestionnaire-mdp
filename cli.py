import click
from commands.init import init
from commands.unlock import unlock

@click.group()
def cli():
    """Gestionnaire de mot de passe"""
    pass

cli.add_command(init)
cli.add_command(unlock)

if __name__ == "__main__":
    cli()