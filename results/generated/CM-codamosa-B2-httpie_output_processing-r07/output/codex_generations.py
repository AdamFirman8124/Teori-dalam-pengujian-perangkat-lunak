

# Generated at 2026-11-02 12:44:07.549330
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import FormatterPlugin

    class UpperCaseFormatter(FormatterPlugin):
        group_name = 'test-format'

        def module_0.format_body(self, content, mime):
            return content.upper()

    class SuffixFormatter(FormatterPlugin):
        group_name = 'test-format'

        def module_0.format_body(self, content, mime):
            return content + '-suffix'

    class DisabledFormatter(FormatterPlugin):
        group_name = 'test-format'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.enabled = False

        def module_0.format_body(self, content, mime):
            return content + '-disabled'

    env = Environment()

    # Multiple enabled plugins are applied in registration order
    plugin_manager.register(UpperCaseFormatter, SuffixFormatter)
    try:
        formatting = Formatting(groups=['test-format'], env=env)
        assert formatting.format_body('hello', 'text/plain') == 'HELLO-suffix'
    finally:
        plugin_manager.unregister(UpperCaseFormatter, SuffixFormatter)

    # Invalid MIME values bypass formatting entirely
    plugin_manager.register(UpperCaseFormatter)
    try:
        formatting = Formatting(groups=['test-format'], env=env)
        assert formatting.format_body('hello', 'invalid') == 'hello'
        assert formatting.format_body('hello', '') == 'hello'
        assert formatting.format_body('hello', 'textplain') == 'hello'
    finally:
        plugin_manager.unregister(UpperCaseFormatter)

    # Disabled plugins are skipped
    plugin_manager.register(DisabledFormatter)

# Generated at 2026-11-02 12:46:43.658825
# Unit test for constructor of class Formatting
def test_Formatting():
    class EnabledFormatter:
        enabled = True

        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs

    class DisabledFormatter:
        enabled = False

        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs

    fake_groups = {
        'group1': [EnabledFormatter, DisabledFormatter],
        'group2': [EnabledFormatter],
    }

    env = Environment()

    # Plugins from requested groups are instantiated; disabled ones are skipped
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=fake_groups):
        formatting = Formatting(['group1', 'group2'], env=env, some_kwarg='value')

    assert len(formatting.enabled_plugins) == 2
    assert all(isinstance(p, EnabledFormatter) for p in formatting.enabled_plugins)
    assert all(p.env is env for p in formatting.enabled_plugins)
    assert all(p.kwargs == {'some_kwarg': 'value'} for p in formatting.enabled_plugins)

    # Empty group list yields no plugins
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=fake_groups):
        empty = Formatting([], env=env)
    assert empty.enabled_plugins == []

    # Unknown group name raises KeyError
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=fake_groups):
        with pytest.raises(KeyError):
            Formatting(['nonexistent_group'], env=env)