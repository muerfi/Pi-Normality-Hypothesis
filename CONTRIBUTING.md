# Contributing

Thank you for taking the time to contribute! This project is a simple exploration of the decimal expansion of π. We welcome bug fixes, new features and documentation improvements.

## Coding style

- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines.
- Use 4 spaces per indentation level.
- Write clear docstrings for modules, classes and functions.
- Keep lines under 100 characters when possible.

## Running tests

Tests are located in the `tests/` directory and use the standard `unittest` module.
Install dependencies first and then run the test suite:

```bash
pip install -r requirements.txt
python -m unittest discover tests
```

Add tests for new functionality whenever relevant and ensure all tests pass before submitting a pull request.

## Submitting pull requests

1. Fork the repository and create a new branch based on `main`.
2. Make your changes and commit with descriptive messages.
3. Run the test suite to verify nothing is broken.
4. Push your branch to your fork and open a pull request targeting `main`.
5. Provide a clear description of what your contribution does and reference any related issues.

We appreciate your contributions!
