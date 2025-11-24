# gitlab-automation-recipes

GitLab Automation Recipes

A collection of small, modular automation tools for GitLab administrators and DevOps engineers.
Each “recipe” is a standalone script that solves a real operational problem: cleaning old pipelines, archiving inactive projects, tagging risky merge requests, and more.

The goal is to make automation approachable. Tiny scripts, clear folders, and plenty of room for contributions.

Why this exists

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
• configurable through .env or YAML
• beginner-friendly to contribute to

Features (Current Recipes)
Archive Inactive Projects

Automatically find projects that haven’t been touched in N days and archive them (with dry-run mode enabled by default).

Cleanup Old Pipelines

Keep your CI/CD neat by deleting pipelines older than a certain age or beyond a retention count.

MR Risk Highlighter

Scan merge requests for certain keywords or paths and automatically apply labels or comments.

Pipeline Failure Notifier

Check for failed pipelines and send message alerts to Slack or Discord.

Getting Started
1. Clone the repo
