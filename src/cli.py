# src/cli.py
import importlib
import sys
from pathlib import Path

import typer
from dotenv import load_dotenv

app = typer.Typer(help="Launcher for GitLab automation recipes.")
DEFAULT_PROVIDER = "gitlab"


def load_env():
    # Load .env if present
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def import_recipe(provider: str, recipe: str):
    """
    Import a recipe module by provider + recipe name.

    Conventions:
    - Files live under: src/providers/<provider>/recipes/
    - File name is snake_case: cleanup_old_pipelines.py
    - CLI name can be kebab-case: cleanup-old-pipelines
    """
    normalized = recipe.replace("-", "_")
    module_path = f"providers.{provider}.recipes.{normalized}"
    return importlib.import_module(module_path)


@app.command()
def run(
    recipe: str = typer.Argument(..., help="The recipe to run, e.g. cleanup-old-pipelines"),
    provider: str = typer.Option(
        DEFAULT_PROVIDER, "--provider", "-p", help="Provider name (default: gitlab)"
    ),
):
    """
    Run a given automation recipe.
    Recipes are simple Python modules with a `main()` function.
    """
    load_env()

    try:
        mod = import_recipe(provider, recipe)
    except ModuleNotFoundError as e:
        typer.echo(f"❌ Could not find recipe '{recipe}' for provider '{provider}'.")
        typer.echo(str(e))
        raise typer.Exit(code=1)

    if not hasattr(mod, "main"):
        typer.echo(f"❌ Recipe module '{mod.__name__}' has no main() function.")
        raise typer.Exit(code=1)

    # For now, recipes read config from env/YAML themselves.
    mod.main()


if __name__ == "__main__":
    app()
