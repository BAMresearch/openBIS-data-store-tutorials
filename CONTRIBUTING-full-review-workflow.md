# Contributing Guide

Thank you for contributing to the openBIS tutorial repository.

This repository is used to collaboratively develop, review, and publish tutorials related to openBIS workflows, including ELN, Inventory, and object connections.

---

# Repository Workflow

## Main Principles

* The `main` branch is always considered the stable and review-approved version.
* Contributors must **not push directly to `main`**.
* Contributors must **not use their `main` branch as the source branch for a pull request**.
* Each contribution should be developed on a dedicated **feature branch** (also called a topic or contribution branch).
* All changes must go through:
  1. A feature branch
  2. A pull request into `main`
  3. Review and approval
  4. Merge by a maintainer

In short:

```text
main -> create feature branch -> make changes -> push feature branch
     -> open pull request into main -> review -> maintainer merges
```

## Why Use a Feature Branch?

The `main` branch should remain a clean copy of the latest approved repository state. A feature branch is a temporary workspace for one specific contribution.

For example:

```text
main
└── tutorial/eln-overview
```

The pull request should be:

```text
tutorial/eln-overview -> main
```

and not:

```text
main -> main
```

Using a dedicated feature branch:

* Keeps each pull request isolated to one logical change.
* Prevents unrelated commits from accidentally appearing in an existing pull request.
* Allows contributors to work on several contributions in parallel.
* Lets contributors respond to review comments by pushing additional commits to the same branch.
* Keeps `main` available as a clean starting point for future work.
* Makes it easy to delete a completed or abandoned contribution without affecting `main`.

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
git clone https://github.com/BAMresearch/openBIS-data-store-tutorials.git
cd openBIS-data-store-tutorials
```

---

# Contributor Workflow

The contributor owns the feature branch and updates it throughout the review process. Maintainers review the pull request and merge approved changes into `main`.

## Step 1 — Update Local `main`

Before starting any new contribution, switch to `main` and update it:

```bash
git checkout main
git pull origin main
```

This ensures that your new branch starts from the latest approved version.

Do not begin new work directly on `main`.

---

## Step 2 — Create a Feature Branch

Create a dedicated branch for **each logical contribution**.

### Branch Naming Convention

Use short, descriptive names that indicate what the branch changes.

Examples:

```text
tutorial/eln-overview
tutorial/eln-step1
tutorial/eln-step2
```

Create the branch from the updated `main` branch:

```bash
git checkout -b tutorial/eln-overview
```

Confirm the active branch if needed:

```bash
git branch
```

The feature branch should be the branch on which you edit, commit, and push your contribution.

### One Branch per Contribution

If you later start a different change, return to `main`, update it, and create another branch:

```bash
git checkout main
git pull origin main
git checkout -b tutorial/another-change
```

Do not reuse one feature branch for unrelated contributions.

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

* Use consistent terminology.
* Keep screenshots clean and readable.
* Avoid sensitive or personal information in screenshots.
* Use descriptive image names.
* Avoid unrelated formatting or file changes in the same contribution.

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

Before committing, check which files you changed:

```bash
git status
```

Review the differences:

```bash
git diff
```

Make sure the changes belong to the current contribution and that no temporary, unrelated, or sensitive files are included.

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

## Step 6 — Push the Feature Branch to GitHub

Push the feature branch, not `main`:

```bash
git push -u origin tutorial/eln-overview
```

After the first push, later updates to the same branch can normally be pushed with:

```bash
git push
```

---

# Pull Request Workflow

## Step 7 — Open a Pull Request

The pull request proposes merging your **feature branch into `main`**.

### GitHub UI Instructions

1. Open the repository on GitHub.
2. Select **Pull Requests**.
3. Click **New Pull Request**.
4. Set the branches as follows:

Base branch — the branch that will receive the approved changes:

```text
main
```

Compare branch — your feature branch containing the proposed changes:

```text
tutorial/eln-overview
```

The intended direction is:

```text
tutorial/eln-overview -> main
```

5. Add:
   * A clear title.
   * A summary of the changes.
   * Any context or notes reviewers need.
6. Request the appropriate reviewer(s).
7. Submit the pull request.

### Important: Do Not Open the Pull Request from `main`

Your contribution should come from a feature branch. Keep `main` clean so it can remain synchronized with the approved repository state and serve as the starting point for future branches.

Once a pull request is open, continue making requested changes on the **same feature branch**. You do not need to create a new pull request for every review update.

---

# Pull Request Expectations

Each pull request should:

* Come from a dedicated feature branch.
* Target `main`.
* Focus on one logical change.
* Be easy to review.
* Include updated screenshots if relevant.
* Avoid unrelated modifications.
* Explain anything reviewers need to verify.

---

# Contributor Responsibilities During Review

After opening a pull request, the contributor should:

* Monitor the pull request for comments or requested changes.
* Ask questions if reviewer feedback is unclear.
* Make requested changes on the same feature branch.
* Commit and push those updates.
* Avoid adding unrelated work to the branch while the pull request is open.

The existing pull request will update automatically when new commits are pushed to its feature branch.

---

# Reviewer and Maintainer Guidelines

Reviewers and maintainers should verify:

* Technical correctness.
* Tutorial clarity.
* Consistent terminology.
* Screenshot quality.
* Correct image links.
* Formatting consistency.
* Absence of sensitive information.
* That the pull request contains only the intended logical change.

Reviewers should leave clear, actionable comments when changes are needed.

Maintainers should not make contributors create a new pull request merely to address normal review comments. The contributor should update the existing feature branch instead.

---

# Handling Review Comments

If reviewers request changes:

1. Stay on or switch back to your feature branch.
2. Make the requested modifications.
3. Review the changes.
4. Commit them.
5. Push again to the same feature branch.

Example:

```bash
git checkout tutorial/eln-overview
git add .
git commit -m "Address reviewer comments on ELN tutorial"
git push
```

The pull request updates automatically.

The review cycle is therefore:

```text
feature branch
      |
      v
pull request
      |
      v
review comments
      |
      v
update same feature branch
      |
      v
push commits
      |
      v
pull request updates automatically
```

Repeat this cycle until the pull request is approved.

---

# Keeping Your Branch Updated

If `main` changes while you are working and your feature branch needs those changes:

```bash
git checkout main
git pull origin main
git checkout tutorial/eln-overview
git merge main
```

Resolve conflicts if needed, then commit and push the result to your feature branch.

Do not solve this by moving your contribution onto `main`.

---

# Merge Policy

Only maintainers merge pull requests.

Repository settings enforce:

* Pull request reviews.
* Protected `main` branch.
* Restricted direct pushes.

## Contributor

The contributor is responsible for:

* Creating the feature branch.
* Making and committing the changes.
* Pushing the feature branch.
* Opening the pull request into `main`.
* Responding to review comments on the same branch.

## Reviewer

The reviewer is responsible for:

* Checking the proposed changes.
* Providing actionable feedback.
* Approving the pull request when it is ready.

## Maintainer

The maintainer is responsible for:

* Protecting the stability of `main`.
* Ensuring required reviews are complete.
* Resolving or coordinating any remaining merge concerns.
* Merging approved pull requests.
* Avoiding direct changes to `main` except where repository policy explicitly permits them.

---

# Merge Strategy

The repository uses:

```text
Squash and merge
```

This keeps the `main` branch history clean and readable while allowing contributors to use multiple commits during development and review.

---

# Branch Deletion

After the pull request has been merged, the feature branch has completed its purpose.

* Delete the feature branch on GitHub.
* Optionally delete it locally.

Delete the local branch:

```bash
git checkout main
git pull origin main
git branch -d tutorial/eln-overview
```

The next contribution should start from the updated `main` branch and use a new feature branch.

---

# Protected Branch Rules

The `main` branch is protected:

* No direct pushes by contributors.
* Pull requests are required.
* Review approval is required.
* Maintainers control merges.

Think of `main` as the stable, approved version of the repository—not as a workspace for an individual contribution.

---

# Documentation Standards

Tutorials should:

* Use consistent structure.
* Include step-by-step instructions.
* Include screenshots where useful.
* Use descriptive headings.
* Keep formatting readable.

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

* Start each contribution from an updated `main`.
* Create a dedicated feature branch for each contribution.
* Keep pull requests focused.
* Use descriptive branch names.
* Write clear commit messages.
* Ask for review early.
* Push review updates to the same feature branch.
* Update documentation with changes.

## Avoid

* Working directly on `main`.
* Opening contribution pull requests from `main`.
* Reusing one branch for unrelated contributions.
* Large unrelated pull requests.
* Unclear image names.
* Committing temporary files.
* Including private information in screenshots.

---

# Quick Reference

## Contributor

```bash
git checkout main
git pull origin main
git checkout -b tutorial/eln-overview

# Make changes

git status
git diff
git add .
git commit -m "Describe the contribution"
git push -u origin tutorial/eln-overview
```

Then open:

```text
tutorial/eln-overview -> main
```

If review changes are requested:

```bash
# Make requested changes on tutorial/eln-overview
git add .
git commit -m "Address reviewer comments"
git push
```

## Maintainer / Reviewer

```text
1. Review the pull request.
2. Request changes or approve it.
3. Contributor updates the same feature branch if necessary.
4. Re-review the updated pull request.
5. Maintainer uses Squash and merge after approval.
6. Feature branch is deleted after merge.
```

---

---

# Full Tutorial Review Workflow

There are two different review workflows in this repository.

## 1. Contributing a Change

Use a **feature branch and pull request** when a contributor proposes changes that differ from `main`.

```text
main -> feature branch -> changes -> pull request -> review -> maintainer merge
```

A pull request is appropriate because GitHub can compare the feature branch with `main` and show reviewers exactly what changed.

Example:

```text
fix/eln-object-creation -> main
```

## 2. Maintainer Requests a Full Tutorial Review

Use a **GitHub Issue / review task** when a maintainer wants collaborators to review a complete tutorial that is already present on `main`.

Do **not** create an unchanged feature branch solely to start this review. Pull requests are designed to compare branch differences. If the review branch contains exactly the same content as `main`, GitHub has no changes to show and may report:

```text
There isn't anything to compare
```

Instead, the maintainer creates a GitHub Issue as the coordination point for the full review.

```text
tutorial on main
      |
      v
maintainer creates review Issue
      |
      v
contributors review complete tutorial
      |
      v
findings and discussion in Issue
      |
      v
correction required?
   |             |
   no           yes
   |             |
   v             v
close Issue   feature branch
                 |
                 v
              correction
                 |
                 v
              PR -> main
                 |
                 v
              review + merge
```

## Creating the Full-Review Issue

Use a descriptive Issue title, for example:

```text
Review requested: ELN tutorial
```

The Issue should identify:

* The tutorial or tutorial section to review.
* Its location in the repository.
* The purpose and scope of the review.
* The contributors or reviewers responsible for it.
* Any deadline or review period, if applicable.
* The criteria reviewers should check.
* How reviewers should report their findings.

The maintainer can assign the Issue to the relevant collaborators and use an appropriate label such as `review`.

## Suggested Full-Review Checklist

- [ ] Technical correctness
- [ ] Tutorial steps can be followed in the documented order
- [ ] Instructions are clear and understandable
- [ ] Terminology is consistent
- [ ] Screenshots match the described workflow
- [ ] Screenshots are readable and contain no sensitive information
- [ ] Image and internal links work correctly
- [ ] Formatting is consistent
- [ ] Required information is not missing
- [ ] Errors and proposed improvements are documented

## Reporting Findings

Comments, questions, and observations about the existing tutorial should be recorded in the review Issue. This keeps discussion of the complete tutorial in one place.

When a finding requires a repository change, use the normal contribution workflow:

```text
review finding
      |
      v
feature branch from updated main
      |
      v
make correction
      |
      v
commit + push
      |
      v
pull request -> main
      |
      v
review + merge
```

Example:

```bash
git checkout main
git pull origin main
git checkout -b fix/eln-object-creation
```

After making the correction:

```bash
git add .
git commit -m "Fix ELN object creation instructions"
git push -u origin fix/eln-object-creation
```

Then open:

```text
fix/eln-object-creation -> main
```

The pull request should reference the full-review Issue so maintainers can track which finding it addresses.

## Maintainer Responsibilities for a Full Tutorial Review

The maintainer should:

* Ensure the tutorial version to review is clearly identified.
* Create the GitHub Issue coordinating the review.
* Define the scope and review expectations.
* Assign or invite the appropriate reviewers.
* Keep findings and discussion organized in the Issue.
* Determine which findings require repository changes.
* Ensure corrections are submitted through feature branches and pull requests.
* Review and merge approved corrections.
* Close the review Issue when the agreed review work is complete.

## Reviewer Responsibilities for a Full Tutorial Review

Reviewers should:

* Review the complete tutorial identified in the Issue.
* Follow the requested review criteria.
* Record findings, questions, and observations in the Issue.
* Avoid creating an unchanged branch solely to initiate review.
* Create a dedicated feature branch when making an actual correction.
* Open a pull request into `main` for proposed repository changes.
* Reference the review Issue when submitting corrections.

## Choosing the Correct Workflow

| Situation | GitHub mechanism |
| --- | --- |
| Contributor proposes file changes | Feature branch + Pull Request |
| Maintainer requests review of an unchanged tutorial already on `main` | GitHub Issue / review task |
| Reviewer finds a correction during a full tutorial review | Feature branch + Pull Request |
| Reviewers need a shared place for discussion of the complete tutorial | GitHub Issue |

The key distinction is:

```text
Pull Request = review proposed changes
GitHub Issue = coordinate review of existing content
```

A full tutorial review can therefore begin with an Issue and later produce one or more pull requests for specific corrections.

---

# Questions or Support

If you are unsure about the workflow:

* Contact a maintainer.
* Open a discussion issue.
* Ask before restructuring repository contents.

Thank you for contributing.
