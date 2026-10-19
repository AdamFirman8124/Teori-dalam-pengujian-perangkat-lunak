

# Generated at 2022-06-14 03:57:55.952594
# Unit test for method bind of class Task
def test_Task_bind():
    forker = lambda reject, resolve: resolve(42)
    Tasker = Task(forker)

    mapper = lambda value: Task.of(value + 1)

    assert Tasker.bind(mapper).fork(None, lambda value: value) == 43

# Generated at 2022-06-14 03:58:01.490103
# Unit test for method bind of class Task
def test_Task_bind():
    def task(resolve, reject):
        def cb(value):
            if value == 1:
                resolve(value)
            else:
                reject('Error')

        return cb

    def mapper(value):
        return Task.of(value + 1)

    def mapper2(value):
        return Task.reject('Error')

    assert Task(task(1, None)).bind(mapper)(None, print) == 2
    assert Task(task(1, None)).bind(mapper2)(print, None) == 'Error'

# Generated at 2022-06-14 03:58:06.030562
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of('a').bind(lambda v: Task.of('b')).fork(
        lambda err: None,
        lambda res: res
    ) == 'b'

    assert Task.reject('a').bind(lambda v: Task.of('b')).fork(
        lambda err: err,
        lambda res: res
    ) == 'a'

# Generated at 2022-06-14 03:58:13.169674
# Unit test for method bind of class Task
def test_Task_bind():
    @Task
    def doubling_task(resolve):
        resolve(2)

    @Task
    def increment_task(resolve):
        resolve(1)

    @Task
    def sum_task(resolve):
        resolve(4)

    @Task
    def get_task():
        return increment_task.bind(lambda value: doubling_task.map(lambda value: value + value))

    assert get_task() == sum_task

# Generated at 2022-06-14 03:58:25.796309
# Unit test for method map of class Task
def test_Task_map():
    def add_one(x):
        return x + 1

    def throw_error(x):
        raise ValueError('Too small')

    def unique_id():
        return uuid.uuid4()

    value = Task.of(1).map(add_one)
    assert value.fork(None, lambda arg: arg) == 2

    value = Task.of(1).map(throw_error)
    assert value.fork(lambda arg: arg, None) == ValueError('Too small')

    value = Task.reject(ValueError('Too small')).map(add_one)
    assert value.fork(lambda arg: arg, None) == ValueError('Too small')

    value = Task.reject(ValueError('Too small')).map(throw_error)
    assert value.fork(lambda arg: arg, None) == Value

# Generated at 2022-06-14 03:58:36.872807
# Unit test for method bind of class Task
def test_Task_bind():
    def test_one():
        def fn(value):
            return Task.of(value+' World!')

        return Task.of('Hello')\
            .bind(fn)

    def test_two():
        def fn(value):
            return Task.of(value+' World!')

        return Task.of('Hello')\
            .map(lambda value: value+' World!')

    assert 'Hello World!' == test_one().fork(lambda value: value, lambda value: value)
    assert 'Hello World!' == test_two().fork(lambda value: value, lambda value: value)

# Generated at 2022-06-14 03:58:44.547156
# Unit test for method bind of class Task
def test_Task_bind():
    def return_value(arg):
        return arg

    def return_error(arg):
        raise arg

    def execute_test(success, *args):
        def test_func(*params):
            return Task.of(params[0])

        if success:
            assert Task.of(args[0]).bind(test_func).fork(
                lambda reject_value, resolve_value: reject_value,
                lambda reject_value, resolve_value: resolve_value
            )(None, None) == args[0]
        else:
            with pytest.raises(args[0]):
                assert Task.of(args[0]).bind(return_error).fork(
                    lambda reject_value, resolve_value: reject_value,
                    lambda reject_value, resolve_value: resolve_value
                )(None, None) == args

# Generated at 2022-06-14 03:58:50.415010
# Unit test for method map of class Task
def test_Task_map():

    t_resolved_2 = Task.of(2)
    t_resolved_4 = Task.of(4)
    t_rejected_8 = Task.reject(8)
    t_rejected_16 = Task.reject(16)

    result = t_resolved_2.map(lambda x: x * 2)
    assert result.fork(lambda _: True, lambda _: False) == False
    assert result.fork(lambda x: x, lambda _: None) == 4

    result = t_rejected_8.map(lambda x: x * 4)
    assert result.fork(lambda _: True, lambda _: False) == True
    assert result.fork(lambda x: x, lambda _: None) == 8


# Generated at 2022-06-14 03:58:56.883573
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    def add_2(arg):
        return arg + 2

    result = Task.of(2).map(add_2)
    assert result.fork(None, lambda value: value) == 4

    result = Task.reject(2).map(add_2)
    assert result.fork(lambda value: value, None) == 2


# Generated at 2022-06-14 03:59:08.098301
# Unit test for method map of class Task
def test_Task_map():
    from nose.tools import assert_equal
    from nose.tools import assert_not_equal

    def foo(value):
        return value + 1

    task1 = Task.of(1).map(foo)
    task2 = Task.of(1)
    task3 = Task.of(1).map(foo).map(foo)
    task4 = Task.of(1).map(foo)

    assert_equal(task1.fork(lambda x: x, lambda x: x), 2)
    assert_equal(task2.fork(lambda x: x, lambda x: x), 1)
    assert_equal(task3.fork(lambda x: x, lambda x: x), 3)
    assert_equal(task4.fork(lambda x: x, lambda x: x), 2)


# Generated at 2022-06-14 03:59:19.473418
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Check if method bind of class Task work as expected.
    """
    import pytest
    from random import randint

    for _ in range(100):
        A = randint(1, 100)
        B = randint(1, 100)
        C = randint(1, 100)
        D = randint(1, 100)

        task1 = Task.of(A)
        task2 = Task.of(B)
        task3 = Task.of(C)
        task4 = Task.of(D)

        task13 = task1.bind(lambda a: task3.map(lambda c: a + c))
        task24 = task2.bind(lambda b: task4.map(lambda d: b + d))

        assert task13.fork(lambda _: None, lambda result: result) == A + C

# Generated at 2022-06-14 03:59:24.620259
# Unit test for method bind of class Task
def test_Task_bind():
    def task1(reject, resolve):
        resolve(1)

    def task2(reject, resolve):
        resolve(2)

    def task3(reject, resolve):
        resolve(3)

    task = Task(task1).bind(lambda x: Task(task2)).bind(lambda x: Task(task3))

    def fork(reject, resolve):
        return task.fork(reject, resolve)

    assert fork(lambda x: x, lambda x: x) == 3


# Generated at 2022-06-14 03:59:32.353966
# Unit test for method map of class Task
def test_Task_map():
    def set_of_Method_map_param(input):
        pass

    def set_of_Method_map_expect_param(output):
        pass

    def set_of_Method_map_expect_result(expect):
        pass

    @given(set_of_Method_map_param())
    def test_when_map_then_take_new_fn(param):
        task = Task.of(param)
        result = task.map(set_of_Method_map_expect_param)

        assert_that(result, instance_of(Task))
        assert_that(result.fork, instance_of(set_of_Method_map_expect_result))


# Generated at 2022-06-14 03:59:38.893487
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2).map(lambda x: x + 1)
    assert task.fork.__closure__[1].cell_contents(None, lambda x: x) == 3

    task = Task.reject(2).map(lambda x: x + 1)
    assert task.fork.__closure__[0].cell_contents(lambda x: x, None) == 2


# Generated at 2022-06-14 03:59:41.315808
# Unit test for method map of class Task
def test_Task_map():
    def add_one(arg):
        return arg + 1

    def fork(_, resolve):
        return resolve(1)

    task = Task(fork)
    assert(isinstance(task.map(add_one), Task))
    assert(isinstance(task.map(add_one).fork, Function))
    assert(task.map(add_one).fork(1, 2) == 2)



# Generated at 2022-06-14 03:59:45.343913
# Unit test for method map of class Task
def test_Task_map():
    def add(value):
        return value + 100

    task = Task(lambda reject, resolve: resolve(10))

    assert task.map(add).fork(
        lambda value: 'rejected',
        lambda value: value
    ) == 110


# Generated at 2022-06-14 03:59:54.244320
# Unit test for method bind of class Task
def test_Task_bind():
    # Test for functional of method bind
    def test(fn, arguments, expected_result):
        result = Task.of(arguments)
        result = result.bind(fn)
        assert result == expected_result

    test(lambda x: Task.of(x + 2), 2, Task(lambda _, resolve: resolve(4)))
    test(lambda x: x + 2, 2, Task(lambda _, resolve: resolve(4)))
    test(lambda x: Task.reject(x + 2), 2, Task(lambda reject, _: reject(4)))
    test(lambda x: Task.of(x + 2), Task(lambda _, resolve: resolve(3)), Task(lambda _, resolve: resolve(5)))



# Generated at 2022-06-14 03:59:59.820798
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(resolve, reject):
        resolve(10)

    task = Task(fork)
    debounce = task.bind(lambda arg: Task.of(arg + 10))

    assert isinstance(debounce, Task)
    assert debounce.fork(lambda arg: arg, lambda arg: arg) == 20



# Generated at 2022-06-14 04:00:04.483234
# Unit test for method bind of class Task
def test_Task_bind():
    def add_1(x):
        return x + 1

    def sqrt(x):
        return math.sqrt(x)

    assert Task.of(2).bind(lambda x: Task.of(add_1(x))).bind(lambda x: Task.of(sqrt(x))).fork(
        lambda reject: "reject",
        lambda resolve: resolve
    ) == math.sqrt(3)


# Generated at 2022-06-14 04:00:16.305623
# Unit test for method bind of class Task
def test_Task_bind():
    def noop1():
        pass

    def noop2():
        pass

    def noop3():
        pass

    def test_fork(reject, resolve):
        noop1()
        reject(2)
        noop2()
        resolve(1)
        noop3()

    task = Task(test_fork)

    reject_data = []
    resolve_data = []

    noop1()

# Generated at 2022-06-14 04:00:24.409082
# Unit test for method map of class Task
def test_Task_map():
    @Task.of
    def function(x, y):
        return x + y

    assert function(1, 2).map(lambda result: result * 2).fork(
        lambda arg: None,
        lambda arg: arg
    ) == 6



# Generated at 2022-06-14 04:00:28.602370
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method
    """
    Task.of(5).bind(lambda arg: Task.of(arg + 10)).fork(None, lambda arg: print(arg))



# Generated at 2022-06-14 04:00:33.910390
# Unit test for method map of class Task
def test_Task_map():
    def resolve(result):
        assert result == 2, "Task map method not map value"

    def reject(error):
        assert False, "Task map method should not return error"

    def function(x):
        return x + 1

    Task.of(1).map(function).fork(reject, resolve)


# Generated at 2022-06-14 04:00:43.144517
# Unit test for method bind of class Task
def test_Task_bind():
    # assert Task.of(lambda a: a * 2).bind(lambda a: Task.of(a)) == 4

    assert Task.of(lambda a: a + 2).map(lambda a: a - 2).fork(
        lambda a: None,
        lambda a: a(2)
    ) == 2

    assert Task.of(lambda a: a + 2).bind(
        lambda a: Task.of(a)
    ).map(lambda a: a(2)).fork(
        lambda a: None,
        lambda a: a
    ) == 4

    def bind(a):
        def result(resolve, reject):
            return Task.of(lambda a: a * 2).fork(
                lambda _: resolve(Task.of(a)),
                lambda _: resolve(Task.of(a))
            )


# Generated at 2022-06-14 04:00:51.520488
# Unit test for method map of class Task
def test_Task_map():
    # Create instance of Task
    task = Task(lambda reject, resolve: resolve(1))

    # Check that result is equal to Task with resolved value
    assert task.map(lambda x: x + 1).fork(
            lambda reject: reject,
            lambda resolve: resolve
        ) == 2, "Expecting 2, but got {}" \
        .format(
            task.map(lambda x: x + 1).fork(
                lambda reject: reject,
                lambda resolve: resolve
            )
        )


# Generated at 2022-06-14 04:00:59.571295
# Unit test for method bind of class Task
def test_Task_bind():
    # mock instance Task with resolve and reject function
    task = Task(lambda reject, resolve: None)

    # mock bind function with callable resolve function
    def bind(fn):
        # call of resolver
        fn(1)

    # store resolve and reject function for call bind
    def resolve(arg):
        pass

    def reject(arg):
        pass

    # check call bind with resolve and reject function for mock instance
    task.bind(bind).fork(reject, resolve)



# Generated at 2022-06-14 04:01:09.132725
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(value):
        pass

    def resolve(value):
        return Task.of(value)

    # Test when fork is rejected
    task1 = Task(lambda _, resolve: resolve('value'))
    task2 = Task(lambda reject, _: reject('value'))

    assert task1.bind(resolve) == Task.of('value')
    assert task2.bind(reject) == Task.of('value')

    # Test when fork is resolve
    task3 = task1.bind(reject)
    task4 = task2.bind(resolve)

    assert task3 == Task.reject('value')
    assert task4 == Task.reject('value')

# Generated at 2022-06-14 04:01:18.736844
# Unit test for method bind of class Task
def test_Task_bind():
    def resolver(n):
        return Task.of(n)

    assert Task.reject('a').bind(resolver).fork(
        lambda n: n,
        lambda _: 'b') == 'a'

    assert Task.of(1).bind(resolver).fork(
        lambda _: 'a',
        lambda n: n) == 1
 
    assert Task.of(1).bind(lambda _: Task.reject('a')).fork(
        lambda n: n,
        lambda _: 'b') == 'a'


# Generated at 2022-06-14 04:01:24.750512
# Unit test for method map of class Task
def test_Task_map():
    """
    1. Take resolved Task with value equal to 5.
    2. Call map method with lambda function that take argument and increment it.
    3. Check with assert equal if resolve attribute of result Task is equal to 6.
    """
    task = Task.of(5)
    result = task.map(lambda x: x + 1)
    assert result.fork(lambda x: x, lambda x: x) == 6


# Generated at 2022-06-14 04:01:28.483420
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(arg):
        return Task(lambda _, resolve: resolve(arg+1))

    task = Task(lambda reject, resolve: resolve(1)).bind(fn)
    assert task.fork(lambda rejected: False, lambda resolved: resolved) == 2


# Generated at 2022-06-14 04:01:41.481475
# Unit test for method bind of class Task
def test_Task_bind():
    # Bind should work
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(lambda x: x, lambda x: x) == 2

    # Bind should handle rejected
    assert Task.reject(1).bind(lambda x: Task.of(x + 1)) == Task.reject(1)


if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:01:48.524662
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda x: Task.of(x + 1)) == Task.of(2)
    assert Task.reject(1).bind(lambda x: Task.of(x + 1)) == Task.reject(1)
    assert Task.of(1).bind(lambda x: Task.reject(x + 1)) == Task.reject(2)
    assert Task.reject(1).bind(lambda x: Task.reject(x + 1)) == Task.reject(1)


# Generated at 2022-06-14 04:01:53.439124
# Unit test for method map of class Task
def test_Task_map():
    def test(input, expect):
        task = Task.of(input).map(lambda value: value + 1)
        result = task.fork(None, lambda value: value)
        assert result == expect

    test(1, 2)
    test(2, 3)

# Generated at 2022-06-14 04:02:03.109293
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(arg):
        assert arg == '1'
        assert callable(then)
        return then(arg)

    assert callable(Task.reject)
    assert callable(Task.of)

    assert callable(Task.reject('ok').bind)
    assert callable(Task.of('ok').bind)

    def bind(arg):
        return Task.of(arg)

    task = Task.of('1')
    foo = task.bind(bind)
    then = foo.fork(lambda _: None, resolve)

    assert task is not foo
    assert foo is not then
    assert then is not None


# Generated at 2022-06-14 04:02:13.158129
# Unit test for method bind of class Task
def test_Task_bind():
    t = Task.of(1).bind(lambda x: Task.of(x + 1))
    assert t.fork(
        lambda arg: False,
        lambda arg: True if arg == 2 else False
    )

    t = Task.of(1).bind(lambda x: Task.reject(x - 1))
    assert t.fork(
        lambda arg: True if arg == 0 else False,
        lambda arg: False
    )

    t = Task.reject(1).bind(lambda x: Task.of(x + 1))
    assert t.fork(
        lambda arg: True if arg == 1 else False,
        lambda arg: False
    )


# Generated at 2022-06-14 04:02:17.187894
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of('Hello')
    task = task.map(lambda value: value + ' world')
    assert task.fork(lambda _: None, lambda value: value) == 'Hello world'


# Generated at 2022-06-14 04:02:18.514843
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2)
    assert task.map(lambda x: x ** 2).fork(lambda x: x, lambda x: x) == 4


# Generated at 2022-06-14 04:02:23.579585
# Unit test for method map of class Task
def test_Task_map():
    """Test for method Task.map"""
    assert Task.of(1).map(lambda v: v + 1).fork(None, lambda v: v) == 2
    assert Task.of(1).map(lambda v: v + 1).map(lambda v: v * 2).fork(None, lambda v: v) == 4
    assert Task.of(1).map(lambda v: v + 1).map(lambda v: v * 2).map(lambda v: v - 1).fork(None, lambda v: v) == 3


# Generated at 2022-06-14 04:02:35.747740
# Unit test for method map of class Task
def test_Task_map():
    import time

    def mapper(value):
        return value + 1

    def check(value):
        return value == 2

    def fork(reject, resolve):
        return resolve(1)

    task = Task(fork)
    mapped_task = task.map(mapper)
    rejected_task = Task.reject(1)

    assert check(mapped_task.fork(lambda _, __: None, lambda arg: arg))
    assert check(rejected_task.map(mapper).fork(lambda _, __: None, lambda arg: arg))
    assert isinstance(task.fork(lambda *_: None, lambda *_: None), None.__class__)
    assert isinstance(time.sleep, task.map(time.sleep).fork(lambda *_: None, lambda *_: None))

# Unit test

# Generated at 2022-06-14 04:02:45.314990
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.

    Use case:
    create some Task, bind to it second Task,
    get Tasks`s attributes and pass them to some function.
    """
    def spy(reject, resolved):
        """
        Take reject and resolved attributes of Task
        and pass them to message handler.
        """
        def message_handler(resolved_message, reject_message):
            """
            Take resolved and failed message and print them.
            """
            print("resolved: {}".format(resolved_message))
            print("reject: {}".format(reject_message))
        resolved("Hello")
        reject("World")

    Task.of("Test").bind(spy).fork(
        lambda reject: print("reject"),
        lambda resolved: print("resolved")
    )

#

# Generated at 2022-06-14 04:03:08.448454
# Unit test for method bind of class Task
def test_Task_bind():
    def add1(x):
        return Task.of(x + 1)

    def double(x):
        return Task.of(x * 2)

    def double_add1(x):
        return add1(x).bind(double)

    assert double_add1(2).fork(lambda arg: arg, lambda arg: arg) == 5


# Generated at 2022-06-14 04:03:16.362640
# Unit test for method bind of class Task
def test_Task_bind():
    source = Task.of(10)

    def mapper(value):
        # type: (int) -> Task[int, int]
        return Task.reject(value * 2)

    assert source.bind(mapper).fork(lambda value: value, lambda _: True) == 20

    def mapper(value):
        # type: (int) -> Task[int, int]
        return Task.of(value * 2)

    assert source.bind(mapper).fork(lambda _: True, lambda value: value) == 20


# Generated at 2022-06-14 04:03:29.363460
# Unit test for method bind of class Task
def test_Task_bind():
    """Check bind function of Task"""
    def fork_for_test(reject, resolve):
        resolve('foo')

    def fork_for_test2(reject, resolve):
        resolve('bar')

    def fork_for_test3(reject, resolve):
        reject('fail')

    def fork_for_test4(reject, resolve):
        resolve('foo')

    def fork_for_test5(reject, resolve):
        resolve('bar')

    def fork_for_test6(reject, resolve):
        reject('fail')

    def get_foo(value):
        """
        Return Task.of('bar').
        """
        return Task.of('bar')

    def get_foo2(value):
        """
        Return Task.of('bar').
        """

# Generated at 2022-06-14 04:03:33.407464
# Unit test for method map of class Task
def test_Task_map():
    def plus1(arg):
        return arg + 1

    def plus(arg):
        def mapped(value):
            return value + arg

        return Task(lambda reject, resolve: resolve(mapped))

    assert Task.of(1).map(plus1).fork(None, lambda arg: arg) == 2
    assert Task.reject(1).map(plus1).fork(None, lambda arg: None) is None
    assert Task.of(2).bind(plus(1)).fork(None, lambda arg: arg(3)) == 5



# Generated at 2022-06-14 04:03:39.305923
# Unit test for method bind of class Task
def test_Task_bind():
    def _plus(arg):
        return Task.of(arg + 10)

    task = Task.of(0).bind(_plus)

    def _reject(arg):
        assert False, "Task must be resolved with value 10."

    def _resolve(arg):
        assert arg == 10

    task.fork(_reject, _resolve)


# Generated at 2022-06-14 04:03:49.468567
# Unit test for method bind of class Task
def test_Task_bind():
    def test_task_1():
        return Task.of(10)

    def test_task_2():
        return Task.of(12)

    def test_task_3():
        return Task.reject(12)

    def test_task_4():
        return Task.of('12')

    def test_task_5():
        return Task.reject('12')

    a = Task.of(10).bind(test_task_1)
    assert a.fork(lambda _: True, lambda x: x == 10) is True

    a = Task.of(10).bind(test_task_2)
    assert a.fork(lambda _: True, lambda x: x == 12) is True

    a = Task.of(10).bind(test_task_3)

# Generated at 2022-06-14 04:03:52.572927
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    result = task.map(lambda a: a + 1).fork(lambda a: a + 5, lambda x: x)

    assert isinstance(result, Task)
    assert result == 2


# Generated at 2022-06-14 04:04:03.859478
# Unit test for method map of class Task
def test_Task_map():
    """
    Unit test for method map of class Task
    """
    def _reject(error):
        raise error

    def run(reject, resolve):
        resolve(1)
        reject(2)

    assert Task(run).map(lambda x: x * 10).fork(lambda x: x, lambda x: x) == 10
    assert Task(run).map(lambda x: x * 10).map(lambda x: x * 5).fork(lambda x: x, lambda x: x) == 50
    assert Task.of(1).map(lambda x: x * 10).fork(lambda x: x, lambda x: x) == 10

    with pytest.raises(RuntimeError) as error:
        Task.reject(RuntimeError()).fork(_reject, lambda x: x)

# Generated at 2022-06-14 04:04:08.307910
# Unit test for method bind of class Task
def test_Task_bind():
    result = Task.of(10).bind(
        lambda arg: Task.of(arg + 1)
    ).fork(
        lambda arg: arg,
        lambda arg: arg
    )

    assert result == 11



# Generated at 2022-06-14 04:04:17.251855
# Unit test for method bind of class Task
def test_Task_bind():
    def test_data(x):
        if x == 42:
            return Task.of(x * 2)
        else:
            return Task.reject(x * 2)

    def task(x):
        return Task.of(x).bind(test_data)

    assert task(42).fork(lambda x: x, lambda x: x) == 84
    assert task(21).fork(lambda x: x, lambda x: x) == 42

if __name__ == "__main__":
    test_Task_bind()

# Generated at 2022-06-14 04:05:03.481002
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return value * 2

    task = Task.of(2)

    assert task.bind(Task.of).fork(lambda _: None, lambda value: value) == 2
    assert task.bind(fn).fork(lambda _: None, lambda value: value) == 4
    assert task.bind(lambda _: Task.reject(2)).fork(
        lambda value: value,
        lambda _: None
    ) == 2



# Generated at 2022-06-14 04:05:14.309877
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind
    """
    def fork_reject(reject, resolve):
        reject('Error occurred')

    def fork_resolve(reject, resolve):
        resolve('Resolved')

    def fork_resolve_mapped_value(reject, resolve):
        resolve('Mapped value')

    class TaskReject(Task):
        """
        Task with reject attribute
        """
        def __init__(self):
            Task.__init__(self, fork_reject)

    def fork_mapper(value):
        """
        Mapper function
        """
        return TaskReject()

    class TaskRejectMapper(Task):
        """
        Task with reject attribute after mapping
        """

# Generated at 2022-06-14 04:05:20.652537
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve(5)

    def fn(value):
        return value + 1

    def fork_res(reject, resolve):
        return resolve(fn(5))

    task = Task(fork)
    result = task.map(fn)

    assert result.fork == fork_res


# Generated at 2022-06-14 04:05:26.078801
# Unit test for method map of class Task
def test_Task_map():
    # input
    task = Task.of(5)
    fn = lambda x: x * 2

    # call method
    result = task.map(fn)

    # assert
    assert isinstance(result, Task)
    assert result.fork(
        lambda arg: False,
        lambda arg: arg == 10
    )


# Generated at 2022-06-14 04:05:32.063195
# Unit test for method map of class Task
def test_Task_map():
    # Init module
    import operator
    from nose.tools import assert_equals, assert_raises

    # Create and call mapper function for Task.map
    def fmap(value):
        return value * 2

    # Default Task
    task = Task.of(2)

    # Test call with mapper
    assert_equals(task.map(fmap).fork(None, lambda x: x), 4)


# Generated at 2022-06-14 04:05:41.339917
# Unit test for method map of class Task
def test_Task_map():
    """
    :type value: A
    :type result: A
    """
    # set result of fork function
    value = 2
    result = 0

    # initiate fork functions
    def add2(resolve, reject):
        return resolve(value + 2)

    def minus2(resolve, reject):
        return resolve(value - 2)

    # create tasks
    task_add2 = Task(add2)
    task_minus2 = Task(minus2)

    # test map
    task_add2.map(lambda value: 2 * value).fork(
        lambda _: None,
        lambda value: result.__setattr__('value', value)
    )

    # check result
    assert result.value == 6


# Generated at 2022-06-14 04:05:45.129749
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(
        lambda err: False,
        lambda val: val == 2
    )

# Generated at 2022-06-14 04:05:56.536464
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task
    """
    def assign_z(number):
        def result(resolve, reject):
            resolve(number * 7)

        return Task(result)

    def add_one(number):
        def result(resolve, reject):
            resolve(number + 1)

        return Task(result)

    def identity_function(number):
        return number

    # Check that map method work correctly
    assert Task.of(5).bind(identity_function).fork(lambda reject, resolve: resolve(1)) == 5
    assert Task.of(5).map(identity_function).fork(lambda reject, resolve: resolve(1)) == 5

    # Check that map method add one to number
    assert Task.of(5).bind(add_one).fork(lambda reject, resolve: resolve(1)) == 6

# Generated at 2022-06-14 04:06:01.906602
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(None, lambda x: x) == 2

    assert Task.reject(1).map(lambda x: x + 1).fork(lambda x: x, None) == 1


# Generated at 2022-06-14 04:06:06.282248
# Unit test for method bind of class Task
def test_Task_bind():
    def split_string(arg):
        return Task.of(arg.split())

    result = Task.of('Python JavaScript')
    result = result.bind(split_string)

    assert result.fork(_, _) == ['Python', 'JavaScript']

# Generated at 2022-06-14 04:07:44.362151
# Unit test for method map of class Task
def test_Task_map():
    """
    Test function map in Task.
    """
    def add_one(value):
        return value + 1

    def sub_two(value):
        return value - 2

    add_one_Task = Task.of(2).map(add_one)
    assert add_one_Task.fork(lambda _: False, lambda arg: arg == 3) is True

    sub_two_Task = add_one_Task.map(sub_two)
    assert sub_two_Task.fork(lambda _: False, lambda arg: arg == 1) is True


# Generated at 2022-06-14 04:07:49.822916
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(arg):
        if arg == 'error':
            raise Exception(arg)

        return Task(lambda _, resolve: resolve(arg))

    assert Task(lambda reject, resolve: resolve(1)) \
        .bind(lambda val: reject(val + 1)) \
        .fork(lambda val: None, lambda val: val) == 2
