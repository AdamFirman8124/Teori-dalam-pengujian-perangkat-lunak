

# Generated at 2026-10-24 13:24:20.189297
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:24:58.658652
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:25:16.811728
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:25:19.231533
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 13:25:21.644584
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 13:25:30.278393
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():cfg = SetupCfgCommandConfig(name="my-cmd", camel="MyCmd", description="My description", commands=("echo hi", "ls -l"))

# Generated at 2026-10-24 13:26:09.729415
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:11.100723
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:26:18.612407
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Build the project',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )

    assert obj.name == 'build'
    assert obj.camel == 'Build'
    assert obj.description == 'Build the project'
    assert obj.commands == ('python setup.py build', 'python setup.py bdist_wheel')

    # It must behave like a tuple
    assert tuple(obj) == ('build', 'Build', 'Build the project',
                          ('python setup.py build', 'python setup.py bdist_wheel'))
    assert len(obj) == 4
    assert obj[0] == 'build'

    # Fields are immutable (NamedTuple)
    try:
        obj.name = 'other'  # type: ignore[misc]
        raised = False
    except AttributeError:
        raised = True
    assert raised is True, 'SetupCfgCommandConfig fields should be immutable'

    # Equality with an equivalent plain tuple
    assert obj == ('build', 'Build', 'Build the project',
                   ('python setup.py build', 'python setup.py bdist_wheel'))


if __name__ == '__main__':
    test_SetupCfgCommandConfig()
    print('test_SetupCfgCommandConfig passed')

# Generated at 2026-10-24 13:26:20.048434
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Build the project',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )

    assert obj.name == 'build'
    assert obj.camel == 'Build'
    assert obj.description == 'Build the project'
    assert obj.commands == ('python setup.py build', 'python setup.py bdist_wheel')

    # It must behave like a tuple
    assert tuple(obj) == ('build', 'Build', 'Build the project',
                          ('python setup.py build', 'python setup.py bdist_wheel'))
    assert len(obj) == 4
    assert obj[0] == 'build'

    # Fields are immutable (NamedTuple)
    try:
        obj.name = 'other'  # type: ignore[misc]
        raised = False
    except AttributeError:
        raised = True
    assert raised is True, 'SetupCfgCommandConfig fields should be immutable'

    # Equality with an equivalent plain tuple
    assert obj == ('build', 'Build', 'Build the project',
                   ('python setup.py build', 'python setup.py bdist_wheel'))


if __name__ == '__main__':
    test_SetupCfgCommandConfig()
    print('test_SetupCfgCommandConfig passed')

# Generated at 2026-10-24 13:26:22.562071
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:25.065105
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:27.475409
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:46.167838
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:47.493170
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:26:48.805570
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:50.253966
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:26:51.688362
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:53.011999
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:26:55.904256
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:26:57.208019
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:26:59.967667
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:01.276839
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:04.099122
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:05.448161
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:08.610735
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:09.923464
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:13.013620
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:14.420290
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:17.288783
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:19.935717
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:22.598247
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:25.016260
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:27.427838
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:29.841814
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:32.256132
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:33.877939
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:35.299066
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:36.612771
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:37.972313
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:39.405608
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:40.839390
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:42.272218
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:43.603581
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:44.929221
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:46.263562
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:47.588739
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:50.422034
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:52.054483
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:55.277052
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:56.599999
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:27:58.249413
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:27:59.568462
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:28:01.097646
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:02.433912
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:28:03.870360
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:05.379915
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:28:07.962720
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:10.514320
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:12.933114
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:15.347974
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:17.769504
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:20.187868
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:22.601041
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:25.021889
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:27.435878
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:29.856894
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:32.276762
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:50.177492
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:52.931452
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:54.255090
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:28:57.136693
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:28:58.435081
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:29:01.121561
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:02.463502
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:29:05.220674
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:06.552645
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:29:09.394303
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:12.065553
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:14.726946
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:17.141240
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:19.557971
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:21.970961
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:24.389539
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:26.812972
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:29.228324
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:31.644847
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:34.062857
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:51.813351
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:54.753454
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:29:56.358702
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:29:59.113207
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:00.450450
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:03.505447
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:04.820048
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:06.247848
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:07.581074
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:09.015148
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:10.339445
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:13.106644
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:14.546296
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:17.668127
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:20.279352
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:22.695048
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:25.311314
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:27.726537
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:30.142251
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:32.556617
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:34.972068
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:37.389167
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:39.992175
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:41.415339
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:44.128298
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:45.503389
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:48.215835
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:49.539635
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:52.391362
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:53.722753
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:30:56.419658
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:30:57.735176
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:31:00.523704
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:01.841903
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:31:04.608135
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:07.029760
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:09.441925
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:13.980697
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:16.581940
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:19.001474
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:21.416598
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:23.841223
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:26.244285
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:28.658939
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:31.080338
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:33.522301
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:35.968845
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:38.536658
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:40.952142
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:44.080190
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:45.423697
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:31:48.131394
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:49.453737
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:31:52.178033
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:53.508470
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:31:56.185050
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:31:57.507334
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:32:00.548395
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:01.878551
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:32:04.423544
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:06.839374
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:09.253791
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:17.484574
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:20.001918
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:22.422380
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:24.839277
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:27.257349
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:29.674195
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:32.090124
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:34.504979
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:36.923546
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:39.337548
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:41.750855
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:44.163718
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:46.582222
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:48.994617
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:51.418752
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:32:53.827038
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:11.540959
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:12.852368
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:33:14.183401
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:15.515491
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:33:16.848199
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:18.208133
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:33:20.903572
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:22.214398
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 13:33:24.776662
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:27.433086
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:30.034003
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:47.344298
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:49.756953
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:52.175857
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:54.592922
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:33:57.012173
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 13:34:39.925265
# Unit test for function each_sub_command_config