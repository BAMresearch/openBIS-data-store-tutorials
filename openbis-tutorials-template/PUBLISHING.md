# Publishing Strategy

This private repository is used for drafting and review. Approved tutorials should be published to a separate public repository.

## Option 1: Manual Promotion

Recommended for early-stage projects.

1. Review and approve the tutorial in the private repository.
2. Copy the approved tutorial folder to the public repository.
3. Open a pull request in the public repository.
4. Merge after final publication review.

## Option 2: GitHub Actions Promotion

Recommended once the workflow is stable.

A GitHub Action can copy approved tutorial folders from this private repository to the public repository when a release tag or manual workflow is triggered.

Suggested release tag format:

```text
tutorial-inventory-basics-v1.0
```

## Option 3: Static Site Deployment

If tutorials are published as a website, use GitHub Pages or another static hosting service from the public repository.
