# Contributing Guide

Thank you for contributing to the openBIS tutorial repository.

This repository is used to collaboratively develop, review, and publish tutorials related to openBIS workflows, including ELN, Inventory, and object connections.

---

# Repository Workflow

## Main Principles

* The `main` branch is always considered the stable and review-approved version.
* Contributors must **not push directly to `main`**.
* All changes must be made through:

  1. Feature branches
  2. Pull requests
  3. Review and approval process

---

# Repository Structure

Current active tutorial:

```text
3-eln/
```

Other tutorial folders may be added gradually.

Example structure:

```text
openbis-tutorials/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── .github/
│   └── pull_request_template.md
├── 1-overview/
├── 2-inventory/
├── 3-eln/
├── 4-connections/
└── openbis-tutorials-template/
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/BAMresearch/openBIS-data-store-tutorials-authors.git
cd openBIS-data-store-tutorials-authors
```

---

# Contributor Workflow

## Step 1 — Update Local `main`

Before starting work:

```bash
git checkout main
git pull origin main
```

This ensures your branch starts from the latest approved version.

---

## Step 2 — Create a Feature Branch

Create a dedicated branch for your work.

### Branch Naming Convention

Use descriptive names.

Examples:

```text
tutorial/eln-overview
tutorial/eln-step1
tutorial/eln-step2
```

Create the branch:

```bash
git checkout -b tutorial/eln-overview
```

---

## Step 3 — Make Changes

Edit only the files related to your task.

Typical locations:

```text
3-eln/index.html
3-eln/images/
3-eln/assets/
```

### Recommendations

* Use consistent terminology
* Keep screenshots clean and readable
* Avoid sensitive or personal information in screenshots
* Use descriptive image names

Good examples:

```text
step-01-login.png
step-02-create-object.png
```

Avoid:

```text
image1.png
screenshot-final2.png
```

---

## Step 4 — Review Your Changes

Before committing:

Check modified files:

```bash
git status
```

Review differences:

```bash
git diff
```

---

## Step 5 — Commit Changes

### Commit Message Guidelines

Use clear and concise messages describing the purpose of the change.

Good examples:

```bash
git commit -m "Add introduction to ELN Phase 7 tutorial"
git commit -m "Update screenshots for object creation workflow"
git commit -m "Fix broken image links in ELN tutorial"
```

Avoid vague messages:

```bash
git commit -m "changes"
git commit -m "update"
git commit -m "final version"
```

Commit changes:

```bash
git add .
git commit -m "Add introduction to ELN Phase 7 tutorial"
```

---

## Step 6 — Push Branch to GitHub

Push your branch:

```bash
git push origin tutorial/eln-overview
```

---

# Pull Request Workflow

## Step 7 — Open a Pull Request

### GitHub UI Instructions

1. Open the repository on GitHub
2. Select **Pull Requests**
3. Click **New Pull Request**
4. Choose:

Base branch:

```text
main
```

Compare branch:

```text
tutorial/eln-overview
```

5. Add:

   * Clear title
   * Summary of changes
   * Notes for reviewers

6. Request reviewers

7. Submit the pull request

---

# Pull Request Expectations

Each pull request should:

* Focus on one logical change
* Be easy to review
* Include updated screenshots if relevant
* Avoid unrelated modifications

---

# Reviewer Guidelines

Reviewers should verify:

* Technical correctness
* Tutorial clarity
* Consistent terminology
* Screenshot quality
* Correct image links
* Formatting consistency
* Absence of sensitive information

---

# Handling Review Comments

If reviewers request changes:

1. Update your local branch
2. Commit the requested modifications
3. Push again to the same branch

Example:

```bash
git add .
git commit -m "Address reviewer comments on ELN tutorial"
git push
```

The pull request updates automatically.

---

# Keeping Your Branch Updated

If `main` changes while you are working:

```bash
git checkout main
git pull origin main
git checkout tutorial/eln-overview
git merge main
```

Resolve conflicts if needed.

---

# Merge Policy

Only maintainers merge pull requests.

Repository settings enforce:

* Pull request reviews
* Protected `main` branch
* Restricted direct pushes

---

# Merge Strategy

The repository uses:

```text
Squash and merge
```

This keeps the commit history clean and readable.

---

# Branch Deletion

After merge:

* Delete the feature branch on GitHub
* Optionally delete it locally

Delete local branch:

```bash
git branch -d tutorial/eln-overview
```

---

# Protected Branch Rules

The `main` branch is protected:

* No direct pushes by contributors
* Pull requests required
* Review approval required
* Maintainers control merges

---

# Documentation Standards

Tutorials should:

* Use consistent structure
* Include step-by-step instructions
* Include screenshots where useful
* Use descriptive headings
* Keep formatting readable

Recommended structure:

```text
tutorial-folder/
├── README.md
├── index.html
├── images/
└── assets/
```

---

# Best Practices

## Do

* Keep pull requests focused
* Use descriptive branch names
* Write clear commit messages
* Ask for review early
* Update documentation with changes

## Avoid

* Large unrelated pull requests
* Direct commits to `main`
* Unclear image names
* Committing temporary files
* Including private information in screenshots

---

# Questions or Support

If you are unsure about the workflow:

* Contact a maintainer
* Open a discussion issue
* Ask before restructuring repository contents

Thank you for contributing.
