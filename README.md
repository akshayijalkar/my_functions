# adaptfunctions

[![PyPI](https://img.shields.io/pypi/v/adaptfunctions.svg)](https://pypi.org/project/adaptfunctions/)
[![Python](https://img.shields.io/pypi/pyversions/adaptfunctions.svg)](https://pypi.org/project/adaptfunctions/)
[![GitHub](https://img.shields.io/badge/GitHub-source-181717?logo=github)](https://github.com/akshayijalkar/my_functions)

**adaptfunctions** is an evolving, open-source Python library of reusable utility functions designed to **save development time, reduce repetitive code, and simplify common analysis tasks**. The project aims to collect practical functions that make it easier to inspect, process, and analyze data without repeatedly writing the same helper logic.

Its long-term goal is to build a useful toolkit for programmers, students, analysts, and researchers. Functions will be added and improved over time as the library grows.

## Project goals

- **Save time:** Reuse common operations instead of implementing them from scratch.
- **Support analysis:** Provide small, practical tools for examining and processing data.
- **Simplify workflows:** Keep utility functions straightforward to install, import, and use.
- **Grow over time:** Expand the collection based on real-world needs and community contributions.

## Currently available

| Function | Purpose |
| --- | --- |
| `clen(value)` | Analyze a mixed-content string; extract alphabetic, integer, and decimal groups; print a summary/table; and return structured results. |

Future functions may cover additional text, numerical, and data-analysis tasks. These are **project directions**, not features available in the current release.

> `clen()` differs from Python's built-in `len()`: it categorizes text content rather than simply returning a sequence length, and it is not a drop-in replacement for `len()`.

## Installation

Requires **Python 3.8 or later**.

```bash
python -m pip install adaptfunctions
```

To update an existing installation:

```bash
python -m pip install --upgrade adaptfunctions
```

## Quick start

```python
from adaptfunctions import clen

result = clen("abc 123 xyz 45.67 test 890 .55")
print(result)
```

Calling `clen()` first prints a summary and a three-column table:

```text
char_len : 10
int_len  : 6
float    : 2

string              int                 float_values
------------------------------------------------------------
abc                 123                 45.67
xyz                 890                 .55
test
```

It also returns a dictionary:

```python
{
    "char_len": 10,
    "int_len": 6,
    "float": 2,
    "string": ["abc", "xyz", "test"],
    "int": ["123", "890"],
    "float_values": ["45.67", ".55"]
}
```

The numeric values found in the input are **returned as strings** so their original text is preserved.

## API reference

### `clen(value)`

Analyze a string, print the categorized data, and return a dictionary.

**Parameter**

| Name | Type | Description |
| --- | --- | --- |
| `value` | `str` | The text to analyze. |

**Return value** (`dict`)

| Key | Type | Meaning |
| --- | --- | --- |
| `char_len` | `int` | Total number of alphabetic characters across extracted letter groups. |
| `int_len` | `int` | Total number of digits in extracted integer groups; digits belonging to floats are excluded. |
| `float` | `int` | Number of decimal-number groups found. |
| `string` | `list[str]` | Contiguous alphabetic groups. |
| `int` | `list[str]` | Contiguous integer groups. |
| `float_values` | `list[str]` | Decimal-number groups, including values such as `.55`. |

**Example: access individual fields**

```python
from adaptfunctions import clen

data = clen("Python 2026 version 3.14")

print(data["string"])        # ['Python', 'version']
print(data["int"])           # ['2026']
print(data["float_values"])  # ['3.14']
print(data["char_len"])      # 13
print(data["int_len"])       # 4
print(data["float"])         # 1
```

**Input validation**

Passing a non-string value raises a `TypeError`:

```python
from adaptfunctions import clen

clen(123)  # TypeError: clen() expects a string
```

### Parsing behavior and limitations

- Consecutive alphabetic characters form one string group; `isalpha()` is used, so Unicode letters are supported.
- Consecutive digits form an integer group unless followed by a decimal point and more digits.
- Decimal groups can start with digits (`12.5`) or with a dot (`.5`).
- Whitespace and other punctuation act as separators and are otherwise ignored.
- Signs are not interpreted as part of numbers: `-12` is extracted as `12`.
- Exponential notation is not parsed as a single number: `1e3` is split into integer and letter groups.
- `clen()` **always prints** its summary/table when called; it also returns the dictionary for programmatic use.

## Project layout

```text
my_functions/
├── pyproject.toml
├── README.md
└── src/
    └── adaptfunctions/
        ├── __init__.py
        └── clen.py
```

## Development

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/akshayijalkar/my_functions.git
cd my_functions
python -m pip install -e .
```

The package uses a `src/` layout with setuptools. To propose improvements or report bugs, open an issue or pull request in the [GitHub repository](https://github.com/akshayijalkar/my_functions).

## Links

- **PyPI:** https://pypi.org/project/adaptfunctions/
- **Source code:** https://github.com/akshayijalkar/my_functions
- **Issues:** https://github.com/akshayijalkar/my_functions/issues

## Author

**Akshay Ijalkar** — creator and maintainer of `adaptfunctions`.
