

# Generated at 2022-06-14 03:57:53.222357
# Unit test for method bind of class Task
def test_Task_bind():
    fetched_number = Task.of(1)

    def fetcher(number):
        return Task.of("Number is " + str(number))

    fetched_text = fetched_number.bind(fetcher)

    def assert_is_succesful(result):
        assert result == "Number is 1"

    def assert_is_failed(error):
        assert False

    fetched_text.fork(assert_is_failed, assert_is_succesful)


# Generated at 2022-06-14 03:58:03.286643
# Unit test for method bind of class Task
def test_Task_bind():
    counter = 0

    def call_counter():
        """
        Increment counter and return it.
        """
        nonlocal counter
        counter += 1
        return counter

    # bind call_counter
    task_counter = Task.of(call_counter)
    # get counter
    task_counter = task_counter.bind(lambda call_counter: Task.of(call_counter()))
    # get counter again
    task_counter = task_counter.bind(lambda call_counter: Task.of(call_counter()))

    # counter must be 2 now
    assert task_counter.fork(None, None) == 2


# Generated at 2022-06-14 03:58:10.642057
# Unit test for method bind of class Task
def test_Task_bind():
    def identity_mapper(value):
        return value

    assert Task.of(1).map(identity_mapper).fork(identity_mapper, identity_mapper) == 1
    assert Task.reject(1).map(identity_mapper).fork(identity_mapper, identity_mapper) == 1

    def mapper(value):
        """
        Take value, convert to one and return new Task with it.
        """
        return Task.of(value + 1)

    assert Task.of(1).bind(mapper).fork(identity_mapper, identity_mapper) == 2
    assert Task.reject(1).bind(mapper).fork(identity_mapper, identity_mapper) == 1


# Generated at 2022-06-14 03:58:19.301257
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve_mapper(value):
        return Task.of(value + 1)

    def rejected_mapper(value):
        return Task.reject(value + 1)

    assert Task.of(2).bind(resolve_mapper).fork(_, resolve) == 3
    assert Task.of(2).bind(rejected_mapper).fork(reject, _) == 3

    assert Task.reject(2).bind(resolve_mapper).fork(reject, _) == 3
    assert Task.reject(2).bind(rejected_mapper).fork(reject, _) == 3


# Generated at 2022-06-14 03:58:23.221759
# Unit test for method map of class Task
def test_Task_map():
    to_str = lambda x: str(x)
    task = Task.of(5)
    mapped_task = task.map(to_str)
    assert mapped_task.fork(None, lambda val: val) == '5'


# Generated at 2022-06-14 03:58:26.217160
# Unit test for method map of class Task
def test_Task_map():
    value = Task.of(1).map(lambda x: x + 1)
    assert value.fork(None, lambda x: x) == 2, \
        "Task must map value by passed function"


# Generated at 2022-06-14 03:58:39.498457
# Unit test for method bind of class Task
def test_Task_bind():
    # reject case
    value_A = {'foo': 'bar'}

# Generated at 2022-06-14 03:58:41.592639
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2)
    task = task.map(lambda a: a * a)
    assert task.fork(None, lambda resolve: resolve) == 4


# Generated at 2022-06-14 03:58:48.901152
# Unit test for method map of class Task
def test_Task_map():
    def assert_task(task, expected_value):
        def assert_task_fork(reject, resolve):
            resolve_called = False
            reject_called = False

            def inner_reject(arg):
                nonlocal reject_called
                reject_called = True

            def inner_resolve(arg):
                nonlocal resolve_called
                resolve_called = True
                assert arg == expected_value

            task.fork(inner_reject, inner_resolve)
            assert reject_called is False
            assert resolve_called is True

        Task(assert_task_fork)

    assert_task(
        Task.of(1).map(lambda a: a + 1),
        2
    )

    assert_task(
        Task.reject(1).map(lambda a: a + 1),
        None
    )




# Generated at 2022-06-14 03:58:54.362596
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        return value

    def reject(value):
        return value

    def add_one(value):
        return value + 1

    task = Task.of(1)
    assert task.fork(reject, resolve) == 1

    assert task.map(add_one).fork(reject, resolve) == 2

# Generated at 2022-06-14 03:59:08.200764
# Unit test for method bind of class Task
def test_Task_bind():
    def lift_a(value):
        return Task.of(value)

    def lift_b(value):
        return Task.reject(value)

    assert Task.of(2).map(lambda x: x * 3).fork(lambda x: x * 2, lambda x: x * 2) == 12

    assert Task.of(2).bind(lift_a).fork(lambda x: x * 2, lambda x: x * 2) == 4

    assert Task.of(2).bind(lambda x: Task.of(x * 3)).fork(lambda x: x * 2, lambda x: x * 2) == 12

    assert Task.of(2).bind(lift_b).fork(lambda x: x * 2, lambda x: x * 2) == 4


# Generated at 2022-06-14 03:59:13.991456
# Unit test for method map of class Task
def test_Task_map():
    def run_task(note):
        def fork(_, resolve):
            resolve(note)

        return Task(fork)
    test_value = 'Test'
    task = run_task(test_value)
    new_task = task.map(lambda value: value.upper())
    assert test_value == new_task.fork(lambda _: None, lambda value: value)


# Generated at 2022-06-14 03:59:18.063678
# Unit test for method bind of class Task
def test_Task_bind():
    """
    >>> task = Task.of(2)
    >>> task.bind(lambda x: Task.of(x + 2)).fork(print, print)
    4
    """


# Generated at 2022-06-14 03:59:25.088292
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(3)
    task = Task(fork)
    def if_success(resolve):
        return resolve(task.value * 7)
    def if_fail(reject):
        return reject(task.value * 5)
    new_task = task.bind(if_success)
    assert new_task.fork(if_fail, if_success).value == 21

## Test for method map of class Task

# Generated at 2022-06-14 03:59:30.521874
# Unit test for method bind of class Task
def test_Task_bind():
    @gen.coroutine
    def callback1():
        raise gen.Return(Task.of('test1'))

    @gen.coroutine
    def callback2():
        raise gen.Return(Task.of('test2'))

    def assert_result(resolve, reject):
        def _callback(result):
            assert result == 'test2'

        _resolve = CallBack.of(callback1).map(callback2).fork(reject, _callback)



# Generated at 2022-06-14 03:59:32.938924
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    task = Task.of(111)
    result = task.map(add_one).fork(lambda error: error, lambda value: value)

    assert result == 112



# Generated at 2022-06-14 03:59:42.982036
# Unit test for method map of class Task
def test_Task_map():
    def add(a):
        return a + 10

    def add_and_throw(a):
        raise ValueError('Add and throw error')

    task = Task.of(10)
    task = task.map(add)
    assert task.fork(lambda _: False, lambda b: b == 20)

    task = Task.of(10)
    task = task.map(add_and_throw)
    assert task.fork(lambda err: isinstance(err, ValueError), lambda _: False)

    task = Task.reject(20)
    task = task.map(add)
    assert task.fork(lambda err: err == 20, lambda _: False)


# Generated at 2022-06-14 03:59:46.882284
# Unit test for method bind of class Task
def test_Task_bind():
    def set_true(value):
        return Task.of({'input': value, 'output': True})

    def set_false(value):
        return Task.reject({'input': value, 'output': False})

    assert Task.of(1).bind(set_true).fork(
        lambda x: None,
        lambda x: x
    ) == {'input': 1, 'output': True}

    Task.of(1).bind(set_false).fork(
        lambda x: x,
        lambda x: x
    ) == {'input': 1, 'output': False}



# Generated at 2022-06-14 03:59:50.911545
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        print("resolve: ", value)

    def reject(error):
        print("reject: ", error)

    Task.of(5) \
        .map(lambda x: x ** 2) \
        .fork(reject, resolve)


# Generated at 2022-06-14 03:59:57.251595
# Unit test for method bind of class Task
def test_Task_bind():
    def function():
        return Task.reject(Exception('error'))

    assert Task.of(1).bind(function).fork(lambda arg: arg[0], lambda _: False) == Exception('error')
    assert Task.of(1).bind(function).fork(lambda _: False, lambda arg: arg[0]) == 1



# Generated at 2022-06-14 04:00:06.738439
# Unit test for method bind of class Task
def test_Task_bind():

    range_tasks = [Task.of(num) for num in [1, 2]]

    # Get list of Task of promises transfered from range_tasks
    bind_tasks = reduce(
        lambda task, num: task.bind(
            lambda befores: Task.of(befores + [num])
        ),
        [],
        range_tasks
    )

    def result(reject, resolve):
        return bind_tasks.fork(
            lambda x: reject(x),
            lambda x: resolve(x)
        )

    bind_task = Task(result)
    # End of unit test

    assert bind_task.fork(None, lambda x: x) == [[1, 2]]


# Generated at 2022-06-14 04:00:15.972891
# Unit test for method map of class Task
def test_Task_map():
    # Task[Function(_, resolve) -> A]
    task = Task.of(1)
    # Task[Function(resolve, _) -> A]
    task1 = Task.reject(1)
    # Function(value) -> B
    mapper = lambda x: x + 1

    # Task[Function(resolve, reject -> A | B]
    task2 = task.map(mapper)
    # Task[Function(resolve, reject -> Any)
    task3 = task1.map(mapper)

    assert task2.fork(identity, identity) == 2
    assert task3.fork(identity, identity) == 1


# Generated at 2022-06-14 04:00:20.553169
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(arg):
        return Task.of(arg + 1)

    def fork(reject, resolve):
        return resolve(Task.of(1).bind(mapper))

    assert Task(fork).fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 04:00:26.047347
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(2).bind(lambda x: Task.of(x + 1))
    assert task.fork(lambda x: None, lambda x: x) == 3

    def fork(reject, resolve):
        raise Exception('test')

    task = Task(fork).map(lambda x: x).bind(lambda x: Task.of(x + 1)).bind(lambda x: Task.of(x + 1))
    assert task.fork(lambda x: None, lambda x: x) is None

# Generated at 2022-06-14 04:00:32.856560
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task.
    """
    def tested_function(arg):
        return Task.of(arg)

    def onFulfilled(value):
        return value

    def onRejected(value):
        return value

    task = Task.of(42)

    assert task.bind(tested_function).fork(onRejected, onFulfilled) == 42

# Generated at 2022-06-14 04:00:41.094634
# Unit test for method bind of class Task
def test_Task_bind():
    """
    This test check bind method of Task class.
    """
    def fn(value):
        return Task.resolve(value + 1)

    def fn_reject(value):
        return Task.reject(value + 1)

    def check_reject(value):
        assert value == 3

    def check_resolve(value):
        assert value == 2

    Task.of(1).bind(fn).bind(fn).fork(check_reject, check_resolve)
    Task.of(1).bind(fn_reject).bind(fn).fork(check_reject, check_resolve)


# Generated at 2022-06-14 04:00:52.008918
# Unit test for method map of class Task
def test_Task_map():
    def add_unit(x):
        return x + 1

    def mul_unit_2(x):
        return x * 2

    def mul_unit_3(x):
        return x * 3

    def div_unit_3(x):
        if x == 0:
            return Task.reject(ZeroDivisionError("division by zero"))
        else:
            return Task.of(x / 3)

    # Error during execution
    assert Task(lambda reject, _: reject(ZeroDivisionError("division by zero"))) \
        .map(add_unit) \
        .fork(lambda e: e.args, lambda v: v) == ("division by zero",)

    assert Task(lambda reject, _: reject(ZeroDivisionError("division by zero"))) \
        .map(mul_unit_2) \
       

# Generated at 2022-06-14 04:00:58.483701
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method
    """
    task = Task.of(1)
    task = task.map(lambda arg: arg + 1)
    task = task.map(lambda arg: arg + 1)

    result = task.fork(
        lambda arg: arg,
        lambda arg: arg,
    )

    assert result == 3

test_Task_bind()

# Generated at 2022-06-14 04:01:05.912455
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(40)
    task = task.map(lambda v: v + 1)

    assert task.fork(None, lambda v: v) == 41

    task = Task.of(40)
    task = task.bind(
        lambda v: Task.of(v + 100)
                  .bind(
                      lambda v2: Task.of(v2 + 200)
                  )
    )

    assert task.fork(None, lambda v: v) == 340


# Generated at 2022-06-14 04:01:10.432582
# Unit test for method map of class Task
def test_Task_map():
    def my_mapper(value):
        return value + 10

    my_initial_task = Task.of(10)
    map_result = my_initial_task.map(my_mapper)
    assert map_result.fork(lambda _, resolve: resolve(0), lambda _, reject: reject(0)) == 20



# Generated at 2022-06-14 04:01:26.312074
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind method of Task class.
    """
    def add(a):
        return Task.of(a + 1)

    def mul(a):
        return Task.of(a * 2)

    def div(a):
        return Task.of(a / 2)

    def error_add(a):
        return Task.of(a / 0)

    assert Task.of(1).bind(add).bind(mul).bind(div).fork(lambda _: None, lambda arg: arg) == 2
    assert Task.of(1).bind(add).bind(mul).bind(error_add).fork(lambda _: None, lambda arg: arg) is None

# Generated at 2022-06-14 04:01:39.784974
# Unit test for method map of class Task
def test_Task_map():
    # All Task stored in this list is unresolved, because we don't call fork method
    # We will store resolved value of Task after calling fork
    # and check equality with expected value.
    results = []

    def test_map(resolve, reject):
        def callback(value):
            results.append(value)

        Task.of(1).map(lambda x: x + 2).fork(reject, callback)
        Task.of(2).map(lambda x: x * 2).fork(reject, callback)
        Task.of(3).map(lambda x: x ** 2).fork(reject, callback)
        Task.reject('not valid').map(lambda _: True).fork(reject, callback)
        Task.reject('not valid').map(lambda _: True).fork(callback, reject)

    # Call test_map

# Generated at 2022-06-14 04:01:49.841167
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method

    :returns: nothing
    :rtype: None
    """
    def duplicate(arg):
        print("duplicate fn call with: {}".format(arg))
        return Task.of(arg * 2)

    def double(arg):
        print("double fn call with: {}".format(arg))
        return Task.of(arg / 2)

    def rejected():
        print("reject fn call")
        return Task.reject("reject fn call")

    def reject_double(arg):
        print("reject_double call with: {}".format(arg))
        return Task.reject(arg * 2)

    # Test for result of Task
    assert Task.of(100).bind(duplicate).bind(double).fork(lambda arg: arg, lambda arg: arg)

# Generated at 2022-06-14 04:01:54.955100
# Unit test for method bind of class Task
def test_Task_bind():
    def f1(x):
        return x + 1

    def f2(x):
        return Task.of(x * 2)

    def f3(x):
        return x * 3


# Generated at 2022-06-14 04:02:00.252997
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    Task.of(2).bind(lambda x: Task.of(x * 3)).fork(
        lambda err: print(err),
        lambda res: print(res)
    )

#Unit test for method of of class Task

# Generated at 2022-06-14 04:02:12.802441
# Unit test for method bind of class Task
def test_Task_bind():
    """Unit test for Task.bind"""
    def logger(arg):
        """
        Logger for test Task.bind

        :param arg: argument to log
        :type arg: Any
        :returns: arg with log information
        :rtype: Any
        """
        print(arg)
        return arg

    def fn(arg):
        """
        Function for test Task.bind

        :param arg: value to process
        :type arg: Any
        :returns: new Task with given argument
        :rtype: Task[reject, resolved]
        """
        return Task.of(arg)

    # Case of call bind with task that is resolve
    result = Task.of(1)
    result = result.bind(fn)
    result.fork(logger, logger)

    # Case of call bind with task that is rejected

# Generated at 2022-06-14 04:02:16.380032
# Unit test for method bind of class Task
def test_Task_bind():
    curried_function = lambda a: lambda b: str(a) + str(b)
    bind_function = lambda value: Task.of(curried_function(value))
    assert Task.bind(
        Task.of(1),
        bind_function
    ).fork(lambda _: _, lambda _: _)(2) == '12'



# Generated at 2022-06-14 04:02:25.470659
# Unit test for method bind of class Task
def test_Task_bind():

    def double(x):
        return x * 2

    def even_adjacent_sum(a, b):
        def isEven(x):
            return x % 2 == 0

        if not isEven(a) or not isEven(b):
            return Task.reject(ValueError("not even"))

        return Task.of(a + b)

    def task_example():
        def double_even(x):
            return Task.of(x).bind(double).bind(double).bind(even_adjacent_sum)

        # Expected result: 24
        double_even(2).fork(print, print)

        # Expected result: ValueError("not even")
        double_even(3).fork(print, print)

    task_example()


# Generated at 2022-06-14 04:02:36.057147
# Unit test for method bind of class Task
def test_Task_bind():
    def success_function(arg):
        return arg + 1

    def failure_function(arg):
        if arg < 0:
            return Task.of(arg)
        else:
            return Task.reject(arg)

    assert(
        Task.of(1).bind(success_function).fork(
            lambda x: x,
            lambda x: x
        ) == 2
    )

    assert(
        Task.reject(1).bind(failure_function).fork(
            lambda x: x,
            lambda x: x
        ) == 1
    )

    assert(
        Task.reject(-1).bind(failure_function).fork(
            lambda x: x,
            lambda x: x
        ) == -1
    )


# Generated at 2022-06-14 04:02:40.366181
# Unit test for method map of class Task
def test_Task_map():

    f = lambda _: True
    g = lambda _: False

    task = Task.of(True)
    other = Task.of(True)

    assert task.map(f).fork(g, f)
    assert task.map(f) == other.map(f)



# Generated at 2022-06-14 04:02:55.346087
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(12)

    mapped = task.map(lambda x: x * 2)

    assert mapped.fork(lambda x: x, lambda x: x) == 24



# Generated at 2022-06-14 04:03:04.944375
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    def multiply_by_two(value):
        return value * 2

    def add_two_and_multiply_by_two(value):
        return value + 2 * 2

    assert Task.of(1).map(add_one).fork(
        lambda value: 0,
        lambda value: value
    ) == 2

    assert Task.of(1).map(multiply_by_two).fork(
        lambda value: 0,
        lambda value: value
    ) == 2

    assert Task.of(1).map(add_one).map(multiply_by_two).fork(
        lambda value: 0,
        lambda value: value
    ) == 4


# Generated at 2022-06-14 04:03:10.170048
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 1

    resolve_method_called = False

    def resolve(value):
        nonlocal resolve_method_called
        assert value == 'ok'
        resolve_method_called = True

    reject_method_called = False

    def reject(value):
        nonlocal reject_method_called
        assert False

    def fork(reject, resolve):
        resolve('ok')

    task = Task(fork)
    task.map(mapper).fork(reject, resolve)

    assert resolve_method_called
    assert not reject_method_called


# Generated at 2022-06-14 04:03:20.321002
# Unit test for method bind of class Task
def test_Task_bind():
    def add1(arg):
        return Task.of(arg + 1)

    def add2(arg):
        return Task.of(arg + 2)

    def reduce(arg):
        return Task.of(arg - 1)

    t = Task.of(1)

    r1 = t.bind(add1).fork(
        lambda reject: "rejected: " + str(reject),
        lambda resolve: "resolved: " + str(resolve)
    )

    assert(r1 == "resolved: 2")

    r2 = t.bind(add1).bind(add2).fork(
        lambda reject: "rejected: " + str(reject),
        lambda resolve: "resolved: " + str(resolve)
    )

    assert(r2 == "resolved: 3")


# Generated at 2022-06-14 04:03:32.230692
# Unit test for method bind of class Task
def test_Task_bind():
    def add(x):
        return Task.of(x + 1)

    def math(x):
        return x * 2

    def is_number(x):
        return isinstance(x, (int, float))

    def multiply_by_two(x):
        return Task.of(x * 2)

    def sub(x):
        return Task.of(x - 1)

    assert_equal(Task(lambda reject, resolve: resolve(2)).bind(add).bind(multiply_by_two).fork(lambda x: None, lambda x: x + 1), 7)
    assert_equal(Task(lambda reject, resolve: resolve(2)).bind(add).bind(multiply_by_two).fork(lambda x: None, lambda x: x + 1), 7)

# Generated at 2022-06-14 04:03:35.518614
# Unit test for method map of class Task
def test_Task_map():
    def test(value):
        assert value == 1


# Generated at 2022-06-14 04:03:46.539381
# Unit test for method bind of class Task
def test_Task_bind():

    # It should return rejected Task when calling bind function.
    # It should return rejected Task with correct value.
    @Task.reject.bind
    def fn(value):
        return Task.reject(value + 1)

    assert isinstance(fn, Task)
    assert fn.fork(lambda x: x, lambda _: None) == 0

    # It should return resolved Task when calling bind function.
    # It should return resolved Task with correct value.
    @Task.of.bind
    def fn(value):
        return Task.of(-value)

    assert isinstance(fn, Task)
    assert fn.fork(lambda _: None, lambda x: x) == 0

    # It should return rejected Task when calling bind function.
    # It should return rejected Task with correct value.

# Generated at 2022-06-14 04:03:49.010876
# Unit test for method map of class Task
def test_Task_map():
    def test(param):
        return param + 1

    assert Task.of(0).map(test).fork(None, lambda value: value) == 1


# Generated at 2022-06-14 04:03:51.483172
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task = task.map(lambda arg: arg + 1)

    assert task.fork(None, sum) == 2


# Generated at 2022-06-14 04:03:59.223421
# Unit test for method bind of class Task
def test_Task_bind():
    def x2(x):
        return Task.of(x * 2)

    def x2_reject(x):
        return Task.reject(x * 2)

    task = Task.of(1).bind(x2).bind(x2).bind(x2)
    assert task.fork(None, lambda x: x) == 8

    task = Task.of(2).bind(x2_reject)
    assert task.fork(lambda x: x, None) == 4

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 04:04:30.639801
# Unit test for method bind of class Task
def test_Task_bind():
    # call resolve function, stored in Task with stored value argument
    assert Task.of('Hi') \
        .bind(lambda val: Task.of(val))\
        .fork(None, lambda val: assertEquals(val, 'Hi')) is None

    # call reject function, stored in Task with stored value argument
    assert Task.reject('Hi') \
        .bind(lambda val: Task.of(val))\
        .fork(lambda val: assertEquals(val, 'Hi'), None) is None


# Generated at 2022-06-14 04:04:36.252647
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    task = Task.of(2)
    new_task = task.bind(lambda num: Task.of(num * 2))
    assert new_task.fork(lambda _: False, lambda val: val == 4)


# Generated at 2022-06-14 04:04:41.509893
# Unit test for method map of class Task
def test_Task_map():
    def test_case(test, result):
        assert test.fork(lambda reject, resolve: resolve(None), lambda value: result) == result

    def add_one(value):
        return value + 1

    test_case(Task(lambda reject, resolve: resolve(1)).map(add_one), 2)
    test_case(Task.of(1).map(add_one), 2)


# Generated at 2022-06-14 04:04:47.012683
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind
    """
    def test_case(a):
        if a:
            return Task.of(None)
        return Task.reject(None)

    def task(a):
        return Task.of(a).bind(test_case)

    resolved_task = task(True)
    rejected_task = task(False)

    assert resolved_task.fork(_is_rejected, _is_resolved)
    assert rejected_task.fork(_is_resolved, _is_rejected)



# Generated at 2022-06-14 04:04:49.986044
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    mapped = task.map(lambda x: x + 1)

    assert mapped.fork(None, lambda x: x) == 2


# Generated at 2022-06-14 04:05:01.428724
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(3)

    def test_bind_1(value):
            return Task.of(str(value))

    def test_bind_2(value):
            return Task.of(value + 5)

    def test_bind_3(value):
        if len(value) > 10:
            return Task.reject("Input value is too long")
        else:
            return Task.of(value + " is correct")

    test_task = Task(fork)
    assert Task.of("3 is correct").fork(lambda arg: arg, lambda arg: arg) == test_task.bind(test_bind_1).bind(test_bind_2).bind(test_bind_3).fork(lambda arg: arg, lambda arg: arg)

# Generated at 2022-06-14 04:05:06.503156
# Unit test for method map of class Task
def test_Task_map():
    result = Task.of(1).map(lambda arg1: arg1 + 1)
    fork(result)

    result = Task.reject(1).map(lambda arg1: arg1 + 1)
    fork(result)


# Generated at 2022-06-14 04:05:15.693414
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value + 1)

    def equal(x, y):
        assert all(x[0] == y[0] and x[1] == y[1] for x, y in zip(x, y))

    with open('result1.txt', mode='w') as file:
        for x in [1, 2, 3, 4, 5, 6]:
            value = Task.of(x).bind(fn).fork(
                lambda arg: "next",
                lambda arg: arg
            )
            print(value, file=file)

    with open('result1_expect.txt', mode='w') as file:
        for x in [1, 2, 3, 4, 5, 6]:
            print(x + 1, file=file)


# Generated at 2022-06-14 04:05:23.513232
# Unit test for method map of class Task
def test_Task_map():
    """
    Test check correct working of map method.
    """
    def multiply(x: int) -> int:
        return x * 2

    task = Task.of(2)
    assert task.fork(lambda x: x, lambda x: x) == 2

    mapped_task = task.map(multiply)
    assert mapped_task.fork(lambda x: x, lambda x: x) == 4


# Generated at 2022-06-14 04:05:33.941601
# Unit test for method bind of class Task
def test_Task_bind():
    def test_1(resolve, reject):
        return resolve(2)

    def test_2(resolve, reject):
        return resolve(7)

    def test_3(resolve, reject):
        return resolve(5)

    task_1 = Task(test_1)
    task_2 = Task(test_2)
    task_3 = Task(test_3)

    def fn_1(value):
        return fn_2(value)

    def fn_2(value):
        return task_2

    def fn_3(value):
        return task_3

    task_1.bind(fn_1).fork(lambda _: print('error 1'), lambda value: print(value))
    task_1.bind(fn_2).fork(lambda _: print('error 2'), lambda value: print(value))


# Generated at 2022-06-14 04:06:34.169497
# Unit test for method bind of class Task
def test_Task_bind():
    def function(value):
        return Task.of(value * 2)

    task = Task.of(1).bind(function)

    def fork(reject, resolve):
        return task.fork(reject, resolve) == task.fork(reject, resolve)

    test.expect(fork(lambda _: False, lambda arg: arg == function(1).fork(reject, resolve)))


# Generated at 2022-06-14 04:06:43.658762
# Unit test for method bind of class Task
def test_Task_bind():
    """
    `Task.bind` creating new Task that with unbound value, that will be
    resolved or rejected by next fork function call.
    """
    hello = lambda name: Task.of('Hello ' + name)

    world = Task.of(1).map(lambda _: Task.of('world'))
    assert world.fork(lambda _: '', lambda value: value) == 'world'

    _world_ = Task.of(1).map(lambda _: 'world')
    assert _world_.fork(lambda _: '', lambda value: value) == 'world'

    hello_world = Task.of('world').bind(hello)
    assert hello_world.fork(lambda _: '', lambda value: value) == 'Hello world'

# Generated at 2022-06-14 04:06:49.235048
# Unit test for method map of class Task
def test_Task_map():

    def resolve_mapper(value):
        return ["a", value]

    test_resolve = Task.of(1)
    assert test_resolve.fork(None, resolve_mapper) == ["a", 1]

    def reject_mapper(value):
        return (value, 11)

    test_reject = Task.reject(2)
    assert test_reject.fork(reject_mapper, None) == (2, 11)



# Generated at 2022-06-14 04:06:59.295032
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task(lambda _, resolve: resolve(x + 1))

    def g(x):
        return Task(lambda _, resolve: resolve(x * 2))

    def h(x):
        return Task(lambda _, resolve: resolve(x - 1))

    def assert_result_is_nine(res):
        assert res == 9

    def assert_result_is_five(res):
        assert res == 5

    Task.of(1) \
        .bind(f) \
        .bind(g) \
        .bind(h) \
        .fork(lambda res: False, assert_result_is_nine)


# Generated at 2022-06-14 04:07:00.866031
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1).bind(lambda x: Task.of(x + 2))

    assert [task.fork(lambda x: x, lambda x: x)] == [3]



# Generated at 2022-06-14 04:07:08.814739
# Unit test for method map of class Task
def test_Task_map():
    # Arrange
    def succeed(value):
        return Task.of(value)

    def failed(value):
        return Task.reject(value)

    # Act
    result = succeed(1).map(lambda value: value + 1).map(lambda value: value + 1)

    # Assert

# Generated at 2022-06-14 04:07:12.982109
# Unit test for method bind of class Task
def test_Task_bind():
    def test_case(arg):
        def fork(resolve, reject):
            resolve(arg)
        return Task(fork)

    assert Task.of(1).bind(test_case).fork(lambda _: None, lambda result: result) == 1


# Generated at 2022-06-14 04:07:21.861981
# Unit test for method map of class Task
def test_Task_map():
    """
    :returns: Unit test result
    :rtype: Bool
    """
    def mul_by_2(x):
        """
        :param x: argument value
        :type x: Int
        :returns: x * 2
        :rtype: Int
        """
        return x * 2

    task = Task.of(1)
    assert task.map(mul_by_2).fork(None, lambda v: v) == 2

    return True


# Generated at 2022-06-14 04:07:27.372674
# Unit test for method map of class Task
def test_Task_map():
    # DEFINE
    class A:
        pass

    class B:
        pass

    def fn(value):
        return B()

    a = A()
    task = Task.of(a).map(fn)

    # ASSERTION
    assert task.fork(lambda value: False, lambda value: True)



# Generated at 2022-06-14 04:07:30.482157
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve('test')

    def fn(arg):
        return Task.reject(arg)

    task = Task(fork)
    assert task.bind(fn).fork(lambda reject: reject, lambda _: False) == 'test'
