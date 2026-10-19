

# Generated at 2022-06-14 03:57:56.078300
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task.map function.
    """
    def resolve(value):
        "Function for resolve value"
        assert value == 3
        return value
    def reject(value):
        "Function for resolve error"
        assert False

    def add(value):
        "Function for mapping"
        return value + 1

    Task(lambda reject, resolve: resolve(2)).map(add).fork(reject, resolve)


# Generated at 2022-06-14 03:57:58.020844
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)
    mapper = lambda value: Task.of(value + 1)
    result = task.bind(mapper)

    def assert_fn(*args):
        assert args == (2, )

    result.fork(lambda value: assert_fn(value))



# Generated at 2022-06-14 03:58:00.774298
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(2) \
        .map(lambda x: x + 1) \
        .fork(None, lambda result: result == 3) == True


# Generated at 2022-06-14 03:58:04.598418
# Unit test for method bind of class Task
def test_Task_bind():
    def method(_):
        return Task.of(True)

    instance = Task.of(5)
    result = instance.bind(method)
    assert result.fork(lambda _: False, lambda _: True)


# Generated at 2022-06-14 03:58:10.491403
# Unit test for method bind of class Task
def test_Task_bind():
    def f(n):
        return Task.of(n*10)

    result = Task.of(1)\
        .bind(f)\
        .fork(
            lambda reason: print('reject'), 
            lambda result: print('result', result)
        )

    assert result == 'result 10'


# Generated at 2022-06-14 03:58:21.779597
# Unit test for method map of class Task
def test_Task_map():

    def add_one(value):
        return value + 1

    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def throw_error():
        raise ValueError(1)

    def add_one_if_even(number):
        if number % 2:
            return number
        return number + 1

    def square_if_odd(number):
        if number % 2:
            return number ** 2
        return number

    def task_of_one():
        return Task.of(1)

    def task_of_two():
        return Task.of(2)

    def task_of_three():
        return Task.of(3)

    def task_of_zero():
        return Task.of(0)


# Generated at 2022-06-14 03:58:25.869033
# Unit test for method map of class Task
def test_Task_map():
    def map_fn(value):
        return value + 1

    assert Task.of(1).map(map_fn) == Task(lambda _, resolve: resolve(2))
    assert Task.reject(1).map(map_fn) == Task(lambda reject, _: reject(1))


# Generated at 2022-06-14 03:58:38.357224
# Unit test for method bind of class Task
def test_Task_bind():
    def get_data():
        import time
        time.sleep(0.5)
        return 1

    def local_task_reject_int(value):
        return Task.reject(value)

    def local_task_resolve_int(value):
        return Task.of(value)

    def add_one(value):
        return value + 1

    assert Task.reject(1).bind(local_task_resolve_int).fork(lambda x: x, lambda x: x) == 1

    assert Task.of(1).bind(local_task_reject_int).fork(lambda x: x, lambda x: x) == 1

    assert Task.reject(1).bind(local_task_reject_int).fork(lambda x: x, lambda x: x) == 1


# Generated at 2022-06-14 03:58:42.332800
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve('task_result')

    def mapper(value):
        def fork(reject, resolve):
            resolve(value)

        return Task(fork)

    task = Task(fork)
    assert (task.bind(mapper).fork(lambda _: None, lambda arg: arg)) == 'task_result'



# Generated at 2022-06-14 03:58:47.438515
# Unit test for method bind of class Task
def test_Task_bind():
    import random

    def generate_random_number():
        return Task.of(random.randint(0, 100))

    task = Task.of(1) \
        .bind(lambda x: Task.of(x + 1)) \
        .bind(lambda x: Task.of(x + 2)) \
        .bind(lambda x: Task.of(x + 3)) \
        .bind(lambda x: generate_random_number())

    assert task.fork(None, lambda x: x) > 1

# Generated at 2022-06-14 03:59:02.139586
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    # Test success result
    def success_mapper(arg):
        """
        Mapper function (success argument)

        :param arg: value to map
        :type arg: A
        :returns: Task with reject, resolve attributes
        :rtype: Task[Function reject, Function resolve]
        """
        return Task.of(arg + 1)

    # Test error result
    def error_mapper(arg):
        """
        Mapper function (reject argument)

        :param arg: value to map
        :type arg: A
        :returns: Task with reject, resolve attributes
        :rtype: Task[Function reject, Function resolve]
        """
        return Task.reject(arg)

    # Test unit
    task_reject = Task.reject

# Generated at 2022-06-14 03:59:10.853629
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(_):
        raise Exception('Reject task called')

    def resolve(result):
        assert result == 'tested'
        print('All test passed.')

    def task_1():
        return Task(lambda reject, resolve: resolve('tested'))

    def task_2():
        return Task(lambda reject, resolve: reject('test rejected'))

    def task_3(arg):
        print(arg)
        return Task(lambda reject, resolve: resolve('tested'))

    task = Task(lambda reject, resolve: resolve(1)).bind(task_3)
    task.fork(reject, resolve)


# Generated at 2022-06-14 03:59:15.247808
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda _: 2).fork(
        lambda _: False,
        lambda _: True
    )

    assert Task.reject(1).map(lambda _: 2).fork(
        lambda arg: arg == 1,
        lambda _: False
    )


# Generated at 2022-06-14 03:59:20.515470
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve(1)

    def mapper(value):
        return value + 1

    task = Task(fork).map(mapper)
    reject, resolve = task.fork
    assert resolve(None) == 2


# Generated at 2022-06-14 03:59:25.539697
# Unit test for method bind of class Task
def test_Task_bind():
    """
    This test check that Task.bind method
    return new instance of class Task with mapped fork function
    to call function and resolve result with Task.fork.
    """
    expected = Task(lambda reject, resolve: resolve(4))
    actual = Task.of(2).bind(lambda arg: Task.of(arg * 2))
    assert actual.fork == expected.fork



# Generated at 2022-06-14 03:59:28.420642
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value * 2)

    result_task = Task.of(5).bind(fn)

    assert result_task.fork(None, lambda value: value) == 10

# Generated at 2022-06-14 03:59:38.349607
# Unit test for method map of class Task
def test_Task_map():
    def sum_fifty(x):
        return x + 50

    def raise_error(x):
        raise Exception(x)

    def check(x):
        return x is 50

    def resolve(args):
        """
        Handle arguments of fork function of resolved Task,
        check results and raise exception if result is not value.

        :param args: arguments of fork function of resolved Task
        :type args: Function(reject, resolve) -> A
        :raises: AssertionError
        """
        v_result, c_result = args(raise_error, lambda x: (x, check(x)))
        assert c_result


# Generated at 2022-06-14 03:59:47.987141
# Unit test for method map of class Task
def test_Task_map():
    def add(a, b):
        return a + b

    assert Task.of("test")\
        .map(lambda word: word.upper())\
        .fork(
            lambda arg: arg,
            lambda arg: arg
        ) == "TEST"

    assert Task.of("test")\
        .map(lambda word: word + "ing")\
        .fork(
            lambda arg: arg,
            lambda arg: arg
        ) == "testing"

    assert Task.reject("test")\
        .map(lambda word: word + "ing")\
        .fork(
            lambda arg: arg,
            lambda arg: arg
        ) == "test"



# Generated at 2022-06-14 03:59:55.473857
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve("ok")

    originalTask = Task(fork)
    newTask1 = originalTask.map(lambda x: x + "!")
    def fn(x):
        def fork(reject, resolve):
            return resolve("ok" + x)

        return Task(fork)

    newTask2 = Task.of("ok")

    assert originalTask.bind(fn).fork(lambda x: x, lambda x: x) == "okok"
    assert newTask1.bind(fn).fork(lambda x: x, lambda x: x) == "ok!ok"


# Generated at 2022-06-14 03:59:59.559527
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(2)

    def add(value):
        return Task(lambda _, resolve: resolve(value + 1))

    assert Task(fork).bind(add).fork(lambda error: error, lambda result: result) == 3


# Generated at 2022-06-14 04:00:08.571273
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        return None

    def reject(value):
        return None

    temp = Task(lambda _, resolve: resolve(123))
    assert isinstance(temp.map(lambda x: x), Task)
    assert temp.fork(reject, resolve) is None
    # TODO: How to check value which stores in resolve and reject?
    # assert temp.fork(lambda x: reject(x), lambda x: resolve(x)) == 123



# Generated at 2022-06-14 04:00:15.982697
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind method of Task class.
    Bind method must return result of task or exception.
    """
    def increment(value):
        return Task.of(value + 1)

    # Test return of result
    task = Task.of(1).bind(increment)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 2

    # Test return of exception
    task = Task.reject(1).bind(increment)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 1



# Generated at 2022-06-14 04:00:24.727530
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Take function, store it and call with Task value during calling fork function.
    Return result of called.

    :param fn: mapper function
    :type fn: Function(value) -> Task[reject, mapped_value]
    :returns:  new Task with mapper resolve attribute
    :rtype: Task[reject, mapped_value]
    """
    def test_reject(value):
        assert value == 2

    def test_resolve(value):
        assert value == 4

    def reject(value):
        assert value == 1

    def resolve(value):
        assert value == 3

    task = Task.of(3)
    task.fork(reject, resolve)

    task = task.bind(
        lambda arg: Task.of(arg + arg))


# Generated at 2022-06-14 04:00:29.873142
# Unit test for method map of class Task
def test_Task_map():
    def unit(x):
        return x + 1

    def test_map():
        return Task.of(3).map(unit).fork(
            lambda v: "reject",
            lambda v: v
        )

    assert test_map() == 4


# Generated at 2022-06-14 04:00:33.817093
# Unit test for method map of class Task
def test_Task_map():
    def func(value):
        return value + 2

    task = Task.of(1)
    task = task.map(func)
    assert task.fork(lambda err: None, lambda res: res) == 3


# Generated at 2022-06-14 04:00:37.979259
# Unit test for method map of class Task
def test_Task_map():
    def func(value):
        return value + '_mapped'

    task = Task.of('value')
    result = task.map(func)

    assert result.fork(None, None) == 'value_mapped'


# Generated at 2022-06-14 04:00:42.841368
# Unit test for method map of class Task
def test_Task_map():
    def result(reject, resolve):
        return Task(lambda _, resolve: resolve(1)).fork(
            lambda arg: reject(arg),
            lambda arg: resolve(arg + 1)
        )

    assert Task(result).value() == 2


# Generated at 2022-06-14 04:00:47.289930
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind
    """
    task = Task.of('foo')
    task_resolve = task.bind(lambda arg: Task.of(arg + 'bar'))
    assert task_resolve.fork(lambda arg: arg, lambda arg: arg) == 'foobar'


# Generated at 2022-06-14 04:00:54.459411
# Unit test for method bind of class Task
def test_Task_bind():

    def tr(val):
        return Task.of(val + 1)

    def err_fn(err):
        raise err

    def fin():
        raise Exception("No reject")

    task = Task.of(1)

    assert task.bind(tr).fork(err_fn, fin) == 2

    def fn2(value):
        return Task.reject(value + 1)

    try:
        task.bind(fn2).fork(fin, err_fn)
    except Exception as err:
        assert err.args[0] == 2
    else:
        assert False, "Must catch exception"

test_Task_bind()


# Generated at 2022-06-14 04:00:59.457552
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        print("resolve %s" % value)

    def reject(value):
        print("reject %s" % value)

    def mapper(x):
        return x * 10

    task = Task.of(2)
    task2 = task.map(mapper)
    task2.fork(reject, resolve)


# Generated at 2022-06-14 04:01:16.199204
# Unit test for method map of class Task
def test_Task_map():
    test_case = [
        {
            'value': 'value',
            'expected': 'value_map'
        }
    ]

    def map_fn(value):
        return value + '_map'

    for test in test_case:
        task = Task.of(test['value'])
        assert task.map(map_fn).fork(None, None) == test['expected']


# Generated at 2022-06-14 04:01:21.423196
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value)

    def test_fn(value):
        return value + 1

    # Task[rejected, A]
    task = Task.reject(0).map(test_fn)

    # Task[resolved, A]
    task.bind(fn)
    # Task[rejected, A]


# Generated at 2022-06-14 04:01:24.354191
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(
        lambda x: 'rejected',
        lambda x: x
    ) == 2


# Generated at 2022-06-14 04:01:33.021617
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(10).bind(lambda x: Task.of(x * 2)).fork(None, lambda result: result == 20)
    assert Task.of(10).bind(Task.of).fork(None, lambda result: result == 10)
    assert Task.of(10).bind(lambda _: Task.of(20)).fork(None, lambda result: result == 20)
    assert Task.reject(10).bind(lambda x: Task.of(x * 2)).fork(lambda result: result == 10, None)
    assert Task.reject(10).bind(Task.reject).fork(lambda result: result == 10, None)
    assert Task.reject(10).bind(lambda _: Task.reject(20)).fork(lambda result: result == 10, None)

# Generated at 2022-06-14 04:01:36.478325
# Unit test for method bind of class Task
def test_Task_bind():
    def add(value: int) -> Task:
        return Task.of(value + 1)

    assert Task.of(1).bind(add).fork(
        lambda i: None,
        lambda i: i
    ) == 2

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:01:39.456297
# Unit test for method bind of class Task
def test_Task_bind():
    def _(arg):
        return Task.of(arg + 2)

    a = Task.of(1).bind(_)
    assert a.fork(lambda arg: '', lambda arg: arg) == 3



# Generated at 2022-06-14 04:01:49.597259
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(5) \
        .bind(lambda x: Task.of(x * x)) \
        .bind(lambda x: Task.of(x + 1))

    assert task.fork(None, lambda a: a) == 26

    def f():
        raise Exception()

    task = Task.of(5) \
        .bind(lambda x: Task.of(x * x)) \
        .bind(f)

    assert task.fork(
        lambda error: error.__class__.__name__,
        None
    ) == 'Exception'

    task = Task.reject(5) \
        .bind(lambda x: Task.of(x * x)) \
        .bind(f)

    assert task.fork(
        lambda error: error,
        None
    ) == 5

# Unit test

# Generated at 2022-06-14 04:01:53.438991
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(5)
    result = task.map(lambda x: x * 2).fork(lambda x: 'Error', lambda x: x)
    assert result == 10


# Generated at 2022-06-14 04:02:00.666599
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(1)

    def add(value):
        return Task.of(value + 1)

    def throw(value):
        return Task.reject(value)

    task = Task(fork)
    assert task.bind(add).fork(lambda arg: arg, lambda arg: arg) == 2
    assert task.bind(throw).fork(lambda arg: arg, lambda arg: arg) == 1

# Generated at 2022-06-14 04:02:13.108115
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test
    """
    def task_resolve(value):
        return Task(lambda _, resolve: resolve(value))

    def task_reject(value):
        return Task(lambda reject, _: reject(value))

    def task_fork(resolve, reject):
        return task_resolve(resolve).fork(reject, reject)

    def test(value):
        return value

    def test_bind(value):
        return value + 10

    def test_error(value):
        return value - 10
    
    def test_bind_error(value):
        return value + 10

    assert Task.of(1).bind(task_resolve).map(lambda value: value + 1).fork(test, test) == 2

# Generated at 2022-06-14 04:02:40.394743
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(value):
        return value

    def resolve(value):
        return value

    def fn(value):
        return Task.of(value + 1)

    result = Task.of(1).bind(fn)
    assert resolve(2) == result.fork(reject, resolve)

    result = Task.reject(1).bind(fn)
    assert reject(1) == result.fork(reject, resolve)

test_Task_bind()

# Generated at 2022-06-14 04:02:44.806007
# Unit test for method map of class Task

# Generated at 2022-06-14 04:02:50.863957
# Unit test for method map of class Task

# Generated at 2022-06-14 04:02:53.246273
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    assert task.fork(lambda arg: arg, lambda arg: arg + 1) == 2


# Generated at 2022-06-14 04:02:56.379223
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).bind(lambda x: Task.of(x + 5)).fork(
        lambda err: 'error',
        lambda data:data
    ) == 7


# Generated at 2022-06-14 04:02:58.889122
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(2).map(lambda n: n + 1).fork(None, lambda n: n) == 3


# Generated at 2022-06-14 04:03:05.307909
# Unit test for method map of class Task
def test_Task_map():
    def square(x):
        return x * x

    def increment(x):
        return x + 1

    def chain_map(x):
        return Task.of(x).map(square).map(increment)

    assert chain_map(2).fork(None, lambda value: 3) == 3
    assert chain_map(3).fork(None, lambda value: 4) == 10


# Generated at 2022-06-14 04:03:08.221082
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 1

    def fork(reject, resolve):
        return resolve(1)

    task = Task(fork)
    assert task.map(mapper).fork(lambda _: None, lambda value: value) == 2



# Generated at 2022-06-14 04:03:16.916337
# Unit test for method map of class Task
def test_Task_map():
    """
    Unit tests for method map of class Task.
    """
    # Mapping over resolved
    assert Callable(Task.of(1).map)
    assert Task.of(1).map(lambda x: x + 1).fork(lambda x: x, lambda x: x) == 2
    assert Task.of(2).map(lambda x: x - 1).fork(lambda x: x, lambda x: x) == 1

    # Mapping over rejected
    assert Task.reject(2).map(lambda x: x + 1).fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 04:03:23.030211
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method
    """
    def value(result):
        assert result == '2', 'Not a right result of mapping'
    def reject(_):
        assert False, 'No rejection in this case'

    task = Task.of(1)
    task.map(str).fork(reject, value)


# Generated at 2022-06-14 04:04:09.354841
# Unit test for method map of class Task
def test_Task_map():
    """Unit test for method map of class Task"""
    def inc(value):
        return value + 1

    def square(value):
        return value * value

    fork = lambda _, resolve: resolve(5)

    task = Task(fork)
    result = task.map(inc).map(square)
    assert result.fork(lambda _: None, lambda value: value) == 36


# Generated at 2022-06-14 04:04:17.928136
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task map by multiply value stored in Task by 5.
    Result of this test must be Task with stored value 20.
    """
    # Create Task and multiply value by 5.
    task = Task.of(4).map(lambda x: x * 5)
    # Call fork and check that resolve function was called with value 20.
    task.fork(
        lambda err: print("Fail:", err),
        lambda res: print("Success:", res)
    )


# Generated at 2022-06-14 04:04:22.986766
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for map method
    """
    # resolve Task
    assert Task.of(5).map(lambda arg: arg - 1).fork(lambda arg: str(arg), lambda arg: str(arg)) == '4'

    # rejected Task
    assert Task.reject(5).map(lambda arg: arg - 1).fork(lambda arg: str(arg), lambda arg: str(arg)) == '5'

if __name__ == '__main__':
    test_Task_map()

# Generated at 2022-06-14 04:04:30.284069
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    def foo(reject, resolve):
        resolve('test')

    t = Task(foo)
    t1 = t.map(lambda arg: arg + ' added')

    def foo1(reject, resolve):
        resolve('test added')

    assert t1.fork == foo1


# Generated at 2022-06-14 04:04:33.922209
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(5)
    result = task.map(lambda value: value ** 2)
    assert result.fork(None, lambda value: value) == 25


# Generated at 2022-06-14 04:04:44.109233
# Unit test for method bind of class Task
def test_Task_bind():
    # call reject during calling fork
    task = Task.reject(4).bind(lambda v: Task.of(v * 2))
    rejected = False
    task.fork(
        lambda value: rejected.__setattr__('value', value),
        lambda _: rejected.__setattr__('value', False)
    )
    assert rejected.value == 4, 'method bind of class Task should call reject function when some error occurs'

    # call resolve during calling fork
    task = Task.of(4).bind(lambda v: Task.of(v * 2))
    resolved = None
    task.fork(
        lambda _: resolved.__setattr__('value', False),
        lambda value: resolved.__setattr__('value', value)
    )

# Generated at 2022-06-14 04:04:49.014483
# Unit test for method map of class Task
def test_Task_map():
    """Map test"""
    def fork(reject, resolve):
        return resolve(1)

    assert Task(fork).map(lambda x: x+1).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 2


# Generated at 2022-06-14 04:04:57.272127
# Unit test for method map of class Task

# Generated at 2022-06-14 04:05:00.718163
# Unit test for method bind of class Task
def test_Task_bind():
    def test(value):
        assert Task.of(value).fork(lambda x: False, lambda y: y == value)

    test(1)
    test(2)
    test(3)
    test(4)


# Generated at 2022-06-14 04:05:03.125550
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(4)
    task = task.map(lambda i: i / 2)
    assert task.fork(lambda i: i, lambda i: i) == 2


# Generated at 2022-06-14 04:06:44.127099
# Unit test for method bind of class Task
def test_Task_bind():
    def add(a, b):
        return a + b

    def add_value(a):
        return Task.of(add(a, 1))

    def map_value(a):
        return Task.of(a + 1)

    def add_tuple_value(a):
        return Task.of(add(a[0], a[1]))

    assert Task.reject("test reject").bind(add_value).fork("value reject", "value resolve") == "test reject"
    assert Task.reject("test reject").bind(add_tuple_value).fork("value reject", "value resolve") == "test reject"
    assert Task.reject("test reject").bind(add_value).bind(map_value).fork("value reject", "value resolve") == "test reject"


# Generated at 2022-06-14 04:06:50.920888
# Unit test for method bind of class Task
def test_Task_bind():
    def example(value):
        return Task.of(value + " World")

    def example_2(value):
        return Task.of(value + "!")

    result = Task.of("Hello") \
        .bind(example) \
        .bind(example_2)

    assert isinstance(result, Task)
    assert isinstance(result.fork, Function)
    assert isinstance(result.fork(lambda x: x, lambda x: x), str)
    assert result.fork(lambda x: x, lambda x: x) == "Hello World!"


# Generated at 2022-06-14 04:07:00.255479
# Unit test for method bind of class Task
def test_Task_bind():
    @lazy
    def get_user_by_id(id):
        if id < 0:
            return Task.reject('Error getting user by id')

        user = {
            'id': id,
            'name': 'Name-' + str(id),
            'age': id + 10
        }
        return Task.of(user)

    @lazy
    def get_post_by_user(user):
        id = user['id'] * 10 + 1
        if id < 0:
            return Task.reject('Error getting post by user')

        post = {
            'id': id,
            'title': 'Title-' + str(id),
            'user': user['name'],
            'date': datetime.datetime.now()
        }

        return Task.of(post)


# Generated at 2022-06-14 04:07:04.120683
# Unit test for method map of class Task
def test_Task_map():
    # Success resolve
    assert (Task(lambda _, resolve: resolve(1))
            .map(lambda x: x + 1)
            .fork(lambda x: None, lambda x: x)) == 2

    # Error reject
    assert (Task(lambda reject, _: reject(1))
            .map(lambda _: 2)
            .fork(lambda x: x, lambda _: None)) == 1


# Generated at 2022-06-14 04:07:06.321551
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2)
    assert task.map(lambda x: x + 1).fork(None, lambda x: x) == 3



# Generated at 2022-06-14 04:07:19.062057
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:07:24.489515
# Unit test for method bind of class Task
def test_Task_bind():

    def fork(reject, resolve):
        reject('error')
        return resolve('success')

    def fn(value):
        def fork(reject, resolve):
            return resolve(value)

        return Task(fork)

    t = Task(fork)
    res = t.bind(fn)

    assert res == {'fork': fork}

    def fork(reject, resolve):
        return resolve('success')

    def fn(value):
        def fork(reject, resolve):
            return reject(value)

        return Task(fork)

    t = Task(fork)
    res = t.bind(fn)

    assert res == {'fork': fork}

# Generated at 2022-06-14 04:07:31.004116
# Unit test for method bind of class Task
def test_Task_bind():
    # Create Task with fork function that return None during call reject attribute.
    task = Task(lambda reject, resolve: None)
    # create new task with bind method
    new_task = task.bind(lambda x: Task.of(x))
    # create function that return Task with True value during call resolve
    resolve_task = lambda _, resolve: resolve(True)

    assert True == new_task.fork(lambda x: False, lambda x: x)
    assert True == new_task.fork(reject_task, resolve_task)


# Generated at 2022-06-14 04:07:37.211201
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test is checking if Task with stored value is passing through bind function.
    """
    assert Task.of("Hello").bind(
        lambda value: Task.of("Hello world, " + value)
    ).fork(
        lambda value: None,
        lambda value: value
    ) == "Hello world, Hello"


# Generated at 2022-06-14 04:07:45.622617
# Unit test for method map of class Task
def test_Task_map():

    def test_map_with_identity():
        identity = lambda arg: arg
        task = Task.of(1).map(identity)
        assert task.fork(lambda x: x, lambda x: x) == 1

    def test_map_with_multiply_by_two():
        multiply_by_two = lambda arg: arg * 2
        task = Task.of(41).map(multiply_by_two)
        assert task.fork(lambda x: x, lambda x: x) == 82

    test_map_with_identity()
    test_map_with_multiply_by_two()

