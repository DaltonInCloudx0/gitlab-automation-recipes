# src/providers/gitlab/recipes/cleanup_old_pipelines.py
"""
Cleanup old GitLab pipelines.

Features:
- Keep last N pipelines
- Or delete older than X days
- Dry-run mode by default
"""

import datetime as dt
import os
from typing import Optional

import gitlab
import typer

from dotenv import load_dotenv

app = typer.Typer(add_completion=False)


def get_gitlab_client():
    base_url = os.environ.get("GITLAB_URL")
    token = os.environ.get("GITLAB_TOKEN")

    if not base_url or not token:
        raise SystemExit("GITLAB_URL and GITLAB_TOKEN must be set in environment or .env")

    gl = gitlab.Gitlab(url=base_url, private_token=token)
    gl.auth()
    return gl


@app.command()
def cleanup(
    project_id: int = typer.Argument(..., help="Numeric project ID."),
    keep_last: int = typer.Option(
        20, "--keep-last", "-k", help="Number of most recent pipelines to keep."
    ),
    older_than_days: Optional[int] = typer.Option(
        None,
        "--older-than-days",
        "-d",
        help="Delete pipelines older than this many days (optional).",
    ),
    dry_run: bool = typer.Option(
        True,
        "--dry-run/--no-dry-run",
        help="Dry-run by default; pass --no-dry-run to actually delete.",
    ),
):
    """
    Delete old pipelines for a project, based on keep_last and/or age.
    """
    load_dotenv()
    gl = get_gitlab_client()
    project = gl.projects.get(project_id)

    typer.echo(f"Ì¥ç Fetching pipelines for project {project_id}...")
    pipelines = project.pipelines.list(order_by="id", sort="desc", per_page=100, all=True)

    typer.echo(f"Total pipelines: {len(pipelines)}")

    cutoff_date = None
    if older_than_days is not None:
        cutoff_date = dt.datetime.utcnow() - dt.timedelta(days=older_than_days)

    to_delete = []

    for idx, pipeline in enumerate(pipelines):
        # keep the first `keep_last`
        if idx < keep_last:
            continue

        if cutoff_date is not None:
            # GitLab timestamps are ISO strings
            created_at = dt.datetime.fromisoformat(pipeline.attributes["created_at"].replace("Z", "+00:00"))
            if created_at > cutoff_date:
                continue

        to_delete.append(pipeline)

    typer.echo(f"Ì∑π Pipelines selected for deletion: {len(to_delete)}")

    for p in to_delete:
        msg = f"- Pipeline #{p.id} on ref {p.ref} (status: {p.status})"
        if dry_run:
            typer.echo(f"[DRY-RUN] {msg}")
        else:
            typer.echo(msg)
            p.delete()

    if dry_run:
        typer.echo("‚úÖ Dry-run complete. No pipelines were actually deleted.")
    else:
        typer.echo("‚úÖ Deletion complete.")


def main():
    """
    Entry point used by src.cli.
    """
    app()
