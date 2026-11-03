

# Generated at 2026-11-02 13:01:02.983046
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    import pygments.styles

    # A style name known to Pygments should return the corresponding style class
    assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('default') is pygments.styles.get_style_by_name('default')

    # Any returned class should be a subclass of pygments.style.Style
    assert issubclass(ColorFormatter.get_style_class('monokai'), pygments.style.Style)

    # An unknown style name should fall back to the bundled Solarized256Style
    assert ColorFormatter.get_style_class('definitely-not-a-style') is Solarized256Style
    assert issubclass(ColorFormatter.get_style_class('definitely-not-a-style'), pygments.style.Style)

# Generated at 2026-11-02 13:08:58.685742
# Unit test for method get_lexer_for_body of class ColorFormatter