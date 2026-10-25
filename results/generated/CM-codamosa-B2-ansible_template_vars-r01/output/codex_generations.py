

# Generated at 2026-10-24 15:03:11.975966
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:14.390895
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:16.806969
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:24.998234
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from ansible.template import Templar

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables if available_variables is not None else {}

    # Case 1: locals is None -> returns self
    templar = FakeTemplar({'foo': 'bar'})
    globals_dict = {'range': range, 'lookup': None}
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    result = j2vars.add_locals(None)
    assert result is j2vars

    # Case 2: locals provided -> returns a new AnsibleJ2Vars with merged locals
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'local1': 'value1'})
    new_j2vars = j2vars.add_locals({'local2': 'value2'})

    assert isinstance(new_j2vars, AnsibleJ2Vars)
    assert new_j2vars is not j2vars

    # Original locals plus new locals should be present
    assert 'local1' in new_j2vars._locals
    assert 'local2' in new_j2vars._locals
    assert new_j2vars._locals['local1'] == 'value1'
    assert new_j2vars._locals['local2'] == 'value2'

    # Original object should be unchanged
    assert 'local2' not in j2vars._locals
    assert j2vars._locals['local1'] == 'value1'

    # Globals and templar should be carried over
    assert new_j2vars._globals is globals_dict
    assert new_j2vars._templar is templar

    # Membership and lookup through the new proxy
    assert 'local1' in new_j2vars
    assert 'local2' in new_j2vars
    assert 'foo' in new_j2vars
    assert 'range' in new_j2vars
    assert 'nonexistent' not in new_j2vars

    assert new_j2vars['local1'] == 'value1'
    assert new_j2vars['local2'] == 'value2'

    # Case 3: empty locals dict -> still returns a new object with copied locals
    new_j2vars_empty = j2vars.add_locals({})
    assert isinstance(new_j2vars_empty, AnsibleJ2Vars)
    assert new_j2vars_empty is not j2vars
    assert new_j2vars_empty._locals == j2vars._locals

    # Case 4: chained add_locals calls accumulate locals
    chained = j2vars.add_locals({'a': 1}).add_locals({'b': 2})
    assert chained._locals['a'] == 1
    assert chained._locals['b'] == 2
    assert chained._locals['local1'] == 'value1'

# Generated at 2026-10-24 15:03:43.429293
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = _FakeTemplar()
    globals_ = {'range': range}

    # 1. scopes stored by reference; 'l_' prefix stripped

# Generated at 2026-10-24 15:03:45.957289
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:48.372971
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:50.786459
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:53.331219
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:55.746777
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:03:58.164389
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:00.580085
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:03.145119
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:05.556202
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:07.969650
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:10.398929
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:12.814924
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:15.230287
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:17.914628
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:20.330475
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:22.744953
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:25.162468
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:27.576142
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:29.993110
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:32.403535
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:37.393467
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:04:53.881051
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = _FakeTemplar()
    globals_ = {'range': range}

    # 1. scopes stored by reference; 'l_' prefix stripped

# Generated at 2026-10-24 15:05:07.805498
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:00.445905
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-24 15:06:01.864745
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:29.841685
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:32.261006
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:34.856575
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:37.265228
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:39.675603
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:42.088491
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:43.400830
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:06:44.710016
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:19.655364
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:22.072048
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:24.487319
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:26.899389
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:29.315721
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:31.728723
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:34.140616
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:36.556207
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:38.968928
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:41.382331
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:43.795697
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:46.212747
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:48.622924
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:51.036839
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:53.449986
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:55.863990
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:07:58.277579
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:00.691895
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:03.105939
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:05.519115
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:07.933731
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:22.059238
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:23.372557
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:24.694232
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:08:59.844977
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:02.474219
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:04.887196
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:07.299676
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:09.713488
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:11.359652
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:12.852431
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:14.162148
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:15.616057
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:17.062022
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:18.391765
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:19.759979
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:36.304533
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:38.718455
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:41.226948
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:43.734079
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:46.148726
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:48.795690
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:51.208206
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:53.620497
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:56.033073
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:09:58.445971
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:00.859430
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:03.273066
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:05.686437
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:08.099443
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:10.513782
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:12.926078
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:15.340746
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:17.753572
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:20.167380
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:22.580940
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:24.994045
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:27.407594
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:29.821330
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:32.234809
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:35.312674
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:37.725160
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:40.138108
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:42.551153
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:44.965116
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:47.377801
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:49.790432
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:52.206185
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:54.617036
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:57.029877
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:10:59.443629
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:01.857604
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:04.273093
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:06.689115
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:08.369608
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:25.157789
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:26.466671
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:27.789660
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:29.130020
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:30.453090
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:31.775659
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:48.343051
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = _FakeTemplar()
    globals_ = {'range': range}

    # 1. scopes stored by reference; 'l_' prefix stripped

# Generated at 2026-10-24 15:11:50.762985
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:53.178347
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:55.593910
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:11:58.009130
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:00.422452
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:02.836703
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:07.242852
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:09.654606
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:12.066398
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:14.478389
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:16.891811
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:19.304241
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:21.717026
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:24.131070
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:26.544974
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:28.959734
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:31.372433
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:49.836739
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-24 15:12:51.151727
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:52.467968
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:12:53.831336
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:13:10.520646
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:13:12.940642
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 15:13:15.350883
# Unit test for method __contains__ of class AnsibleJ2Vars