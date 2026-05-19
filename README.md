# data-store-tutorials
This is a public repository to review and share tutorials. Reviewers are the Data Store team of the .  Contents are tutorials to train how to use the openBIS-Data Store research data management system.

## Purpose
This repository supports the internal development of tutorials for researchers learning to use openBIS, and shares contents with openBIS users at BAM including:

- Inventory
- ELN / Electronic Lab Notebook
- Parent-Child connections
- Customization

Approved tutorials can be tagged as reviewed.

## Repository Structure

```text
openbis-tutorials-template/
  README.md
  CONTRIBUTING.md
  REVIEW_CHECKLIST.md
  PUBLISHING.md
  tutorials/
    overview/
      index.html
      images/
      assets/
      README.md
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

## Tutorial Folder Convention

Each tutorial should follow this structure:

```text
/tutorial-name/
  index.html
  assets/
  datasets/
  images/
    step1-name-1.png
    step1-name-2.png
    step2-name-1.png
  README.md
```
