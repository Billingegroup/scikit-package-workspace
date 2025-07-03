# scikit-package-workspace

This is the template for Level 3 of sharing code in `scikit-package`. Please visit the following link for the latest developments and documentation: [https://github.com/scikit-package/scikit-package](https://github.com/scikit-package/scikit-package).

Please read the following guidelines for future contributors:

- The goal is to reuse the code across separate projects.
- Users learn to use `pre-commit` but **without `flake8`**, as `flake8` often slows things down. The basic ones are `black`, `prettier`, and `docformatter`.
- Include `tests` since users may want to share tested code before sharing it with colleagues.
- Use a single `requirements.txt` file (it is too early to divide it into multiple `.txt` files).
