# Playwright Python Boilerplate (widelab.co)

A simple Playwright + pytest (Python) test automation boilerplate for `https://www.widelab.co`.

## Scope

- Page Object Model (POM) with a base class and dedicated pages: home/blog.
- At least 3 selector types:
  - CSS
  - XPath
  - relative XPath (`.//...`) scoped to a parent element.
- Basic smoke and blog assertions.
- Bonus points included:
  - pytest markers (`smoke`, `blog`)
  - screenshot on test failure
  - one parametrized test.

## Requirements

- Python 3.10+ (validated on 3.13)
- `pip`

## Installation

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

## Running tests

Run all tests:

```powershell
.\.venv\Scripts\python -m pytest -v
```

Run smoke tests only:

```powershell
.\.venv\Scripts\python -m pytest -m smoke -v
```

Run blog tests only:

```powershell
.\.venv\Scripts\python -m pytest -m blog -v
```

Run a single file:

```powershell
.\.venv\Scripts\python -m pytest tests/test_blog_page.py -v
```

## Project structure

```text
.
|-- src/
|   |-- pages/
|   |   |-- base_page.py
|   |   |-- home_page.py
|   |   `-- blog_page.py
|-- tests/
|   |-- conftest.py
|   |-- test_home_page.py
|   `-- test_blog_page.py
|-- requirements.txt
|-- pytest.ini
`-- README.md
```

## POM and selector strategies

- `BasePage` contains shared operations: `open`, `click`, `is_visible`, `get_attribute`.
- `HomePage` uses:
  - CSS: `a[href*='blog']`
  - XPath: `(//h1 | //h2)[1]`
  - relative XPath: `.//a[contains(..., 'BLOG')]` scoped to `nav`.
- `BlogPage` uses:
  - XPath for GIF lookup: `//img[contains(@src, '.gif') or contains(@src, 'giphy')]`
  - CSS fallback for GIF/cat-related image candidates.

## Failure artifacts

On test failure, a screenshot is saved to:

`artifacts/screenshots/<test_name>.png`
