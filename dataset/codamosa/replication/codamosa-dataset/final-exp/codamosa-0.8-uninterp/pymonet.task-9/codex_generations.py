

# Generated at 2022-06-14 03:58:04.600565
# Unit test for method bind of class Task
def test_Task_bind():
    yoyo = Task.of('yo yo')


# Generated at 2022-06-14 03:58:15.494667
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method.

    Should return rejected Task when parent Task is rejected.
    Should return resolved Task when parent Task is resolved.

    :return: None
    :rtype: None
    """
    def test_handler(done, value):
        assert value == 'abc'
        done()

    def test_handler_reject(done, value):
        assert value == 'abc'
        done()

    def task_reject(reject, _):
        reject('abc')

    def task_resolve(resolve, _):
        resolve('abc')

    def test_task(resolve, reject):
        return Task(task_resolve).bind(lambda value: Task(task_reject)).fork(reject, resolve)


# Generated at 2022-06-14 03:58:18.741338
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    assert Task.of(2).map(add_one).fork(None, lambda x: x) == 3



# Generated at 2022-06-14 03:58:30.847918
# Unit test for method bind of class Task
def test_Task_bind():
    t1 = Task.of(1)
    t2 = Task.of(2)
    t3 = Task.of(3)

    t4 = t1.bind(lambda v1: t2)
    assert t4.fork(lambda x: x, lambda x: x) == 2
    t5 = t2.bind(lambda v2: t3)
    assert t5.fork(lambda x: x, lambda x: x) == 3

    def sum_task(a, b, c):
        return Task.of(a + b + c)

    t6 = t1.bind(lambda x: t2.bind(lambda y: t3.map(lambda z: sum_task(x, y, z))))
    assert t6.fork(lambda x: x, lambda x: x) == 6


# Generated at 2022-06-14 03:58:43.200094
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test.
    """
    def inc(value):
        return value + 1

    def square(value):
        return value * value

    def toTask(value):
        return Task.of(value)

    def fork(reject, resolve):
        return resolve(939)


# Generated at 2022-06-14 03:58:46.664370
# Unit test for method map of class Task
def test_Task_map():
    """
    >>> Task.of(5).map(lambda value: value * 2).fork(
    ...     lambda arg: print("reject:" + str(arg)),
    ...     lambda arg: print("resolve:" + str(arg))
    ... )
    resolve:10
    """

    pass


# Generated at 2022-06-14 03:58:53.680388
# Unit test for method bind of class Task
def test_Task_bind():
    def create_task(value):
        def fork(_, resolve):
            return resolve(value)
        return Task(fork)

    param = 'hello'
    task = create_task(param)
    assert isinstance(task.bind(lambda x: create_task(x + ' world')), Task)
    assert task.fork(lambda x: x, lambda x: x + ' world') == param + ' world'


# Generated at 2022-06-14 03:59:04.401021
# Unit test for method map of class Task
def test_Task_map():
    # Create lambda for check `A` equals `B`
    eq = lambda a, b: a == b

    # Create helper function for check `Task` resolve attribute
    def resolve_check(task, expected):
        def result(resolve, _):
            return resolve(task(resolve, _)) == expected

        return Task(result)

    # Create helper function for check `Task` reject attribute
    def reject_check(task, expected):
        def result(_, reject):
            return reject(task(_, reject)) == expected

        return Task(result)

    # Create success tasks
    val = 1
    task1 = Task.of(val)
    task2 = Task((lambda _, resolve: resolve(val)))
    task3 = Task(lambda _, resolve: resolve(val + 2))


# Generated at 2022-06-14 03:59:15.064392
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """

    def identity(value):
        """
        Identity function.
        """
        return value

    def inc(number):
        """
        Increase number by 1.
        """
        return number + 1

    def task_of_number_plus1_and_times2(number):
        """
        Task with process of increase number by 1 and times 2.
        """
        return Task.of(number).bind(inc).map(lambda arg: arg * 2)

    def task_of_number_plus1(number):
        """
        Task with process of increase number by 1.
        """
        return Task.of(number).bind(inc)

    def task_of_number_times2(number):
        """
        Task with process of times number by 2.
        """

# Generated at 2022-06-14 03:59:26.839187
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Bind function to Task.

    Function bind used to extend list of behavior.
    It takes one function with 2 arguments (reject, resolve)
    and If this function resolved return task with resolved attribute
    otherwise reject attribute.
    """
    def resolve_number(number):
        return Task(lambda _, resolve: resolve(number))

    task = Task.of(2).bind(lambda number: resolve_number(number * 3))

    assert 6 == task.fork(
        lambda value: value,
        lambda value: value
    )

    assert 'ERROR' == task.fork(
        lambda value: 'ERROR',
        lambda value: value * 2
    )

    def resolve_error(value):
        return Task(lambda _, reject: reject(value))


# Generated at 2022-06-14 03:59:33.988939
# Unit test for method map of class Task
def test_Task_map():
    def check(reject, resolve):
        assert False, "Should not be reject"

    task = Task.of(1)
    task = task.map(lambda v: v + 10)
    assert task.fork(check, lambda v: v == 11)


# Generated at 2022-06-14 03:59:45.703240
# Unit test for method map of class Task
def test_Task_map():
    """ Unit test for method map of class Task. """
    t0 = Task.of(None)
    t1 = t0.map(lambda _: "value")

    assert_true(callable(t1.fork))
    assert_equal(t1.fork(None, None), None)

    t2 = Task.of("value")
    t3 = t2.map(lambda a: a + "1")

    assert_true(callable(t3.fork))
    assert_equal(t3.fork(None, None), "value1")

    t4 = Task.of("value")
    t5 = t4.map(lambda _: 1 / 0)

    assert_true(callable(t5.fork))
    assert_raises(ZeroDivisionError, t5.fork, None, None)

# Unit

# Generated at 2022-06-14 03:59:49.366745
# Unit test for method bind of class Task
def test_Task_bind():
    def add(a):
        return Task.of(a + a)

    task = Task.of(2).bind(add)

    assert task.fork(lambda _: False, lambda value: value == 4) is True


# Generated at 2022-06-14 03:59:55.700648
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + " hello "

    def mapper2(value):
        return value + " world"

    task = Task.of("hello").map(mapper).map(mapper2)

    def fork(reject, resolve):
        reject("hello")
        resolve("hello")

    task2 = Task(fork)

    assert task.fork(None, None) == "hello hello  world"
    assert task2.fork(lambda arg: arg, lambda arg: arg) == "hello"


# Generated at 2022-06-14 04:00:01.468389
# Unit test for method map of class Task
def test_Task_map():
    # Positive test (resolved)
    assert Task.of(42)\
        .map(lambda arg: arg + 1)\
        .fork(lambda value: None, lambda value: value) == 43

    # Positive test (rejected)
    assert Task.reject("oh no!")\
        .map(lambda arg: arg + 1)\
        .fork(lambda value: value, lambda value: None) == "oh no!"



# Generated at 2022-06-14 04:00:05.074686
# Unit test for method map of class Task
def test_Task_map():
    """
    Test method map Task class
    """
    def fork(reject, resolve):
        resolve(5)

    def mapper(value):
        return value * 2

    task = Task(fork)
    task = task.map(mapper)
    assert task.fork(None, None) == 10


# Generated at 2022-06-14 04:00:14.489036
# Unit test for method bind of class Task
def test_Task_bind():
    task1 = Task.of(1)
    task2 = Task.of(2)
    task3 = Task.of(3)

    def plus(a):
        def plus_x(b):
            return Task.of(a + b)
        return plus_x

    result = task1.bind(plus(task2.fork(lambda _: _, lambda __: __))).fork()
    assert result == 3

    result = task1.map(plus(task2.fork(lambda _: _, lambda __: __))).fork()
    assert result == Task(plus(task2.fork(lambda _: _, lambda __: __))(1))

# Generated at 2022-06-14 04:00:24.455416
# Unit test for method bind of class Task
def test_Task_bind():
    """ Test method bind of class Task
    """
    def reject(value):
        return value

    def resolve(value):
        return value

    def mapped_value(value):
        return value * 2

    def fork(reject, resolve):
        return resolve(3)

    def fork_with_error(reject, resolve):
        return reject(3)

    assert Task(fork).bind(lambda arg: Task.of(mapped_value(arg)))\
        .fork(reject, resolve) == mapped_value(3)
    assert Task(fork).bind(lambda arg: Task.reject(mapped_value(arg)))\
        .fork(resolve, reject) == mapped_value(3)
    assert Task(fork_with_error).bind(lambda arg: Task.of(mapped_value(arg)))\
       

# Generated at 2022-06-14 04:00:30.538821
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).bind(lambda x: Task.of(x * x)).fork(
        lambda x: x,
        lambda x: x
    ) == 4

    assert Task.of(2).bind(lambda x: Task.reject(x)).fork(
        lambda x: x,
        lambda x: x
    ) == 2

# Generated at 2022-06-14 04:00:41.159668
# Unit test for method bind of class Task
def test_Task_bind():
    def test_Task(resolve, reject):
        return Task(lambda _, resolve: resolve(1))

    def first_map(arg):
        return Task(lambda _, resolve: resolve(arg + 1))

    def second_map(arg):
        return Task(lambda _, resolve: resolve(arg + 1))

    def third_map(arg):
        return Task(lambda _, resolve: resolve(arg + 1))

    def test_resolve(arg):
        print(arg)

    def test_error(arg):
        print(arg)

    task = test_Task(first_map, test_error)
    task = task.bind(first_map)
    task = task.bind(second_map)
    task = task.bind(third_map)
    task.fork(test_error, test_resolve)


# Generated at 2022-06-14 04:00:54.324607
# Unit test for method bind of class Task
def test_Task_bind():
    stub_resolve1 = StubFunction()
    stub_resolve2 = StubFunction()
    stub_fork = StubFunction(lambda reject, resolve: resolve(1))

    task = Task(stub_fork)
    mapper = Task.of(lambda x: x + 1)
    binded = task.bind(mapper.map)

    binded.fork(stub_resolve1, stub_resolve2)

    assert stub_resolve1.calls_count == 0
    assert stub_resolve2.calls_count == 1
    assert stub_resolve2.last_args[0] == 2
    assert stub_fork.calls_count == 1


# Generated at 2022-06-14 04:01:01.853687
# Unit test for method map of class Task
def test_Task_map():
    """
    Call and check method map of class Task.
    """
    # Define test functions
    def test_map(reject, resolve):
        resolve(1)

    def test_add(value):
        return value + 1

    def test_result(reject, resolve):
        resolve(2)

    # Call and check map function
    test_task = Task(test_map)
    test_task_mapped = test_task.map(test_add)
    assert test_task_mapped.fork(
        lambda arg: arg,
        lambda arg: arg
    ) == test_task_mapped.fork(
            lambda arg: arg,
            lambda arg: arg
        )



# Generated at 2022-06-14 04:01:07.706057
# Unit test for method bind of class Task
def test_Task_bind():
    def a(x):
        return Task.of(x + 10)

    def b(x):
        return Task.of(x + 20)

    def c(x):
        return Task.of(x + 30)

    assert Task.of(5).bind(a).bind(b).bind(c).fork(lambda _: 1, lambda x: x) == 65


# Generated at 2022-06-14 04:01:11.238872
# Unit test for method bind of class Task
def test_Task_bind():
    def test_case(arg):
        def make_task(value):
            return Task.of(value)

        return Task.of(arg).bind(make_task)

    task = test_case.fork(lambda _: print("assertionError"), lambda _: print("ok"))

# Generated at 2022-06-14 04:01:13.589848
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of('Hello')
    task = task.bind(lambda arg: Task.of(arg + ', World!'))
    assert task.fork(lambda arg: arg, lambda arg: arg) == 'Hello, World!'


# Generated at 2022-06-14 04:01:16.728709
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda val: Task.of(val + 1)).fork(identity, identity) == 2
    assert Task.of(1).bind(lambda val: Task.reject(val + 1)).fork(identity, identity) == 2

# Generated at 2022-06-14 04:01:23.190461
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind method of class Task.
    """
    def test_task():
        """
        Pass task which need to test.
        """
        return Task(lambda reject, resolve: resolve('test'))

    assert Task(
        lambda reject, resolve: test_task().bind(lambda val: Task.of(val + '_')).fork(reject, resolve)
    ).fork(lambda err: None, lambda value: value) == 'test_'


# Generated at 2022-06-14 04:01:33.116636
# Unit test for method bind of class Task
def test_Task_bind():
    """Unit test for method bind of class A"""
    def fail(resolve, reject):
        reject(1)

    def success(resolve, reject):
        resolve(2)

    def success_bind(value):
        return Task.of(value + 1)

    def fail_bind(value):
        return Task.reject(value * 3)

    assert Task(success).bind(success_bind).fork(
        lambda value: 3,
        lambda value: 4
    ) == 4

    assert Task(success).bind(fail_bind).fork(
        lambda value: 5,
        lambda value: 6
    ) == 5

    assert Task(fail).bind(success_bind).fork(
        lambda value: 7,
        lambda value: 8
    ) == 7


# Generated at 2022-06-14 04:01:36.250642
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    task = Task.of(lambda x, y: x * y)
    assert task.bind(lambda fn: Task.of(fn(1, 2))).fork(None, None) == 2


# Generated at 2022-06-14 04:01:46.983186
# Unit test for method bind of class Task
def test_Task_bind():

    # Task with resolve value 42
    t1 = Task.of(42)

    # Task with reject value 42
    t2 = Task.reject(42)

    # Task with resolve value 43
    t3 = Task.of(43)

    # Task with reject value 43
    t4 = Task.reject(43)

    # Task.bind with of
    # In this case we return t3 (see bind_test function)
    # and in t3 we have value 43, that send to resolve function
    t5 = t1.bind(bind_test)

    # Task.bind with reject
    # In this case we return t4 (see bind_test function)
    # and in t4 we have value 43, that send to reject function
    t6 = t1.bind(reject_test)

    # Task.bind with of


# Generated at 2022-06-14 04:01:56.600998
# Unit test for method map of class Task
def test_Task_map():
    """
    Execute function Task.map().

    :return: None
    """
    def fn(value):
        return value + 2

    task = Task.of(2).map(fn)

    assert task.fork(None, lambda value: value) == 4



# Generated at 2022-06-14 04:02:01.206439
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(10).map(lambda x: x * 10).fork(lambda _: False, lambda x: x == 100)
    assert Task.of(10).map(lambda x: x * 10).fork(lambda _: True, lambda x: x == 0)


# Generated at 2022-06-14 04:02:13.554370
# Unit test for method map of class Task
def test_Task_map():
    # Should be 10
    print(Task.of(5).map(lambda x: x * 2).fork(
        lambda err: print("Err"),
        lambda val: print(val)
    ))

    # Should be None
    def fn(value):
        print("Err from fn")

    def fn2(value):
        print("Err from fn2")

    print(Task.reject("Error").map(fn2).fork(
        lambda err: print("Err"),
        lambda val: print(val)
    ))

    # Should be 10
    Task.reject("Error").map(fn).fork(
        lambda err: print("Err"),
        lambda val: print(val)
    )

    # Should be 15

# Generated at 2022-06-14 04:02:19.644744
# Unit test for method map of class Task
def test_Task_map():
    def fork(_, resolve):
        resolve('value')

    task = Task(fork)
    result = task.map(lambda value: value + '1').fork(lambda reject: None, lambda resolve: resolve)
    assert result == 'value1'

    result = task.map(lambda value: value[1:2]).fork(lambda reject: None, lambda resolve: resolve)
    assert result == 'a'


# Generated at 2022-06-14 04:02:25.017396
# Unit test for method bind of class Task
def test_Task_bind():
    def add(value):
        return value + 2

    def sub(value):
        return value - 2

    def mul(value):
        return value * 2

    assert(
        Task.of(2).bind(lambda arg: Task.of(add(arg))).bind(lambda arg: Task.of(sub(arg))).bind(lambda arg: Task.reject(mul(arg))).fork(lambda arg: arg, lambda _: None) == 8
    )



# Generated at 2022-06-14 04:02:36.237070
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method.
    """

# Generated at 2022-06-14 04:02:41.987516
# Unit test for method map of class Task
def test_Task_map():
    def test_result(value):
        return Task.of(value + 1)

    def mapper(value):
        return value + 1

    fork = Task.of(1).map(mapper).fork
    assert fork(assert_fail, assert_equal(2))

    fork = test_result(1).map(mapper).fork
    assert fork(assert_fail, assert_equal(3))
    assert_ok()


# Generated at 2022-06-14 04:02:46.209960
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(x):
        return Task.of(x + 1)

    def fork(reject, resolve):
        resolve(1)

    task = Task(fork)
    new_task = task.bind(fn)

# Generated at 2022-06-14 04:02:56.619618
# Unit test for method map of class Task
def test_Task_map():
    def test(x):
        return Task(lambda _, resolve: resolve(x))

    def add(x):
        return x + 1

    def test_fn(x):
        return Task(lambda _, resolve: resolve(x))

    def test_fn_error(x):
        return Task(lambda reject, _: reject(x))


# Generated at 2022-06-14 04:03:03.890623
# Unit test for method map of class Task
def test_Task_map():
    # methods map and of
    assert Task.of(1).map(lambda x: x + 1).fork(None, lambda v: v) == 2
    assert Task.of(1).map(lambda x: x + 1).map(lambda x: x + 1).fork(None, lambda v: v) == 3

    # methods map and reject
    assert Task.reject(1).map(lambda x: x + 1).fork(lambda v: v, None) == 1


# Generated at 2022-06-14 04:03:14.775073
# Unit test for method bind of class Task
def test_Task_bind():
    call = []
    # Create task with side effect in resolved promise
    def side_effect():
        call.append(1)
        return Task.of(1)

    # Setup new Task with mapper
    task = Task.of(1) \
        .bind(lambda _: Task.of(None)) \
        .bind(side_effect) \
        .bind(lambda _: Task.of(None))

    task.fork(None, lambda _: call.append(2))  # Call task
    assert call == [1, 2], "Should be [1, 2] but got {}".format(call)

# Generated at 2022-06-14 04:03:18.391749
# Unit test for method map of class Task
def test_Task_map():
    value = 1
    called = False

    def called_mapper(_):
        nonlocal called
        called = True

    task = Task.of(value).map(called_mapper)
    task.fork(lambda _: None, lambda _: None)

    assert called



# Generated at 2022-06-14 04:03:23.786295
# Unit test for method map of class Task
def test_Task_map():
    def fn(value):
        return value + 10

    task = Task.of(10).map(fn)
    _, result = task.fork(lambda _: 'reject', lambda _: 'resolve')

    assert result(100) == 110



# Generated at 2022-06-14 04:03:32.774779
# Unit test for method map of class Task
def test_Task_map():
    value = 2

    def add(arg):
        return arg + 1

    def sub(arg):
        return arg - 1

    def mul(arg):
        return arg * 2

    assert Task.of(value).map(add).fork(lambda _: 'error', lambda arg: arg) == 3
    assert Task.of(value).map(add).map(sub).fork(lambda _: 'error', lambda arg: arg) == 2
    assert Task.of(value).map(add).map(mul).fork(lambda _: 'error', lambda arg: arg) == 6
    assert Task.of(value).map(mul).map(add).fork(lambda _: 'error', lambda arg: arg) == 5


# Generated at 2022-06-14 04:03:38.288396
# Unit test for method map of class Task
def test_Task_map():
    def get_value(arg):
        return arg ** 2

    def task_fork(reject, resolve):
        return resolve(3)

    def map_fork(reject, resolve):
        return resolve(9)

    task = Task(task_fork)

    assert task.map(get_value).fork(None, None) == map_fork(None, None)



# Generated at 2022-06-14 04:03:42.046073
# Unit test for method map of class Task
def test_Task_map():
    def test(value):
        return Task.of(value + 1)

    Task.of(1).map(lambda x: x + 1).fork(
        lambda arg: print("reject"),
        lambda arg: print(arg)
    )

# Generated at 2022-06-14 04:03:49.838072
# Unit test for method bind of class Task
def test_Task_bind():
    # Test success of TaskMap
    assert Task.of(1).bind(lambda arg: Task.of(arg+1)).fork(lambda _: None, lambda arg: arg) == 2

    # Test rejection of TaskMap
    def test_rejection(value):
        return Task.reject(value).bind(lambda _: Task.of(None)).fork(lambda arg: arg, lambda _: None)

    assert test_rejection(1) == 1
    assert test_rejection(None) == None
    assert test_rejection(Task) == Task
    assert test_rejection("test") == "test"


# Generated at 2022-06-14 04:03:54.182366
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Run unit test for Task.bind method.
    """
    def my_bind_function(value):
        return Task.of(value - 2)

    my_value = Task.of(1).bind(my_bind_function).fork(
        lambda reject: "reject",
        lambda resolve: resolve
    )

    assert my_value == -1



# Generated at 2022-06-14 04:04:04.705133
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        reject('error')
        resolve('ok')

    class Call:
        def __init__(self):
            self.args = []

        def __call__(self, *args, **kwargs):
            self.args.append(args)

    call_functor_fork = Call()

    task = Task(fork)
    functor_fork = task.map(call_functor_fork)

    functor_fork('ok', 'ok')

    assert(fork.__name__ == functor_fork.fork.__name__)
    assert(len(call_functor_fork.args) == 1)
    assert(call_functor_fork.args[0] == ('ok',))


# Generated at 2022-06-14 04:04:11.353035
# Unit test for method bind of class Task
def test_Task_bind():

    def twice(x):
        return x + x

    def toTask(x):
        return Task.of(x)

    value = [1, 2, 3, 4, 5]
    t = Task.of(value)
    assert t.bind(twice) == t.map(twice)
    assert t.bind(toTask) == t


# Generated at 2022-06-14 04:04:23.886474
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Use case: Task mapper with Task result
    """
    def mapper_return_task(arg):
        """
        Mapper return Task
        """
        return Task.of(arg + 5)

    initial_task = Task.of(10)


# Generated at 2022-06-14 04:04:34.189201
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task[A + B] = Task[A].bind(Task[B])
    """
    def f():
        return Task.of(2)

    def g():
        return Task.of(3)

    def test(x):
        return Task.of(5)

    def test_fail(x):
        return Task.reject(5)

    assert Task.of(1).bind(f).bind(g).fork(None, test)
    assert not Task.of(1).bind(f).bind(g).fork(test_fail, None)

# Generated at 2022-06-14 04:04:37.182571
# Unit test for method bind of class Task
def test_Task_bind():
    def add(value):
        return Task.of(value + 2)

    assert Task.of(2).bind(add).fork(None, lambda val: val) == 4


# Generated at 2022-06-14 04:04:42.610937
# Unit test for method map of class Task
def test_Task_map():
    def double(x):
        return x * 2

    def reject(v):
        return v

    def resolve(v):
        return v

    task = Task(lambda reject, resolve: resolve(2))
    assert task.map(double).fork(reject, resolve) == 4



# Generated at 2022-06-14 04:04:50.217941
# Unit test for method map of class Task
def test_Task_map():
    def result_resolved(arg):
        assert arg == 2

    def result_rejected(arg):
        assert arg == 1

    task = Task(lambda reject, resolve: resolve(1))
    task.map(lambda x: x + 1).fork(
        result_rejected,
        result_resolved
    )

    Task.of(1).map(lambda x: x + 1).fork(
        result_rejected,
        result_resolved
    )
# End of unit test for method map of class Task


# Generated at 2022-06-14 04:04:55.097935
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(5)
    task2 = task.map(lambda x: x * 2)
    task2.fork(
        lambda x: print("rejected: ", x),
        lambda x: print("resolved: ", x)
    )


# Generated at 2022-06-14 04:04:58.730698
# Unit test for method bind of class Task
def test_Task_bind():
    @Task.of(1)
    def fn(x): return x + 1

    assert fn.bind(lambda x: Task.of(x + 2)).fork(lambda x: x, lambda x: x) == 4



# Generated at 2022-06-14 04:05:05.828862
# Unit test for method map of class Task
def test_Task_map():
    def add(a):
        return a + 2

    def mul(a):
        return a * 2

    # Successful execution
    assert Task.of(2).map(add).fork(lambda _: None, lambda arg: arg) == 4

    # Successful execution
    assert(Task.of(2)
           .map(add)
           .map(mul)
           .fork(lambda _: None, lambda arg: arg)
           ) == 8

    # Reject execution
    var = [0]

    def reject(a):
        var[0] = a

    assert Task.reject(2).map(add).fork(reject, lambda _: None) == 2



# Generated at 2022-06-14 04:05:10.133342
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    foo = Task.reject(42)
    bar = foo.bind(lambda x: Task.of(x + 1))
    assert bar.fork(lambda x: print(x), lambda x: print(x)) == 43


# Generated at 2022-06-14 04:05:15.687820
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).map(lambda x: x * 2).bind(lambda x: Task.of(x + 3)).fork(
        lambda x: x * 2,
        lambda x: x / 2
    ) == 7

    assert Task.of(2).bind(
        lambda x: Task.reject('ERROR') if x == 2 else Task.of(x**2)
    ).fork(
        lambda x: x[-1].lower(),
        lambda x: x / 2
    ) == 'r'


# Generated at 2022-06-14 04:05:28.213113
# Unit test for method map of class Task
def test_Task_map():
    pass

# Generated at 2022-06-14 04:05:31.024385
# Unit test for method map of class Task
def test_Task_map():
    result = Task.of(1).map(lambda num: num * 2)
    assert result.fork(lambda err: None, lambda data: data) == 2


# Generated at 2022-06-14 04:05:36.219071
# Unit test for method bind of class Task
def test_Task_bind():
    def task_fork(reject, resolve):
        return resolve(5)

    task = Task(task_fork)

    new_task = task.bind(
        lambda x: Task.of(x + 3)
    )

    assert new_task.fork(lambda x: x, lambda x: x) == 8

# Generated at 2022-06-14 04:05:43.002078
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(resolve):
        return lambda arg: resolve(arg)

    def reject(reject):
        return lambda arg: reject(arg)

    def fork(fork):
        return lambda reject, resolve: fork(reject)(resolve)

    def bind(fn):
        return lambda task: Task(lambda reject, resolve: task.fork(reject, lambda value: fn(value).fork(reject, resolve)))

    def bind_check(fn):
        return lambda task: Task(lambda reject, resolve:
            fork(task)(
                reject,
                lambda value: fork(fn(value))(reject, resolve)
            )
        )

    reject_check = lambda value: Task(lambda reject, resolve: reject(value))
    resolve_check = lambda value: Task(lambda reject, resolve: resolve(value))


# Generated at 2022-06-14 04:05:52.036962
# Unit test for method map of class Task
def test_Task_map():
    A, B, C = 1, 2, 3

    t = Task.of(A)

    assert t.map(lambda arg: arg).fork(lambda _: None, lambda arg: None) == A
    assert t.map(lambda arg: None).fork(lambda _: None, lambda arg: None) is None
    assert t.map(lambda arg: B).fork(lambda _: None, lambda arg: None) == B
    assert t.map(lambda arg: C).fork(lambda _: None, lambda arg: None) == C


# Generated at 2022-06-14 04:05:55.522530
# Unit test for method bind of class Task
def test_Task_bind():
    def bind_func(v):
        return Task.of(v + 1)

    task = Task.of(1).bind(bind_func)

    assert task.fork(lambda _: _, lambda v: v) == 2



# Generated at 2022-06-14 04:05:58.766602
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(str).map(lambda x: x + '2').fork == '12'


# Generated at 2022-06-14 04:06:02.600957
# Unit test for method map of class Task
def test_Task_map():
    def test_Task_map():
        def add(value):
            return value + 1

        return Task.reject(2).map(add).fork(
            lambda value: value == 2,
            lambda value: False
        )

    assert test_Task_map()


# Generated at 2022-06-14 04:06:10.189244
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    assert isinstance(task.map(lambda x: x + 1), Task)
    assert isinstance(task.map(lambda x: x + 1).map(lambda x: x * 2), Task)
    assert task.map(lambda x: x + 1).fork(lambda x: x, lambda x: x) == 2
    assert task.map(lambda x: x + 2).fork(lambda x: x, lambda x: x) == 3


# Generated at 2022-06-14 04:06:15.738303
# Unit test for method bind of class Task
def test_Task_bind():
    def test_func(arg):
        return Task.of(arg + 1)

    def run(arg):
        return (
            Task.of(arg)
            .bind(test_func)
            .map(lambda val: val / 10)
            .fork(lambda val: None, lambda val: val)
        )

    assert run(1) == 0.2
    assert run(2) == 0.3
    assert run(5) == 0.6


# Generated at 2022-06-14 04:06:43.342704
# Unit test for method bind of class Task
def test_Task_bind():
    # Define Task for test
    def do_something():
        return Task.of("do something")

    def do_something_else(value):
        return Task.of(value + " and do something else")

    def do_nothing():
        return Task.of(None)

    def do_all(value):
        return (
            do_something()
            .bind(lambda res: do_something_else(res))
            .bind(lambda res: do_nothing())
        )

    def test():
        return do_all('test')

    # Run test
    def on_resolve(msg):
        assert msg == "do something and do something else"

    def on_reject(msg):
        assert False, msg

    test().fork(on_reject, on_resolve)


# Generated at 2022-06-14 04:06:56.771056
# Unit test for method bind of class Task
def test_Task_bind():
    def concat_foo(arg):
        return Task.of(arg + "foo")

    def concat_bar(arg):
        return Task.of(arg + "bar")

    def reject(arg):
        return Task.reject(arg)

    assert Task.of(1).bind(lambda _: Task.of(2)).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 2

    assert Task.of(1).bind(lambda _: Task.reject(2)).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 2

    assert Task.reject(1).bind(lambda _: Task.of(2)).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 1


# Generated at 2022-06-14 04:07:00.740847
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1).map(lambda x: x + 1)
    assert task.fork(lambda x: None, lambda x: x) == 2


# Generated at 2022-06-14 04:07:14.652641
# Unit test for method bind of class Task
def test_Task_bind():
    def _test(test):
        return Task.of(test)

    def _test2(test):
        return Task.of((test + '!!!', test * 2))

    task = Task.of('HELLO')
    task = task.bind(_test)

    assert task.fork(lambda a: a, lambda a: a) == 'HELLO'

    task = task.bind(_test)

    assert task.fork(lambda a: a, lambda a: a) == 'HELLO'

    task = Task.of('HELLO')
    task = task.bind(_test)
    task = task.bind(_test)
    task = task.bind(_test2)

    assert task.fork(lambda a: a, lambda a: a) == ('HELLO!!!', 'HELLOHELLO')


# Generated at 2022-06-14 04:07:21.903247
# Unit test for method bind of class Task
def test_Task_bind():
    def resolver(a, b):
        return Task.of(a + b)

    def mapper(a):
        return Task.of(a * 2)

    t = Task((lambda r, s: resolver(1, 2).fork(r, s)))
    t2 = Task((lambda r, s: t.bind(mapper).fork(r, s)))

    assert t2.fork(lambda a: a, lambda a: a) == 6

# Generated at 2022-06-14 04:07:26.825275
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 1

    task = Task.of(20)
    new_task = task.map(mapper)
    assert new_task.fork(
        lambda value: False,
        lambda value: True if value == 21 else False
    )


# Generated at 2022-06-14 04:07:29.691662
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task.
    """
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(None, lambda x: x) == 2


# Generated at 2022-06-14 04:07:36.849724
# Unit test for method bind of class Task
def test_Task_bind():
    def id(value):
        return value
    def inc(value):
        return value + 1.0

    assert Task.of(0).bind(inc).fork(id, inc) == 1
    assert Task.of(1).bind(inc).fork(id, inc) == 2
    assert Task.of(0).bind(inc).bind(inc).fork(id, inc) == 2


# Generated at 2022-06-14 04:07:46.804815
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(a):
        if a > 3:
            return Task.reject(a)
        return Task.of(a)

    # Test that function passed to a method bind, returns a
    # function which returns Task when called
    sut = Task.of(1).bind(mapper)
    assert callable(sut)
    assert callable(sut.fork)

    test_result = None

    def test_resolve(result):
        nonlocal test_result
        test_result = result

    def test_reject(error):
        test_result = error

    sut.fork(test_reject, test_resolve)

    # Test that argument of reject function of bind function is a
    # argument of reject function of passed in function
    sut = Task.of(100).bind(mapper)


# Generated at 2022-06-14 04:07:58.384766
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method Task class.
    """
    def assert_task(task):
        """
        Test task for expected values of resolved task.
        :param task: some Task
        """
        assert task.fork(lambda x: 'reject', lambda x: 'resolve') == 'resolve'

    # Test for value
    assert_task(Task.of(123).map(lambda x: x + 10))

    # Test for function
    assert_task(Task.of(123).map(lambda x: lambda y: x + y).map(lambda f: f(10)))

    # Test for Task
    assert_task(Task.of(123).map(lambda x: Task.of(x + 10)))

    # Test for Promise