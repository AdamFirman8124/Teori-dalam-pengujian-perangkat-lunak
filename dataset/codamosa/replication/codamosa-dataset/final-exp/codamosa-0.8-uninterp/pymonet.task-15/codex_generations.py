

# Generated at 2022-06-14 03:57:54.772417
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve(42)

    task = Task(fork)
    plus_one = lambda arg: arg + 1
    new_task = task.map(plus_one)

    assert new_task.fork(lambda _: None, lambda arg: arg) == 43


# Generated at 2022-06-14 03:58:03.425395
# Unit test for method map of class Task
def test_Task_map():
    """
    Test function for map function of Task
    """
    def fn(x):
        """
        :param x: integer
        :type x: int
        :returns: x + 1
        :rtype: int
        """
        return x + 1

    def mapped_fn(x):
        """
        :param x: integer
        :type x: int
        :returns: x + 1
        :rtype: int
        """
        return x + 1

    # Create resolved Task
    task = Task.of(3)

    # Mapped argument should be checked with isinstance(result, Task)
    result = task.map(mapped_fn)

    # Check if result of map is a Task
    assert isinstance(result, Task)

    # Check if result of map is equal to Task, which store result of fn

# Generated at 2022-06-14 03:58:06.352480
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 1

    task = Task.of(42)
    task_result = task.map(mapper).fork(lambda _: None, lambda value: value)

    assert task_result == 43


# Generated at 2022-06-14 03:58:12.106357
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(2)

    def bind_fn(value):
        def fork_fn(reject, resolve):
            resolve(value * 2)

        return Task(fork_fn)

    task = Task(fork)
    assert task.bind(bind_fn).fork(lambda value: None, lambda value: value) == 4

# Generated at 2022-06-14 03:58:15.885398
# Unit test for method map of class Task
def test_Task_map():
    """Unit test for method map of class Task."""

    # data
    t = Task(lambda _, resolve: resolve("test"))
    mapper_fn = lambda x: x + "!"

    # test
    assert t.map(mapper_fn).fork(lambda x: x, lambda x: x) == "test!"


# Generated at 2022-06-14 03:58:19.302219
# Unit test for method map of class Task
def test_Task_map():
    result = Task(lambda _, resolve:
                  resolve("test")).map(lambda val: len(val))

    assert result.fork(None, lambda x: x) == 4


# Generated at 2022-06-14 03:58:24.314571
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task.of(x + 1)

    assert Task.of(2).bind(f).fork(lambda x: f, lambda x: x) == 3


# Generated at 2022-06-14 03:58:34.346150
# Unit test for method map of class Task
def test_Task_map():
    """
    Task.map test
    map(fn) => Task[Fork(onResolve(fn(value)))
    """
    def task(reject, resolve):
        resolve(100)

    T = Task(task).map(lambda x: x * 2)
    assert T.fork(None, None) == 200


# Generated at 2022-06-14 03:58:37.026743
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(arg):
        return Task.of(arg + 5)

    task = Task.of(2).bind(mapper)
    assert task.fork(lambda err: False, lambda res: res) == 7


# Generated at 2022-06-14 03:58:38.908721
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    assert task.map(lambda x: x + 1).fork(None, lambda x: x == 2) is True


# Generated at 2022-06-14 03:58:47.636947
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(x):
        return Task.reject(x)

    def resolve(x):
        return Task.of(x)

    def mapper_task_of(value, number):
        return Task.of(value ** number)

    def mapper_task_reject(value, number):
        return reject(value ** number)

    assert (Task.of(10).bind(lambda x: mapper_task_of(x, 2)) ==
            Task.of(100))

    assert (Task.of(10).bind(lambda x: mapper_task_reject(x, 2)) ==
            Task.reject(100))

    print('Passed')


# Generated at 2022-06-14 03:58:53.734023
# Unit test for method map of class Task
def test_Task_map():
    def plus1(a):
        return a + 1

    def plus2(a):
        return a + 2

    task = Task.of(1)

    assert task.map(plus1).fork(lambda _: None, lambda arg: arg) == 2
    assert task.map(plus2).fork(lambda _: None, lambda arg: arg) == 3


# Generated at 2022-06-14 03:58:57.704176
# Unit test for method map of class Task
def test_Task_map():
    import pytest

    task = Task.of(10)
    task_2 = task.map(lambda x: x + 10)

    assert task_2.fork(lambda _: False, lambda x: x) == 20


# Generated at 2022-06-14 03:59:03.088800
# Unit test for method map of class Task
def test_Task_map():
    """
    Tests Task .map method
    """
    def identity(x):
        return x

    def plus(x, y):
        return x + y

    assert Task.of(1).map(identity) == Task.of(1)
    assert Task.of(1).map(plus).map(identity) == Task.of(1)


# Generated at 2022-06-14 03:59:09.132888
# Unit test for method map of class Task
def test_Task_map():
    """
    Task.map should return a task which
    - take result of a function call as arg of resolve function
    - take result of a function call as arg of reject function
    """
    def a_fn(x):
        return x + x

    def b_fn(x):
        return x * 2

    def c_fn(x):
        return x - 1

    a_mapped_task = Task.of(1).map(a_fn)
    assert a_mapped_task.fork(lambda a: None, lambda a: a) == 2

    b_mapped_task = a_mapped_task.map(b_fn)
    assert b_mapped_task.fork(lambda b: None, lambda b: b) == 4


# Generated at 2022-06-14 03:59:17.446742
# Unit test for method map of class Task
def test_Task_map():
    import pytest

    # Test return Task with resolved value
    assert Task.of(1).map(lambda v: v + 1).fork(
            lambda reject: None,
            lambda resolve: resolve
        ) == (None, 2)

    # Test return Task with rejected value
    assert Task.reject(1).map(lambda v: v + 1).fork(
            lambda reject: reject,
            lambda resolve: None
        ) == (1, None)

    # Test raise error if Task is rejected
    def test_error():
        Task.reject(1).map(lambda v: v + 1)

    pytest.raises(Error, test_error)


# Generated at 2022-06-14 03:59:27.889696
# Unit test for method map of class Task
def test_Task_map():
    Task_of_5 = Task.of(5)
    double_Task_of_5 = Task_of_5.map(lambda x: 2 * x)

    assert Task_of_5.fork(lambda x: 'rejected', lambda x: 'resolved') == 'resolved'
    assert Task_of_5.fork(lambda x: None, lambda x: x) == 5

    assert double_Task_of_5.fork(lambda x: 'rejected', lambda x: 'resolved') == 'resolved'
    assert double_Task_of_5.fork(lambda x: None, lambda x: x) == 10

    Task_of_0 = Task.of(0)
    double_Task_of_0 = Task_of_0.map(lambda x: 2 / x)


# Generated at 2022-06-14 03:59:33.242390
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value * 2

    assert Task.of(1).map(mapper).fork(None, lambda a: a) == 2
    assert Task.reject(1).map(mapper).fork(lambda a: a, None) == 1


# Generated at 2022-06-14 03:59:44.117943
# Unit test for method map of class Task
def test_Task_map():
    @Task.of
    def a():
        return 1

    def plus(value):
        return value + 1

    task = a()
    assert task.fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 1
    assert task.map(plus).fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 2

    # Task reject
    @Task.reject
    def a():
        return 1

    def plus(value):
        return value + 1

    task = a()
    assert task.fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 1
    assert task.map(plus).fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 1


# Generated at 2022-06-14 03:59:50.534877
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('test').map(lambda arg: arg + '!').fork(lambda err: 'err', lambda res: res) == 'test!'

    assert not Task.reject('test').map(lambda arg: arg + '!').fork(lambda err: err, lambda res: 'res') == 'err'
    assert Task.reject('test').map(lambda arg: arg + '!').fork(lambda err: err, lambda res: 'res') == 'test'


# Generated at 2022-06-14 04:00:00.530535
# Unit test for method bind of class Task
def test_Task_bind():
    def right(_):
        return Task.of("right")

    def left(_):
        return Task.reject("left")

    task = Task.of("value")
    assert task.bind(right).fork(lambda x: x, lambda y: y) == "right"
    assert task.bind(left).fork(lambda x: x, lambda y: y) == "left"


# Generated at 2022-06-14 04:00:07.138642
# Unit test for method bind of class Task
def test_Task_bind():
    def add_five_to_a_value(arg):
        return arg + 5

    def multiple_by_five(arg):
        return Task.of(arg * 5)

    from_value = Task.of(42)
    from_bind = from_value.bind(add_five_to_a_value).bind(multiple_by_five)

    from_map = from_value.map(add_five_to_a_value).map(multiple_by_five)

    def is_correct(reject, resolve):
        assert from_bind._fork(reject, resolve) == from_map._fork(reject, resolve)
        return True

    Task.of(True).bind(is_correct).run()

# Generated at 2022-06-14 04:00:11.089754
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1).bind(lambda x: Task.of(x + 2))
    result = task.fork(None, lambda t: t)

    assert result == 3, 'Task bind method works wrong'


# Generated at 2022-06-14 04:00:19.764574
# Unit test for method bind of class Task
def test_Task_bind():

    task = Task(lambda _, resolve: resolve(5))

    new_task = task.bind(
        lambda value: Task(
            lambda _, resolve: resolve(value * 2)
        )
    )

    assert new_task.fork(lambda _: False, lambda value: value == 10)

    new_task = task.bind(
        lambda value: Task(
            lambda reject, _: reject(value * 2)
        )
    )

    assert new_task.fork(lambda value: value == 10, lambda _: False)

# Generated at 2022-06-14 04:00:24.821002
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Check correct working of method bind of class Task

    :returns: Boolean value of test result
    :rtype: bool
    """

    def mapper(value):
        return Task.of(value + 1)

    task = Task.of(0)
    result_task = task.bind(mapper)

    return result_task.fork(lambda x: -1, lambda x: x) == 1


# Generated at 2022-06-14 04:00:29.934435
# Unit test for method map of class Task
def test_Task_map():
    @pytest.fixture
    def task():
        return Task(lambda _, resolve: resolve(10))

    def test_task_map(task):
        assert task.map(lambda x: x + 10).fork(None, lambda value: value == 20)



# Generated at 2022-06-14 04:00:36.289720
# Unit test for method map of class Task
def test_Task_map():
    """Test Task[reject, resolve] -> Task[reject, resolve].map(fn: Function(A) -> B)"""
    assert Task(lambda _, resolve: resolve(1))\
        .map(lambda x: x + 1)\
        .map(lambda x: x * 2)\
        .fork(_, lambda x: x) == 4


# Generated at 2022-06-14 04:00:42.154956
# Unit test for method bind of class Task
def test_Task_bind():
    value = Task.of(1).bind(lambda x: Task.of(x + 2)).fork(lambda _: None, lambda x: x)
    assert value == 3

    value = Task.reject(1).bind(lambda x: Task.of(x + 2)).fork(lambda x: x, lambda _: None)
    assert value == 1


# Generated at 2022-06-14 04:00:45.840745
# Unit test for method map of class Task
def test_Task_map():
    """
    Tests of method map of class Task.
    """
    def fn(value):
        return value + 2

    assert Task.of(2).map(fn).fork(
        lambda value: False,
        lambda value: 4 == value
    )


# Generated at 2022-06-14 04:00:49.047448
# Unit test for method map of class Task
def test_Task_map():
    def f(_, resolve): return resolve('f')
    def g(_, resolve): return resolve('g')

    assert Task(f).fork == Task(f).map(lambda _: None).fork
    assert Task(g).fork == Task(f).map(lambda x : g(x)).fork


# Generated at 2022-06-14 04:01:01.902368
# Unit test for method bind of class Task
def test_Task_bind():
    def create_task(value):
        """
        Function that accept value and return new Task with this value.

        :param value: value to store in Task
        :type value: A
        :returns: new Task with resolve value argument
        :rtype: Task[Function(_, resolve) -> A]
        """
        return Task.of(value)

    def double(value):
        """
        Function that accept value and return multiply by two.

        :param value: value to multiply by two
        :type value: A
        :returns: multiply by two
        :rtype: int
        """
        return value * 2

    task = Task.of(1)

    assert task.bind(create_task).fork(lambda err: err, lambda val: val) == 1
    assert task.map(double).bind(create_task).fork

# Generated at 2022-06-14 04:01:08.993675
# Unit test for method bind of class Task
def test_Task_bind():
    def method(value):
        return Task.of(value)

    def method_reject(value):
        return Task.reject(value)

    assert Task(lambda reject, resolve: resolve(42)).bind(method).fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == 42

    assert Task(lambda reject, resolve: resolve(42)).bind(method_reject).fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == 42

# Generated at 2022-06-14 04:01:18.099620
# Unit test for method map of class Task
def test_Task_map():

    def identity(x):
        return x

    one_task = Task.of(1)
    two_task = one_task.map(identity)

    def fork(reject, resolve):
        reject("test_reject")
        resolve("test_resolve")

    two_task_with_fork = Task(fork)

    assert 1 == two_task.fork(lambda a: a, lambda a: a)
    assert "test_resolve" == two_task_with_fork.fork(lambda a: a, lambda a: a)

# Generated at 2022-06-14 04:01:23.869208
# Unit test for method bind of class Task
def test_Task_bind():
    def tasks_fork(reject, resolve):
        resolve(5)

    def add_fork(reject, resolve):
        resolve(5)

    orig_task = Task(tasks_fork)
    new_task = Task(add_fork)

    task = orig_task.bind(lambda x: new_task)
    assert task.fork(lambda _: False, lambda x: x == 5)

# Generated at 2022-06-14 04:01:26.844886
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for corrent work of method map of class Task
    """
    assert Task.of(1).map(lambda arg: arg + 1).fork(None, lambda arg: arg) == 2



# Generated at 2022-06-14 04:01:39.006572
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """

    # Set test for Task class
    result = Task.of(3).bind(lambda x: Task.of(x + 1)).bind(lambda x: Task.of(x + 1))
    assert result.fork(
        lambda x: x,
        lambda x: x
    ) == 5

    # Set test for exception occured
    result = Task.of(3).bind(lambda x: Task.of(x + 1)).bind(lambda _: Task.reject('error'))
    assert result.fork(
        lambda x: x,
        lambda _: 'should not get here'
    ) == 'error'

if __name__ == "__main__":
    test_Task_bind()

# Generated at 2022-06-14 04:01:45.055432
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        print('resolve: %s' % value)

    def reject(value):
        print('reject: %s' % value)

    def fn(value):
        return Task.of(value + 1)

    task = Task.of(1)
    task.bind(fn).fork(reject, resolve)
    task = Task.reject(1)
    task.bind(fn).fork(reject, resolve)


# Generated at 2022-06-14 04:01:58.175255
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method.
    """
    def test_positive(value):
        """
        Return task with value.
        """
        return Task.of(value)

    def test_negative(value):
        """
        Return task with value.
        """
        return Task.reject(value)


    def clear_result(value):
        """
        Return task with value.
        """
        return Task.of(value)

    def error_result(value):
        """
        Return task empty value.
        """
        return Task.of(None)

    def clear_error(value):
        """
        Return task empty value.
        """
        return Task.of(None)

    def error_error(value):
        """
        Return task empty value.
        """
        return Task.of

# Generated at 2022-06-14 04:02:06.722327
# Unit test for method bind of class Task
def test_Task_bind():
    def branch(x, resolve, reject):
        if x == 0:
            resolve(0)
        else:
            reject('x != 0')

    def fork(x):
        def _(reject, resolve):
            return branch(x, resolve, reject)

        return Task(_)

    def other_fork(x):
        def _(reject, resolve):
            resolve(x)

        return Task(_)

    assert fork(0).bind(other_fork).fork(lambda err: 0, lambda res: res) == 0
    assert fork(1).bind(other_fork).fork(lambda err: err, lambda res: 0) == 'x != 0'



# Generated at 2022-06-14 04:02:10.310520
# Unit test for method map of class Task
def test_Task_map():
    def increment(x):
        return x + 1

    task = Task.of(1)
    assert task.map(increment).fork(lambda err: 'error', lambda val: val) == 2



# Generated at 2022-06-14 04:02:23.573655
# Unit test for method map of class Task
def test_Task_map():
    def simple_mapper(value):
        return value * 2

    value = 17
    task = Task.of(value)

    task_mapped = task.map(simple_mapper)
    assert task_mapped.fork(
        lambda _: False,
        lambda result: result == simple_mapper(value)
    )

    task = Task.of(value)
    task_mapped = task.map(simple_mapper).map(str)

    assert task_mapped.fork(
        lambda _: False,
        lambda result: result == str(simple_mapper(value))
    )

test_Task_map()


# Generated at 2022-06-14 04:02:29.946817
# Unit test for method map of class Task
def test_Task_map():
    @Task.of
    def success(data):
        return data

    assert success(10)
    assert success(10).map(lambda x: x).fork(lambda a: False, lambda a: True)
    assert success(10).map(lambda x: x + 1).fork(lambda a: False, lambda a: True)



# Generated at 2022-06-14 04:02:40.366038
# Unit test for method bind of class Task
def test_Task_bind():
    def create_lazy_add(arg):
        def lazy_add(value):
            return value + arg

        return lazy_add

    def create_lazy_sub(arg):
        def lazy_sub(value):
            return value - arg

        return lazy_sub

    def create_lazy_func(arg):
        def lazy_func(value):
            return Task.of(value - arg)

        return lazy_func

    assert Task.of(10).bind(create_lazy_add(1)).fork(None, lambda result: result == 11)
    assert Task.of(10).bind(create_lazy_sub(1)).fork(None, lambda result: result == 9)
    assert Task.of(10).bind(create_lazy_func(1)).fork(None, lambda result: result == 9)

#

# Generated at 2022-06-14 04:02:46.358701
# Unit test for method map of class Task
def test_Task_map():
    """
    Function to test map method of Task class.
    """
    # define a variable to store result
    result = None

    def foo(_, resolve):
        return resolve(42)

    # create task and map it
    task = Task(foo).map(lambda value: value * 2)

    # fork task
    task.fork(
        lambda value: print('REJECTED:', value),
        lambda value: result.append(value)
    )

    # check task value
    assert result == [84]



# Generated at 2022-06-14 04:02:56.133324
# Unit test for method map of class Task
def test_Task_map():
    def test_result(task, value):
        result = task.fork(lambda _: None, lambda arg: arg)
        assert result == value

    def test_error(task, value):
        result = task.fork(lambda arg: arg, lambda _: None)
        assert result == value

    Task.of(4).map(lambda x: x * 2).map(lambda y: y + 1).map(lambda z: z ** 2)\
        .fork(test_error, test_result)

    Task.reject(4).map(lambda x: x * 2).map(lambda y: y + 1).map(lambda z: z ** 2)\
        .fork(test_result, test_error)


# Generated at 2022-06-14 04:02:59.818123
# Unit test for method map of class Task
def test_Task_map():
    def g(arg):
        return arg + "!!!"

    def f(arg):
        return arg + "!!"

    assert Task.of("Hi").map(g).map(f).fork(None, print) == "Hi!!!!"


# Generated at 2022-06-14 04:03:05.125491
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        """
        :param value: value to map
        :type value: B
        :returns: Task[reject, mapped_value]
        :rtype: Task[B]
        """
        return Task.of(value * 2)

    task_result = Task.of(2).bind(mapper)
    assert task_result.fork(lambda a: a, lambda a: a) == 4

# Generated at 2022-06-14 04:03:08.570988
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(_, resolve):
        return resolve(1)

    def task_fork(reject, resolve):
        return resolve('task_fork')

    task = Task(fork)
    t = Task(task_fork)
    task.bind(lambda _: t).fork(lambda _: False, lambda x: x == 'task_fork')


# Generated at 2022-06-14 04:03:18.264654
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)
    result = task.bind(lambda v: Task.of(v * 2))
    assert result.fork(
        lambda v: 0,
        lambda v: v
    ) == 2

    task = Task.of(1)
    result = task.bind(lambda v: Task.reject(v * 2))
    assert result.fork(
        lambda v: v,
        lambda v: 0
    ) == 2

    task = Task.reject(1)
    result = task.bind(lambda v: Task.of(v * 2))
    assert result.fork(
        lambda v: v,
        lambda v: 0
    ) == 1


# Generated at 2022-06-14 04:03:24.642388
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2)
    task = task.map(lambda x: x + 1)
    assert task.fork(lambda x: 1, lambda y: y) == 3
    task = task.map(lambda x: x + 2)
    assert task.fork(lambda x: 1, lambda y: y) == 5


# Generated at 2022-06-14 04:03:43.580385
# Unit test for method bind of class Task
def test_Task_bind():
    def to_Task(value):
        return Task(lambda _, resolve: resolve(value))

    def to_Task_err(value):
        return Task(lambda reject, _: reject(value))

    assert (Task.of('hello world')
            .bind(lambda value: to_Task_err(value))
            .fork(lambda error: 'error', lambda value: value)
            == 'error').ok(
                'Task should be rejected during calling bind function if first Task was rejected')

    assert (Task.of(1)
            .bind(lambda value: to_Task(value + 1))
            .fork(lambda error: 'error', lambda value: value)
            == 2).ok(
                'Task should be resolved with value 2 during calling bind function if first Task was resolved')


# Generated at 2022-06-14 04:03:46.361170
# Unit test for method bind of class Task
def test_Task_bind():
    IncrementTask = Task.of(2).bind(lambda value: Task.of(value + 1))
    assert IncrementTask.fork(lambda value: None, lambda value: none) == 3
    AssertionError = AssertionError()
    ErrorTask = Task.of(2).bind(lambda value: Task.reject(AssertionError))
    assert ErrorTask.fork(lambda value: value, lambda value: value) == AssertionError


# Generated at 2022-06-14 04:03:49.243037
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of('10')
    mapped_task = task.map(lambda x: int(x))
    assert mapped_task.fork(lambda x: x, lambda x: x * 2) == 20


# Generated at 2022-06-14 04:03:55.046310
# Unit test for method map of class Task
def test_Task_map():
    # given
    add_two = lambda x: x + 2
    multiply_by_two = lambda x: x * 2
    task_of_2 = Task.of(2)

    # when
    mapped_task = task_of_2.map(add_two).map(multiply_by_two)
    result = mapped_task.fork(
        lambda err: 'error',
        lambda res: res,
    )

    # then
    eq_(result, 8)


# Generated at 2022-06-14 04:04:01.414116
# Unit test for method map of class Task
def test_Task_map():
    def fn(value):
        return value + 1

    task = Task.of(0)

    assert task.fork(lambda _: "rejected", lambda a: a) == 0
    assert task\
        .map(fn)\
        .fork(lambda _: "rejected", lambda a: a) == 1

    assert Task.of(0)\
        .map(fn)\
        .map(fn)\
        .fork(lambda _: "rejected", lambda a: a) == 2

    assert Task.reject(0)\
        .map(fn)\
        .fork(lambda _: "rejected", lambda a: a) == "rejected"


# Generated at 2022-06-14 04:04:08.559569
# Unit test for method bind of class Task
def test_Task_bind():
    test_Task = Task.of(2)

    assert test_Task.bind(lambda value: Task.of(value + 2)).fork(
        lambda value: value + 10,
        lambda value: value - 10
    ) == 4

    assert test_Task.bind(lambda value: Task.reject(value - 2)).fork(
        lambda value: value + 10,
        lambda value: value - 10
    ) == 8


if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:04:19.576732
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind.
    also test Task.map.
    """
    def test():
        raise NotImplemented

    err = 'error'

    def test_1():
        return Task.of(3).bind(lambda x: Task.reject(err))

    def test_2():
        return Task.of(10).map(lambda x: x + 1).map(lambda x: x / 0)

    def test_3():
        return Task.of(10).map(lambda x: Task.reject(err)).bind(lambda x: x)

    def test_4():
        return Task.reject(err).map(lambda x: x + 1)

    def test_5():
        return Task.of(None).map(lambda x: x + 1).bind(lambda x: x)


# Generated at 2022-06-14 04:04:26.347379
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Create resolved Task, bind with mapper that return resolved Task
    and check that result of bind is Task with stored result of mapped function.

    :returns: None
    :rtype: None
    """
    result = Task.of(1).bind(lambda x: Task.of(x + 1))
    r, f = result.fork(lambda _: 1, lambda _: 2)
    assert r == 2
    assert f == 2


# Generated at 2022-06-14 04:04:36.942636
# Unit test for method bind of class Task
def test_Task_bind():
    def identity(x):
        return x

    def twice(x):
        return x % 2 + x // 2

    def twice_task(x):
        return Task.of(twice(x))

    result = Task.of(42).map(identity)
    print("Identity: ", result.fork(identity, identity))

    result = Task.of(42).map(twice)
    print("Twice: ", result.fork(identity, identity))

    result = Task.of(42).bind(twice_task)
    print("Twice_task: ", result.fork(identity, identity))

# Generated at 2022-06-14 04:04:41.739471
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    """
    result = Task.of(2).bind(
        lambda x: Task.of(x + 2)
    ).fork(
        lambda err: err,
        lambda val: val
    )
    result_should_be = 4

    assert result == result_should_be, "bind method for Task failed."


# Generated at 2022-06-14 04:04:54.841309
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + '!'

    result = Task.of('Hello').map(mapper)
    assert result.fork(
        lambda value: None, # TODO: check if this correct
        lambda value: value == 'Hello!'
    )


# Generated at 2022-06-14 04:05:00.866917
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        """
        Map function which return *1.3 of value.

        :param value: number
        :type value: int
        :returns: new number
        :rtype: int
        """
        return value * 1.3

    task = Task.of(1).map(mapper)
    assert task.fork(lambda reject: reject, lambda resolve: resolve) == 1.3


# Generated at 2022-06-14 04:05:07.417170
# Unit test for method map of class Task
def test_Task_map():
    """
    Run tests for method map of class Task
    :param value: value to store in Task
    :type value: A
    :returns: resolved Task
    :rtype: Task[Function(_, resolve) -> A]
    """
    def test_sum(callback):
        """
        Test callback for sum of 1+2=3
        """
        assert callback(1 + 2) == 3

    def test_mul(callback):
        """
        Test callback for multiplication of 1*2=2
        """
        assert callback(1 * 2) == 2

    def test_div(callback):
        """
        Test callback for division of 2/2=1
        """
        assert callback(2 / 2) == 1

    Task.of(1 + 2).fork(
        lambda arg: None,
        test_sum
    )

# Generated at 2022-06-14 04:05:13.146079
# Unit test for method map of class Task
def test_Task_map():
    def af(n):
        return n ** 2

    def bf(n):
        return n

    assert Task.of(5).map(af).fork(None, bf) == 25

    assert Task.of(5).map(af).map(bf).fork(None, bf) == 25



# Generated at 2022-06-14 04:05:17.264730
# Unit test for method bind of class Task
def test_Task_bind():
    def test_method(value):
        return Task.of(value + 1)

    assert Task.of(1).bind(test_method).fork(None, lambda value: value) == 2


# Generated at 2022-06-14 04:05:25.381146
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(arg):
        return Task.reject(arg * 2)

    def fork(reject, resolve):
        resolve(2)

    result = Task(fork).bind(mapper)
    result = result.fork(lambda reject: reject, lambda resolve: resolve)
    assert result == 4

    result = Task(fork).bind(lambda reject, resolve: Task.reject(reject * 2))
    result = result.fork(lambda reject: reject, lambda resolve: resolve)
    assert result == 4

test_Task_bind()



# Generated at 2022-06-14 04:05:27.308257
# Unit test for method map of class Task
def test_Task_map():
    def test():
        fun = lambda x: x + 5
        task = Task.of(5)
        assert task.map(fun).fork(None, lambda value: value) == 10
    test()


# Generated at 2022-06-14 04:05:31.708208
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for Task.map
    :return: lambda
    """
    return (
        lambda: Task.reject('err').map(lambda value: value).fork(
            lambda reject: True,
            lambda resolve: False
        ),
        True
    )


# Unit tests for method of of class Task

# Generated at 2022-06-14 04:05:41.169398
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind.
    """
    def mul_two(resolved_value):
        """
        Multiply value to two.

        :param resolved_value: value from resolved Task
        :type resolved_value: int
        :return: result of multiplying
        :rtype: int
        """
        assert resolved_value == 1
        return resolved_value * 2

    def add_one(resolved_value):
        """
        Add one to resolved Task.

        :param resolved_value: value from resolved Task
        :type resolved_value: int
        :return: result of adding
        :rtype: int
        """
        assert resolved_value == 2
        return resolved_value + 1


# Generated at 2022-06-14 04:05:54.116791
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method.
    """
    def fn(number):
        """
        Just return number.

        :param number: argument to return
        :type number: Any
        :returns: number
        :rtype: Any
        """
        return number

    def inner_fn(resolve, reject):
        """
        Just call resolve with arg.

        :param resolve: resolve callback
        :type resolve: Function(value) -> Any
        :param reject: reject callback
        :type reject: Function(value) -> Any
        """
        resolve(1)

    task = Task(inner_fn).bind(fn)


# Generated at 2022-06-14 04:06:09.668351
# Unit test for method bind of class Task
def test_Task_bind():
    task_reject = lambda x, _: x
    def task_resolve(value):
        def fork(_, resolve):
            return resolve(value)
        return Task(fork)

    fn = lambda x: task_resolve(x)
    task = task_resolve(1)

    assert task.bind(fn).fork(task_reject, task_reject) == 1


# Generated at 2022-06-14 04:06:10.336486
# Unit test for method bind of class Task
def test_Task_bind():
    pass

# Generated at 2022-06-14 04:06:19.830817
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    def resolve(value):
        print("Resolve: {0}".format(value))
        assert value == 2

    def reject(value):
        print("Reject: {0}".format(value))
        assert False

    def add_one(x):
        return Task.of(x + 1)

    def concat(value):
        return value + " string"

    Task(1).bind(add_one).bind(add_one).fork(reject, resolve)
    Task.reject("reject").bind(add_one).bind(add_one).fork(reject, resolve)

    resolve("reject")

test_Task_bind()


# Generated at 2022-06-14 04:06:26.614365
# Unit test for method map of class Task
def test_Task_map():
    def add_two(x):
        return x + 2

    def add_three(x):
        return x + 3

    task = Task.of(1)
    task = task.map(add_two)
    assert task.fork(lambda _: None, lambda x: x) == 3

    task = Task.of(1)
    task = task.map(add_two)
    task = task.map(add_three)
    assert task.fork(lambda _: None, lambda x: x) == 5



# Generated at 2022-06-14 04:06:39.521518
# Unit test for method map of class Task
def test_Task_map():
    data = [1, 2, 3, 4]

    # Tested function
    def get_data(index):
        return Task.of(data[index])

    # Tested function
    def get_index(index):
        return Task.of(index)

    # Tested function
    def get_index_if_value_exist(index):
        if index < len(data):
            return Task.of(index)
        else:
            return Task.reject("This index {} not exist in data".format(index))

    # Tested function
    def get_value(index):
        return Task.of(data[index])

    # Tested function
    def get_value_if_index_exist(index):
        if index < len(data):
            return Task.of(data[index])
        return Task.reject

# Generated at 2022-06-14 04:06:49.413947
# Unit test for method map of class Task
def test_Task_map():
    # Simple example with positive case
    def hello_fn(msg):
        return "hello " + msg

    task = Task.of("world").map(hello_fn)

    def _reject(_):
        raise AssertionError("not expected")

    def _resolve(value):
        assert value == "hello world"

    task.fork(_reject, _resolve)

    # Test for exception in mapper function
    task = Task.of("world").map(lambda _: 1 / 0)

    def _resolve(_):
        raise AssertionError("not expected")

    task.fork(_resolve, _reject)

    # Test for exception in map function
    task = Task.of("world")
    task.map = lambda _: 1 / 0

    task.fork(_reject, _resolve)

    # Test

# Generated at 2022-06-14 04:06:53.817859
# Unit test for method bind of class Task
def test_Task_bind():
    def func(value):
        def inner(reject, resolve):
            return reject(value)
        return Task(inner)

    assert Task.of('value').bind(func).fork(lambda arg: arg, lambda _: 'other') == 'value'


# Generated at 2022-06-14 04:07:00.280901
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test that bind uses new Task as result of mapping and
    that it call resolve attribute of new Task
    """
    class TestTask(Task):
        def __init__(self, fork):
            Task.__init__(self, fork)

        def fork(self, _, resolve):
            resolve('test_value')

    task = TestTask(lambda _, resolve: resolve(0))
    task.bind(lambda value: TestTask(lambda _, resolve: resolve(value))).fork(
        lambda _: False,
        lambda value: value == 'test_value'
    )

    assert True

# Generated at 2022-06-14 04:07:06.039971
# Unit test for method map of class Task
def test_Task_map():
    # case: function map is work
    # Arrange
    task_of_value = Task.of(2)
    mapper = lambda value: value * 2

    # Act
    result = task_of_value.map(mapper)

    # Assert
    assert result.fork(None, lambda value: value) == 4

    # case: function map didn't called if passed value is rejected
    # Arrange
    task_of_value = Task.reject(2)
    mapper = lambda value: value * 2

    # Act
    result = task_of_value.map(mapper)

    # Assert
    assert result.fork(lambda value: value, None) == 2


# Generated at 2022-06-14 04:07:10.784003
# Unit test for method map of class Task
def test_Task_map():
    assert Task(
        lambda _, resolve: resolve(10)
    ).map(
        lambda value: value + 1
    ).fork(lambda v: v, lambda v: v) == 11


# Generated at 2022-06-14 04:07:21.621252
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1).map(lambda x: x + 1)
    assert task.fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 04:07:25.539636
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    assert task.fork(None, lambda arg: arg)() == 1

    after_fn_task = task.map(lambda arg: arg * 2)
    assert after_fn_task.fork(None, lambda arg: arg)() == 2

    def fn_with_zero_arguments(a, b, c):
        return 0

    after_fn_with_zero_arguments_task = task.map(fn_with_zero_arguments)
    assert after_fn_with_zero_arguments_task.fork(None, lambda arg: arg)() == 0



# Generated at 2022-06-14 04:07:29.691053
# Unit test for method bind of class Task
def test_Task_bind():
    def example_function(value):
        return Task.reject(value * 2)

    task = Task.of(100)
    result = task.bind(example_function)  # 200


# Generated at 2022-06-14 04:07:35.125428
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value * 2)
    res = Task.of(1)
    assert res.bind(mapper).fork(lambda a: False, lambda a: True) == True
    assert res.bind(mapper).fork(lambda a: False, lambda a: a) == 2


# Generated at 2022-06-14 04:07:39.654418
# Unit test for method map of class Task
def test_Task_map():
    executor = Executor()
    executor.add(
        Task.of(5).map(lambda x: x ** 2).fork,
        lambda y: assertEqual(y, 25)
    )
    executor.run()


# Generated at 2022-06-14 04:07:43.860903
# Unit test for method map of class Task
def test_Task_map():
    def func(x):
        return x + 1

    def call_fork(fork):
        return fork(lambda x: x, lambda x: x)

    assert call_fork(Task(lambda _, resolve: resolve(1)).map(func).fork) == 2


# Generated at 2022-06-14 04:07:52.172574
# Unit test for method map of class Task
def test_Task_map():
    # this is pretty bad test, because of asynchronous nature of Task
    # but it's just prototype
    def tp_fork(reject, resolve):
        resolve(2)
    tp_task = Task(tp_fork)

    def tp_map(value):
        assert value == 2
        return value ** 2

    tp_new_task = tp_task.map(tp_map)