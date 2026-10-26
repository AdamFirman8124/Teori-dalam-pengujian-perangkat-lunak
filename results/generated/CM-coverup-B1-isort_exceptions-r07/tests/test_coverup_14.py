# file: project/isort/exceptions.py:171-180
# asked: {"lines": [175, 176], "branches": []}
# gained: {"lines": [175, 176], "branches": []}

from isort.exceptions import MissingSection


def test_missing_section_includes_import_module_and_section_in_error_message():
    import_module = "example_module"
    section = "CUSTOM"

    error = MissingSection(import_module, section)

    assert str(error) == (
        "Found example_module import while parsing, but CUSTOM was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert error.args == (str(error),)
