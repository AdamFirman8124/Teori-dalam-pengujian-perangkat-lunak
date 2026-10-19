

# Generated at 2024-03-18 05:33:57.590732
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:34:03.967333
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:34:10.438399
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='alpha') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='beta') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='alpha') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:34:16.796942
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:34:24.542632
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha pre-release bump on existing alpha pre-release
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Test beta pre-release bump on existing alpha pre-release

# Generated at 2024-03-18 05:34:31.890951
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:34:38.081806
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:34:43.526913
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:34:52.809193
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:35:00.914569
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:35:38.046061
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:35:43.582993
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:35:50.312918
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:35:59.280207
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:36:06.811703
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:36:17.475435
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:36:25.662734
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:36:31.454118
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:36:39.012558
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:36:46.935677
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:37:21.525528
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='alpha') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='beta') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='alpha') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:37:28.342457
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:37:34.283981
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:37:39.506549
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:37:44.523105
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test

# Generated at 2024-03-18 05:37:54.812983
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha pre-release bump on minor version
    assert bump_version('1.2.0', position=1, pre_release='alpha') == '1.3.0a0'
    # Test beta pre-release bump on patch version

# Generated at 2024-03-18 05:38:01.462940
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:38:07.795882
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha pre-release bump on existing alpha pre-release
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Test beta pre-release bump on existing alpha pre-release

# Generated at 2024-03-18 05:38:14.928991
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:38:20.015442
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:39:02.094965
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha pre-release bump on existing alpha pre-release
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Test beta pre-release bump on existing alpha pre-release

# Generated at 2024-03-18 05:39:09.244396
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:39:18.129725
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:39:24.090561
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test beta pre-release increment

# Generated at 2024-03-18 05:39:29.608606
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:39:34.620719
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:39:42.550419
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:39:49.827316
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:39:57.286218
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test

# Generated at 2024-03-18 05:40:03.565949
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:40:39.548921
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:40:48.754620
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:40:56.575293
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:41:04.043296
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3') == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha pre-release bump on existing alpha pre-release
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Test beta pre-release bump on existing alpha pre-release

# Generated at 2024-03-18 05:41:11.960538
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:41:20.764286
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release increment
    assert bump_version('1.2.3a0', pre_release='a') == '1.2.3a1'
    # Test

# Generated at 2024-03-18 05:41:28.300550
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2024-03-18 05:41:36.703149
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:41:43.037181
# Unit test for function bump_version
def test_bump_version():    # Test major version bump
    assert bump_version('1.2.3', position=0) == '2.0.0'
    # Test minor version bump
    assert bump_version('1.2.3', position=1) == '1.3.0'
    # Test patch version bump
    assert bump_version('1.2.3', position=2) == '1.2.4'
    # Test alpha pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test beta pre-release bump on patch version
    assert bump_version('1.2.3', pre_release='b') == '1.2.4b0'
    # Test alpha pre-release bump on minor version

# Generated at 2024-03-18 05:41:51.945256
# Unit test for function bump_version
def test_bump_version():    assert bump_version('1.2.2') == '1.2.3'