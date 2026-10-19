

# Generated at 2022-06-14 03:58:04.699310
# Unit test for method bind of class Task
def test_Task_bind():
    def task_1(reject, resolve):
        resolve('hello')

    def task_2(reject, resolve):
        reject(42)


# Generated at 2022-06-14 03:58:11.077175
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for Task.map(fn) method:
    Should return Task.resolve(fn(stored_task_value))
    """
    value = 1
    task = Task.of(value).map(lambda arg: arg + 2)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 3


# Generated at 2022-06-14 03:58:18.080749
# Unit test for method bind of class Task
def test_Task_bind():
    def t():
        return Task.of(1)

    def te():
        return Task.reject(1)

    def f(value):
        return Task.of(value * 2)

    def fe(value):
        return Task.reject(value * 2)

    assert Task.of(1).bind(f).fork(lambda x: x, lambda x: x) == 2
    assert Task.of(1).bind(fe).fork(lambda x: x, lambda x: x) == 1
    assert t().bind(f).bind(fe).fork(lambda x: x, lambda x: x) == 2
    assert te().bind(f).bind(fe).fork(lambda x: x, lambda x: x) == 1



# Generated at 2022-06-14 03:58:23.221577
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        assert value == 10
        return value

    def reject(value):
        assert False

    assert Task.of(2).map(lambda arg: arg * 5).fork(reject, resolve)


# Generated at 2022-06-14 03:58:30.531188
# Unit test for method map of class Task
def test_Task_map():
    def assert_task_map_eq(arg, result):
        fork = lambda _, resolve: resolve(arg)
        task = Task(fork)
        test = task.map(lambda arg: arg + 2)
        assert test.fork(lambda _: None, lambda arg: arg) == result

    arg = 2
    assert_task_map_eq(arg, arg + 2)
    arg = True
    assert_task_map_eq(arg, arg)
    arg = "s"
    assert_task_map_eq(arg, arg)
    arg = []
    assert_task_map_eq(arg, arg)

    def assert_task_reject_eq(arg, result):
        fork = lambda reject, _: reject(arg)
        task = Task(fork)

# Generated at 2022-06-14 03:58:40.779735
# Unit test for method bind of class Task
def test_Task_bind():
    def result_mapper(value):
        return Task.of(value * value)

    def assert_fn(reject, resolve):
        def reject_assert(arg):
            assert arg == 'reject'

        def resolve_assert(arg):
            assert arg == 100

        reject(reject_assert('reject'))
        resolve(resolve_assert(100))

    assert Task(assert_fn).bind(result_mapper).fork(
        lambda arg: arg,
        lambda arg: arg
    )


# Generated at 2022-06-14 03:58:44.923162
# Unit test for method map of class Task

# Generated at 2022-06-14 03:58:49.924978
# Unit test for method map of class Task
def test_Task_map():
    def multiply(number: int) -> int:
        return number * 2

    def map_result(fn, arg, expected):
        assert Task(arg).map(fn).fork(None, None) == expected

    map_result(multiply, lambda _, resolve: resolve(1), 2)
    map_result(multiply, lambda _, resolve: resolve(2), 4)
    map_result(multiply, lambda _, resolve: resolve(5), 10)
    map_result(multiply, lambda _, resolve: resolve(10), 20)
    map_result(multiply, lambda _, resolve: resolve(17), 34)


# Generated at 2022-06-14 03:58:54.461967
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task.map method.
    """
    task_0 = Task.of(1)
    task_1 = task_0.map(lambda arg: arg + 1)

    assert task_1.fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 03:59:04.904926
# Unit test for method bind of class Task
def test_Task_bind():
    # Define counter for check, expand when task will called.
    calls = 0
    # Bind error to reject argument.
    def on_error(error):
        nonlocal calls
        # Increase bound.
        calls += 1
        # Return error value, hack for check assertEquals
        return error

    # Bind handled value to resolve argument.
    def on_result(result):
        nonlocal calls
        # Increase bound.
        calls += 1
        # Return result value, hack for check assertEquals
        return result

    # Define function, which return Task without errors
    def successful_task():
        return Task.of(1)

    # Define function, which return Task with errors
    def failure_task():
        return Task.reject('Error!')


# Generated at 2022-06-14 03:59:16.088520
# Unit test for method bind of class Task
def test_Task_bind():
    def test(fn_name):
        def call_fn(arg):
            fn = globals()[fn_name]
            return fn(arg)

        return Task(
            lambda reject, resolve: resolve(call_fn)
        ).bind(lambda arg: arg)

    # Call on not existing function
    global test_Task_bind
    assert test('test_Task_bind').fork(
        lambda arg: True,
        lambda arg: False
    )

    # Call on existing function
    test_Task_bind = lambda arg: arg
    assert test('test_Task_bind').fork(
        lambda arg: False,
        lambda arg: True
    )


# Generated at 2022-06-14 03:59:23.454668
# Unit test for method bind of class Task
def test_Task_bind():
    def test_mapper(value):
        assert isinstance(value, int)
        return Task.of(value + 1)

    assert Task.of(1).bind(test_mapper).fork(
        lambda err: False,
        lambda res: res == 2
    )
    assert Task.reject(1).bind(test_mapper).fork(
        lambda err: err == 1,
        lambda res: False
    )


# Generated at 2022-06-14 03:59:27.748616
# Unit test for method map of class Task

# Generated at 2022-06-14 03:59:33.983155
# Unit test for method map of class Task
def test_Task_map():
    def add(x, y):
        return x + y

    def add_one(x, y):
        return x + y + 1

    def add_three_times(x, y):
        return add(add(add(x, y), y), y)

    assert Task.reject(1).map(add).fork(
        lambda x: x,
        lambda y: y
    ) == 1

    assert Task.of(1).map(add_one).fork(
        lambda x: x,
        lambda y: y
    ) == 2

    assert Task.of(1).map(add_three_times).fork(
        lambda x: x,
        lambda y: y
    ) == 4


# Generated at 2022-06-14 03:59:45.703088
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task class
    """
    def task_resolve_1(resolve, reject):
        return resolve(1)

    def task_resolve_2(resolve, reject):
        return resolve(2)

    def task_reject_1(resolve, reject):
        return reject(1)

    def task_reject_2(resolve, reject):
        return reject(2)

    def task_map_resolve_1(resolve, reject):
        return resolve(lambda x: x * 2)

    def task_map_resolve_2(resolve, reject):
        return resolve(lambda x: x * 3)

    def task_map_reject_1(resolve, reject):
        return reject(lambda x: x * 2)


# Generated at 2022-06-14 03:59:54.560087
# Unit test for method map of class Task
def test_Task_map():
    def assert_map(function):
        # check that map store function
        def assert_mapper_stored(mapper):
            def assert_mapper_fork(reject, resolve):
                def assert_mapper(arg):
                    assert arg == "value"
                    return resolve("mapped")

                return mapper(reject, assert_mapper)

            mapped = function.map(mapper)
            mapped.fork(assert_mapper_fork, assert_mapper_fork)

        return assert_mapper_stored

    assert_Task_map = assert_map(Task.of("value"))
    assert_Task_map(assert_map(Task.of("value")).__func__)


# Generated at 2022-06-14 04:00:01.511589
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(_, resolve):
        resolve(1)

    # Now we have our task with resolve value 1
    task = Task(fork)

    def map_fn(value):
        def fork(_, resolve):
            resolve(value)
        return Task(fork)

    # If bind will return result of called function
    # it will return task with resolve value 1
    assert task.bind(map_fn).fork(
        lambda reject: reject('reject'),
        lambda resolve: resolve('resolve')
    ) == 'resolve'


# Generated at 2022-06-14 04:00:07.892318
# Unit test for method map of class Task
def test_Task_map():
    """
    Task -> map -> Task[resolve -> B]
    """
    js = Js(None)

    assert(js.evalJs(
        "var promise = new Promise(function(resolve, reject){ resolve('Hello'); });" +
        "var result = promise.then(function(value){ return value + ' ' + 'World!'; });"
    )) == 'Hello World!'

    assert(js.evalJs(
        "var promise = new Promise(function(resolve, reject){ resolve(42); });" +
        "var result = promise.then(function(value){ return value + 1; });"
    )) == 43

    task = Task.of(42).map(lambda value: value + 1)
    # -> Task[reject, resolve -> 43]
    assert(task.fork(js.str, js.str))

# Generated at 2022-06-14 04:00:10.424451
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method.
    """
    def resolve_adder(value):
        return Task.of(value + 1)

    task = Task.of(1)
    task = task.bind(resolve_adder)
    assert task.fork(
        lambda reject: None,
        lambda resolve: resolve
    ) == 2


# Generated at 2022-06-14 04:00:20.548294
# Unit test for method map of class Task
def test_Task_map():
    # pylint: disable=too-many-locals
    def test_foo(value):
        assert value == 42
        return 54

    def test_reject(value):
        assert value == 54
        return 79

    def test_resolve(value):
        assert value == 79
        return 906

    x = Task(lambda reject, resolve: resolve(42)).map(test_foo).fork(test_reject, test_resolve)
    y = Task(lambda reject, resolve: reject(42)).map(test_foo).fork(test_reject, test_resolve)
    assert x == 906
    assert y == 54

test_Task_map()



# Generated at 2022-06-14 04:00:34.209478
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    def task_of_add_one(resolve, reject):
        return resolve(add_one)

    def task_of_add_one_then_add_one(resolve, reject):
        return resolve(add_one(add_one))

    task_of_add_one(lambda _, value: print(value), lambda value: print(value))
    task_of_add_one_then_add_one(lambda _, value: print(value), lambda value: print(value))

# Generated at 2022-06-14 04:00:43.384082
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    @Task.of(None)
    def add_one_and_fork(resolve, reject):
        resolve(add_one(1))

    assert add_one_and_fork.map(add_one).fork(
        lambda reject_val: 'rejected',
        lambda resolve_val: resolve_val
    ) == 3

    @Task.reject(None)
    def reject_and_add_one(resolve, reject):
        reject(add_one(1))

    assert reject_and_add_one.map(add_one).fork(
        lambda reject_val: reject_val,
        lambda resolve_val: 'resolved'
    ) == 2


# Generated at 2022-06-14 04:00:50.997325
# Unit test for method map of class Task
def test_Task_map():

    def add1(x):
        return x + 1

    def err_in_map():
        raise ValueError('Error in map')

    # Case 1
    t1 = Task.of(5).map(add1)
    assert t1.fork(lambda _: False, lambda x: x == 6)

    # Case 2
    t2 = Task.of(5).map(err_in_map)
    assert t2.fork(lambda e: e == ValueError('Error in map'), lambda _: False)


# Generated at 2022-06-14 04:00:58.324619
# Unit test for method map of class Task
def test_Task_map():
    src_Task = Task.of(1)


# Generated at 2022-06-14 04:01:03.429458
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of('hello')
    task_after_bind = task.bind(lambda result: Task.reject(result + '!'))
    task_after_fork = task_after_bind.fork(lambda result: result, lambda result: result)
    assert 'hello!' == task_after_fork


# Generated at 2022-06-14 04:01:06.335507
# Unit test for method map of class Task

# Generated at 2022-06-14 04:01:14.460840
# Unit test for method map of class Task
def test_Task_map():
    # The test no need to check whether it is laziness of func_to_call
    # because it will be tested separately in test_fork.
    def assert_map(func_to_call, expected_value):
        called = False
        def call_map(arg):
            nonlocal called
            called = True
            return arg

        task = Task.of(func_to_call).map(call_map)
        result = task.fork(lambda _: None, lambda _: None)
        assert result is expected_value
        assert not called, "Function should not be called before fork"

    # success case
    assert_map(123, 123)
    assert_map((), ())
    assert_map([1, 2, 3], [1, 2, 3])

    # error case
    assert_map(None, None)

# Generated at 2022-06-14 04:01:25.939872
# Unit test for method bind of class Task
def test_Task_bind():
    def _get_user(user_id):
        return future("user")

    def _get_stat(user_id):
        return future("stat")

    def _get_repos(user_id):
        return future("repos")

    def _get_contribs(repo):
        return future("contribs")

    def render_repos(repos):
        return future("rendered repos")

    def render_profile(user, stat):
        return future("rendered profile")

    def render_contribs(contribs):
        return future("rendered contribs")

    get_user = Task.of(_get_user)
    get_stat = Task.of(_get_stat)
    get_repos = Task.of(_get_repos)

# Generated at 2022-06-14 04:01:32.686828
# Unit test for method bind of class Task
def test_Task_bind():
    def add(x):
        return Task.of(x + 1)

    def isOdd(x):
        return Task.of(bool(x % 2))

    assert Task.of(2).bind(add).bind(add).bind(add).bind(isOdd).fork(
        lambda x: False,
        lambda x: True
    )


# Generated at 2022-06-14 04:01:42.813134
# Unit test for method bind of class Task
def test_Task_bind():
    add_one = lambda x: x + 1
    assert Task.of(1).bind(lambda x: Task.reject(x)).fork(
        lambda x: 'rejected',
        lambda x: 'resolved'
    ) == 'rejected'
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(
        lambda x: 'rejected',
        lambda x: 'resolved'
    ) == 'resolved'
    assert Task.reject(1).bind(lambda x: Task.of(x + 1)).fork(
        lambda x: 'rejected',
        lambda x: 'resolved'
    ) == 'rejected'


# Generated at 2022-06-14 04:01:55.169209
# Unit test for method map of class Task
def test_Task_map():
    def mul3(value):
        return value * 3

    def fork(reject, resolve):
        return resolve(2)

    task = Task(fork).map(mul3)

    assert 6 == task.fork(lambda _: 0, lambda arg: arg)

# Generated at 2022-06-14 04:02:00.872231
# Unit test for method map of class Task
def test_Task_map():
    def func(a):
        return a * 2

    test_task = Task.of(2)
    assert test_task.fork(lambda _: None, lambda a: a) == 2
    new_task = test_task.map(func)
    assert new_task.fork(lambda _: None, lambda a: a) == 4


# Generated at 2022-06-14 04:02:06.492239
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve(1)

    task = Task(fork)

    def fn(value):
        return value + 1
    
    result = task.map(fn)

    assert result.fork(lambda x: x, lambda x: x) == 2



# Generated at 2022-06-14 04:02:09.622391
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('hello').map(lambda arg: arg + ' world').fork(
        lambda arg: None,
        lambda arg: arg
    ) == 'hello world'


# Generated at 2022-06-14 04:02:16.504803
# Unit test for method map of class Task
def test_Task_map():
    # Given
    fn_1 = lambda x: x + 1
    task_1 = Task.of(1)
    task_2 = task_1.map(fn_1)

    # When
    result_1 = task_1.fork(lambda _: None, lambda x: x)
    result_2 = task_2.fork(lambda _: None, lambda x: x)

    # Then
    assert result_1 == 1
    assert result_2 == 2

# Generated at 2022-06-14 04:02:21.455847
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.reject(value)

    value = 1
    result, equal = Task.of(value).bind(fn), Task.reject(value)
    assert equal.fork(lambda arg: arg, lambda arg: arg) == result.fork(lambda arg: arg, lambda arg: arg)


# Generated at 2022-06-14 04:02:27.837372
# Unit test for method bind of class Task
def test_Task_bind():

    def add(arg):
        return Task.of(arg + 1)

    task = Task.of(2)

    assert task.bind(add).bind(add).fork(
        lambda x: print(x, 'rejected', x == 3),
        lambda x: print(x, 'resolved', x == 4)
    )

    def contains(arg):
        return Task.of(arg in values)

    values = ['a', 'b', 'c']

    assert task.bind(add).bind(contains).fork(
        lambda x: print(x, 'rejected', x == 3),
        lambda x: print(x, 'resolved', x == True)
    )



# Generated at 2022-06-14 04:02:34.218663
# Unit test for method map of class Task
def test_Task_map():
    def delayed_success(x, callback):
        callback(None, x)

    def test_task_success():
        def promise_success(resolve, reject):
            delayed_success(42, lambda error, value: resolve(value))

        return Task(promise_success)

    assert test_task_success().map(lambda x: x + 1).map(lambda x: x * 3).fork(None, lambda x: x) == 129



# Generated at 2022-06-14 04:02:37.733361
# Unit test for method map of class Task
def test_Task_map():
    Task.of(2).map(lambda x: x * 2).fork(lambda _: 1, lambda x: x + 3)
    assert Task.of(2).map(lambda x: x * 2).fork(lambda _: 1, lambda x: x + 3) == 7


# Generated at 2022-06-14 04:02:46.870500
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task.bind is helper method that allow bind other Task to Task.

    Task accept two functions params during calling fork function
    First function is reject function.
    Second function is resolve function.
    """
    # Helper function with 3 params
    # Return new Task that resolve function with
    # stored params
    def map1(reject, resolve, value):
        return resolve(value)

    # Helper function with 3 params
    # Return new Task that reject function with
    # stored params
    def map2(reject, resolve, value):
        return reject(value)

    task1 = Task.of(1)
    task2 = Task(map1)
    task3 = Task(map2)
    task4 = Task.reject(1)

    # resolve values to 1

# Generated at 2022-06-14 04:03:06.942639
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(2).bind(lambda x: Task.of(x * 2)).fork(lambda x: x, lambda x: x) == 4

# Generated at 2022-06-14 04:03:12.372645
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:03:21.417175
# Unit test for method map of class Task
def test_Task_map():

    def dummyFn(x):
        return x

    def dummyFn2(x):
        return x * x

    # Test with resolved Task
    t1 = Task.of(2).map(dummyFn)
    t2 = Task.of(2).map(dummyFn2)

    assert t1.fork(None, lambda x: x) == 2
    assert t2.fork(None, lambda x: x) == 4

    # Test with rejected Task
    t3 = Task.reject(2).map(dummyFn)
    t4 = Task.reject(2).map(dummyFn2)

    assert t3.fork(lambda x: x, None) == 2
    assert t4.fork(lambda x: x, None) == 2


# Generated at 2022-06-14 04:03:29.792106
# Unit test for method map of class Task
def test_Task_map():
    """
    Check map function
    """
    def test_func(value):
        """
        Test function for map method.

        :param value: value to return
        :type value: A
        :returns: value
        :rtype: A
        """
        return value

    value = 1

    assert Task.of(value).map(lambda arg: arg).fork(None, lambda arg: arg) == value

    assert Task.of(value).map(test_func).fork(None, lambda arg: arg) == value


# Generated at 2022-06-14 04:03:34.473556
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task.of(x * x)

    def g(x):
        return Task.of(x + x)

    assert Task.of(10).bind(f).bind(g).fork(None, print) == 20

    # Test calling resolve function of task
    result = []
    Task.of(10).bind(f).bind(g).fork(None, lambda x: result.append(x))
    assert result == [20]

    # Test calling resolve function of task
    result = []
    Task.of(10).bind(f).bind(g).fork(lambda x: result.append(x), None)
    assert result == []


# Generated at 2022-06-14 04:03:45.638931
# Unit test for method bind of class Task
def test_Task_bind():
    def sum_two(n):
        return Task.of(n + 2)

    def sum_three(n):
        return Task.of(n + 3)

    def sum_two_and_three(n):
        return Task.of(n) \
            .bind(sum_two) \
            .bind(sum_three)

    def test(task):
        def is_equal(x):
            return x == 5

        return task.map(is_equal)

    fn = sum_two_and_three
    assert Task.of(0).bind(fn).fork(lambda _: False, lambda x: x) == True
    assert fn(0).fork(lambda _: False, lambda x: x) == True

# Generated at 2022-06-14 04:03:50.393304
# Unit test for method map of class Task
def test_Task_map():
    value = 1
    identity = lambda arg: arg
    increment = lambda arg: arg + 1

    task = Task.of(value)
    task = task.map(increment).map(increment).map(increment)

    assert task.map(identity).fork(lambda x: x, lambda y: y) == value + 3

test_Task_map()


# Generated at 2022-06-14 04:03:54.648585
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve("Hello World!")

    def mapper(value):
        return value + " MAPPPPPPPPP"

    task = Task(fork)
    result = task.map(mapper)

    assert result.fork(lambda _: "reject", lambda value: value) == "Hello World! MAPPPPPPPPP"


# Generated at 2022-06-14 04:04:00.102164
# Unit test for method map of class Task
def test_Task_map():
    """Check map method of Task"""
    result = None

    def resolve(value):
        nonlocal result
        result = value

    def reject(value):
        nonlocal result
        result = value

    def test(reject, resolve):
        resolve(5)

    task = Task(test).map(lambda value: value + 2)
    task.fork(reject, resolve)
    assert result == 7



# Generated at 2022-06-14 04:04:10.332805
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    value = True
    new_value = False
    error = ValueError('error')
    resolved_task = Task.of(value)
    rejected_task = Task.reject(error)

    def fork_resolved_task(reject, resolve):
        resolve(value)

    def fork_rejected_task(reject, _):
        reject(error)

    def fork_both(reject, resolve):
        reject(error)
        resolve(value)

    resolved_task = resolved_task.bind(lambda arg: Task.of(new_value))
    rejected_task = rejected_task.bind(lambda arg: Task.of(new_value))

    assert resolved_task.fork(lambda arg: value, lambda arg: new_value) is value

# Generated at 2022-06-14 04:04:54.906971
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(123)
        return 999

    def mapper(value):
        return Task.of(str(value))

    assert Task(fork).bind(mapper).fork(lambda _: None, lambda result: result) == "123"

# Generated at 2022-06-14 04:05:00.914788
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    Task accept fork function, resolve and reject functions.
    Task.fork execute fork function, and it should return result of calling resolve or reject.

    For resolving Task is used Task.of method.
    """
    assert Task.of(3).bind(lambda x: Task.of(x * 2)).fork(
        lambda x: x,
        lambda x: x * 2
    ) == 6



# Generated at 2022-06-14 04:05:07.675495
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve('timeout')

    task = Task(fork)
    task = task.map(lambda arg: arg + ' 100')

    assert task.fork(None,None) == task.bind(lambda arg: Task.of(arg + ' 200')).fork(None,None)
    return task.fork(None,None)


# Generated at 2022-06-14 04:05:11.690595
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1).bind(lambda x: Task.of(x + 1))
    assert task.fork(lambda x: x ** 2, lambda x: x ** 3) == 4


# Generated at 2022-06-14 04:05:19.772376
# Unit test for method map of class Task
def test_Task_map():

    def mapper(v):
        return v + 'p'

    rejected = Task.reject('t')
    resolved = Task.of('t')
    assert rejected.fork(identity, identity) == rejected.map(mapper).fork(identity, identity) == 't'
    assert resolved.fork(identity, identity) == resolved.map(mapper).fork(identity, identity) == 'tp'


# Generated at 2022-06-14 04:05:21.460706
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value * 2)

    task = Task.of(5).bind(fn).fork(lambda value: value, lambda value: value)

    assert task == 10

# Generated at 2022-06-14 04:05:28.760163
# Unit test for method bind of class Task
def test_Task_bind():
    test_func = lambda arg: arg + 10
    task = Task.of(100).bind(test_func)

    assert (task.fork(None, None) == 110)

    def task_content(reject, resolve):
        print("This is from task")
        pass

    task_obj = Task(task_content)

    task_obj_1 = task_obj.bind(test_func)

    assert task_obj_1.fork(None, None) == None


# Generated at 2022-06-14 04:05:39.628320
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test that method bind of class Task call async function and
    returns resolved Task with result of function.
    """
    def add_one(value):
        """
        Add one to input parameter

        :param value: some number
        :type value: int
        :returns: value + 1
        :rtype: int
        """
        return value + 1

    @gen.coroutine
    def async_add_one(value):
        """
        Add one to input parameter asyncly.

        :param value: some number
        :type value: int
        :returns: value + 1
        :rtype: int
        """
        result = yield gen.Task(lambda callback: (time.sleep(2), callback(value + 1)))
        raise gen.Return(result)


# Generated at 2022-06-14 04:05:45.561167
# Unit test for method bind of class Task
def test_Task_bind():
    """
    1st test:
        `fork` function calls `reject` with argument `"Parse error"`
        `map` return new Task with loaded `fork` function
        `bind` return Task with loaded `fork` function
        in `fork` function `reject` call with argument `"Parse error"`
    2nd test:
        `fork` function calls `resolve` with argument `"Hello World"`
        `map` return new Task with loaded `fork` function
        `bind` return Task with loaded `fork` function
        in `fork` function `resolve` call with argument `"Hello World"`
    """
    def fork(reject, resolve):
        return reject("Parse error")

    def fn(value):
        return Task.of(value)


# Generated at 2022-06-14 04:05:51.742958
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(10)

    task = Task(fork)

    def mapper(value):
        return Task(lambda reject, resolve: resolve(value + 1))

    assert task.bind(mapper).fork(lambda x: None, lambda x: x) == 11, 'Test fail'



# Generated at 2022-06-14 04:07:29.126617
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.reject(1).bind(lambda value: Task.of(value + 1))
    assert task.fork(
        lambda rejected_value: rejected_value == 1,
        lambda _: False
    )

    task = Task.of(1).bind(lambda value: Task.of(value + 1))
    assert task.fork(
        lambda _: False,
        lambda accepted_value: accepted_value == 2
    )


# Generated at 2022-06-14 04:07:33.938933
# Unit test for method map of class Task
def test_Task_map():
    def test(arg):
        assert arg == 'foo'
        return 'bar'


# Generated at 2022-06-14 04:07:45.390847
# Unit test for method map of class Task
def test_Task_map():
    """
    test_Task_map: execute 5 test cases
    """
    def _test_Task_map(value):
        """
        :param value: value for check
        :type value: Any
        """
        assert len(value) == 4
        assert value[1] == 10
        assert value[3] == 5

    def _test_Task_map_deep(value):
        """
        :param value: value for check
        :type value: Any
        """
        assert len(value) == 4
        assert value[0] == 1

    @predicate
    def _test_Task_map_deep_reject(x):
        """
        :param x: value for check
        :type x: Any
        """
        assert x == "foo"

    # Test case: map function and check result

# Generated at 2022-06-14 04:07:56.399758
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task.
    Function multiply by two given value and call next binded function with result.
    Next binded function multiply by two given value and call next binded function with result.
    Next binded function return given value.
    Result of test is function for create Task with multiply by 2 value, given multipliers
    """
    def test(a, b):
        def multiply(x):
            return x * 2

        return Task.of(a) \
            .bind(lambda x: Task.of(multiply(x))) \
            .bind(lambda x: Task.of(multiply(x) * b))

    assert test(2, 4).fork(lambda _: None, lambda arg: arg) == 16