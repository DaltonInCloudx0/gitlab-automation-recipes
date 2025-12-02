# gitlab-automation-recipes


**A collection of small, modular automation tools for GitLab administrators and DevOps engineers.**

Each “recipe” is a small, focused automation for real GitLab admin problems: cleaning old pipelines, archiving inactive projects, tagging risky merge requests, and more.

Over time, this will plug into a larger multi-provider toolkit (GitLab, AWS, Kubernetes, etc.), but GitLab is the first-class citizen and starting point.

## Why this exists

Running GitLab—whether self-managed or SaaS—always leads to the same chores:

• old pipelines pile up
• inactive repos never get archived
• high-risk merge requests slip through unnoticed
• notifications end up noisy or inconsistent

These aren’t glamorous tasks, but they matter.
This repository collects practical, repeatable automations that reduce manual work and improve consistency across teams.

Every recipe is:

• self-contained
• documented with an example
• configurable through ```.env``` or YAML
• beginner-friendly to contribute to

## Features (Current Recipes)
### Archive Inactive Projects

Automatically find projects that haven’t been touched in N days and archive them (with dry-run mode enabled by default).

### Cleanup Old Pipelines

Keep your CI/CD neat by deleting pipelines older than a certain age or beyond a retention count.

### MR Risk Highlighter

Scan merge requests for certain keywords or paths and automatically apply labels or comments.

### Pipeline Failure Notifier

Check for failed pipelines and send message alerts to Slack or Discord.

## Getting Started
### 1. Clone the repo

```
git clone https://github.com/yourusername/gitlab-automation-.git
cd gitlab-automation-
```

### 2. Install dependencies

If using ```pyproject.toml```:

```
pip install .
```

Or with a requirements file:

```
pip install -r requirements.txt
```

### 3. Copy ```.env.example``` → ```.env```

```
cp .env.example .env
```

Fill in:

```
GITLAB_URL=https://gitlab.yourdomain.com
GITLAB_TOKEN=your-access-token
```

### 4. Run a recipe

```
python -m src.cli archive-inactive-projects

```

Or run a specific file directly:

```
python src/providers/gitlab/recipes/archive_inactive_projects.py

```

## Configuration

You can configure recipes using:

  1. Environment variables (```.env```)

  2. YAML file (```config.yaml```)

Example YAML:

```
default:
  gitlab_url: "https://gitlab.com"
  token: "YOUR_TOKEN"

recipes:
  archive_inactive_projects:
    inactive_days: 90
    dry_run: true

  cleanup_old_pipelines:
    keep_last: 20
```

## Recipes (Detailed)

Each recipe has its own example file in ```/examples/```.

archive_inactive_projects.py

Find projects whose last activity exceeds ```inactive_days```.
Supports:

 - dry run

 - group filtering

 - verbose output

### cleanup_old_pipelines.py

Delete pipelines older than X days or only keep the latest N.

### mr_risk_highlighter.py

Rules can be based on:

 - file paths

 - branch names

 - commit messages

 - regex patterns

Automatically applies labels.

### notify_failed_pipelines.py

Checks for pipeline failures and posts:

 - pipeline ID

 - branch

 - failed job names

 - timestamp

Supports Slack, Discord, or webhook URL.

## CLI Usage

The CLI acts as a launcher for recipes:

```
python -m src.cli <recipe-name> [options]
```

Example:

```
python -m src.cli cleanup-old-pipelines --project-id 123 --keep-last 10
```

## Contributing

Contributions are welcome and encouraged.

To add a new recipe:

  1. Create a new file under ```src/providers/gitlab/recipes/```

  2. Add an example in ```/examples/```

  3. Add minimal tests in ```/tests/```

  4. Document any config needed

  5. Open a PR

Recipes should stay small, focused, and easy to understand.

## Roadmap

Planned additions:

 - Dockerized GitLab sandbox for local testing

 - Enhanced CLI with auto-discovery of recipes

 - More recipes (security scanning, runner cleanup, log collectors)

 - Building toward a larger “GitLab CE Deploy/Upgrade Helper” project

 - Optional Web UI for running recipes

## License

MIT License. Use these scripts freely in your GitLab workflows.
