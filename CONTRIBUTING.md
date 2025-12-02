# Contributing

Thanks for checking out `gitlab-automation-recipes` í²œ

## How recipes work

- Provider-specific code lives under `src/providers/<provider>/recipes/`.
- Each recipe is a small Python module with a `main()` function.
- Recipes can use Typer internally for flags/options.

## Adding a new GitLab recipe

1. Create `src/providers/gitlab/recipes/<your_recipe_name>.py`
2. Expose a `main()` function.
3. (Optional) Use `typer.Typer()` inside and call it from `main()`.
4. Add a basic test in `tests/`.
5. Open a PR!

## Style

- Keep recipes small and focused.
- Avoid hard-coding secrets or tokens.
- Prefer `.env` or YAML config.

