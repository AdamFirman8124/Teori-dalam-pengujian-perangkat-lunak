

# Generated at 2022-06-14 03:58:05.011989
# Unit test for method bind of class Task
def test_Task_bind():
    @Task.of
    def A(reject, resolve):
        return 'A'

    @Task.of
    def B(reject, resolve):
        return 'B'

    def C(reject, resolve):
        return 'C'

    def test_fail(reject, resolve):
        reject('fail')

    assert A().bind(lambda value: B()).map(lambda value: value) == 'B'
    assert A().bind(lambda value: B()).bind(lambda value: C()).fork(
        lambda value: 'rejected',
        lambda value: value
    ) == 'C'
    assert A().bind(lambda value: B()).bind(lambda value: test_fail()).fork(
        lambda value: 'rejected',
        lambda value: value
    ) == 'rejected'

# Unit test

# Generated at 2022-06-14 03:58:15.247334
# Unit test for method bind of class Task
def test_Task_bind():
    assert_equals = partial(assert_equal,
        expected_value = "world",
        expected_type = str
    )

    def task(resolve, reject):
        resolve("world")

    def task_error(resolve, reject):
        raise Exception("Error")

    def task_refactor(arg):
        return Task(task)

    def task_refactor_error(arg):
        return Task(task_error)

    assert_equals(Task(task).bind(task_refactor).fork(None, assert_equals))

    assert_raises(
        Exception,
        Task(task).bind(task_refactor_error).fork,
        None,
        assert_equals
    )

# Generated at 2022-06-14 03:58:18.594164
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value + 1)

    assert Task.of(0).bind(fn).fork(lambda _: False, lambda x: x == 1) == True

# Generated at 2022-06-14 03:58:29.201463
# Unit test for method map of class Task
def test_Task_map():
    """
    Unit test of function map in class task
    """

    def double(number):
        return number * 2

    def fail(reject, resolve):
        resolve(10)

    task = Task(fail)
    assert task.map(double).fork(
        lambda arg: arg + 1,
        lambda arg: arg * 2
    ) == 20

    def fail_with_error(reject, resolve):
        reject(10)

    task = Task(fail_with_error)
    assert task.map(double).fork(
        lambda arg: arg + 1,
        lambda arg: arg * 2
    ) == 11

    def success(reject, resolve):
        resolve(1)

    task = Task(lambda _, resolve: resolve(1))

# Generated at 2022-06-14 03:58:37.786520
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task class.
    """
    def some_fn(value):
        return value + 1

    resolve_executed = None
    reject_executed = None
    def resolve(value):
        nonlocal resolve_executed
        resolve_executed = value

    def reject(value):
        nonlocal reject_executed
        reject_executed = value

    task = Task.of(1)
    mapped_task = task.map(some_fn)
    mapped_task.fork(reject, resolve)

    assert resolve_executed == 2
    assert reject_executed is None


# Generated at 2022-06-14 03:58:40.884543
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test of Task#bind method
    """
    assert Task(lambda reject, resolve: resolve(1)) \
        .bind(lambda x: Task(lambda reject, resolve: resolve(x))) \
        .fork(lambda reject, resolve: resolve(2)) == 1


# Generated at 2022-06-14 03:58:48.389571
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    def test_one():
        """
        Test with unit value
        """
        def func(arg):
            return arg * 2
        unit = Task.of(10)
        gen = Task.of(10).map(func)
        assert gen.fork(None, None) == 20

    def test_two():
        """
        Test with simple value
        """
        def func(arg):
            return arg * 2
        unit = Task.of((1, 2, 3, 4, 5))
        gen = Task.of((1, 2, 3, 4, 5)).map(func)
        assert gen.fork(None, None) == (2, 4, 6, 8, 10)

    test_one()
    test_two()


# Generated at 2022-06-14 03:58:58.484992
# Unit test for method map of class Task
def test_Task_map():
    def resolve(arg):
        return arg

    def reject(arg):
        return 'rejected: ', arg

    def mapper(arg):
        return 'mapped: ', arg

    task = Task.of(1)
    assert task.fork(reject, resolve) == 1

    task = task.map(mapper)
    assert task.fork(reject, resolve) == mapper(1)

    task = Task.reject(1)
    assert task.fork(reject, resolve) == 'rejected: ', 1

    task = task.map(mapper)
    assert task.fork(reject, resolve) == 'rejected: ', 1



# Generated at 2022-06-14 03:59:09.439265
# Unit test for method map of class Task
def test_Task_map():
    """
    Function test_Task_map is unit test for method map of class Task.
    """

    def reject(value):
        """
        :param value: value to store in Task
        :type value: A
        :returns: rejected Task
        :rtype: Task[Function(reject, _) -> A]
        """
        return Task(lambda reject, _: reject(value))

    def resolve(value):
        """
        :param value: value to store in Task
        :type value: A
        :returns: resolved Task
        :rtype: Task[Function(_, resolve) -> A]
        """
        return Task(lambda _, resolve: resolve(value))


# Generated at 2022-06-14 03:59:12.899434
# Unit test for method map of class Task
def test_Task_map():
    def mult_by_2(value):
        return 2 * value

    assert Task.of(1).map(mult_by_2).fork(lambda x: x, lambda x: x) == 2



# Generated at 2022-06-14 03:59:26.439638
# Unit test for method map of class Task
def test_Task_map():
    def resolve_from_1_to_2(resolve):
        resolve(2)
        return 3

    def resolve_from_2_to_3(resolve):
        resolve(3)
        return 5

    def resolve_from_3_to_4(resolve):
        resolve(4)
        return 7

    def resolve_from_4_to_5(resolve):
        resolve(5)
        return 9

    assert Task.of(1).map(resolve_from_1_to_2).map(resolve_from_2_to_3).map(resolve_from_3_to_4).map(resolve_from_4_to_5).fork(None, lambda value: value) == 9


# Generated at 2022-06-14 03:59:30.964458
# Unit test for method map of class Task
def test_Task_map():
    def mapper_value(value):
        return value * 2

    def mapper_err(value):
        raise ValueError(value)

    assert Task.of(1).map(mapper_value).fork(lambda _: False, lambda x: x) == 2
    assert Task.reject(1).map(mapper_err).fork(lambda x: x, lambda _: False) == 1
    assert Task.reject(1).map(mapper_value).fork(lambda x: x, lambda _: False) == 1
    assert Task.of(1).map(mapper_err).fork(lambda x: x, lambda _: False) == 1



# Generated at 2022-06-14 03:59:34.977655
# Unit test for method map of class Task
def test_Task_map():
    def plus(a): return a + 1

    def multiply2(a): return a * 2

    result = Task.of(1)
    assert result.map(plus).fork(None, lambda arg: arg) == 2
    assert result.map(multiply2).fork(None, lambda arg: arg) == 2


# Generated at 2022-06-14 03:59:40.209326
# Unit test for method map of class Task
def test_Task_map():
    def add(x, y): return x + y

    def increase(x): return x + 1

    res = Task.of(1).map(increase).fork(None, lambda v: add(1, v))
    assert res == 3, res



# Generated at 2022-06-14 03:59:44.700446
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(lambda x: x, lambda x: x) == 2
    assert Task.reject(1).bind(lambda x: Task.of(x + 1)).fork(lambda x: x, lambda x: x) == 1


# Generated at 2022-06-14 03:59:51.792811
# Unit test for method map of class Task
def test_Task_map():
    """
    Test if map return new Task with mapped resolve attribute.
    """
    def fn(x):
        return x + 1

    def task_resolved(reject, resolve):
        resolve(5)

    def task_rejected(reject, resolve):
        reject(10)

    assert Task(task_resolved).map(fn).fork(lambda r: r, lambda r: r) == 6
    assert Task(task_rejected).map(fn).fork(lambda r: r, lambda r: r) == 10



# Generated at 2022-06-14 04:00:05.585290
# Unit test for method bind of class Task
def test_Task_bind():
    Task.of(2).bind(lambda v: Task.reject(v)).fork(
        lambda r: assertEqual(r, 2),
        lambda r: assertEqual(r, 2)
    )

    Task.reject(2).bind(lambda v: Task.reject(v)).fork(
        lambda r: assertEqual(r, 2),
        lambda r: assertEqual(r, 2)
    )

    Task.of(2).bind(lambda v: Task.of(v)).fork(
        lambda r: assertEqual(r, 2),
        lambda r: assertEqual(r, 2)
    )


# Generated at 2022-06-14 04:00:16.218796
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method with example:
    '1' + '1' => '1' + '1'
    which should return another Task with resolve value equals 2
    """
    task = Task.reject(1)
    task = task.bind(lambda value: Task.reject(value + 1))
    task = task.bind(lambda value: Task.reject(value + '1'))
    task = task.bind(lambda value: Task.reject(value + '1'))
    task = task.bind(lambda value: Task.reject(int(value)))
    task = task.bind(lambda value: Task.reject(value + 1))

    result = task.fork(None, None)

    assert result == 2


# Generated at 2022-06-14 04:00:22.765360
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of('task value')

    def reject():
        return Task.reject(Exception(''))

    def fork(reject, resolve):
        return resolve(value)

    task = Task(fork)
    assert task.bind(fn).fork(None, lambda x: x) == 'task value'
    assert task.bind(reject).fork(None, None) is None
    assert task.bind(reject).fork(Exception, None).__class__ == Exception

# Generated at 2022-06-14 04:00:29.362937
# Unit test for method map of class Task
def test_Task_map():
    values = []
    promise = Task(lambda reject, resolve: resolve(1))
    promise.map(lambda arg: values.append(arg) or arg + 1)
    promise.fork(lambda arg: arg, lambda arg: values.append(arg) or arg)

    assert values == [1, 2]


# Generated at 2022-06-14 04:00:42.451819
# Unit test for method map of class Task
def test_Task_map():
    """
    If Task has resolved status, map and bind method should return new Task with mapped value.
    """

    # Create Task with resolved status:
    task = Task.of(3)

    # Create mapping function:
    def add_two(value):
        return value + 2

    # Apply map function:
    result = task.map(add_two)

    # Create test object:
    expected_value = 5

    # Call fork method:

# Generated at 2022-06-14 04:00:49.419961
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        if value == 0:
            return Task.of(value + 1)
        return Task.reject('Some error')

    task_of = Task.of(0).bind(fn)
    assert task_of.fork(lambda x: x, lambda x: x) == 1

    task_reject = Task.of(1).bind(fn)
    assert task_reject.fork(lambda x: x, lambda x: x) == 'Some error'

    def some_task(reject, resolve):
        return resolve('task')

    task = Task(some_task).bind(fn)
    assert task.fork(lambda x: x, lambda x: x) == 'task'


# Generated at 2022-06-14 04:00:56.766937
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value * 2

    # create and call Task with fork function that return +100
    result = Task(lambda reject, resolve: resolve(100)).map(mapper)

    assert result.fork(
        lambda arg: False,
        lambda arg: arg
    ) == 200


# Generated at 2022-06-14 04:01:08.336546
# Unit test for method map of class Task
def test_Task_map():
    """
    Create a function, wich take value resolve attribute
    of Task and return reject attribute of Task with mapped value.
    """

    def x(arg):
        return Task.reject(arg ** 2)

    # Create a resolved Task with value 10
    task = Task.of(10)

    # Create new Task with mapped reject attribute
    mapped_task = task.map(lambda x: x ** 2)

    # Check it.
    assert mapped_task.fork(
        lambda reject: reject,
        lambda resolve: None
    ) == 100

    # Create new Task with mapped resolve attribute
    mapped_task = task.map(x)

    # Check it.
    assert mapped_task.fork(
        lambda reject: reject,
        lambda resolve: None
    ) == 100



# Generated at 2022-06-14 04:01:15.370264
# Unit test for method bind of class Task
def test_Task_bind():
    # We have function to call
    def inner_func(reject, resolve):
        # Example of data
        data = 'Example'
        # Call fork to resolve Task
        resolve(data)

    # We have function to call
    def inner_func2(reject, resolve):
        # Example of data
        data = 'Example2'
        # Call fork to resolve Task
        resolve(data)

    # We have function to call
    def inner_func3(reject, resolve):
        # Example of data
        data = 'Example3'
        # Call fork to resolve Task
        resolve(data)

    # We have wrapper for inner_func
    def inner_func_wrapper(reject, resolve):
        # Create new Task based on inner_func
        task = Task(inner_func)
        # Call fork and pass reject and resolve

# Generated at 2022-06-14 04:01:25.964766
# Unit test for method bind of class Task
def test_Task_bind():
    def check_bind(task, expected):
        output = task.fork(lambda reject: reject, lambda resolve: resolve)
        assert output == expected

    def add(value):
        return Task.of(value + 5)

    def divide_by_two(value):
        return Task.of(value / 2)

    # Empty task
    check_bind(
        Task(lambda reject, resolve: resolve(None)).bind(add),
        None
    )
    check_bind(
        Task.of(5).bind(divide_by_two).bind(add),
        7.5
    )
    check_bind(
        Task.of(5).bind(add).bind(divide_by_two),
        5
    )

# Generated at 2022-06-14 04:01:30.126844
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task = task.map(lambda value: value * 2)
    assert task.fork(lambda value: None, lambda value: value) == 2


# Generated at 2022-06-14 04:01:36.288810
# Unit test for method map of class Task
def test_Task_map():
    def apply_Task(iterable):
        return reduce(lambda applier, f: applier.map(f), iterable, Task.of(1))

    def apply_list(iterable):
        return reduce(lambda acc, f: f(acc), iterable, 1)

    iterable = [
        lambda n: n + 1,
        lambda n: n + 2,
        lambda n: n + 3,
    ]

    assert apply_Task(iterable).fork(None, identity) == apply_list(iterable)


# Generated at 2022-06-14 04:01:40.020353
# Unit test for method bind of class Task
def test_Task_bind():
    """Test method bind of class Task."""
    def callback(arg):
        return Task.of(arg)

    task = Task.of(1)
    task = task.bind(callback)

    assert task.fork(lambda _: 'error', lambda value: value) == 1

# Generated at 2022-06-14 04:01:50.022791
# Unit test for method bind of class Task
def test_Task_bind():
    def add_1(x):
        return Task.of(x + 1)

    def str(x):
        return Task.of(str(x))

    def boom(x):
        return Task.reject(x)

    assert Task(lambda reject, resolve: resolve(0)).bind(add_1).bind(
        str).bind(add_1).bind(str).fork(lambda x: x, assert_(1)) is None

    assert Task(lambda reject, resolve: resolve(0)).bind(add_1).bind(
        str).bind(boom).bind(str).fork(assert_(RuntimeError), lambda x: x) is None

    assert Task(lambda reject, resolve: resolve(0)).bind(boom).bind(
        str).bind(add_1).bind(str).fork(assert_(RuntimeError), lambda x: x)

# Generated at 2022-06-14 04:02:01.110423
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task.
    """
    result = Task.of(5).map(lambda x: x + 2)
    assert result.fork is not None

    def fake_reject(value):
        assert False

    def fake_resolve(value):
        assert value == 7

    result.fork(fake_reject, fake_resolve)


# Generated at 2022-06-14 04:02:08.127034
# Unit test for method map of class Task
def test_Task_map():
    called = [False]

    def stub():
        called[0] = True
        return True

    def stub2(arg):
        return not arg

    result = Task.of(1) \
        .map(stub) \
        .map(stub2) \
        .fork(lambda arg: arg, lambda _: True)

    assert result == True
    assert called[0] == True


# Generated at 2022-06-14 04:02:16.682103
# Unit test for method bind of class Task
def test_Task_bind():
    Task.of(2).bind(lambda x: Task.of(x ** 2)).fork(
        lambda x: print('Fail with', x),
        lambda x: print('Success with', x),
    )

    Task.of(2).bind(lambda x: Task.of(x ** 2)).bind(
        lambda x: Task.reject(x)
    ).fork(
        lambda x: print('Fail with', x),
        lambda x: print('Success with', x)
    )

    Task.reject(ValueError('Not a number!')).bind(
        lambda x: Task.reject(x)
    ).fork(
        lambda x: print('Fail with', x),
        lambda x: print('Success with', x)
    )



# Generated at 2022-06-14 04:02:23.960549
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(3).map(add(1))
    assert task.fork(None, None) == 4

    task = Task.of(3).map(add(1)).map(add(2))
    assert task.fork(None, None) == 6

    task = Task(add_task(3)).map(add(1))
    assert task.fork(None, None) == 4

    task = Task(add_task(3)).map(add(1)).map(add(2))
    assert task.fork(None, None) == 6


# Generated at 2022-06-14 04:02:29.029519
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(a):
        return Task.of(a)

    expect(
        Task.of(2).bind(fn).fork(
            lambda arg: arg,
            lambda arg: arg * 2
        )
    ).to.be(4)



# Generated at 2022-06-14 04:02:39.634443
# Unit test for method map of class Task
def test_Task_map():
    @Task.of
    def make(*args, **kwargs):
        return args, kwargs

    @Task.reject
    def error(*args, **kwargs):
        return args, kwargs

    def mapper(value):
        return value

    assert callable(make(1, 2))
    assert callable(make(1, 2, test=3))
    assert callable(error(1, 2))
    assert callable(error(1, 2, test=3))
    assert isinstance(make(1, 2).map(mapper), Task)
    assert isinstance(make(1, 2, test=3).map(mapper), Task)
    assert isinstance(error(1, 2).map(mapper), Task)

# Generated at 2022-06-14 04:02:42.072311
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).bind(lambda value: Task.of(value * value)).fork(
        lambda value: value,
        lambda value: value
    ) == 4


# Generated at 2022-06-14 04:02:49.541800
# Unit test for method map of class Task
def test_Task_map():
    def add_two(a):
        print('add two')
        return a + 2

    def fail(a):
        print('fail')
        return a + 1

    def resolve_success(a):
        print('resolve success')
        return a + 3

    def reject_failure(a):
        print('reject failure')
        return a + 4

    def resolve_success_with_failure(a):
        print('resolve success with failure')
        return a + 5

    def reject_failure_with_failure(a):
        print('reject failure with failure')
        return a + 6

    def resolve_success_with_failure_with_resolve(a):
        print('resolve success with failure with resolve')
        return a + 7


# Generated at 2022-06-14 04:02:54.902902
# Unit test for method map of class Task
def test_Task_map():
    from nose.tools import assert_equals

    def map(value):
        return value + '!'

    task = Task.of('Hello').map(map)

    def assert_callback(result):
        assert_equals(result, 'Hello!')

    def assert_errback(error):
        assert False

    task.fork(assert_errback, assert_callback)


# Generated at 2022-06-14 04:03:02.914948
# Unit test for method map of class Task
def test_Task_map():
    def fn(*args):
        return Task.of(True)

    assert Task(lambda _, resolve: resolve(True)).map(fn).fork(lambda _: False, lambda arg: arg)

    assert not Task(lambda _, reject: reject(False)).map(fn).fork(lambda arg: arg, lambda _: True)

    assert not Task(lambda reject, resolve: resolve(True)).map(lambda _: False).fork(
        lambda arg: arg,
        lambda _: False,
    )

    assert Task(lambda reject, resolve: reject(False)).map(lambda _: True).fork(
        lambda _: True,
        lambda _: False,
    )

# Generated at 2022-06-14 04:03:21.094893
# Unit test for method bind of class Task
def test_Task_bind():
    result = Task.of(10).bind(lambda arg: Task.of(arg + 10))
    assert result.fork(None, lambda arg: arg) == 20, result
    result = Task.of(10).bind(lambda arg: Task.reject(arg + 10))
    assert result.fork(lambda arg: arg, None) == 20, result
    result = Task.reject(10).bind(lambda arg: Task.of(arg + 10))
    assert result.fork(lambda arg: arg, None) == 10, result
    result = Task.reject(10).bind(lambda arg: Task.reject(arg + 10))
    assert result.fork(lambda arg: arg, None) == 10, result



# Generated at 2022-06-14 04:03:28.963887
# Unit test for method map of class Task
def test_Task_map():
    """
    Function to test method map of class Task
    """
    # Setup
    def fork(reject, resolve):
        return resolve(1)

    def fn(arg):
        return arg + 1

    task = Task(fork)
    # Exercise
    actual = task.map(fn)
    # Verify
    assert actual.fork(lambda _: 1, lambda arg: arg) == 2
    # Cleanup - none necessary


# Generated at 2022-06-14 04:03:34.699952
# Unit test for method bind of class Task
def test_Task_bind():
    def get_user(name):
        def callback(resolve, reject):
            resolve('andrey')
        return Task(callback)

    def get_user_name(user):
        def callback(resolve, reject):
            resolve(user.get('name'))
        return Task(callback)

    def get_user_name_capitalized(user_name):
        def callback(resolve, reject):
            resolve(user_name.capitalize())
        return Task(callback)

    assert Task.of({'name': 'andrey'}) \
        .bind(get_user_name) \
        .bind(get_user_name_capitalized) \
        .fork(lambda _: None, lambda x: x) == 'Andrey'


# Generated at 2022-06-14 04:03:40.832991
# Unit test for method map of class Task
def test_Task_map():
    def test_t(fn):
        def resolved(value):
            return Task.of(value).map(fn)

        def rejected(value):
            return Task.reject(value).map(fn)

        return resolved, rejected

    return {
        'map resolve': test_t(lambda x: x * x),
        'map reject': test_t(lambda x: x)
    }


# Generated at 2022-06-14 04:03:48.684617
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(_):
        assert False

    def reject(_):
        assert False

    def success_task(_):
        return Task.of(2)

    def failed_task(_):
        return Task.reject(2)

    # Test success task
    success_task = Task.of(1).bind(success_task)
    success_task.fork(reject, resolve)

    # Test failed task
    failed_task = Task.of(1).bind(failed_task)
    failed_task.fork(reject, resolve)

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:03:51.164967
# Unit test for method map of class Task
def test_Task_map():
    def fn(value):
        return value + 1

    assert Task.of("a").map(fn).fork(lambda x: False, lambda value: value == "a1")


# Generated at 2022-06-14 04:04:00.876996
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind
    """
    def first(number):
        return Task.of(number+1)

    def second(number):
        return Task.of(number+2)

    def third(number):
        return Task.reject(number+3)

    # test for rejection
    assert Task.of(1).bind(lambda _: third(2)).fork(
        lambda reject: reject,
        lambda _: None,
    ) == 5

    # test for chaining
    assert Task.of(1).bind(lambda _: first(2)).bind(lambda _: second(3)).fork(
        lambda _: None,
        lambda resolve: resolve,
    ) == 6


# Generated at 2022-06-14 04:04:04.762007
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task class
    """
    test_double = Task.of(1).map(double)

    assert test_double.fork(identity, identity) == 2


# Generated at 2022-06-14 04:04:11.423137
# Unit test for method map of class Task
def test_Task_map():
    def plus_one(arg):
        return arg + 1

    def plus_two(arg):
        return arg + 2

    assert Task.of(1).map(plus_one).fork(lambda _: None, lambda arg: arg) == 2
    assert Task.of(1).map(plus_two).fork(lambda _: None, lambda arg: arg) == 3


# Generated at 2022-06-14 04:04:21.394052
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task.
    """
    def increment(value):
        return value + 1

    def throw_error(value):
        raise Exception('error')

    def throw_error_test():
        pass

    def check_task(task, value, error=None):
        """
        Check that task contain right value or error.
        If error is None next check it value is correct, else check error is correct.

        :param task: instance of Task
        :type task: Task
        :param value: correct value in task
        :type value: A
        :param error: correct error in task
        :type error: Error | None
        """

# Generated at 2022-06-14 04:04:52.425030
# Unit test for method bind of class Task
def test_Task_bind():
    """
    We have type A and type B.
    We have function #A -> B with side effects.
    We have Task[A] - for store result of function.
    We have Task[B] - for store result of function.
    We want to call function with result of Task[A] and get result in Task[B].
    """

    def value2Task() -> typing.Callable[[int], Task[int]]:
        """
        :param value: value to return
        :type value: int
        :return: Task with stored value
        :rtype: Task[int]
        """
        return lambda arg: Task.of(arg)


# Generated at 2022-06-14 04:05:02.767548
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for map function of Task class
    """
    # test for map function with resolving
    @mock.patch('mock_task.Task.reject')
    def test_map(mock_reject, mock_resolve):
        mock_reject.return_value = mock.sentinel.rejected
        mock_resolve.return_value = mock.sentinel.resolved
        resolved_task = Task.of(1)
        mapped_task = resolved_task.map(lambda x: x + 1)
        assert mock_reject.call_count == 0
        assert mock_resolve.call_count == 0
        result = mapped_task.fork(
            lambda reject: mock.sentinel.rejected,
            lambda resolve: mock.sentinel.resolved
        )
        assert result is mock.sentinel

# Generated at 2022-06-14 04:05:13.929024
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task test_Task_bind: assert Task.bind is working correct
    """
    # Test create subclass for check if arguments types are correct
    assert issubclass(Task(lambda _, __: 1).bind(lambda _: Task(lambda __, ___: 2)).__class__, Task)

    def resolve_wrapper(task, result):
        """
        Call fork of task with mock resolve and reject and return result of resolve

        :param task: task to resolve
        :type task: Task[Function(reject, resolve) -> Any]
        :param result: result to return by resolve
        :type result: Any
        :returns: result of resolve
        :rtype: Any
        """
        return task.fork(lambda _: None, lambda arg: result)


# Generated at 2022-06-14 04:05:18.946338
# Unit test for method bind of class Task
def test_Task_bind():
    def add_1(arg):
        return Task.of(arg + 1)

    def subtract_1(arg):
        return Task.of(arg - 1)


# Generated at 2022-06-14 04:05:29.772607
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(123)
    task = task.map(lambda value: value + 1)
    assert task.fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == 124

    task = Task.of(123)
    task = task.map(lambda value: value + 1).map(lambda value: value * 2)
    assert task.fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == 248

    task = Task.of(123)
    task = task.map(lambda value: 0 / value)
    assert repr(task.fork(
        lambda reject: reject,
        lambda resolve: resolve
    )) == repr(ZeroDivisionError())



# Generated at 2022-06-14 04:05:35.085409
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test method bind of class Task.
    """
    task = Task.of(3).bind(lambda value: Task.of(value).bind(lambda value: Task.of(value + 2)))

# Generated at 2022-06-14 04:05:40.101431
# Unit test for method map of class Task
def test_Task_map():
    # Setup
    @Task.of("42")
    def add_1_and_convert_to_string(value):
        return str(int(value) + 1)

    actual_result = add_1_and_convert_to_string.map(lambda value: "Answer is: " + value)

    assert actual_result.fork(
        lambda _: None,
        lambda value: value
    ) == "Answer is: 43"


# Generated at 2022-06-14 04:05:42.623003
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).bind(lambda x: Task.of(x * 2)).fork(lambda x: x, lambda x: x) == 4
    assert Task.reject(2).bind(lambda x: Task.reject(x * 2)).fork(lambda x: x, lambda x: x) == 4



# Generated at 2022-06-14 04:05:46.151106
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    task = Task.of(1).map(add_one)

    assert task.fork(lambda result: result, lambda result: result) == 2


# Generated at 2022-06-14 04:05:50.418238
# Unit test for method bind of class Task
def test_Task_bind():
    def task(reject, resolve):
        resolve(1)
        reject(2)

    def task_with_error(reject, resolve):
        resolve(3)
        reject(4)

    def mapper(value):
        return value

    def task_with_error_expected(reject, resolve):
        resolve(5)
        reject(6)

    # If reject called then function `fn` should not be called

# Generated at 2022-06-14 04:06:46.065398
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of class Task.
    Call map method with plus two mapper and check result
    """
    def plus_two(_):
        return 2

    task = Task.of(1)
    assert task.map(plus_two).fork(
        lambda _: False,
        lambda _: True
    ) == True


# Generated at 2022-06-14 04:06:53.083525
# Unit test for method map of class Task
def test_Task_map():
    def forked(reject, resolve):
        resolve(3)

    task = Task(forked)

# Generated at 2022-06-14 04:07:03.559041
# Unit test for method map of class Task
def test_Task_map():
    # Task[Function(reject, resolve) -> int]
    task = Task.of(10)
    # Task[Function(reject, resolve) -> "10"]
    stringified = task.map(str)
    # Task[Function(reject, resolve) -> "10 * 2"]
    multiplied = task.map(lambda x: str(x * 2))
    # task.fork => resolve(10)  and return None
    # stringified.fork => resolve("10") and return None
    # multiplied.fork => resolve("10 * 2") and return None
    assert None == task.fork(None, print)
    assert None == stringified.fork(print, print)
    assert None == multiplied.fork(print, print)
    return True


# Generated at 2022-06-14 04:07:10.341085
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Create Task with fork function, this function return value which store in Task.
    Bind method return new Task with fork function with argument of old Task's fork.
    """
    assert 5 == Task(lambda _, resolve: resolve(5)).bind(
        lambda value: Task(lambda _, resolve: resolve(value))
    ).fork(None, lambda value: value)


# Generated at 2022-06-14 04:07:21.092148
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of("OK")
    result = task.bind(lambda value: Task.of("OK")).fork(lambda x: x, lambda _: "ERROR")
    assert result == "OK"

    task = Task.of("OK")
    result = task.bind(lambda value: Task.reject("ERROR")).fork(lambda x: x, lambda _: "ERROR")
    assert result == "ERROR"

    task = Task.reject("ERROR")
    result = task.bind(lambda value: Task.of("OK")).fork(lambda x: x, lambda _: "ERROR")
    assert result == "ERROR"

    task = Task.reject("ERROR")
    result = task.bind(lambda value: Task.reject("ERROR FROM FORK")).fork(lambda x: x, lambda _: "ERROR")

# Generated at 2022-06-14 04:07:22.970553
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(42).map(lambda value: value + 11).fork(None, lambda resolve: resolve) == 53

# Generated at 2022-06-14 04:07:28.342744
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(42).map(lambda x: x*2)
    assert task.fork(lambda x: x, lambda x: x) == 84

    task = Task.reject(42).map(lambda x: x*2)
    assert task.fork(lambda x: x, lambda x: x) == 42


# Generated at 2022-06-14 04:07:37.564664
# Unit test for method map of class Task
def test_Task_map():
    def f(x):
        return x * 2

    def g(x):
        return x + 2

    def h(x):
        return x - 5

    def t(f, value):
        return Task.of(value).map(f)


# Generated at 2022-06-14 04:07:43.502287
# Unit test for method map of class Task
def test_Task_map():
    def plus(value):
        return value + 3

    def return_value_from_plus(value):
        return Task.of(plus(value))

    assert Task.of(3).map(plus).fork(lambda x: None, lambda x: x) == 6
    assert Task.of(3).bind(return_value_from_plus).fork(lambda x: None, lambda x: x) == 6



# Generated at 2022-06-14 04:07:49.910809
# Unit test for method bind of class Task
def test_Task_bind():
    """
    test for Task class
    """
    def resolve_callback(val):
        """
        Dummy resolve callback for Task.
        """
        pass

    def reject_callback(val):
        """
        Dummy reject callback for Task.
        """
        pass

    def multiply_by_two(val):
        """
        Multiply by two argument.
        """
        return val * 2

    def add_two(val):
        """
        Add two to argument.
        """
        return val + 2

    task = Task.of(2).bind(lambda val: Task.of(val * 2))

    task.fork(reject_callback, resolve_callback) == 4

    assert task.fork(reject_callback, resolve_callback) == 4