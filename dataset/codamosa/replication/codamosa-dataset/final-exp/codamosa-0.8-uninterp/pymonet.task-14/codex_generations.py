

# Generated at 2022-06-14 03:57:58.873486
# Unit test for method bind of class Task
def test_Task_bind():
    add_one = lambda x: x + 1
    task_add_one = Task.of(add_one)

    assert task_add_one == Task(lambda _, resolve: resolve(add_one))
    assert task_add_one.fork(lambda x: x, lambda x: x(2)) == 3

    task_of_task = task_add_one.bind(Task.of)
    assert task_of_task == Task(lambda _, resolve: resolve(add_one))

    task_of_reject = task_add_one.bind(Task.reject)
    assert task_of_reject == Task(lambda reject, _: reject(add_one))

    task_bind = task_add_one.bind(lambda value: Task(lambda _, resolve: resolve(value(2))))
    assert task_bind == Task

# Generated at 2022-06-14 03:58:04.106994
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for validate work of method `Task.map`
    """
    double = lambda x: x * 2
    task_execute_double = Task.of(5).map(double)

# Generated at 2022-06-14 03:58:11.975418
# Unit test for method map of class Task
def test_Task_map():
    def add(x):
        return x + 1

    def add_char(x):
        return str(x) + 'x'

    @async_test
    def success():
        Task.of(1).map(add).fork(on_error, assert_equal(2))

    @async_test
    def success_chained():
        Task.of(1).map(add).map(add).map(add).fork(on_error, assert_equal(4))

    @async_test
    def success_chained_with_chars():
        Task.of(1).map(add).map(add_char).map(add).map(add_char).fork(on_error, assert_equal('2x'))

    @async_test
    def success_with_rejected_status():
        Task

# Generated at 2022-06-14 03:58:19.545338
# Unit test for method map of class Task
def test_Task_map():
    # create Task instance
    task = Task(lambda reject, resolve: resolve(1))
    # call task fork with mapper function
    result = task.map(lambda value: value * 2).fork(
        lambda arg: arg,
        lambda arg: arg
    )

    assert result == 2


# Generated at 2022-06-14 03:58:22.635536
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method.
    """
    assert Task.of(10).bind(lambda arg: Task.of(arg + 5)).fork(None, lambda arg: arg) == 15


# Generated at 2022-06-14 03:58:35.815839
# Unit test for method map of class Task
def test_Task_map():
    def assert_equals(value):
        def result(x):
            assert x == value

        return result

    def test_resolve():
        return Task(lambda _, resolve: resolve("a"))

    def test_rejected():
        return Task(lambda reject, _: reject("a"))

    test_resolve()\
        .map(lambda x: x + "b")\
        .fork(assert_equals("ab"),
              assert_equals("a"))

    test_rejected()\
        .map(lambda x: x + "b")\
        .fork(assert_equals("a"),
              assert_equals("ab"))


# Generated at 2022-06-14 03:58:39.485886
# Unit test for method map of class Task
def test_Task_map():
    un = Task.of(1)
    un = un.map(lambda a: a + 1)
    un = un.map(lambda a: a * 2)

    assert un.fork(
        lambda a: a,
        lambda a: a
    ) == 4
# test_Task_map()


# Generated at 2022-06-14 03:58:47.235300
# Unit test for method bind of class Task
def test_Task_bind():
    """
    This test assert that order of calling methods map and bind is not important.
    Both cases must return equal value.
    """
    first_task = Task.of(5).bind(lambda x: Task.of(x + 5)).map(lambda x: x * 2)
    second_task = Task.of(5).map(lambda x: x + 5).bind(lambda x: Task.of(x * 2))

    first_value = first_task.fork(
        lambda arg: arg,
        lambda arg: arg
    )

    second_value = second_task.fork(
        lambda arg: arg,
        lambda arg: arg
    )

    assert first_value == second_value == 20


# Definition of Monad instance for Task class

# Generated at 2022-06-14 03:58:59.439187
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method with following functions:
        1. map(lambda x: x + 1)
        2. map(lambda x: x + 2)
    Test that value of result is (result of 1) + (result of 2) = 5
    """
    def result_for_map(resolve, reject):
        resolve(2)

    def task_map1(arg):
        return arg + 1

    def task_map2(arg):
        return arg + 2

    task_map1_result = Task(result_for_map).map(task_map1)
    task_map2_result = Task(result_for_map).map(task_map2)
    task_map1_value = task_map1_result.fork(lambda arg: arg, lambda arg: arg)
    task_map2_value = task

# Generated at 2022-06-14 03:59:05.084566
# Unit test for method bind of class Task
def test_Task_bind():
    def generate_task(value):
        return Task.of(value).map(lambda x: x + 1)

    def fork_task(resolve, reject):
        generate_task(100).fork(reject, resolve)

    assert Task(fork_task).bind(lambda v: v).fork(lambda x: x, lambda x: x) == 101



# Generated at 2022-06-14 03:59:14.370219
# Unit test for method bind of class Task
def test_Task_bind():
    assert_equal(
        Task.of(1).bind(lambda value: Task.of(value+1)).fork(
            lambda reject: reject,
            lambda resolve: resolve,
        ),
        2,
    )

    assert_equal(
        Task.reject(1).bind(lambda value: Task.of(value+1)).fork(
            lambda reject: reject,
            lambda resolve: resolve,
        ),
        1,
    )


# Generated at 2022-06-14 03:59:17.929970
# Unit test for method map of class Task
def test_Task_map():
    def dummy(resolve, reject):
        return None

    task = Task(dummy)
    result = task.map(lambda arg: arg + 1)
    assert type(result) is Task

# Generated at 2022-06-14 03:59:24.691560
# Unit test for method map of class Task
def test_Task_map():
    """
    Test method map of class Task.
    """
    def inc(value):
        """
        Take number and incriment it.

        :param value: number
        :type value: Number
        :returns: number + 1
        :rtype: Number
        """
        return value + 1


# Generated at 2022-06-14 03:59:30.710111
# Unit test for method bind of class Task
def test_Task_bind():
    # test for resolved Task
    result = Task.of(42).bind(
        lambda value: Task.of(value * value)
    ).fork(
        lambda err: None,
        lambda value: value
    )

    assert result == 1764

    # test for rejected Task
    result = Task.reject(42).bind(
        lambda value: Task.of(value * value)
    ).fork(
        lambda err: err,
        lambda value: None
    )

    assert result == 42


# Generated at 2022-06-14 03:59:35.877612
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)

    task.fork(
        lambda v: "fail",
        lambda v: v == 1 or "fail"
    )

    task.map(lambda v: v + 1).fork(
        lambda v: "fail",
        lambda v: v == 2 or "fail"
    )

test_Task_map()


# Generated at 2022-06-14 03:59:41.023180
# Unit test for method map of class Task
def test_Task_map():
    for number in range(100):
        value = random.randint(0, 100)

# Generated at 2022-06-14 03:59:51.566948
# Unit test for method map of class Task
def test_Task_map():
    """
    Take Tasks with some values and mapper function,
    assert that fork function of task return correct results.
    """
    print('test: Task -> map')

    def resolve(value):
        """
        :param value: value that have to be stored in Task
        :type value: Any
        :returns: new Task with stored value
        :rtype: Task
        """
        return Task(lambda _, resolve: resolve(value))

    task1 = Task.of(1).map(lambda value: value + 1)
    assert task1.fork(None, lambda value: value) == 2

    task2 = Task.of((lambda value: value + 1))
    assert task2.map(lambda fn: fn(1)).fork(None, lambda value: value) == 2


# Generated at 2022-06-14 04:00:02.204183
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind method of Task class.
    """
    # Success case.
    mapper = lambda value: Task.of(value + 1)
    result = Task.of(1).bind(mapper)
    assert result.fork(lambda _: 0, lambda _: 1) == 2, 'Error: bind return incorrect result.'

    # Failure case.
    mapper = lambda value: Task.reject(value + 1)
    result = Task.of(1).bind(mapper)
    assert result.fork(lambda _: 0, lambda _: 1) == 0, 'Error: bind return incorrect result.'


# Generated at 2022-06-14 04:00:10.365351
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:00:14.489318
# Unit test for method bind of class Task
def test_Task_bind():
    gen_number = Task(lambda _, resolve: resolve(5))
    # test bind
    assert_equal(gen_number.bind(lambda num: Task.of(num * 7)).fork(lambda _: (), lambda result: result), 35)


# Generated at 2022-06-14 04:00:26.676381
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task(lambda on_reject, on_resolve: on_resolve({'a': 1, 'b': {'c': 3}}))
    def mapper(values):
        return Task.of({'c': values['b']['c'], 'a': values['a']})
    task = task.bind(mapper)

    def on_reject(value):
        return {'fail': value}

    def on_resolve(value):
        return {'success': value}

    assert task.fork(on_reject, on_resolve) == {'success': {'c': 3, 'a': 1}}


# Generated at 2022-06-14 04:00:30.447541
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value * 2)

    task = Task.of(2)
    result = task.bind(fn).fork(None, None)
    assert result == 4

# Generated at 2022-06-14 04:00:39.158570
# Unit test for method bind of class Task
def test_Task_bind():
    # Task with value and function
    task = Task.of(1)
    def add10(x):
        """
        Function to add 10 to x.

        :param x: value to add 10
        :type x: int
        :returns: x + 10
        :rtype: int
        """
        return x + 10

    # Test bind with correct result
    assert [True, True] == [
        task.bind(add10) == Task.of(11),
        task.bind(lambda x: Task.reject(x)) == Task.reject(1)
    ]


# Generated at 2022-06-14 04:00:51.219713
# Unit test for method bind of class Task
def test_Task_bind():
    def task_of(value):
        return Task.of(value)

    def task_reject(value):
        return Task.reject(value)

    def mapper(value):
        return value + 1

    def reject_to_string(value):
        return str(value)

    def resolve_to_string(value):
        return str(value)

    test_value = 42

    # Test correct mapping
    test_case = task_of(test_value)
    result_case = test_case.bind(
        lambda _: task_of(mapper(test_value))
    ).fork(reject_to_string, resolve_to_string)

    assert (result_case == '43')

    # Test rejected mapping
    test_case = task_of(test_value)
    result_case = test_

# Generated at 2022-06-14 04:00:56.093448
# Unit test for method map of class Task
def test_Task_map():
    def _(a, b):
        assert a == 1
        assert b == 2
        return a + b

    assert Task.of(1).map(_).fork(None, lambda value: value) == 3


# Generated at 2022-06-14 04:01:06.747602
# Unit test for method bind of class Task
def test_Task_bind():
    from unittest import TestCase

    class Test(TestCase):
        def test_bind(self):
            task = Task.of(2)

# Generated at 2022-06-14 04:01:13.561850
# Unit test for method bind of class Task
def test_Task_bind():
    def test(value, callback):
        def fork(reject, resolve):
            callback(value)

            def _reject(arg):
                callback(arg)
                return reject(arg)

            def _resolve(arg):
                callback(arg)
                return resolve(arg)

            return Task(fork).bind(lambda arg: Task(_reject, _resolve)).fork(reject, resolve)

        return Task(fork)

    def callback(value):
        print(value)
        return value

    test(1, callback)
    test('reject', callback)

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:01:23.723699
# Unit test for method bind of class Task
def test_Task_bind():
    def get_task():
        return Task(
            lambda reject, resolve: resolve(1)
        )

    def get_task_that_call_reject_of_another_task():
        return Task(
            lambda reject, resolve: get_task().bind(
                lambda arg: Task.reject(arg)
            ).fork(lambda arg: resolve(arg), lambda arg: reject(arg))
        )

    def get_task_which_returning_resolved_task():
        return Task(
            lambda reject, resolve: get_task().bind(
                lambda arg: Task.of(arg)
            ).fork(lambda arg: resolve(arg), lambda arg: reject(arg))
        )


# Generated at 2022-06-14 04:01:32.559110
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for class Task.map method
    """
    inc_task = Task.of(1).map(lambda a: a + 1)
    assert inc_task.fork(None, lambda args: args) == 2

    add_task = Task.of(1).map(lambda a: Task.of(2)).bind(lambda a: Task.of(3 + a))
    assert add_task.fork(None, lambda args: args) == 5

    assert Task.of(2).map(lambda a: a + 1).map(lambda a: a * 2).fork(None, lambda args: args) == 6
    assert Task.reject(1).map(lambda a: a + 1).fork(lambda args: args, None) == 1

# Generated at 2022-06-14 04:01:35.104402
# Unit test for method map of class Task
def test_Task_map():
    def fn(arg):
        return arg + '!'

    assert Task.of(4).map(fn) == '4!'
    assert Task.of('Hello Word').map(fn) == 'Hello Word!'


# Generated at 2022-06-14 04:01:52.925423
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(arg):
        return Task.of(arg)

    def fork(reject, resolve):
        return 2 + 2

    obj = Task(fork)
    res = obj.bind(fn)

    def test_reject(arg):
        assert arg == 2
        return 2

    def test_resolve(arg):
        assert arg == 2
        return 2

    assert res.fork(test_reject, test_resolve) == 2



# Generated at 2022-06-14 04:01:58.344569
# Unit test for method map of class Task
def test_Task_map():
    def input_sync():
        return 1

    def result_sync(value):
        return value + 1

    input_async = Task.of(1)
    result = input_async.map(result_sync)

    assert result.fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 04:02:02.787286
# Unit test for method map of class Task
def test_Task_map():
    def test_function(x):
        return x**2

    task = Task(
        lambda reject, resolve: resolve(2)
    )

    task_mapped = task.map(test_function)
    assert task_mapped.fork(lambda res: res, lambda _: None) == 4


# Generated at 2022-06-14 04:02:14.434150
# Unit test for method bind of class Task
def test_Task_bind():
    def mul_3(value):
        return value * 3

    def is_number(value):
        return isinstance(value, numbers.Number)
    assert Task.of(5).bind(mul_3).fork(
        lambda value: "Reject",
        lambda value: "Resolve: {}".format(value)
    ) == "Resolve: 15"
    assert Task.of(5).bind(lambda value: Task.reject(value)).fork(
        lambda value: "Reject: {}".format(value),
        lambda value: "Resolve"
    ) == "Reject: 5"

# Generated at 2022-06-14 04:02:19.295453
# Unit test for method map of class Task
def test_Task_map():
    def test(a, b):
        expect(Task.of(a).map(lambda x: x + b).fork(None, lambda x: x)).to(equal(a + b))

    test(1, 1)
    test(123, 321)


# Generated at 2022-06-14 04:02:27.410934
# Unit test for method bind of class Task
def test_Task_bind():
    def a(value):
        return Task.of(value + 1)

    def b(value):
        return Task.reject(value + 1)

    task1 = Task.of(1)
    task2 = Task.of(1)
    task3 = Task.reject(1)
    task4 = Task.reject(1)

    task1 = task1.bind(a)
    task2 = task2.bind(b)
    task3 = task3.bind(a)
    task4 = task4.bind(b)

    assert task1._fork is not None
    assert task2._fork is not None
    assert task3._fork is not None
    assert task4._fork is not None


# Generated at 2022-06-14 04:02:33.880780
# Unit test for method map of class Task
def test_Task_map():
    """
    Test case for Task.map method
    """
    def fork(reject, resolve):
        resolve(3)

    def mapper(value):
        return value * value

    task = Task(fork)

    def fork_test(reject, resolve):
        resolve(9)

    actual = task.map(mapper)
    expected = Task(fork_test)

    assert actual.fork == expected.fork


# Generated at 2022-06-14 04:02:40.414114
# Unit test for method map of class Task
def test_Task_map():
    """
    Run unit test for method map of class Task.
    :returns: None
    :rtype: None
    """
    def fork(reject, resolve):
        return reject('test')

    fn = lambda arg: arg + '_resolved'
    task = Task(fork)

    assert task.map(fn).fork(
        lambda value: '%s_error' % value,
        lambda value: '%s_resolve' % value
    ) == 'test_error'


# Generated at 2022-06-14 04:02:50.281525
# Unit test for method map of class Task
def test_Task_map():
    """
    Test class Task method map, that given Task return new Task and call fork with result of mapper.

    :returns: (passed, failed)
    :rtype: tuple[int, int]
    """
    passed = 0
    failed = 0

    results = []

    # Use mapper function and compare result with expected
    def mapper(value):
        results.append(value)
        return value + 1

    value = 1
    task = Task.of(value)

    task.map(mapper).fork(
        lambda arg: arg,
        lambda arg: arg
    )

    result = results[0]

    # test
    if result == value:
        passed += 1
    else:
        failed += 1
        print('Test Task.map() FAILED')

# Generated at 2022-06-14 04:02:55.701558
# Unit test for method map of class Task
def test_Task_map():
    task = Task.reject("value")

    def fn(value):
        assert value == "value"
        return "mapped_value"

    def reject(reason):
        assert reason == "value"

    def resolve(value):
        assert value == "mapped_value"

    task.map(fn).fork(reject, resolve)


# Generated at 2022-06-14 04:03:22.937666
# Unit test for method bind of class Task
def test_Task_bind():
    """
    This test ensure that Task.bind function store function argument and return Task
    that has a fucntion that call Task.fork function of stored function.
    And this Task.fork call Task.fork of Task result of called of stored function with arguments.
    """
    val = 'test'

    def sync_task(arg):
        assert arg == val
        return Task.of('sync')

    def async_task(arg):
        assert arg == val
        return Task.of('async')

    task = Task.of(val)
    result = task.bind(sync_task)

    assert isinstance(result, Task)
    assert result.fork(lambda reject, resolve: resolve('sync')) == 'sync'

    result = task.bind(async_task)

    assert isinstance(result, Task)

# Generated at 2022-06-14 04:03:27.955882
# Unit test for method map of class Task
def test_Task_map():
    def increment(arg):
        return arg + 1

    def test(resolve, reject):
        return resolve(1)

    task = Task(test)
    result = task.map(increment)
    assert result.fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 04:03:30.810595
# Unit test for method map of class Task
def test_Task_map():
    f = lambda x: x + 10
    assert Task.of(1).map(f).fork(raise_, identity) == 11
    assert Task.reject(1).map(f).fork(identity, raise_) == 1


# Generated at 2022-06-14 04:03:36.926370
# Unit test for method bind of class Task
def test_Task_bind():
    def sync_map_fn(value):
        return value

    def sync_bind_fn(value):
        return Task.of(value)

    assert Task.of(1).bind(sync_map_fn) == Task.of(1).map(sync_map_fn)
    assert Task.of(1).bind(sync_bind_fn) == Task.of(1)


# Generated at 2022-06-14 04:03:40.393487
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    assert task.map(lambda a: a * 5).fork(
        lambda err: False,
        lambda err: err == 1 * 5
    )


# Generated at 2022-06-14 04:03:47.909276
# Unit test for method map of class Task
def test_Task_map():
    """
    Check result of map
    """
    def test():
        """
        Check map function
        """
        def mapper(value):
            """
            Mapper function
            """
            return value + 5

        def resolver(value):
            """
            Resolver function
            """
            return value

        def rejecter(value):
            """
            Rejecter function
            """
            return value

        task = Task.of(5)
        return task.map(mapper).fork(rejecter, resolver)

    assert test() == 10


# Generated at 2022-06-14 04:03:53.151222
# Unit test for method bind of class Task
def test_Task_bind():
    # Setup
    value = "value"

    def mapper(value):
        return Task.of(value)

    # Call
    result = Task.of(value).bind(mapper)

    # Assertion
    assert result.fork(lambda _: None, lambda v: v) == value


# Generated at 2022-06-14 04:04:04.538313
# Unit test for method map of class Task
def test_Task_map():
    # Define test variables and functions
    def identity(x): return x
    def plus_one(x): return x+1
    def plus(x, y): return x+y
    def equal(x, y): return x == y

    # Check map of Task.of(1)
    assert equal(Task.of(1).map(identity).fork(lambda x: x, lambda x: x), 1)
    assert equal(Task.of(1).map(plus_one).fork(lambda x: x, lambda x: x), 2)

    # Check map of Task.of(1).map(plus_one)
    assert equal(Task.of(1).map(plus_one).map(identity).fork(lambda x: x, lambda x: x), 2)

# Generated at 2022-06-14 04:04:07.925895
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda _, resolve: resolve(1)).map(lambda arg: arg).fork(
        lambda r: None,
        lambda r: r
    ) == 1


# Generated at 2022-06-14 04:04:17.384395
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda x: Task.of(x + 1)) == Task.of(2)

    assert Task.of(1).bind(lambda x: Task.reject(x + 1)) == Task.reject(2)

    assert Task.reject(1).bind(lambda x: Task.of(x + 1)) == Task.reject(1)

    assert Task.reject(1).bind(lambda x: Task.reject(x + 1)) == Task.reject(1)


# Generated at 2022-06-14 04:05:05.399353
# Unit test for method map of class Task
def test_Task_map():
    def assert_map(value, task_fn, mapped_value):
        task = Task.of(value).map(task_fn)
        assert task.fork(None, lambda arg: arg) == mapped_value

    assert_map(1, lambda x: x + 1, 2)
    assert_map('1', lambda x: int(x), 1)
    assert_map(2, lambda x: x, 2)



# Generated at 2022-06-14 04:05:12.094880
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task.
    :return: no return
    """
    def cb(result):
        """
        Callback function for fork of Task
        :param result: result of fork function
        :return: no return
        """
        assert result == 2

    Task.of(1).map(lambda value: value + 1).fork(lambda err: 1/0, cb)
    print("Test Task.map: Success")


# Generated at 2022-06-14 04:05:26.012333
# Unit test for method map of class Task
def test_Task_map():
    def test(arg1, arg2, arg3):
        value = 0
        value += arg1
        value += arg2
        value += arg3
        return value

    params = [
        Task.of(1),
        Task.reject(2),
        Task.of(3)
    ]

    Task.of(1) \
        .map(lambda arg: arg + 2) \
        .bind(lambda arg: Task.of(arg + 1)) \
        .map(lambda arg: arg + 1) \
        .fork(
            lambda arg: print('error', arg),
            lambda arg: print('result', arg)
        )


# Generated at 2022-06-14 04:05:34.602261
# Unit test for method bind of class Task
def test_Task_bind():
    def test_on_resolve(x):
        return Task.of(x)

    def test_on_reject(x):
        return Task.of(x + 1)

    # Test resolve case
    result_task = Task.of(2).bind(test_on_resolve)
    assert result_task.fork(test_on_reject, test_on_resolve) == Task.of(2)

    # Test reject case
    result_task = Task.reject(2).bind(test_on_reject)
    assert result_task.fork(test_on_reject, test_on_resolve) == Task.of(3)


# Generated at 2022-06-14 04:05:39.790877
# Unit test for method map of class Task
def test_Task_map():
    """
    It should return new Task with mapped resolve method.
    """
    task_of_value = Task.of(1)
    assert task_of_value.fork(lambda _: "bad", lambda v: "good") == "good"

    add1 = lambda x: x + 1
    task_map = task_of_value.map(add1)
    assert task_map.fork(lambda _: "bad", lambda v: "good") == "good"



# Generated at 2022-06-14 04:05:43.452820
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    _ = Task.of(1)
    assert _.map(lambda x: x + 1).fork(lambda _: False, lambda _: True)
    assert _.bind(lambda x: Task.of(x + 1)).fork(lambda _: False, lambda _: True)
    assert not _.bind(lambda _: Task.reject(1)).fork(lambda _: True, lambda _: False)



# Generated at 2022-06-14 04:05:51.842452
# Unit test for method bind of class Task
def test_Task_bind():
    # write unit test here
    def raising_reject(value):
        raise value

    def raising_resolve(value):
        raise value

    test_task_1 = Task.of(42)
    assert test_task_1.bind(lambda value: Task.of(value + 1)).fork(raising_reject, lambda value: value) == 43
    assert test_task_1.bind(lambda value: Task.reject(value + 1)).fork(lambda value: value, raising_resolve) == 43


# Generated at 2022-06-14 04:05:57.291998
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    def test_Task_map_concat_str_with_one(value):
        assert value == 'one'

    task_one_resolve = Task.of(1)
    task_one_map = task_one_resolve.map(add_one)
    task_one_map.fork(lambda _: 'one', test_Task_map_concat_str_with_one)


# Generated at 2022-06-14 04:06:01.188322
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1).map(lambda x: x + 1)
    assert task.fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 04:06:05.036998
# Unit test for method bind of class Task
def test_Task_bind():
    def t(reject, resolve):
        return resolve(2)

    def m(value):
        return Task(t)

    assert Task(t).bind(m) == Task(t)


# Generated at 2022-06-14 04:07:46.644775
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map
    """
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    a = random.randint(0, 10)
    b = random.randint(0, 10)

    task = Task.of((a, b))

# Generated at 2022-06-14 04:07:51.466537
# Unit test for method map of class Task
def test_Task_map():
    """
    Test function for Task.map() method.
    """
    def add_one(num):
        return num + 1

    task = Task(lambda _, resolve: resolve(1))
    assert task.map(add_one).fork(lambda _: None, lambda value: value) == 2


# Generated at 2022-06-14 04:07:59.156907
# Unit test for method map of class Task
def test_Task_map():
    def add(number):
        return number + 1

    def error(number):
        return number // 0

    value = Task.of(1)
    result = value.map(add)
    assert result.fork(lambda arg: arg, lambda arg: arg) == 2

    error_value = Task.of(1)
    error_result = error_value.map(error)

    try:
        error_result.fork(lambda arg: arg, lambda arg: arg)
        assert False
    except Exception:
        assert True
