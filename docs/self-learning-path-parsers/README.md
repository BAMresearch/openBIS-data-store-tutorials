<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Self-Learning Path: Using Parsers</title>

  <style>
    :root {
      --bg: #f7f8fa;
      --surface: #ffffff;
      --text: #1f2933;
      --muted: #5f6b76;
      --border: #d9dee5;
      --primary: #005ea8;
      --primary-dark: #00467f;
      --accent: #eaf4fb;
      --success: #eef7ef;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }

    a {
      color: var(--primary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    header {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
    }

    .header-inner {
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-logo {
      width: 46px;
      height: 46px;
      border: 1px solid var(--border);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: var(--muted);
      background: #fff;
    }

    .brand-text strong {
      display: block;
      font-size: 1rem;
    }

    .brand-text span {
      color: var(--muted);
      font-size: 0.9rem;
    }

    nav a {
      margin-left: 1rem;
      font-size: 0.95rem;
    }

    main {
      max-width: 1100px;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem;
    }

    .hero {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 2rem;
      margin-bottom: 2rem;
    }

    .hero h1 {
      margin-top: 0;
      margin-bottom: 0.75rem;
      font-size: 2rem;
      line-height: 1.2;
    }

    .hero p {
      max-width: 800px;
      color: var(--muted);
      font-size: 1.05rem;
    }

    .note {
      background: var(--accent);
      border-left: 4px solid var(--primary);
      padding: 1rem 1.2rem;
      border-radius: 6px;
      margin-top: 1.5rem;
    }

    section {
      margin-top: 2.5rem;
    }

    section h2 {
      margin-bottom: 0.75rem;
      font-size: 1.5rem;
    }

    .section-intro {
      color: var(--muted);
      max-width: 850px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .card h3 {
      margin-top: 0;
      margin-bottom: 0.5rem;
      font-size: 1.1rem;
    }

    .card p {
      color: var(--muted);
      font-size: 0.95rem;
    }

    .card .meta {
      margin-top: 1rem;
      font-size: 0.85rem;
      color: var(--muted);
    }

    .card a.button {
      display: inline-block;
      margin-top: 0.9rem;
      padding: 0.55rem 0.9rem;
      border-radius: 6px;
      background: var(--primary);
      color: #fff;
      font-weight: bold;
    }

    .card a.button:hover {
      background: var(--primary-dark);
      text-decoration: none;
    }

    .workflow {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: center;
      margin-top: 1rem;
    }

    .workflow-step {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 0.55rem 0.9rem;
      font-weight: bold;
      font-size: 0.95rem;
    }

    .workflow-arrow {
      color: var(--muted);
      font-weight: bold;
    }

    .two-column {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }

    .panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .panel h3 {
      margin-top: 0;
    }

    pre {
      background: #f1f3f5;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      overflow-x: auto;
      font-size: 0.9rem;
    }

    code {
      font-family: Consolas, Monaco, "Courier New", monospace;
    }

    footer {
      border-top: 1px solid var(--border);
      background: var(--surface);
      margin-top: 3rem;
    }

    .footer-inner {
      max-width: 1100px;
      margin: 0 auto;
      padding: 1.5rem;
      color: var(--muted);
      font-size: 0.9rem;
    }

    @media (max-width: 700px) {
      .header-inner {
        flex-direction: column;
        align-items: flex-start;
      }

      nav a {
        margin-left: 0;
        margin-right: 1rem;
      }

      .hero {
        padding: 1.4rem;
      }
    }
  </style>
</head>

<body>

<header>
  <div class="header-inner">
    <div class="brand">
      <div class="brand-logo">LOGO</div>

      <div class="brand-text">
        <strong>BAM Data Store</strong>
        <span>openBIS Training Materials</span>
      </div>
    </div>

    <nav>
      <a href="#tutorials">Tutorials</a>
      <a href="#workflow">Workflow</a>
      <a href="#repositories">Repositories</a>
      <a href="../../README.md">Main README</a>
    </nav>
  </div>
</header>

<main>

  <section class="hero">
    <h1>Self-Learning Path: Using Parsers</h1>

    <p>
      Learn how to use supported parsers to process research data and prepare it
      for workflows with BAM Data Store / openBIS.
    </p>

    <p>
      The learning materials are provided as Jupyter notebooks with practical
      examples, executable Python code, and example datasets.
    </p>

    <div class="note">
      <strong>Training repository only.</strong>
      This learning path explains how to use parsers. Parser source code,
      implementation details, tests, and software releases are maintained in
      separate parser development repositories.
    </div>
  </section>

  <section>
    <h2>Who is this learning path for?</h2>

    <p class="section-intro">
      These tutorials are designed for researchers and other BAM Data Store
      users who need to process research data using supported parsers.
      Basic familiarity with Python and Jupyter notebooks is helpful.
    </p>
  </section>

  <section>
    <h2>Learning objectives</h2>

    <ul>
      <li>Understand the role of parsers in a research data workflow.</li>
      <li>Identify the appropriate parser for a supported use case.</li>
      <li>Prepare input data for parsing.</li>
      <li>Configure and execute parsers from Jupyter notebooks.</li>
      <li>Inspect parser output and expected results.</li>
      <li>Recognize common input or configuration problems.</li>
      <li>Use parser output as part of an openBIS workflow.</li>
    </ul>
  </section>

  <section id="tutorials">
    <h2>Tutorials</h2>

    <p class="section-intro">
      Follow the tutorials in order if you are new to parsers, or select the
      notebook relevant to your workflow.
    </p>

    <div class="cards">

      <article class="card">
        <h3>01 · Introduction to Parsers</h3>

        <p>
          Learn what parsers do, how they fit into the BAM Data Store workflow,
          and what to expect from the parser tutorials.
        </p>

        <div class="meta">
          Level: Beginner<br>
          Format: Jupyter Notebook
        </div>

        <a class="button"
           href="01-introduction-to-parsers/introduction-to-parsers.ipynb">
          Open notebook
        </a>
      </article>

      <article class="card">
        <h3>02 · Parser A</h3>

        <p>
          Learn how to prepare input data, configure Parser A, execute it, and
          inspect the generated output.
        </p>

        <div class="meta">
          Level: Beginner / Intermediate<br>
          Format: Jupyter Notebook
        </div>

        <a class="button"
           href="02-parser-name-a/parser-name-a.ipynb">
          Open notebook
        </a>
      </article>

      <article class="card">
        <h3>03 · Parser B</h3>

        <p>
          Work through a second parser example and compare its input and output
          requirements with other parser workflows.
        </p>

        <div class="meta">
          Level: Intermediate<br>
          Format: Jupyter Notebook
        </div>

        <a class="button"
           href="03-parser-name-b/parser-name-b.ipynb">
          Open notebook
        </a>
      </article>

      <article class="card">
        <h3>99 · Complete Workflow</h3>

        <p>
          Apply the concepts from the previous tutorials in an end-to-end
          research data processing workflow.
        </p>

        <div class="meta">
          Level: Intermediate<br>
          Format: Jupyter Notebook
        </div>

        <a class="button"
           href="99-complete-workflow/parser-workflow.ipynb">
          Open notebook
        </a>
      </article>

    </div>
  </section>

  <section>
    <h2>Typical tutorial structure</h2>

    <pre><code>02-parser-name-a/
├── README.md
├── parser-name-a.ipynb
├── metadata.yml
├── datasets/
│   ├── input/
│   └── expected-output/
└── images/</code></pre>

    <p>
      Each tutorial should be as self-contained as practical and provide the
      notebook, example data, compatibility information, and any supporting images.
    </p>
  </section>

  <section>
    <h2>Parser versions and compatibility</h2>

    <p>
      Parsers, notebooks, and openBIS may evolve independently. Each tutorial
      should therefore document the versions against which it was tested.
    </p>

    <pre><code>Parser: Example Parser
Tested parser version: 2.3.1
Tested openBIS version: 6.x
Last tutorial test: 2026-09-04</code></pre>
  </section>

  <section id="repositories">
    <h2>Tutorial repository and parser development repository</h2>

    <div class="two-column">

      <div class="panel">
        <h3>This tutorial repository</h3>

        <ul>
          <li>Jupyter notebooks</li>
          <li>example datasets</li>
          <li>user exercises</li>
          <li>expected results</li>
          <li>user-oriented explanations</li>
          <li>training workflows</li>
        </ul>
      </div>

      <div class="panel">
        <h3>Parser development repository</h3>

        <ul>
          <li>parser source code</li>
          <li>implementation details</li>
          <li>unit and integration tests</li>
          <li>software dependencies</li>
          <li>developer documentation</li>
          <li>parser releases</li>
        </ul>
      </div>

    </div>

    <div class="note">
      Parser source code should not be duplicated in this tutorial repository.
      Tutorials should use released or otherwise supported parser versions.
    </div>
  </section>

  <section>
    <h2>Reporting problems</h2>

    <div class="two-column">

      <div class="panel">
        <h3>Tutorial problem</h3>

        <p>Report it in this tutorials repository when the issue concerns:</p>

        <ul>
          <li>unclear instructions;</li>
          <li>missing files;</li>
          <li>incorrect paths;</li>
          <li>outdated screenshots;</li>
          <li>example datasets;</li>
          <li>notebook reproducibility.</li>
        </ul>
      </div>

      <div class="panel">
        <h3>Parser software problem</h3>

        <p>Report it to the parser maintainers when the issue concerns:</p>

        <ul>
          <li>parser crashes;</li>
          <li>incorrect parser behavior;</li>
          <li>unsupported formats;</li>
          <li>installation problems;</li>
          <li>feature requests.</li>
        </ul>
      </div>

    </div>
  </section>

  <section id="workflow">
    <h2>Tutorial development workflow</h2>

    <p class="section-intro">
      Tutorials are developed and reviewed internally before being promoted to
      the public training repository.
    </p>

    <div class="workflow">
      <span class="workflow-step">Draft</span>
      <span class="workflow-arrow">→</span>
      <span class="workflow-step">Internal Review</span>
      <span class="workflow-arrow">→</span>
      <span class="workflow-step">Approval</span>
      <span class="workflow-arrow">→</span>
      <span class="workflow-step">Publication</span>
    </div>
  </section>

  <section>
    <h2>Contributing</h2>

    <p>
      Members of the project team can contribute new tutorials or improve
      existing materials through the standard branch and pull-request workflow.
    </p>

    <ol>
      <li>Create a branch.</li>
      <li>Update or add the tutorial.</li>
      <li>Test the notebook and example datasets.</li>
      <li>Open a pull request.</li>
      <li>Request review.</li>
      <li>Address feedback.</li>
      <li>Merge after approval.</li>
    </ol>

    <p>
      See
      <a href="../../CONTRIBUTING.md"><code>CONTRIBUTING.md</code></a>
      for detailed contribution and review instructions.
    </p>
  </section>

  <section>
    <h2>Related resources</h2>

    <ul>
      <li>
        <a href="../../README.md">
          BAM Data Store tutorials repository
        </a>
      </li>

      <li>
        BAM Data Store / openBIS user documentation
      </li>

      <li>
        Corresponding parser development repositories
      </li>
    </ul>
  </section>

</main>

<footer>
  <div class="footer-inner">
    BAM Data Store · openBIS Training Materials
  </div>
</footer>

</body>
</html>