# openBIS Tutorials Development Repository

Private working repository for developing, reviewing, and versioning openBIS tutorials before publication to a public researcher-facing repository.

## Purpose

This repository supports the internal development of tutorials for researchers learning to use openBIS, including:

- Inventory
- ELN / Electronic Lab Notebook
- Parent-Child connections
- Customization

Approved tutorials can be promoted to a separate public repository after review.

## Repository Structure

```text
openbis-tutorials-template/
  README.md
  CONTRIBUTING.md
  REVIEW_CHECKLIST.md
  PUBLISHING.md
  tutorials/
    inventory/
      index.html
      images/
      assets/
      README.md
    eln/
      index.html
      images/
      assets/
      README.md
    parent-child-connections/
      index.html
      images/
      assets/
      README.md
    customization/
      index.html
      images/
      assets/
      README.md
  .github/
    PULL_REQUEST_TEMPLATE/
      tutorial_review.md
    workflows/
      validate-tutorials.yml
```

## Recommended Workflow

1. Create a feature branch for each tutorial or revision.
2. Add or update tutorial content under `tutorials/<tutorial-name>/`.
3. Open a pull request using the tutorial review template.
4. Assign at least one content reviewer and one technical reviewer.
5. Revise based on feedback.
6. Merge only after approval.
7. Promote approved tutorials to the public repository.

## Naming Convention

Use lowercase folder names with hyphens:

```text
inventory-basics
eln-create-entry
parent-child-connections
custom-object-types
```

## Tutorial Folder Convention

Each tutorial should follow this structure:

```text
/tutorial-name/
  index.html
  images/
    step1.png
    step2.png
  assets/
  README.md
```

