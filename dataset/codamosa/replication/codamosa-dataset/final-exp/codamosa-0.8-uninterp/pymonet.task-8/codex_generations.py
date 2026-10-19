

# Generated at 2022-06-14 03:57:55.463505
# Unit test for method map of class Task
def test_Task_map():
    def sum(a, b): return a + b

    assert Task.of(1).map(sum).fork(lambda _: False, lambda value: value == (1 + 1))
    assert Task.of(1).map(lambda a, b: a + b).fork(lambda _: False, lambda value: value == (1 + 1))


# Generated at 2022-06-14 03:57:59.354176
# Unit test for method map of class Task
def test_Task_map():
    def test():
        def map_func(arg):
            return arg + 1

        task = Task(lambda reject, resolve: resolve(1))

        def fork_func(reject, resolve):
            return resolve(2)

        result = task.map(map_func)

        assert result.fork == fork_func, 'assertion error'

    test()


# Generated at 2022-06-14 03:58:04.115985
# Unit test for method map of class Task
def test_Task_map():
    def fn(arg):
        return arg * 2

    fork = lambda _, resolve: resolve(2)
    task = Task(fork)
    mapped_task = task.map(fn)
    assert fn(task.fork(None, None)) == mapped_task.fork(None, None)


# Generated at 2022-06-14 03:58:10.040225
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(lambda x: x, lambda x: x) == 2
    assert Task.of(1).map(lambda x: x).fork(lambda x: x, lambda x: x) == 1
    assert Task.of(1).map(lambda x: x + 1).map(lambda x: x * 2).fork(lambda x: x, lambda x: x) == 4
    assert Task.reject(1).map(lambda x: x + 1).fork(lambda x: x, lambda x: x) == 1

test_Task_map()


# Generated at 2022-06-14 03:58:13.407522
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task(lambda reject, resolve: resolve(5)).bind(lambda x: Task.reject(x + 5)).fork(
        lambda x: x + 1,
        lambda x: x + 1
    ) == 11


# Generated at 2022-06-14 03:58:25.797296
# Unit test for method bind of class Task
def test_Task_bind():
    # Method f1 should be called during fork of Task
    f1 = mock.MagicMock(return_value=2)
    t1 = Task.of(1).map(f1)
    assert t1.fork(lambda _: None, lambda _: None) == 2
    t2 = Task.of(1).map(f1).map(f1)
    assert t2.fork(lambda _: None, lambda _: None) == 4

    # Method f2 should be called during fork of Task
    f2 = mock.MagicMock(return_value=2)
    t2 = Task.of(1).bind(f2)
    assert t2.fork(lambda _: None, lambda _: None) == 2
    t3 = Task.of(1).bind(f2).bind(f2)

# Generated at 2022-06-14 03:58:39.256404
# Unit test for method bind of class Task
def test_Task_bind():
    """
    See if method bind works correctly
    """
    def f(x):
        return x * x

    def g(x):
        return x + 1

    def h(x):
        return Task.of(x)

    def t(x):
        return Task.reject(x)

    a = Task.of(1).map(f).bind(h).map(g)
    assert a.fork(lambda x: None, lambda x: x) == 4, "Test of Task.bind method failed"
    b = Task.of(1).map(f).bind(t).map(g)
    assert b.fork(lambda x: x, lambda x: None) == 1, "Test of Task.bind method failed"
    c = Task.reject(1).map(f).bind(h).map(g)
   

# Generated at 2022-06-14 03:58:45.303070
# Unit test for method map of class Task
def test_Task_map():
    def resolve(x):
        return x
    def reject(x):
        return x

    # test with reject
    task = Task(lambda reject, _: reject(42))
    assert task.map(lambda x: x + 1).fork(reject, resolve) == 42

    # test with resolve
    task = Task(lambda _, resolve: resolve(42))
    assert task.map(lambda x: x + 1).fork(reject, resolve) == 43



# Generated at 2022-06-14 03:58:49.425137
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(42)

    def fork_error(reject, resolve):
        reject('error')

    def bind(value):
        return Task.reject(value * 2)

    task = Task(fork)
    assert task.bind(bind).fork(lambda x: x, lambda x: x) == 84

    task_error = Task(fork_error)
    assert task_error.bind(bind).fork(lambda x: x, lambda x: x) == 'error'


# Generated at 2022-06-14 03:59:00.351932
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x * 2).fork(None, lambda value: value) == 2
    assert Task.of(1) \
        .map(lambda x: x + 7) \
        .map(lambda x: x + 5) \
        .fork(None, lambda value: value) == 13

    assert Task.reject(1).map(lambda x: x * 2).fork(lambda value: value, None) == 1
    assert Task.of(1) \
        .map(lambda x: x + 7) \
        .map(lambda x: x + 5) \
        .map(lambda x: x + 1) \
        .fork(lambda value: value, None) == 14


# Generated at 2022-06-14 03:59:16.776926
# Unit test for method map of class Task
def test_Task_map():
    from trampoline import trampoline
    test_object_1 = Task(lambda _, resolve: resolve(1))
    test_object_2 = Task(lambda _, resolve: resolve(1))
    test_object_3 = Task(lambda _, resolve: resolve(3))

    def custom_function(arg):
        return arg + 1

    assert trampoline(test_object_1.map(custom_function).fork(lambda _: 1, lambda _: 2)) == 2
    assert trampoline(test_object_2.map(custom_function).fork(lambda _: 1, lambda _: 2)) == 2
    assert trampoline(test_object_3.map(custom_function).fork(lambda _: 1, lambda _: 2)) == 2


# Generated at 2022-06-14 03:59:21.119318
# Unit test for method bind of class Task
def test_Task_bind():
    Task(lambda _, resolve: resolve(57)).bind(
        lambda arg: Task.of(arg + 10)
    ).fork(
        lambda arg: arg is None,
        lambda arg: arg == 67
    )


# Generated at 2022-06-14 03:59:26.140711
# Unit test for method map of class Task
def test_Task_map():
    f = lambda x: x + 1
    g = lambda x: x + 2
    value = 42
    task = Task.of(42).map(f).map(g)

    assert Task.of(42).map(f).map(g).fork(lambda err: err, lambda val: val) == f(g(value))


# Generated at 2022-06-14 03:59:28.573169
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(x):
        return Task.of(x * 2)

    assert Task.of(2).bind(fn).fork(None, lambda x: x) == 4


# Generated at 2022-06-14 03:59:32.049206
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    task = Task.of(1).map(add_one)
    assert task.fork(lambda value: value, lambda value: value) == 2

    assert Task.of(None).map(add_one).fork(lambda value: value, lambda value: value) is None


# Generated at 2022-06-14 03:59:34.841290
# Unit test for method map of class Task
def test_Task_map():
    """
    Test basic map method of class Task
    """
    result = Task.of(10)

    assert result.map(lambda x: x + 5).fork(None, lambda x: x) == 15


# Generated at 2022-06-14 03:59:40.874160
# Unit test for method bind of class Task
def test_Task_bind():
    wrapped_func = Task.of(1).bind(lambda v: Task.of(v + 1)).fork(
        lambda e: e,
        lambda v: v + 1)
    assert wrapped_func == 3


if __name__ == "__main__":
    import sys
    test_Task_bind()
    print("All test passed")

# Generated at 2022-06-14 03:59:43.528509
# Unit test for method map of class Task
def test_Task_map():
    a = Task.of(1).map(lambda x: x + 1)
    assert isinstance(a, Task)

    assert(Task.of(2).map(lambda x: x * 2).fork(lambda x: x, lambda x: x)) == 4


# Generated at 2022-06-14 03:59:53.756173
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper_reject(arg):
        return Task.reject(arg)

    def mapper_resolve(arg):
        return Task.of(arg)


# Generated at 2022-06-14 03:59:58.812144
# Unit test for method map of class Task

# Generated at 2022-06-14 04:00:16.103969
# Unit test for method bind of class Task
def test_Task_bind():
    def good(x): return Task.of(x + 1)
    def bad(x):
        if x == 0:
            return Task.reject(x)
        else:
            return Task.of(7 / (x - 1))

    def expect_resolve(value):
        assert value == 6

    def expect_reject(value):
        assert value == 0

    Task.of(5).bind(good).fork(expect_reject, expect_resolve)
    Task.of(6).bind(good).bind(bad).fork(expect_reject, expect_resolve)

    def expect_reject(value):
        assert value == 5

    Task.of(5).bind(bad).fork(expect_reject, expect_resolve)

# Generated at 2022-06-14 04:00:23.715309
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task.bind should call fork on result of argument and
    should return new Task with mapped value.
    """
    def fork(reject, resolve):
        resolve(3)

    def mapper(value):
        assert value == 3

        def resolve(value):
            assert value == 3  # mapped value
            return value

        def reject(value):
            assert value == 3  # rejected value
            return value

        return Task(lambda reject, resolve: resolve(value))

    task = Task(fork)
    result = task.bind(mapper)
    result.fork(mapper, mapper)



# Generated at 2022-06-14 04:00:28.087874
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('foo').map(lambda x: x.upper()).fork(
        lambda x: 'foo',
        lambda x: x
    ) == 'FOO'


# Generated at 2022-06-14 04:00:31.605821
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(2).map(operator.mul(2)).fork(
        lambda error: None,
        lambda result: result
    ) == 4

mock = MagicMock()


# Generated at 2022-06-14 04:00:39.326421
# Unit test for method map of class Task
def test_Task_map():
    @Task
    def divide(reject, resolve):
        if divisor == 0:
            reject(ZeroDivisionError("Division by zero"))
        else:
            resolve(dividend / divisor)

    dividend = 64
    divisor = 8

    r = Task.of(dividend) \
        .map(lambda v: divide(dividend, v)) \
        .map(lambda v: v.fork(lambda e: e.error, lambda v: v))

    assert r == 8



# Generated at 2022-06-14 04:00:43.478342
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(arg):
        res = arg + 1
        return Task.of(res)

    assert Task.of(1).bind(fn).fork(None, lambda res: res) == 2


# Generated at 2022-06-14 04:00:53.535903
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task(lambda reject, resolve: resolve(99))

    assert task.bind(lambda x: Task.of(x + 1)).fork(
        lambda x: f"reject {x}",
        lambda x: f"resolve {x}"
    ) == "resolve 100"

    assert task.bind(lambda x: Task.of(x + 1)).bind(lambda x: Task.of(x*x)).fork(
        lambda x: f"reject {x}",
        lambda x: f"resolve {x}"
    ) == "resolve 10100"


# Generated at 2022-06-14 04:01:02.122854
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task.
    """
    def map1(value):
        return Task.of('map1_result')

    def map2(value):
        return Task.of('map2_result')

    def error_reject(value):
        return Task.reject(value + '_error')

    def error_resolve(value):
        return Task.of(value + '_error')

    def first_task():
        return Task.of('value')

    assert first_task().bind(map1).fork(
        lambda value: value,
        lambda value: value
    ) == 'map1_result'

    assert first_task().map(map1).bind(map2).fork(
        lambda value: value,
        lambda value: value
    ) == 'map2_result'



# Generated at 2022-06-14 04:01:06.223060
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for class Task method map.
    """
    def mapper(value):
        return value + "!"

    def test_fork(_, resolve):
        resolve("hello")

    assert Task(test_fork).map(mapper).fork(lambda _: False, lambda result: result == "hello!")



# Generated at 2022-06-14 04:01:10.348753
# Unit test for method bind of class Task
def test_Task_bind():
    def result_task(value):
        return Task.of(value)

    def value_fn(value):
        return argument_value

    argument_value = 'some value'
    assert Task.of(argument_value).bind(result_task).fork(None, value_fn) == argument_value


# Generated at 2022-06-14 04:01:25.781739
# Unit test for method map of class Task
def test_Task_map():

    def resolve(value):
        return value + 10

    def reject(error):
        return error + ' error'

    def func(reject, resolve):
        return "text"

    fn = lambda arg: arg + "1"
    task = Task(func)
    changed_task = task.map(fn)
    assert(changed_task.fork(reject, resolve) == "text1")



# Generated at 2022-06-14 04:01:31.507562
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2)
    assert task.map(lambda x: x * 2).fork(None, lambda x: x) == 4
    assert task.map(lambda x: x / 0).fork(
        lambda e: e.args[0],
        None
    ) == ZeroDivisionError


# Generated at 2022-06-14 04:01:35.980973
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task class.
    """
    def mapper(value):
        return value * value


# Generated at 2022-06-14 04:01:39.410656
# Unit test for method map of class Task
def test_Task_map():
    def test(x):
        assert (x == 2)

    def resolve(x):
        test(x)

    Task.of(1).map(lambda x: x + 1).fork(None, resolve)


# Generated at 2022-06-14 04:01:48.219062
# Unit test for method bind of class Task
def test_Task_bind():
    def calculate_number(number):
        if number == 1:
            return Task.of(number)
        if number == 2:
            return Task.reject(number)

        return Task(
            lambda reject, resolve: resolve(number)
        )

    assert Task.bind(calculate_number(1), Task.of).fork(lambda x: 0, lambda x: x) == 1
    assert Task.bind(calculate_number(2), Task.of).fork(lambda x: x, lambda x: 0) == 2
    assert Task.bind(calculate_number(3), Task.of).fork(lambda x: 0, lambda x: x) == 3

# Generated at 2022-06-14 04:01:55.637124
# Unit test for method map of class Task

# Generated at 2022-06-14 04:02:06.569191
# Unit test for method map of class Task
def test_Task_map():
    real = Task(lambda _, resolve: resolve(42)).map(lambda x: x + 1)
    assert real.fork('reject', 'resolve') is 'resolve'

    real = Task(lambda _, resolve: resolve(42)).map(lambda x: x + 1)
    assert real.fork('reject', lambda: real.fork('reject', 'resolve')) is 'resolve'

    real = Task(lambda _, resolve: resolve(42)).map(lambda x: x + 1)
    assert real.fork('reject', lambda: real.fork('reject', lambda: real.fork('reject', 'resolve'))) is 'resolve'

    real = Task(lambda _, resolve: resolve(42)).map(lambda x: x + 1)

# Generated at 2022-06-14 04:02:11.070723
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        resolve(2)

    t = Task(fork)

    def square(x):
        return x ** 2

    assert t.map(square).fork(lambda x: x, lambda x: x) == 4


# Generated at 2022-06-14 04:02:14.726690
# Unit test for method map of class Task
def test_Task_map():
    def add10(x):
        return x + 10

    assert Task.of(2).map(add10).fork(
        lambda reject: None,
        lambda resolve: resolve
    ) == 12


# Generated at 2022-06-14 04:02:25.250285
# Unit test for method bind of class Task
def test_Task_bind():
    def fetch(url):
        def inner_reject(reject):
            return reject("Network Error")

        def inner_resolve(resolve):
            return resolve("Result from " + url)

        return Task(lambda reject, resolve: inner_resolve(resolve))

    def render(data):
        return Task(lambda reject, resolve: resolve("Rendered " + data))

    def render_error(data):
        return Task(lambda reject, resolve: reject("Rendered " + data))

    def parse_error(data):
        return Task(lambda reject, resolve: reject("Parsed " + data))

    def parse(data):
        return Task(lambda reject, resolve: resolve("Parsed " + data))


# Generated at 2022-06-14 04:02:49.285555
# Unit test for method bind of class Task
def test_Task_bind():
    value = Task.of(5)
    assert value.bind(
        lambda arg: Task.of(arg + 3)
    ).fork(
        lambda reject: reject(False),
        lambda resolve: resolve == 8
    )


# Generated at 2022-06-14 04:02:57.414912
# Unit test for method map of class Task
def test_Task_map():
    # test success case
    list_ = []
    task = Task.of(1).map(lambda x: x + 1)

    task.fork(
        lambda error: list_.append('rejected'),
        lambda success: list_.append('resolved')
    )

    assert list_ == ['resolved']

    # test failure case
    list_ = []
    task = Task.reject(1).map(lambda x: x + 1)

    task.fork(
        lambda error: list_.append('rejected'),
        lambda success: list_.append('resolved')
    )

    assert list_ == ['rejected']


# Generated at 2022-06-14 04:03:03.748812
# Unit test for method bind of class Task
def test_Task_bind():
    def test_fork(reject, resolve):
        return resolve(10)

    task = Task(test_fork)

    def test_plus_1(value):
        assert value == 10
        return Task.of(value + 1)

    plus_task = task.bind(test_plus_1)


# Generated at 2022-06-14 04:03:04.509993
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:03:06.799057
# Unit test for method map of class Task
def test_Task_map():
    def add(a):
        return a + 1

    assert Task.of(3).map(add).fork(lambda x: x, lambda x: x) == 4, "Task map method test failed"


# Generated at 2022-06-14 04:03:10.819515
# Unit test for method bind of class Task
def test_Task_bind():
    def a(value):
        return Task.reject(value)

    def b(value):
        return Task.of(value * 2)

    task_a = Task.of(5).bind(a)
    task_b = Task.of(5).bind(b)

    assert task_a.fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 5
    assert task_b.fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 10


# Generated at 2022-06-14 04:03:18.125126
# Unit test for method bind of class Task
def test_Task_bind():
    """
    This test call bind method of Task class with some mapper function,
    and check that this function transform input value by adding X string.
    """
    def identity(x):
        return x

    def add_x(value):
        return Task.of(value + "X")

    result = Task.of(1)
    assert result.bind(identity) == result
    assert result.bind(add_x).fork(identity, identity) == 2

# Testing
if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:03:31.049275
# Unit test for method bind of class Task
def test_Task_bind():
    """
    :returns: Unit test result
    :rtype: bool
    """
    is_called = 0
    fork_call_count = 0

    def fork_func(reject, resolve):
        nonlocal fork_call_count
        fork_call_count += 1
        resolve(is_called)

    def fork_func1(reject, resolve):
        resolve(is_called + 1)

    def fork_func2(reject, resolve):
        resolve(is_called + 2)

    task = Task(fork_func)
    result = task
    for i in range(10):
        result = result.bind(lambda x: Task(fork_func1))

    result = result.bind(lambda x: Task(fork_func2))


# Generated at 2022-06-14 04:03:39.452456
# Unit test for method map of class Task
def test_Task_map():
    class A: pass
    def fn(arg):
        assert isinstance(arg, A)
        return arg

    task = Task.of(A()).map(fn)
    assert isinstance(task.fork, FunctionType)
    assert task.fork(lambda arg: arg, lambda arg: arg).__class__ == A

    task = Task.of(A()).map(fn).map(fn).map(fn)
    assert isinstance(task.fork, FunctionType)
    assert task.fork(lambda arg: arg, lambda arg: arg).__class__ == A


# Generated at 2022-06-14 04:03:46.590893
# Unit test for method map of class Task
def test_Task_map():
    resolve = None
    reject = None

    def map_fn(value):
        return value * 2

    def fork_fn(reject_arg, resolve_arg):
        nonlocal resolve
        nonlocal reject

        resolve = resolve_arg
        reject = reject_arg

        return 42

    task = Task(fork_fn)

    next_task = task.map(map_fn)

    assert next_task.fork(None, None) == 42

    assert next_task.fork(reject, resolve) == 84


# Generated at 2022-06-14 04:04:33.794535
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        reject('error')

    def mapper(resolve):
        raise Exception('mapper error')

    task = Task(fork)
    assert task.bind(mapper).fork(lambda e: e, lambda v: v) == 'error'


# Generated at 2022-06-14 04:04:37.856868
# Unit test for method bind of class Task
def test_Task_bind():
    def check(result):
        assert result == 'mapped value'


# Generated at 2022-06-14 04:04:42.263216
# Unit test for method map of class Task
def test_Task_map():
    def add1(value):
        return value + 1

    task = Task.of(1)
    assert task.map(add1).fork(lambda reject: reject, lambda resolve: resolve) == 2


# Generated at 2022-06-14 04:04:47.777061
# Unit test for method bind of class Task
def test_Task_bind():

    def _():
        return Task.of('1') \
            .bind(lambda arg: Task.of(arg + '2')) \
            .bind(lambda arg: Task.of(arg + '3'))

    assert _().fork(lambda _: 'error', lambda value: value) == '123'


# Generated at 2022-06-14 04:04:52.602076
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(5)
    test_result = task.map(lambda x: x*x)

    assert test_result.fork(lambda arg: arg, lambda arg: arg) == 25
    assert type(test_result) == Task


# Generated at 2022-06-14 04:04:58.564485
# Unit test for method map of class Task
def test_Task_map():
    def hello_world_handler(e):
        print('Hello World!')

    def square_handler(x):
        return x * x

    def exception_handler(e):
        sys.exit(1)

    def fork(reject, resolve):
        return reject('test')

    Task(fork).map(square_handler).fork(hello_world_handler, exception_handler)


# Generated at 2022-06-14 04:05:03.593595
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method Task.map
    """
    def assert_equal(value, expected):
        assert value == expected, "Value %s is not equal to expected %s" % (value, expected)

    task = Task.of('value')
    result = task.map(lambda arg: arg + '_mapped').fork(lambda arg: arg, lambda arg: arg)
    assert_equal(result, "value_mapped")



# Generated at 2022-06-14 04:05:11.592423
# Unit test for method bind of class Task
def test_Task_bind():
    Task.of(2).map(lambda x: x + 5).bind(lambda x: Task.of(x * x)).fork(
        lambda x: print('Rejected: ', x),
        lambda x: print('Resolved: ', x)
    )

    Task.reject('Error').map(lambda x: x + 5).bind(lambda x: Task.of(x * x)).fork(
        lambda x: print('Rejected: ', x),
        lambda x: print('Resolved: ', x)
    )


# Generated at 2022-06-14 04:05:18.026080
# Unit test for method bind of class Task
def test_Task_bind():
    test_data = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test(a):
        assert a == next(test_data)
        return Task.of(a)
    Task.of(1).bind(test).fork(lambda _: None, lambda _: None)


# Generated at 2022-06-14 04:05:29.917992
# Unit test for method map of class Task
def test_Task_map():
    def resolve_check_fn(argument):
        assert argument == 2

    def reject_check_fn(argument):
        assert argument == 1

    function = Task.of(1).map(lambda x: x + 1).fork
    function(reject_check_fn, resolve_check_fn)

    function = Task.reject(1).map(lambda x: x + 1).fork
    function(reject_check_fn, reject_check_fn)

    function = Task(
        lambda reject, resolve: reject(1)
    ).map(lambda x: x + 1).fork
    function(reject_check_fn, reject_check_fn)

    function = Task(
        lambda reject, resolve: resolve(1)
    ).map(lambda x: x + 1).fork

# Generated at 2022-06-14 04:07:19.960802
# Unit test for method bind of class Task
def test_Task_bind():
    def task1_mapper(value):
        """
        take value from task1 and return result of this value.
        """
        return Task.of(value*value)

    def task2_mapper(value):
        """
        take value from task2 and return result of this value + 1.
        """
        return Task.of(value+1)

    def task_reject_mapper(value):
        """
        Take value from Task and return rejected Task with value * 2
        """
        return Task.reject(value * 2)

    def test_mapper(value):
        """
        Take value from Task and return value + 1
        """
        return value + 1

    task1 = Task.of(1)
    task2 = task1.bind(task1_mapper).bind(task2_mapper)


# Generated at 2022-06-14 04:07:23.970304
# Unit test for method map of class Task
def test_Task_map():
    from pytest import raises
    from . import _nil

    assert Task(_nil).map(_nil) is not None

    assert Task.of(10).map(lambda x: x + 10).fork(_nil, lambda x: x) == 20

    with raises(Exception) as excinfo:
        Task.reject(10).map(lambda x: x + 10).fork(_nil, _nil)

    assert str(excinfo.value) == '10'


# Generated at 2022-06-14 04:07:28.441443
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task(
        lambda reject, resolve: resolve('foo')
    ).bind(
        lambda value: Task(lambda reject, resolve: resolve(value + 'bar'))
    ) == Task(
        lambda reject, resolve: resolve('foobar')
    )


# Generated at 2022-06-14 04:07:33.224315
# Unit test for method bind of class Task
def test_Task_bind():
    def is_five(a):
        return Task((lambda reject, resolve: resolve(a == 5)))

    t = Task(lambda reject, resolve: resolve(5))
    assert t.bind(is_five).fork(lambda a: False, lambda a: True) == True

# Generated at 2022-06-14 04:07:43.199309
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task.

    :returns: OK or value of error
    :rtype: string
    """
    assert Task(lambda reject, resolve: resolve("Test")).bind(lambda _: Task.of("Test result"))\
        .fork(lambda _: None, lambda result: result) == "Test result"

    # Test for reject
    assert Task(lambda reject, resolve: reject("Test error"))\
        .bind(lambda _: Task.of("Test result"))\
        .fork(lambda result: result, lambda _: None) == "Test error"

    return "Ok"


# Generated at 2022-06-14 04:07:46.442299
# Unit test for method bind of class Task
def test_Task_bind():
    value = 1

    def mapper(value):
        return Task.of(value + 1)

    task = Task.of(value).bind(mapper)

    result = task.fork(lambda arg: arg, lambda arg: arg)

    assert result is value + 1


# Generated at 2022-06-14 04:07:58.160728
# Unit test for method bind of class Task
def test_Task_bind():
    def task_resolve():
        return Task.of("x")

    def task_reject():
        return Task.reject("y")

    def mapper_resolve(x):
        return Task.of("z")

    def mapper_reject(x):
        return Task.reject("z")

    result = task_resolve().bind(mapper_resolve)
    assert result.fork(lambda x: print(x), lambda x: "z") == "z"

    result = task_reject().bind(mapper_resolve)
    assert result.fork(lambda x: "y", lambda x: print(x)) == "y"
    
    result = task_reject().bind(mapper_reject)