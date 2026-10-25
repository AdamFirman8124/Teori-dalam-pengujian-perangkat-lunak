# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest

from sty import Register, Style
from sty.rendertype import Sgr


def test_setattr_on_muted_register_renders_style_with_empty_value():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

    rule = Sgr(1)
    style = Style(rule, value="original")

    reg.myattr = style

    # __setattr__ should have replaced the value with a Style built from the
    # same rules but with an empty rendered value (line 83).
    stored = reg.myattr
    assert isinstance(stored, Style)
    assert stored.rules == (rule,)
    assert str(stored) == ""
