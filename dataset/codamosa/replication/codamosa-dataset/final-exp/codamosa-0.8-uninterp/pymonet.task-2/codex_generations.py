

# Generated at 2022-06-14 03:57:52.542279
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(4)
    task = task.bind(lambda x: Task.of(x + 4))
    assert isinstance(task, Task)
    assert task.fork(lambda value: value, lambda value: value) == 8



# Generated at 2022-06-14 03:57:56.284550
# Unit test for method map of class Task
def test_Task_map():
    value_a = 5
    value_b = 6
    task_a = Task.of(value_a)
    result_a = task_a.map(lambda arg: arg + 1).fork(lambda a: a, lambda a: a)

    assert result_a == value_b


# Generated at 2022-06-14 03:58:07.785537
# Unit test for method map of class Task
def test_Task_map():
    # test for map, where both value and error are strings
    def test_Task_map_string(value, error):
        # construct Task object
        task = Task(lambda reject, resolve: reject(error) if value else resolve(value))

        # check that results of map is Task with mapped resolve and unchanged reject
        assert task.map(lambda _: 'map').fork('error', lambda _: 'resolve') == 'error'
        assert task.map(lambda _: 'map').fork(lambda _: 'error', lambda _: 'resolve') == 'error'
        assert task.fork('error', lambda _: 'map').map(lambda _: 'resolve') == 'resolve'
        assert task.fork(lambda _: 'error', lambda _: 'map').map(lambda _: 'resolve') == 'resolve'

    # test for

# Generated at 2022-06-14 03:58:17.023920
# Unit test for method bind of class Task
def test_Task_bind():
    def func(arg):
        return Task.of(arg + 1)

    def func_error(arg):
        return Task.reject(arg + 1)

    assert Task\
        .of(1)\
        .bind(func)\
        .fork(
            lambda arg: arg,
            lambda _: None
        ) == 2

    assert Task\
        .of(1)\
        .bind(func)\
        .bind(lambda arg: Task.of(arg + 1)) \
        .fork(
            lambda arg: arg,
            lambda _: None
        ) == 3

    assert Task\
        .of(1)\
        .bind(func_error)\
        .fork(
            lambda arg: arg,
            lambda _: None
        ) == 2


# Generated at 2022-06-14 03:58:23.821408
# Unit test for method map of class Task
def test_Task_map():

    def fn(arg):
        return arg ** 2

    def fork(_, resolve):
        return resolve(2)

    task = Task(fork)

    assert task.map(fn).fork(
        reject=None,
        resolve=lambda arg: arg
    ) == 4



# Generated at 2022-06-14 03:58:39.500567
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        """
        Function to call during fork function call
        to store result of fork function call.

        :param value: object to resolve
        :type value: A
        :returns: object to store
        :rtype: A
        """
        global result
        result = value

    def reject(value):
        """
        Function to call during fork function call
        to store result of fork function call.

        :param value: object to reject
        :type value: A
        :returns: object to store
        :rtype: A
        """
        global result
        result = value

    # case 1
    global result
    result = None

    task = Task.of(2)
    task = task.map(lambda x: x * 2)
    task.fork(reject, resolve)

    assert result

# Generated at 2022-06-14 03:58:43.676566
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    # GIVEN a task with resolved value
    task = Task.of(3)
    # WHEN we apply to Task of map method
    # THEN we must get new Task with resolved value multiple on 3
    new_task = task.map(lambda x: x * 3)
    return new_task.fork(lambda x: x, lambda x: x) == 9
assert test_Task_map()


# Generated at 2022-06-14 03:58:45.986677
# Unit test for method bind of class Task
def test_Task_bind():
    result = Task.of(1)
    task = result.bind(lambda x: Task.of(x + 2))
    assert task.fork(lambda x: False, lambda x: x == 3)


# Generated at 2022-06-14 03:58:54.815862
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        if value:
            return Task.of(value)
        else:
            return Task.reject('reject')

    # Should return value
    assert Task.of(1).bind(resolve).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 1

    # Should return 'rejected'
    assert Task.of(0).bind(resolve).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 'reject'

# Generated at 2022-06-14 03:59:04.367532
# Unit test for method map of class Task
def test_Task_map():
    @Task
    def add2(reject, resolve):
        resolve(2 + 2)

    @add2.map
    def adding(num):
        return num + 2

    assert adding.fork is not None, "map method don't return Task"
    assert adding.fork(lambda _: None, print) is not None, 'fork method don\'t run resolve function'
    assert adding.fork(print, lambda _: None) is not None, 'fork method don\'t run reject function'

    with pytest.raises(TypeError):
        @add2.map
        def not_adding(num):
            return num % 2

        not_adding.fork(lambda _: None, print)



# Generated at 2022-06-14 03:59:10.332468
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 12

    task = Task.of(10).map(mapper)
    assert task.fork(lambda _: False, lambda arg: arg == 22)


# Generated at 2022-06-14 03:59:19.974836
# Unit test for method map of class Task
def test_Task_map():
    def check_map(mapped):
        assert mapped.fork(lambda a: a, lambda a: a * 2) == 60

    def reject(_):
        pass

    resolve = lambda x: x * 3

    task = Task(
        lambda rejected, resolved: resolved(10)
    )
    mapped = task.map(lambda a: a * 2)
    check_map(mapped)
    task = Task(
        lambda rejected, resolved: rejected(10)
    )
    mapped = task.map(lambda a: a * 2)
    check_map(mapped)
    task = Task(
        lambda rejected, resolved: resolved(10)
    )
    mapped = task.map(lambda a: a * 2).map(lambda a: a * 3)
    check_map(mapped)

# Generated at 2022-06-14 03:59:24.852886
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(5).map(lambda x: x * x).fork(
        lambda x: "error",
        lambda x: "success"
    ) == "success"

    assert Task.of(5).map(lambda x: x * x).fork(
        lambda x: "error",
        lambda x: x
    ) == 25


# Generated at 2022-06-14 03:59:33.179495
# Unit test for method bind of class Task
def test_Task_bind():
    def bind_true(resolve, reject):
        return Task.of(True).bind(lambda arg: Task.of(arg)).fork(reject, resolve)

    def bind_false(resolve, reject):
        return Task.of(False).bind(lambda arg: Task.of('test')).fork(reject, resolve)

    assert Task(bind_true).fork(lambda x: False, lambda x: x)
    assert Task(bind_false).fork(lambda x: False, lambda x: x == 'test')

    def bind_rejected(resolve, reject):
        return Task.reject('rejected').bind(lambda x: Task.of('test')).fork(reject, resolve)

    assert Task(bind_rejected).fork(lambda x: x == 'rejected', lambda x: False)



# Generated at 2022-06-14 03:59:39.892434
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task.of(x * 2)

    assert Task.of(3).bind(f).fork(
        lambda error: None,
        lambda value: value == 6
    )

    assert Task.of(3).bind(f).bind(f).fork(
        lambda error: None,
        lambda value: value == 12
    )

test_Task_bind()


# Generated at 2022-06-14 03:59:42.678082
# Unit test for method bind of class Task
def test_Task_bind():
    from expect import expect


    def plus(n):
        return Task.of(n + 1)

    # assert
    expect(Task.of(100).bind(plus).fork(lambda r: r, lambda r: r)).to_equal(101)



# Generated at 2022-06-14 03:59:47.448155
# Unit test for method bind of class Task
def test_Task_bind():
    def fork1(reject, resolve):
        resolve(1)

    def fork2(reject, resolve):
        resolve(2)

    task1 = Task(fork1)
    task2 = Task(fork2)

    def mapper1(value):
        assert (value == 1)
        return value + 1

    def mapper2(value):
        assert (value == 2)
        return value + 2

    def test_equals(value):
        assert (value == 2)
        return True

    assert Task(fork1).bind(lambda value: task2).map(mapper2).map(test_equals).fork(lambda _: False, lambda value: value)

# Generated at 2022-06-14 03:59:54.883848
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind(fn) -> Task[reject, mapped_value]
    """

    def fn(value):
        return value * 2

    def fn_task(value):
        return Task.of(value * 2)

    assert Task.of(1).bind(fn) == Task.of(2)
    assert Task.of(1).bind(fn_task) == Task.of(2)
    assert Task.reject(1).bind(fn) == Task.reject(1)
    assert Task.reject(1).bind(fn_task) == Task.reject(1)

# Generated at 2022-06-14 03:59:59.438301
# Unit test for method map of class Task
def test_Task_map():
    TASK_OF_ONE = Task.of(1)
    RESULT = TASK_OF_ONE.map(lambda x: x + 1)
    assert RESULT.fork(None, lambda value: value) == 2


# Generated at 2022-06-14 04:00:03.840954
# Unit test for method map of class Task
def test_Task_map():
    def inc(x):
        return x + 1

    t = Task.of(1)
    result = t.map(inc)

    assert result.fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 2


# Generated at 2022-06-14 04:00:11.474067
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda _, _: 1) \
        .map(lambda x: x + 1) \
        .fork(
            lambda arg: arg,
            lambda arg: arg
        ) == 2


# Generated at 2022-06-14 04:00:21.449554
# Unit test for method bind of class Task
def test_Task_bind():
    @Task.of
    def add(a, b):
        return a + b

    @Task.of
    def square(a):
        return a ** 2

    @Task.of
    def cube(a):
        return a ** 3

    @Task.of
    def sum(a, b):
        return a + b

    def combine(a, b):
        return a.bind(lambda a: b.map(lambda b: (a, b)))

    def get_result(result):
        x, y, z = result

        return x + y ** 2 + z ** 3

    assert get_result(
        Task.of(1).bind(lambda a:
        Task.of(2).map(lambda b:
        combine(a, b))).fork(None, lambda result: result)) == 14

    assert get_result

# Generated at 2022-06-14 04:00:24.389116
# Unit test for method map of class Task
def test_Task_map():
    inc = lambda x: x + 1
    to_str = lambda x: str(x)

    assert (
        Task(lambda _, resolve: resolve(1))
        .map(inc)
        .map(inc)
        .map(to_str)
        .fork(lambda _: None, lambda x: x)
        == '3'
    )

# Generated at 2022-06-14 04:00:37.233127
# Unit test for method map of class Task
def test_Task_map():
    yield "Task.map - of"
    test = Task.of("To be mapped")
    actual = test.map(lambda item: item + " Mapped, mapper")
    expected = Task.of("To be mapped Mapped, mapper")

    assert actual.fork(lambda item: item, lambda item: item) == expected.fork(lambda item: item, lambda item: item)
    yield "Task.map - reject"
    test = Task.reject("To be mapped")
    actual = test.map(lambda item: item + " Mapped, mapper")
    expected = Task.reject("To be mapped")

    assert actual.fork(lambda item: item, lambda item: item) == expected.fork(lambda item: item, lambda item: item)
    yield "Task.map - reject in of"

# Generated at 2022-06-14 04:00:44.583307
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        resolve(3)

    def fork_reject(reject, resolve):
        reject(3)

    def times_two(value):
        return value * 2

    assert Task(fork).map(times_two).fork(lambda a: a, lambda a: a) == 6
    assert Task(fork_reject).map(times_two).fork(lambda a: a, lambda a: a) == 3



# Generated at 2022-06-14 04:00:47.672558
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda _, resolve: resolve(1)).map(lambda x: x + 1).fork(
        lambda reject: assert_(False),
        lambda resolve: assert_(resolve == 2)
    )


# Generated at 2022-06-14 04:00:54.785268
# Unit test for method map of class Task
def test_Task_map():
    divide_by_2 = lambda x: x / 2
    original_value = 5
    mapped_value = divide_by_2(original_value)

    # Check not raising error

# Generated at 2022-06-14 04:01:02.681848
# Unit test for method bind of class Task
def test_Task_bind():
    import json
    import urllib
    from urllib.request import urlopen

    # read url from console
    url = input("Enter url: ")

    # return requested url and read content as utf-8
    # return Task of this
    def readurl(url):
        def result(reject, resolve):
            return urllib.request.urlopen(url, timeout=5).read().decode('utf-8')

        return Task(result)

    # parse json and take first part of three
    # return Task of this
    def parse_json(json_str):
        return Task.of(json.loads(json_str)[0])

    # print result
    def print_result(value):
        print(value)

    # handle errors

# Generated at 2022-06-14 04:01:08.137561
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve('world')

    def mapper(arg):
        return Task.of('hello ' + arg)

    t = Task(fork)
    result = t.bind(mapper)
    assert result.fork(lambda arg: 'reject', lambda arg: arg) == 'hello world', 'result of executed bind is invalid'


# Generated at 2022-06-14 04:01:15.265981
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task.map method.
    """
    sum_result = Task.of(1).map(lambda x: x + 1)
    assert Task.of(2) == sum_result

    # error handling
    add_error = Task.reject(2).map(lambda x: x + 1)
    assert Task.reject(2) == add_error

    # lazy
    lazy = Task(lambda reject, resolve: resolve(1))
    assert Task.of(2) == lazy.map(lambda x: x + 1)

    # test compose
    add2 = Task.of(1).map(lambda x: x + 1)
    add3 = Task.of(2).map(lambda x: x + 1)

# Generated at 2022-06-14 04:01:27.914630
# Unit test for method map of class Task
def test_Task_map():
    task = Task(
        lambda reject, resolve: reject('error')
    )
    f = task.map(lambda value: value + '1')

    assert isinstance(f.fork, types.FunctionType)
    assert f.fork(
        lambda arg: arg,
        exception
    ) == 'error'

    task = Task(
        lambda reject, resolve: resolve('value')
    )
    f = task.map(lambda value: value + '1')

    assert isinstance(f.fork, types.FunctionType)
    assert f.fork(
        exception,
        lambda arg: arg
    ) == 'value1'


# Generated at 2022-06-14 04:01:41.116837
# Unit test for method bind of class Task
def test_Task_bind():
    # pylint: disable=unused-argument
    # pylint: disable=unused-variable
    def assertTask(result_task, expected_value):
        result_event = []
        def resolve_handler(arg):
            result_event.append('resolve')
            result_event.append(arg)

        def reject_handler(arg):
            result_event.append('reject')
            result_event.append(arg)

        result_task.fork(reject_handler, resolve_handler)
        eq_(result_event, expected_value)


    task_instance = Task(lambda reject, resolve: resolve('success'))
    assertTask(
        task_instance.bind(lambda arg: Task.of('mapped')),
        ['resolve', 'mapped']
    )


# Generated at 2022-06-14 04:01:50.755185
# Unit test for method map of class Task
def test_Task_map():
    """
    1. Create task with fork function, which return increment of argument
    2. Create task with fork function, which return decrement of argument
    3. Create task with fork function, which return None
    4. Create task with fork function, which return decrement of argument
    5. Create task with fork function, which return increment of argument
    6. Create task with fork function, which return None

    7. Run two steps and check result equals 1
    8. Run two steps and check result equals -1
    9. Run two steps and check result equals 0
    10. Run two steps and check result equals -1
    11. Run two steps and check result equals 1
    12. Run two steps and check result equals 0
    """
    def step(fn, argument):
        def result(reject, resolve):
            return fn(reject, resolve)(argument)



# Generated at 2022-06-14 04:01:56.955910
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        return Task.of(value + 1)

    def reject(value):
        return Task.reject(value)

    task1 = Task.of(1)
    task2 = task1.map(lambda value: value + 1).bind(resolve)
    task3 = task1.map(lambda value: value + 1).bind(reject)

    assert task1.fork(lambda value: False, lambda value: value == 1) == True
    assert task2.fork(lambda value: False, lambda value: value == 3) == True
    assert task3.fork(lambda value: value == 2, lambda value: False) == True

# Generated at 2022-06-14 04:02:00.002975
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(2).map(lambda x: x*2).fork(lambda x: x, lambda x: x) == 4


# Generated at 2022-06-14 04:02:03.464836
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(5).map(lambda x: x + 3).fork(None, lambda y: y) == 8


# Generated at 2022-06-14 04:02:13.007663
# Unit test for method map of class Task
def test_Task_map():
    def fork(_, resolve):
        resolve(9)

    def mapper(value):
        return value * 2

    forked_task = Task(fork).map(mapper)
    assert forked_task.fork(lambda arg: arg, lambda arg: arg) == 18

    def fork(_, resolve):
        resolve(9)

    def mapper(value):
        return value * 2

    def foo(arg):
        return arg * 2

    forked_task = Task(fork).map(mapper).map(foo)
    assert forked_task.fork(lambda arg: arg, lambda arg: arg) == 36;



# Generated at 2022-06-14 04:02:22.055707
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Function for testing bind method of class Task.
    """
    inc = lambda value: value + 1
    task = Task.of(1)
    actual = task.bind(lambda v: Task.of(3)).bind(inc)
    actual.fork(
        lambda e: e,
        lambda v: v == (1 + 1 + 1)
    )

    actual = task.bind(lambda v: Task.reject(3)).bind(inc)
    actual.fork(
        lambda e: e,
        lambda v: v == (1 + 1 + 1)
    )


# Generated at 2022-06-14 04:02:27.170566
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(a):
        return Task.of(a + 2)

    def fork(_, resolve):
        resolve(1)

    task = Task(fork)
    assert Task(task.bind(fn).fork).fork(print, lambda a: a) == 3



# Generated at 2022-06-14 04:02:32.949925
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method with resolve used
    """
    identity = lambda arg: arg
    inc = lambda arg: arg + 1
    dec = lambda arg: arg - 1
    binded = Task.of(1).bind(lambda arg: Task.of(inc(arg))).map(dec)
    assert binded.fork(identity, identity) == 1


# Generated at 2022-06-14 04:02:46.273752
# Unit test for method map of class Task
def test_Task_map():
    def fn(input):
        return input + 1

    def assert_task_map(fn, expected, message):
        actual = Task(
            lambda _, resolve: resolve(1)
        ).map(fn)

        assert actual.fork(lambda _: None, lambda _: None) == expected, message

    assert_task_map(lambda _: None, 2, 'should return Task with resolved 2')
    assert_task_map(fn, 2, 'should return Task with resolved 2')
    assert_task_map(lambda _: Task.reject(2), 2, 'should return Task with rejected 2')


# Generated at 2022-06-14 04:02:57.006983
# Unit test for method map of class Task
def test_Task_map():
    def test_successful_mapping():
        t = Task.of(5)

        def mapper(x):
            return x + 2

        t2 = t.map(mapper)

        def cb(err, data):
            assert err is None
            assert data == 7

        t2.fork(lambda err: cb(err, None), lambda data: cb(None, data))

    def test_failed_mapping():
        t = Task.reject(5)

        def mapper(x):
            return x + 2

        t2 = t.map(mapper)

        def cb(err, data):
            assert data is None
            assert err == 5

        t2.fork(lambda err: cb(err, None), lambda data: cb(None, data))

    test_successful_mapping()

# Generated at 2022-06-14 04:03:08.613630
# Unit test for method map of class Task
def test_Task_map():
    def test(resolve, reject):
        return resolve(2)

    def task(resolve, reject):
        return Task.of(2)

    def expected(resolve, reject):
        return resolve(4)

    assert_that(Task(test).map(lambda i: i * 2).fork).is_a(Function)
    assert_that(Task(test).map(lambda i: i * 2).fork(None, None)).is_a(NoneType)

    assert_that(Task(test).map(lambda i: i * 2).fork(lambda _: None, None)).is_a(NoneType)
    assert_that(Task(test).map(lambda i: i * 2).fork(None, lambda _: None)).is_a(NoneType)


# Generated at 2022-06-14 04:03:17.571612
# Unit test for method map of class Task
def test_Task_map():
    def resolve(arg):
        return arg

    def reject(arg):
        return arg

    def plus_one(value):
        return value + 1

    task_of_1 = Task.of(1)
    assert task_of_1.fork(reject, resolve) == 1
    assert task_of_1.map(plus_one).fork(reject, resolve) == 2

    rejected_task = Task(lambda reject, _: reject(1))
    assert rejected_task.fork(reject, resolve) == 1
    assert rejected_task.map(plus_one).fork(reject, resolve) == 1


# Generated at 2022-06-14 04:03:30.549408
# Unit test for method bind of class Task
def test_Task_bind():
    # We use this function for generate Task with delay
    def process_result(value, reject, resolve):
        def process():
            if value == 0:
                return reject(value)
            else:
                return resolve(value)

        Timer(1, process).start()

    # Task with value
    task = Task(lambda reject, resolve: process_result(1, reject, resolve))
    task = task.map(lambda a: a + 1)
    task = task.bind(lambda a: Task(lambda reject, resolve: process_result(a + 1, reject, resolve)))
    task = task.bind(lambda a: Task(lambda reject, resolve: process_result(a + 1, reject, resolve)))

    # Call resolve function with result of Task
    task.fork(print, print)

    # Task with error

# Generated at 2022-06-14 04:03:42.095287
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(lambda x: x, lambda x: x) == 2
    assert Task.reject(1).bind(lambda x: Task.of(x + 1)).fork(lambda x: x, lambda x: x) == 1
    assert Task.of(1).bind(lambda x: Task.reject(x + 1)).fork(lambda x: x, lambda x: x) == 2
    assert Task.reject(1).bind(lambda x: Task.reject(x + 1)).fork(lambda x: x, lambda x: x) == 2
    assert Task.reject(1).bind(lambda x: Task.reject(x + 1)).fork(lambda x: x, lambda x: x) == 2

# Generated at 2022-06-14 04:03:52.075431
# Unit test for method map of class Task
def test_Task_map():
    import time
    from random import randint

    # Create function for generate task
    def generate_task(value):
        def fork(reject, resolve):
            time.sleep(randint(200, 1000) / 1000)
            resolve(value)

        return Task(fork)

    # Create sum function
    def sum(value):
        return lambda arg: value + arg

    # Create function for generating tasks in list
    def generate_tasks(number, value=0):
        return list(map(
            lambda arg: generate_task(arg),
            range(number)
        ))

    # Create promise
    def generate_promise(number):
        def promise(resolve, reject):
            def fork(reject, resolve):
                value = 0

                def reduce(task):
                    nonlocal value

# Generated at 2022-06-14 04:03:57.232828
# Unit test for method map of class Task
def test_Task_map():
    def add_const(x):
        return x + 1

    assert Task.of(1).map(add_const).fork(None, lambda x: x) == 2
    assert Task.of(1).map(lambda _: None).fork(None, lambda x: x) == None
    assert Task.reject(1).map(add_const).fork(lambda x: x, None) == 1
    assert Task.reject(1).map(lambda _: None).fork(lambda x: x, None) == 1


# Generated at 2022-06-14 04:04:03.963944
# Unit test for method map of class Task
def test_Task_map():
    def add_one(num):
        """
        Add one to num.

        :param num: number to add one
        :type num: Int
        :returns: number with one added
        :rtype: Int
        """
        return num + 1

    assert Task.of(1).map(add_one).fork(
        lambda reject: reject - 1,
        lambda resolve: resolve
    ) == 2

# Generated at 2022-06-14 04:04:11.089992
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    def fn(value):
        return value + 1

    def fork(reject, resolve):
        resolve(1)
        assert True

    mocked = Mock(side_effect=fork)
    task.fork = mocked

    result = task.map(fn)
    result.fork(None, None)
    mocked.assert_called_once()


# Generated at 2022-06-14 04:04:21.224433
# Unit test for method map of class Task
def test_Task_map():
    # TODO: complete this test
    assert Task(lambda _, resolve: resolve(1)) \
        .map(lambda value: value + 1) \
        .fork(lambda err: err, lambda value: value) == 2



# Generated at 2022-06-14 04:04:30.284481
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(2)

    def bind_fn(value):
        return Task(lambda reject, resolve: resolve(value + 1))

    task = Task(fork)
    new_task = task.bind(bind_fn)

    def fork_new_task(reject, resolve):
        assert reject(None) == None
        assert resolve(3) == None

    new_task.fork(lambda x: None, fork_new_task)

test_Task_bind()


# Generated at 2022-06-14 04:04:38.410148
# Unit test for method map of class Task
def test_Task_map():
    def result_of(task):
        return task.fork(
            lambda arg: "rejected: " + str(arg),
            lambda arg: "resolved: " + str(arg)
        )

    assert result_of(Task.of(10).map(inc)) == "resolved: 11"
    assert result_of(Task.reject(10).map(inc)) == "rejected: 10"
    assert result_of(Task.reject(10).map(inc).map(dec)) == "rejected: 10"


# Generated at 2022-06-14 04:04:41.570694
# Unit test for method bind of class Task
def test_Task_bind():
    # Case 1: reject was called with first argument
    def reject(value):
        assert value == 1

    # Case 2: resolve was called with first argument
    def resolve(value):
        assert value == 3

    # Case 3: fork was called with reject and resolve
    def fork(reject, resolve):
        return reject(1)

    # Case 4: call chain
    task = Task(fork) \
        .bind(lambda x: Task.of(x + 1)) \
        .bind(lambda x: Task.of(x + 1))

    task.fork(reject, resolve)



# Generated at 2022-06-14 04:04:51.930257
# Unit test for method bind of class Task
def test_Task_bind():
    def subtract_one(x):
        return Task.of(x - 1)

    def multiply(x, y):
        return Task.of(x * y)

    def divide(x, y):
        if y == 0:
            return Task.reject('division by zero')
        return Task.of(x / y)

    def divide_and_subtract(x, y, z):
        return divide(x, y).bind(lambda a: multiply(a, z)).bind(subtract_one)

    def run(fork, reject, resolve):
        return fork(reject, resolve)

    def test_failure():
        task = divide_and_subtract(10, 0, 10)
        actual = run(task.fork, lambda x: x, lambda x: None)

# Generated at 2022-06-14 04:04:59.522857
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        reject('error')

    t = Task(fork)
    task = t.map(lambda x: x * x)

    assert task.fork(lambda x: x + 1, lambda x: x - 1) == 'error1'

    def fork(reject, resolve):
        resolve(3)

    t = Task(fork)
    task = t.map(lambda x: x * x)

    assert task.fork(lambda x: x + 1, lambda x: x - 1) == 8



# Generated at 2022-06-14 04:05:06.640526
# Unit test for method map of class Task
def test_Task_map():
    fn, task, value = [], [], []

    def test_one(reject, resolve):
        reject(fn[0])
        resolve(task[0])
        return value[0]

    def test_two(reject, resolve):
        reject(fn[1])
        resolve(task[1])
        return value[1]

    def test_one_map(x):
        value[0] = x
        return x + 1

    def test_two_map(x):
        value[1] = x
        return x + 1

    task = Task(test_one)
    task2 = Task(test_two)
    task.map(test_one_map).fork(
        lambda x: fn[0] == x,
        lambda x: task[0] == x
    )
    task2.map

# Generated at 2022-06-14 04:05:09.163137
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1).bind(
        lambda n: Task.of(n + 1).bind(
            lambda n: Task.of(n + 2)
        )
    )

    assert task.fork(lambda _: _, lambda _: _) == 4
    assert Task.reject(2).fork(lambda _: _, lambda _: _) == 2


if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:05:13.714987
# Unit test for method map of class Task
def test_Task_map():
    def task_2_map(resolve, _):
        resolve(2)

    task = Task(task_2_map)
    task_double = task.map(lambda x: 2 * x)

    def double_task(_, resolve):
        resolve(4)

    assert task_double.fork == double_task


# Generated at 2022-06-14 04:05:25.942546
# Unit test for method bind of class Task
def test_Task_bind():
    method_config = [
        {
            "name": "map",
            "args": [lambda x: x + 1],
            "result": Task(lambda reject, resolve: resolve(6))
        },
        {
            "name": "map",
            "args": [lambda x: Task.of(x + 1)],
            "result": Task(lambda reject, resolve: resolve(6))
        }
    ]
    config = {
        "class": Task,
        "method_configs": method_config,
        "init_args": [Task(lambda reject, resolve: resolve(5))]
    }

    for test in test_task_method(config):
        yield test


# Generated at 2022-06-14 04:05:38.852139
# Unit test for method map of class Task
def test_Task_map():
    value = 123

    def fn(v):
        return v + 111

    res = Task.of(value).map(fn).fork(None, lambda x: x)

    assert res == fn(value)



# Generated at 2022-06-14 04:05:45.391265
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        if value > 5:
            return Task.reject('Error')
        return Task.of(value+1)

    task = Task.of(4)
    assert task.bind(mapper).fork(lambda v: v, lambda v: v) == 5
    assert Task.of(8).bind(mapper).fork(lambda v: v, lambda v: v) == 'Error'


# Generated at 2022-06-14 04:05:56.735610
# Unit test for method map of class Task
def test_Task_map():
    """
    Check that method map of class Task is work or not.

    :returns: nothing
    :rtype: None
    """
    valid_task = Task.of({
        'type': 'valid',
        'value': 5
    })
    invalid_task = Task.of({
        'type': 'invalid',
        'value': 10
    })
    mapped_valid_task = valid_task.map(lambda value: value['value'])
    mapped_invalid_task = invalid_task.map(lambda value: value['value'])
    # check result of valid task
    assert(mapped_valid_task.fork(lambda reject: 'error', lambda resolve: resolve) == 5)
    # check result of invalid task

# Generated at 2022-06-14 04:06:02.029660
# Unit test for method map of class Task
def test_Task_map():
    def inc(number):
        return number + 1
    t = Task.of(5)
    mapped_t = t.map(inc)

    assert mapped_t.fork(lambda a: 'reject', lambda a: 'resolve') == 'resolve'


# Generated at 2022-06-14 04:06:12.029538
# Unit test for method map of class Task
def test_Task_map():
    def _map(arg):
        return arg*2

    def _reject(_):
        raise Exception('Task rejected')

    def _resolve(arg):
        return arg

    # Run test
    assert Task(lambda reject, resolve: resolve(2)).map(_map).fork(_reject, _resolve) == 4
    assert Task(lambda reject, resolve: resolve(5)).map(_map).fork(_reject, _resolve) == 10
    assert Task.of(5).map(_map).fork(_reject, _resolve) == 10
    assert Task.reject(5).map(_map).fork(_reject, _resolve) == 5



# Generated at 2022-06-14 04:06:16.327180
# Unit test for method map of class Task
def test_Task_map():
    result = Task.of(1) \
        .map(lambda arg: arg + 1) \
        .map(lambda arg: arg * 2) \
        .map(lambda arg: arg - 1) \
        .fork(
            lambda arg: print("Rejected"),
            lambda arg: print("Resolved: " + str(arg))
        )


# Generated at 2022-06-14 04:06:26.981029
# Unit test for method bind of class Task
def test_Task_bind():
    def plus5(value):
        try:
            return Task.of(value + 5)
        except:
            return Task.reject('plus5 error')

    def times2(value):
        try:
            return Task.of(value * 2)
        except:
            return Task.reject('times2 error')

    add5_times2 = lambda value: Task.of(value).bind(plus5).bind(times2)

    result1 = add5_times2(2).fork(lambda e: e, lambda v: v) # = 14
    result2 = add5_times2('str').fork(lambda e: e, lambda v: v) # = times2 error

    assert result1 == 14, 'result1 is not equal 14'

# Generated at 2022-06-14 04:06:33.052878
# Unit test for method map of class Task
def test_Task_map():
    """
    Resolve Task with sum of stored value and argument value.
    """
    def add(x):
        return x + 1

    task = Task.of(2)
    task = task.map(add)
    def fork(reject, resolve):
        return resolve(add(2))
    assert task.fork == fork


# Generated at 2022-06-14 04:06:43.581995
# Unit test for method map of class Task
def test_Task_map():
    """
    Map method must return new Task, that resolve attribute call function with the same
    argument, but argument is the result of function from argument of map.
    """
    # Test to resolve state
    def test_add1_to_value_in_resolve():
        """
        Test that resolve attribute of returned Task will call
        lambda x: x + 1 with value 10
        """
        # Create Task with resolve attribute that return x + 1
        task = Task(lambda _, resolve: resolve(10)).map(lambda x: x + 1)

        # For hack result in test (we can't know what function will call resolve attribute)
        # we need to fake it
        # Here we will replace resolve function by our function
        # that check that argument of resolve is 11
        resolved_value = None

# Generated at 2022-06-14 04:06:46.895379
# Unit test for method bind of class Task
def test_Task_bind():
    a = Task.of(1)
    b = a.bind(lambda x: Task.of(x + 1))
    c = b.fork(
        lambda x: x,
        lambda x: x
    )
    assert c == 2


# Generated at 2022-06-14 04:07:20.845005
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve():
        pass

    def reject():
        pass

    errors = []
    task = Task(lambda reject, resolve: resolve(42))
    after_bind_task = task.bind(lambda x: Task(lambda reject, resolve: resolve('42')))

    def on_success():
        try:
            assert task.fork(reject, resolve) == 42
            assert after_bind_task.fork(reject, resolve) == '42'
        except Exception as e:
            errors.append(repr(e))

    def on_error():
        try:
            assert task.fork(reject, resolve) == 42
        except Exception as e:
            errors.append(repr(e))

    after_bind_task.fork(on_error, on_success)

# Generated at 2022-06-14 04:07:30.972550
# Unit test for method map of class Task
def test_Task_map():
    def foo(fn):
        squared = fn(2)
        assert 21 == squared

    def bar(fn):
        squared = fn(3)
        assert 9 == squared

    def baz(fn):
        squared = fn(5)
        assert 25 == squared

    three = Task.of(3)
    five = Task.of(5)
    seven = Task.of(7)

    # example 1
    comp1 = three.map(lambda x: x*x)
    comp1.fork(lambda _: None, foo)

    # example 2
    comp2 = five.map(lambda x: x*x)
    comp2.fork(lambda _: None, bar)

    # example 3
    comp3 = seven.map(lambda x: x*x)
    comp3.fork(lambda _: None, baz)

# Generated at 2022-06-14 04:07:34.249799
# Unit test for method map of class Task
def test_Task_map():
    def stub(a):
        return a + 1

    for i in range(100):
        assert Task(None).map(stub)(i) == stub(i)


# Generated at 2022-06-14 04:07:39.604594
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        resolve(1)

    task = Task(fork)
    mapper = lambda v: v + 1
    mapped_task = task.map(mapper)

# Generated at 2022-06-14 04:07:48.416929
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(False)

    def fork_reject(reject, resolve):
        return reject("error")

    def map1(value):
        return value

    def map2(value):
        return Task.of(value)

    def map_reject(value):
        return Task.reject("mapped error")

    assert Task(fork).map(map1).fork(lambda y: y, lambda y: False) is False
    assert Task(fork_reject).map(map1).fork(lambda y: True, lambda y: False) is True
    assert Task(fork).bind(map2).fork(lambda y: y, lambda y: False) is False
    assert Task(fork).bind(map_reject).fork(lambda y: True, lambda y: False) is True