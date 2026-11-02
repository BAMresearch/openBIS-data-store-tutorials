
# openBIS Data Store Tutorials

This repository provides practical guidelines, tutorials, and self-learning materials for using the openBIS Data Store to organize research data, document experiments and corresponding datasets, and connect Lab Notebook datasets with Inventory items for traceability.

The learning materials cover both the openBIS graphical user interface (GUI) and programmatic interaction with openBIS using pyBIS, its Python API.

## Self-learning paths

Choose a learning path based on how you want to interact with the openBIS Data Store. If you are new user of the Data Store, start with the **Self-learning path: Getting started with the GUI (Graphical User Interface)**

### Self-learning path: Getting started with the GUI (Graphical User Interface)

This learning path introduces the fundamental concepts and practical steps for organizing and managing research data through the openBIS graphical user interface (GUI).

Start with the research data representation guideline, then follow the tutorials relevant to your role. **Data Store Stewards** should complete the group setup tutorials before division members begin working with the tutorials.

#### Tutorials

| # | Tutorial | Intended audience | What you will learn |
|---|---|---|---|
| 1 | [Guideline to represent research data in the Data Store](https://bamresearch.github.io/openBIS-data-store-tutorials/represent-data-research-data/) | Data Store Stewards and division members | Learn the principles for representing research data and metadata. **Start here.** |
| 2 | [Custom ELN settings for the group](https://bamresearch.github.io/openBIS-data-store-tutorials/custom-eln) | Data Store Stewards only | Prepare the division's electronic Lab Notebook settings before other users begin. |
| 3 | [Upload data in the Lab Notebook](https://bamresearch.github.io/openBIS-data-store-tutorials/lab-notebook/) | Data Store Stewards and division members | Register experimental steps and upload associated research data. |
| 4 | [Prepare Inventory structures for the group](https://bamresearch.github.io/openBIS-data-store-tutorials/inventory-data-stewards/) | Data Store Stewards only | Create Inventory projects and collections and register shared items. |
| 5 | [Register Inventory items](https://bamresearch.github.io/openBIS-data-store-tutorials/inventory-users/) | Data Store Stewards and division members | Register Inventory items generated or used during research. |
| 6 | [Connect Lab Notebook data with Inventory items](https://bamresearch.github.io/openBIS-data-store-tutorials/connect-data/) | Data Store Stewards and division members | Connect experimental steps with instruments, chemicals, and samples for traceability. |

### Self-learning path: pyBIS

This learning path introduces **pyBIS**, the Python API for openBIS, and explores programmatic data management.

> **Work in progress:** This self-learning path is currently under development. For now, it includes the introductory workshop prepared for the **Data Store Days at BAM (11–13 November 2026)**. Additional learning materials will be added as the learning path evolves.

#### Workshop: pyBIS Level 0

**Beyond the GUI: Hands-On with pyBIS and Data Modelling for Research Workflows**

This five-hour introductory workshop is designed for researchers interested in interacting with the openBIS Data Store using Python and exploring how research workflows can be modelled in openBIS. No prior Python experience is required.

The workshop combines two complementary parts:

- **Hands-on pyBIS (3.5 hours):** Introduction to programmatic interaction with openBIS, including retrieving and filtering research objects, modifying metadata, automating data uploads, and exporting information.
- **Conceptual data modelling (1.5 hours):** Exploring how research workflows, objects, metadata, and relationships can be represented in openBIS to support data organization and traceability.

The workshop materials include an overview and agenda, computer setup instructions, a collaborative data modelling activity, and a Research Workflow Canvas.

**[PyBIS Self-Learning Path](docs/self-learning-path-pybis/README.md)**

## Using this repository

Choose the self-learning path that best matches your needs:

- **GUI learning path:** Follow the tutorials in the table above to learn how to organize research data, document experiments, and manage Inventory items through the openBIS graphical user interface.
- **pyBIS learning path:** Explore the introductory workshop and supporting materials to learn about programmatic interaction with openBIS and data modelling.

To browse the source files and supporting resources, use the [repository's file listing](https://github.com/BAMresearch/openBIS-data-store-tutorials/tree/main).

## Repository structure

Tutorials and learning materials are organized by topic. In addition to the tutorial folders:

- [`docs/`](docs/) contains documentation, materials intended for publication, and self-learning resources.
  - [`self-learning-path-pybis/`](docs/self-learning-path-pybis/) contains learning materials on pyBIS and data modelling, starting with the [`workshop-pybis-level0/`](docs/self-learning-path-pybis/workshop-pybis-level0/) prepared for the Data Store Days at BAM.
- [`openbis-tutorials-template/`](openbis-tutorials-template/) contains a template for creating tutorials.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how to contribute.

Browse the [full repository](https://github.com/BAMresearch/openBIS-data-store-tutorials/tree/main) to see all files and supporting resources.

## Contributing and feedback

Found a broken link, unclear instruction, outdated screenshot, or have an idea for a tutorial? [Open an issue](https://github.com/BAMresearch/openBIS-data-store-tutorials/issues) with the tutorial name and a brief description, or follow the [contribution guidelines](CONTRIBUTING.md) to propose changes. Tutorial updates are reviewed by the Data Store team.

## License

Content is shared under the [Creative Commons Attribution 4.0 International license](LICENSE).
