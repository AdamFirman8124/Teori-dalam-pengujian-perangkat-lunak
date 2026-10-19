

# Generated at 2024-05-31 03:32:05.565401
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:06.670293
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:07.955704
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:08.982866
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:10.035428
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:13.731908
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:32:19.470307
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:32:23.856157
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    sys.platform = 'sunos'
    facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in facts
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

    sys.platform = 'linux'
    with patch('glob.glob', return_value=['/sys/class/fc_host/host0/port_name']), \
         patch('ansible.module_utils.facts.utils.get_file_lines', return_value=['0x21000014ff52a9bb']):
        facts = collector.collect()
        assert 'fibre_channel_wwn' in facts

# Generated at 2024-05-31 03:32:30.053184
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:32:30.946722
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:45.602808
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:46.786971
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:50.880644
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:32:54.977643
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a suitable module object if needed
    collected_facts = {}

    # Mocking sys.platform to test different branches
    original_platform = sys.platform


# Generated at 2024-05-31 03:32:56.315122
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:32:57.510310
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:33:02.019639
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:33:03.214681
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:33:04.653702
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:33:05.817244
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:33:23.334322
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a suitable module object if needed
    collected_facts = {}

    # Mocking sys.platform to test different branches
    original_platform = sys.platform


# Generated at 2024-05-31 03:33:28.053978
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a fake Ansible module if needed
    collected_facts = {}

    # Mocking sys.platform to test different platforms
    original_platform = sys.platform


# Generated at 2024-05-31 03:33:32.254585
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:33:34.714520
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    collected_facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in collected_facts
    assert collected_facts['fibre_channel_wwn'] == ['10000090fa1658de']

# Generated at 2024-05-31 03:33:36.085578
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:33:39.696948
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:33:42.769589
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a suitable module object if needed
    collected_facts = {}

    # Mocking sys.platform to test different branches
    original_platform = sys.platform


# Generated at 2024-05-31 03:33:46.309205
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:33:48.315655
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    collected_facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in collected_facts
    assert collected_facts['fibre_channel_wwn'] == ['10000090fa1658de']

# Generated at 2024-05-31 03:33:53.111067
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:34:06.243076
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:34:07.277731
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:34:08.527827
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:34:12.927316
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    sys.platform = 'sunos'
    facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in facts
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

    sys.platform = 'linux'
    with patch('glob.glob', return_value=['/sys/class/fc_host/host0/port_name']), \
         patch('ansible.module_utils.facts.utils.get_file_lines', return_value=['0x21000014ff52a9bb']):
        facts = collector.collect()
        assert 'fibre_channel_wwn' in facts

# Generated at 2024-05-31 03:34:14.550607
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert isinstance(collector._fact_ids, set)
    assert collector._fact_ids == set()

# Generated at 2024-05-31 03:34:15.491003
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:34:19.179449
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:34:21.649856
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:34:28.982541
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:34:30.169266
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:35:03.741129
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:35:06.998159
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:35:09.284944
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:35:10.829615
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:35:14.354885
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:35:18.165144
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:35:21.578657
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:35:25.198687
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a suitable module object if needed
    collected_facts = {}

    # Mocking sys.platform to test different branches
    original_platform = sys.platform


# Generated at 2024-05-31 03:35:29.583346
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:35:32.886756
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    sys.platform = 'sunos'
    facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in facts
    assert facts['fibre_channel_wwn'] == ['10000090fa1658de']

    sys.platform = 'linux'
    with patch('glob.glob', return_value=['/sys/class/fc_host/host0/port_name']), \
         patch('ansible.module_utils.facts.utils.get_file_lines', return_value=['0x21000014ff52a9bb']):
        facts = collector.collect()
        assert 'fibre_channel_wwn' in facts

# Generated at 2024-05-31 03:36:27.479189
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:36:28.444483
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:36:32.080495
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:36:35.880442
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:36:36.984356
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:36:40.515732
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:36:41.555841
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:36:44.535576
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/fakepath'
    module_mock.run_command.return_value = (0, 'HBA Port WWN: 10000090fa1658de\n', '')

    collected_facts = collector.collect(module=module_mock)
    assert 'fibre_channel_wwn' in collected_facts
    assert collected_facts['fibre_channel_wwn'] == ['10000090fa1658de']

# Generated at 2024-05-31 03:36:45.510698
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:36:46.760443
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:29.864943
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None  # Mock module if necessary

# Generated at 2024-05-31 03:38:30.909268
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:31.898689
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:35.163071
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    module = None

# Generated at 2024-05-31 03:38:36.254391
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert isinstance(collector._fact_ids, set)
    assert collector._fact_ids == set()

# Generated at 2024-05-31 03:38:42.399059
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    module = None  # Mock or create a fake Ansible module if needed
    collected_facts = {}

    # Mocking sys.platform to test different platforms
    original_platform = sys.platform


# Generated at 2024-05-31 03:38:44.739794
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:45.817288
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:51.216338
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():    collector = FcWwnInitiatorFactCollector()

# Generated at 2024-05-31 03:38:52.467575
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():    collector = FcWwnInitiatorFactCollector()