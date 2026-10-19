

# Generated at 2022-06-14 03:58:06.144308
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Return reject Task if one of Task in bind sequence is rejected.
    Return resolve Task if all Tasks in bind sequence is resolved
    """
    task = Task.of(1).bind(lambda arg: Task.of(arg + 1)).bind(lambda arg: Task.of(arg + 2))
    assert task.fork(lambda a: None, lambda a: a) == 4

    task = Task.of(1).bind(lambda arg: Task.of(arg + 1)).bind(lambda arg: Task.reject(arg + 2))
    assert task.fork(
        lambda a: None,
        lambda a: None
    ) == None

    task = Task.of(1).bind(lambda arg: Task.reject(arg + 1)).bind(lambda arg: Task.of(arg + 2))

# Generated at 2022-06-14 03:58:10.053133
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(2).map(lambda x: x * 2)

    assert task.fork(None, lambda x: x) == 4


# Generated at 2022-06-14 03:58:16.662383
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Unit test for method bind of class Task
    """
    def result(reject, resolve): resolve(42)
    def bind(reject, resolve): resolve(43)
    def bind2(reject, resolve):
        return Task(result).bind(lambda value: Task(bind))\
        .fork(lambda value: reject(value), lambda value: resolve(value))

    assert Task(bind2).fork(lambda value: value, lambda value: value) == 43


# Generated at 2022-06-14 03:58:25.584750
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(a):
        return Task.of(a + 1)

    def reject(a):
        return Task.reject(a + 1)

    task = Task(resolve)

    assert task.bind(resolve).fork(lambda x: x, lambda x: x) == 3
    assert task.bind(reject).fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 03:58:35.492988
# Unit test for method map of class Task
def test_Task_map():
    called = False
    result = ''

    class FakeResolve:
        def __call__(self, arg):
            nonlocal called, result
            called = True
            result = arg

    fakeResolve = FakeResolve()

    task = Task.of('test')
    task.map(lambda arg: arg.upper()).fork(None, fakeResolve)

    assert called
    assert result == 'TEST'


# Generated at 2022-06-14 03:58:36.994235
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(None, assert_(2))


# Generated at 2022-06-14 03:58:40.004547
# Unit test for method bind of class Task
def test_Task_bind():
    @Task.of
    def value():
        return 1

    @Task.of
    def value2():
        return 2

    func = lambda _: value2()

    assert value().bind(func).fork(None, None) == 2


# Generated at 2022-06-14 03:58:45.676374
# Unit test for method bind of class Task
def test_Task_bind():
    def _resolve_with_value(value):
        return Task.of(value)

    task = Task.of(0).bind(_resolve_with_value)
    assert task.fork(lambda x: x, lambda x: x) == 0

    def _resolve_with_error(value):
        return Task.reject(value)

    task = Task.of(0).bind(_resolve_with_error)
    assert task.fork(lambda x: x, lambda x: x) == 0


# Generated at 2022-06-14 03:58:51.381852
# Unit test for method bind of class Task
def test_Task_bind():
    print('test Task.bind')
    # mock for Task.fork
    class Mock:
        def __init__(self, reject, resolve):
            self._reject, self._resolve = reject, resolve

        def _fork(self, arg):
            if isinstance(arg, Exception):
                self._reject(arg)
            else:
                self._resolve(arg)

    result_value = 'result'
    result_reject = Exception('reject')
    value = 'ok'

    # should return same Task if function not return Task object
    task = Task(lambda _, resolve: resolve(value))
    new_task = task.bind(lambda arg: 'ok')
    mock = Mock(lambda reject: None, lambda resolve: None)
    new_task.fork(mock._fork, mock._fork)

# Generated at 2022-06-14 03:58:59.684858
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x): return Task.of(x)
    def g(x): return Task.of(x + 1)
    def h(x): return Task.of(x * 2)

    with pytest.raises(Exception):
        Task.reject('foo').bind(f).fork(lambda x: print('rejected with', x), lambda x: print('resolution with', x))

    assert Task.of(3).bind(f).bind(g).bind(h).fork(lambda x: 'rejected with', lambda x: x) == 8

# Generated at 2022-06-14 03:59:05.991299
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task(lambda reject, resolve: resolve(1)) \
        .bind(lambda x: Task(lambda reject, resolve: resolve(x + 2))) \
        .fork(lambda _: -1, lambda x: x) == 3


# Generated at 2022-06-14 03:59:13.954349
# Unit test for method map of class Task
def test_Task_map():
    """
    Function to test map method of class Task.
    """

# Generated at 2022-06-14 03:59:26.187723
# Unit test for method map of class Task
def test_Task_map():
    def assert_task(task):
        assert isinstance(task, Task)
        assert type(task.fork) == FunctionType

    def assert_task_executed_correctly(task, expected_value=None):
        """
        :param task: task, which will be executed
        :type task: Task[Function(_, resolve) -> A] | Task[Function(resolve, _) -> A]
        :param expected_value: expected value. if not specified, do not test value
        :type expected_value: A
        """
        rejected_arg = []
        resolved_arg = []
        task.fork(
            lambda arg: rejected_arg.append(arg),
            lambda arg: resolved_arg.append(arg)
        )
        if expected_value:
            assert rejected_arg == []

# Generated at 2022-06-14 03:59:27.984788
# Unit test for method map of class Task
def test_Task_map():
    """
    Test suite for method map of class Task.
    """
    pass


# Generated at 2022-06-14 03:59:38.130385
# Unit test for method bind of class Task
def test_Task_bind():
    print("Testing method bind of class Task:")

    # Helper function for testing
    def test(x, y):
        assert x == y, "Fail for x = {0} and y = {1}".format(x, y)
        print("Pass for x = {0} and y = {1}".format(x, y))

    print("Checking of normal behavior:")
    task = Task.of(6)
    task = task.bind(lambda x: Task.of(x + 1))
    task = task.bind(lambda x: Task.of(x * 7))
    task.fork(
        lambda x: None,
        lambda x: test(x, 49)
    )

    print("Checking of exception:")
    ex = Exception("Test exception")
    task = Task.of(6)

# Generated at 2022-06-14 03:59:47.039211
# Unit test for method bind of class Task
def test_Task_bind():
    def timer(value):
        def fork(reject, resolve):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('google.com', 80))
            resolve(value)
            s.close()

        return Task(fork)

    assert Task.reject('error') \
        .bind(timer) \
        .fork(lambda x: x, lambda x: x) == 'error'

    assert Task.of(1) \
        .bind(timer) \
        .fork(lambda x: x, lambda x: x) == 1

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 03:59:55.625402
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Composition of three Task
    """
    def sum_one(arg):
        return Task.of(arg + 1)

    def sum_two(arg):
        return Task.of(arg + 2)

    def sum_three(arg):
        return Task.of(arg + 3)

    task_in = Task.of(42)
    task_one = task_in.bind(sum_one)
    task_two = task_one.bind(sum_two)
    task_sym = task_two.bind(sum_three)

    def fork(reject, resolve):
        task_sym.fork(reject, resolve)

    assert fork(None, None) == 48

test_Task_bind()

# Generated at 2022-06-14 04:00:02.643421
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test full working of bind.
    Test bind of empty task and bind of task which return task.
    """
    def increment(value):
        return value + 1

    def get_task_with_incremented(value):
        return Task.of(increment(value))

    assert Task.of(1).bind(get_task_with_incremented).fork(lambda _: False, lambda result: result == 2)
    assert Task.of(1).bind(lambda _: Task.of(2)).fork(lambda _: False, lambda result: result == 2)

# Generated at 2022-06-14 04:00:10.783004
# Unit test for method bind of class Task
def test_Task_bind():
    def bind_fork(reject, resolve):
        resolve('test')

    def bind_map(value):
        assert value == 'test'
        return value

    def bind_resolve(value):
        assert value == 'test'
        return Task.of('test value')

    def bind_reject(value):
        assert value == 'test value'

    task = Task(bind_fork).map(bind_map).bind(bind_resolve).fork(bind_reject, bind_reject)

# Generated at 2022-06-14 04:00:22.440918
# Unit test for method bind of class Task
def test_Task_bind():
    def parse_response(response):
        if response.status_code != 200:
            return Task.reject("error")

        return Task.of(response.json())

    def fetch_user(username):
        url = "https://api.github.com/users/{}".format(username)
        response = requests.get(url)
        return parse_response(response)

    def find_github_user(user_id):
        return Task.of(user_id) \
            .map(lambda uid: "github_user_{}".format(uid)) \
            .bind(fetch_user)

    def fail(a):
        assert a == "error"

    def succeed(a):
        assert a["login"] == "github_user_5"


# Generated at 2022-06-14 04:00:31.489015
# Unit test for method bind of class Task
def test_Task_bind():
    def my_map(v):
        return Task.of(v + ' world')

    task = Task.of('Hello').bind(my_map)

    def my_error(error):
        assert error == 'Something is wrong'

    def my_resolve(value):
        assert value == 'Hello world'

    task.fork(my_error, my_resolve)


# Generated at 2022-06-14 04:00:39.243392
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda x: Task.of(x + 1)).fork(
        lambda e: e,
        lambda v: v
    ) == 2

    assert Task.of(1).bind(lambda x: Task.reject(x)).fork(
        lambda e: e,
        lambda v: v
    ) == 1

    assert Task.reject(1).bind(lambda x: Task.of(x + 1)).fork(
        lambda e: e,
        lambda v: v
    ) == 1


# Generated at 2022-06-14 04:00:47.586365
# Unit test for method map of class Task
def test_Task_map():
    def add_one(value):
        return value + 1

    def take_first(value):
        return value[0]

    assert Task.of(1).map(add_one).map(add_one).map(str).fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == '3'

    assert Task.of("Hello World").map(lambda x: x.split(" ")).map(take_first).fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == "Hello"


# Generated at 2022-06-14 04:00:53.285290
# Unit test for method bind of class Task
def test_Task_bind():
    # arrange
    task_arg = Task.of(1)
    task_expectation = Task.of(2)
    task_result = None

    # act
    task_result = task_arg.bind(lambda value: task_expectation)

    # assert
    def callback(expectation):
        assert expectation == 2
    task_result.fork(
        lambda arg: print("error {}".format(arg)),
        callback
    )

# Generated at 2022-06-14 04:00:57.903314
# Unit test for method map of class Task
def test_Task_map():
    def _():
        task = Task(lambda _, resolve: resolve(100))

        def fn(x):
            return x * x

        yield task.map(fn) == Task(
            lambda _, resolve: resolve(fn(100))
        )


# Generated at 2022-06-14 04:01:08.477037
# Unit test for method bind of class Task
def test_Task_bind():
    def add3(task):
        def add3(number):
            return number + 3

        return task.map(add3)

    def add10(task):
        def add10(number):
            return number + 10

        return task.map(add10)

    assert Task(lambda _, resolve: resolve(125)).bind(add3).fork(
        None, lambda x: x
    ) == 128
    assert Task(lambda _, resolve: resolve(125)).bind(add10).fork(
        None, lambda x: x
    ) == 135
    assert Task(lambda _, resolve: resolve(125)).bind(add3).bind(add10).fork(
        None, lambda x: x
    ) == 131


# Generated at 2022-06-14 04:01:14.913943
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return Task(lambda reject, resolve: resolve(value + 1))

    task = Task.of(1).map(mapper)
    assert task.fork(lambda reject: reject, lambda resolve: resolve) == 2

    task = Task.reject(1).map(mapper)
    assert task.fork(lambda reject: reject, lambda resolve: resolve) == 1

    task = Task.of(1).map(lambda x: x + 1)
    assert task.fork(lambda reject: reject, lambda resolve: resolve) == 2

    task = Task.reject(1).map(lambda x: x + 1)
    assert task.fork(lambda reject: reject, lambda resolve: resolve) == 1


# Generated at 2022-06-14 04:01:17.657600
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(5).bind(lambda arg: Task.of(arg + 1)).fork(lambda _: None, lambda arg: arg) == 6


# Generated at 2022-06-14 04:01:22.187267
# Unit test for method map of class Task
def test_Task_map():

    def map_test(value):
        return value * 2

    assert Task.of(2).map(map_test).fork(lambda a: a, lambda a: a) == 4
    assert Task.reject(2).map(map_test).fork(lambda a: a, lambda a: a) == 2


# Generated at 2022-06-14 04:01:31.116320
# Unit test for method bind of class Task
def test_Task_bind():
    def func(value):
        if value > 6:
            return Task.reject(value)
        return Task.of(value)

    def mapper(value):
        return value + 1

    # Lambda
    assert isinstance(Task.of(5).bind(func).map(mapper).fork, types.MethodType)

    # First case
    assert Task.of(3).bind(func).map(mapper).fork(
        lambda value: ("left", value),
        lambda value: ("right", value)
    ) == ('right', 4)

    # Second case
    assert Task.of(7).bind(func).map(mapper).fork(
        lambda value: ("left", value),
        lambda value: ("right", value)
    ) == ('left', 7)

# Generated at 2022-06-14 04:01:43.603666
# Unit test for method bind of class Task
def test_Task_bind():
    def add(x):
        return Task.of(2 + x)

    def fail():
        return Task.reject(Exception("FAIL"))

    assert Task.reject("bla-bla").bind(add).fork("print", "print") == "bla-bla"
    assert Task.of("bla-bla").bind(add).fork("print", "print") == "bla-bla2"
    assert Task.of("bla-bla").bind(fail).fork("print", "print") == "FAIL"



# Generated at 2022-06-14 04:01:49.819451
# Unit test for method map of class Task
def test_Task_map():
    """ run unit tests """
    def run(resolve, reject):
        return resolve(2)

    def mapper(arg):
        """ Unit test for Task.map(fn) """
        return arg + 2

    assert Task(run).map(mapper).fork(
        lambda _: False,
        lambda arg: arg == 4
    )

# Generated at 2022-06-14 04:01:54.236540
# Unit test for method bind of class Task
def test_Task_bind():

    def fork(reject, resolve):
        return resolve(42)

    def mapper(value):
        return Task.of(value + 10)

    task = Task(fork)
    new_task = task.bind(mapper)
    new_fork = new_task.fork

    def test_fork(value):
        assert value == 52

    new_fork(test_fork, None)


# Generated at 2022-06-14 04:01:59.080018
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)
    task_after_map = task.map(lambda value: value + 1)
    assert 1 == task.fork(lambda value: 1, lambda value: 2)
    assert 2 == task_after_map.fork(lambda value: 1, lambda value: 2)

# Generated at 2022-06-14 04:02:08.491495
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method.
    """

# Generated at 2022-06-14 04:02:09.188548
# Unit test for method map of class Task
def test_Task_map():
    pass

# Generated at 2022-06-14 04:02:15.055554
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task map
    """

    fake_reject = lambda x: None
    fake_resolve = lambda x: x

    fork = lambda reject, resolve: resolve(3)
    task = Task(fork)

    assert task.map(lambda x: x + 2).fork(fake_reject, fake_resolve) == 5


# Generated at 2022-06-14 04:02:21.905716
# Unit test for method bind of class Task
def test_Task_bind():
    def reject_callback(arg):
        return 1 + arg

    def resolve_callback(arg):
        return Task.of(arg + 1)

    a = Task.reject(0)
    b = a.bind(resolve_callback)
    c = b.bind(resolve_callback)
    assert c.fork(reject_callback, lambda _: None) == 2


# Generated at 2022-06-14 04:02:23.243612
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(100) \
        .map(lambda x: x + 2) \
        .fork(lambda x: print('Reject ' + str(x)), lambda x: x) == 102



# Generated at 2022-06-14 04:02:35.490781
# Unit test for method bind of class Task
def test_Task_bind():
    def task_reject(value):
        return Task(lambda reject, _: reject(value))

    def task_resolve(value):
        return Task(lambda _, resolve: resolve(value))

    def task_of(value):
        return Task.of(value)

    def identity(value):
        return value

    def test_bind_reject_reject(value):
        task = Task.reject(value)

        def nested_reject(arg):
            return task_reject(arg)

        result = task.bind(nested_reject)
        assert isinstance(result, Task)

# Generated at 2022-06-14 04:02:48.013561
# Unit test for method bind of class Task
def test_Task_bind():
    def create_task(value):
        return Task.of(value)

    task = Task.of(1)
    task.bind(create_task).fork(
        lambda arg: assert_equal(arg, 1),
        lambda arg: assert_equal(arg, 1)
    )


# Generated at 2022-06-14 04:02:50.962670
# Unit test for method map of class Task
def test_Task_map():
    a = Task.of(1)
    b = a.map(lambda arg: arg + 1)

    assert b.fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 04:02:54.736694
# Unit test for method map of class Task
def test_Task_map():
    def get_foo():
        def foo(reject, resolve):
            time.sleep(random.randint(1, 3))
            if random.randint(1, 100) < 10:
                reject('foo')
            resolve(random.randint(1, 100))

        return Task(foo)

    task = get_foo().map(lambda arg: arg * 2).fork(lambda arg: print('foo: ', arg), print)
    task = get_foo().map(lambda arg: arg * 2).map(lambda arg: arg + 2).fork(lambda arg: print('foo: ', arg), print)



# Generated at 2022-06-14 04:03:02.553312
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    :returns: assert result
    :rtype: Boolean
    """
    def test_fn(arg):
        if arg < 0:
            return Task.reject("arg less zero")
        else:
            return Task.of(arg * 2)

    def test_reject(arg):
        return Task.reject(arg)

    return (
        Task.of(2).bind(test_fn).fork(None, lambda arg: arg == 4) &
        Task.of(-2).bind(test_fn).fork(None, test_reject)
    )

# Generated at 2022-06-14 04:03:12.353202
# Unit test for method bind of class Task
def test_Task_bind():
    def add(a):
        return Task.of(a + 2)

    def mul(a):
        return Task.of(a * 2)

    def div(a):
        return Task.of(a / 2)

    def someError():
        return Task.reject(True)

    def test(fork):
        return Task(fork).bind(add).bind(mul).bind(div).bind(add).fork(
            lambda arg: 'error',
            lambda arg: arg
        )

    assert test(lambda reject, res: res(2)) == 5

    assert test(lambda reject, res: reject(2)) == 'error'

# Generated at 2022-06-14 04:03:21.383230
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task.bind
    """

    # Create two functions: one resolve and one reject value
    # and return Task whose fork function use one function from
    # argument
    def create_task(fn):
        return Task(lambda reject, resolve: fn(reject, resolve))

    # Create two functions: one receive and return value
    # and second use first function and apply with value to resolve

    def receive_value(value):
        def receive(reject, resolve):
            resolve(value)

        return receive

    def receive_value_under_task(value):
        return Task(receive_value(value))

    # Create function which when called return Task
    # resolve with received value

    def bind_receive_value(reject, resolve):
        receive_value_under_task(1).fork(reject, resolve)

   

# Generated at 2022-06-14 04:03:31.049735
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.reject(value)

    def result(reject, resolve):
        return Task.of(5).fork(reject, resolve)

    expected = Task(result)
    actual = Task.of(5).bind(fn)

    print('test Task.bind()')
    print('\texpected: {}'.format(expected))
    print('\tactual: {}'.format(actual))
    print('\tresolve(): {}'.format(actual.resolve()))
    print('\treject(): {}'.format(actual.reject()))


# Generated at 2022-06-14 04:03:41.027565
# Unit test for method map of class Task
def test_Task_map():
    """
    Test Task.map method
    """

    def reject(value):
        return None, value

    def resolve(value):
        return value, None

    def original(reject, resolve):
        return resolve(100)

    def mapper(value):
        return value + 200

    def expect_value(value):
        return 1/0

    def expect_error(value):
        return 2

    a = Task(original)

    value = a.map(mapper)\
        .fork(reject, resolve) == (300, None)
    error = a.map(expect_value)\
        .fork(resolve, reject) == (300, None)

    return (value and error)



# Generated at 2022-06-14 04:03:49.241996
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(1)
        return 'fork'

    def fork_reject(reject, resolve):
        reject(2)
        return 'fork_reject'

    resolve_task = Task(fork)
    reject_task = Task(fork_reject)

    result = resolve_task\
        .bind(lambda x: Task.of(x + 1))\
        .bind(lambda x: Task.of(x + 2))\
        .bind(lambda x: Task.reject(x + 3))\
        .fork(lambda x: x, lambda x: x)

    assert result == 5


# Generated at 2022-06-14 04:03:51.698182
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('foo').map(lambda value: value + 'bar').fork(lambda arg: arg, lambda arg: 'answer') == 'answer'


# Generated at 2022-06-14 04:04:18.496040
# Unit test for method map of class Task
def test_Task_map():
    def test_mapper(value):
        return value + 1

    def test_resolver(resolve, reject):
        return resolve(1)

    def test_rejecter(resolve, reject):
        return reject(1)

    assert Task(test_resolver).map(test_mapper).fork(
        reject=lambda value: value,
        resolve=lambda value: value
    ) == 2

    assert Task(test_rejecter).map(test_mapper).fork(
        reject=lambda value: value,
        resolve=lambda value: value
    ) == 1


# Generated at 2022-06-14 04:04:28.134574
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        print("resolve: " + str(value))
    def reject(value):
        print("reject: " + str(value))

    def add(x):
        return x + 1

    def add_task(x):
        return Task.of(x + 1)

    Task.of(1).map(add).fork(reject, resolve)
    Task.of(1).bind(add_task).fork(reject, resolve)
    Task.of(1).bind(lambda x: Task.reject(x + 1)).fork(reject, resolve)

#test_Task_bind()


# Generated at 2022-06-14 04:04:39.633363
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test method bind.
    """
    def add1(number):
        return Task.of(number + 1)

    def mult2(number):
        return Task.of(number * 2)

    def div2(number):
        return Task.of(number / 2)

    def test(test_value, expected_value):
        """
        Test Task map function.

        :param test_value: value to test
        :type test_value: number
        :param expected_value: expected value
        :type expected_value: number
        :raises AssertionError: if test_value != expected_value
        """
        assert Task.of(test_value).bind(add1).bind(mult2).bind(div2).fork(_, identity) == expected_value

    test(1, 1.5)
    test

# Generated at 2022-06-14 04:04:47.130149
# Unit test for method bind of class Task
def test_Task_bind():
    fn1 = lambda arg: return_value(arg)
    fn2 = lambda arg: Task.of(arg)
    fn3 = lambda arg: Task.of('bind')

    t1 = Task.of(1)
    t2 = Task.reject({})
    t3 = Task.of('task')

    assert t1.bind(fn1) == 1
    assert t2.bind(fn2) == '{}'
    assert t3.bind(fn3) == 'bind'

# Generated at 2022-06-14 04:04:51.176354
# Unit test for method map of class Task
def test_Task_map():
    @Task.of(666)
    def test_task():
        return Task
    test_task = test_task.map(lambda value: value + 1)
    test_task.fork(None, print)


# Generated at 2022-06-14 04:04:55.194994
# Unit test for method map of class Task
def test_Task_map():
    def add_value(arg):
        return arg + 2

    stored = Task.of(2)
    actual = stored.map(add_value).fork(None, lambda x: x)
    expected = 4

    assert actual == expected



# Generated at 2022-06-14 04:05:04.188944
# Unit test for method map of class Task
def test_Task_map():
    """
    Run unittest for Task#map
    """

    def test_suite(resolve, reject):
        """
        Test Task class
        """
        left = Task(lambda _, resolve: resolve(a + b)) \
               .map(lambda arg: arg * 2) \
               .map(lambda arg: arg + 2)

        right = Task.of(a + b) \
               .map(lambda arg: arg * 2) \
               .map(lambda arg: arg + 2)

        resolve(left == right)

    a = 1
    b = 1
    right_answer = True

    test_suite_task = Task(test_suite)

    assert test_suite_task.fork(lambda _: None,
                                lambda result: result == right_answer)

# Generated at 2022-06-14 04:05:13.996926
# Unit test for method bind of class Task
def test_Task_bind():
    def test_method_resolving():
        def mapper(value):
            return value * 4
        task = Task.of("test")
        result = task.bind(lambda x: Task.of(x * 2)).map(mapper)
        assert result.fork(identity, identity) == "testtesttesttest"

    def test_method_rejecting():
        def mapper(value):
            return value * 4
        task = Task.of("test")
        result = task.bind(lambda x: Task.reject(x * 2)).map(mapper)
        assert result.fork(identity, identity) == "testtest"

    test_method_resolving()
    test_method_rejecting()


# Generated at 2022-06-14 04:05:20.302634
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(10)

    task = Task(fork)

    assert(type(task.bind(lambda _: Task.of(10))) == Task)

# Generated at 2022-06-14 04:05:30.815939
# Unit test for method map of class Task
def test_Task_map():
    text = Task.of('some text')

    assert text.fork(lambda _: False, lambda a: a == 'some text')
    assert text.map(lambda a: '{}{}'.format(a, 1)).fork(lambda _: False, lambda a: a == 'some text1')
    assert text.map(lambda _: None).fork(lambda _: False, lambda a: a is None)
    assert text.map(lambda a: '{}{}'.format(a, 1)).fork(lambda _: False, lambda a: a == 'some text1')
    assert text.map(lambda _: Task.of(10)).fork(lambda _: False, lambda a: a == 10)


# Generated at 2022-06-14 04:06:16.589963
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value + 1)

    fn = Task.of(1).bind(mapper).fork

    assert 2 == fn(lambda _: None, lambda arg: arg)



# Generated at 2022-06-14 04:06:24.509979
# Unit test for method bind of class Task
def test_Task_bind():
    def test_fork(reject, resolve):
        assert reject == reject_fn
        assert resolve == resolve_fn
        resolve_fn('foo')

    def mapper(value):
        assert value == 'foo'
        return value

    def reject_fn(value):
        assert value == 'bar'

    def resolve_fn(value):
        assert value == 'foo'

    task = Task(test_fork)
    task.bind(mapper).fork(reject_fn, resolve_fn)



# Generated at 2022-06-14 04:06:29.738763
# Unit test for method map of class Task
def test_Task_map():
    """
    Testing map method of class Task.
        1. Create instance of Task with lambda function as arg.
        2. Call map method with additional lambda function as arg.
        2. Check that result of map method works as expected.
    """
    task_map = Task(lambda reject, resolve: resolve(1)).map(lambda a: a + 1)

# Generated at 2022-06-14 04:06:32.400697
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(3).bind(lambda x: Task.of(x + 1)).fork(None, lambda x: x) == 4


# Generated at 2022-06-14 04:06:43.289151
# Unit test for method map of class Task
def test_Task_map():
    def fork_mock_for_ok_test(reject, resolve):
        resolve(10)

    def fork_mock_for_fails_test(reject, resolve):
        reject('error')

    def square_mock(value):
        return value ** 2

    def square_mock_for_fails_test(value):
        raise ValueError('error')

    result_task = Task(fork_mock_for_ok_test).map(square_mock)
    assert result_task.fork(lambda arg: arg, lambda arg: arg) == 100

    result_task = Task(fork_mock_for_fails_test).map(square_mock)
    assert result_task.fork(lambda arg: arg, lambda arg: arg) == 'error'


# Generated at 2022-06-14 04:06:56.721584
# Unit test for method map of class Task
def test_Task_map():
    def my_mapper(arg):
        return arg + 1

    def my_reject(arg):
        return arg

    def my_resolve(arg):
        return arg

    def literal(arg):
        return arg

    def mapped(arg):
        return my_mapper(arg)

    test_cases = [
        {
            'input': Task.of(1),
            'fn': my_mapper,
            'reject': my_reject,
            'resolve': my_resolve
        },
        {
            'input': Task.reject(1),
            'fn': my_mapper,
            'reject': my_reject,
            'resolve': my_resolve
        }
    ]


# Generated at 2022-06-14 04:07:05.464175
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """

    fn_resolve_one = lambda x: 1
    fn_resolve_two = lambda x: 2

    assert Task.of(1).map(fn_resolve_one).fork(None, fn_resolve_one) == 1
    assert Task.of(1).map(fn_resolve_one).fork(None, fn_resolve_two) == 2

    assert Task.of(1).map(fn_resolve_one).map(fn_resolve_one).fork(None, fn_resolve_one) == 1
    assert Task.of(1).map(fn_resolve_one).map(fn_resolve_one).fork(None, fn_resolve_two) == 2


# Generated at 2022-06-14 04:07:18.535738
# Unit test for method bind of class Task
def test_Task_bind():
    def add_one(x):
        return x + 1

    def double(x):
        return x * 2

    def add_one_task(x):
        return Task.of(add_one(x))

    def double_task(x):
        return Task.of(double(x))

    assert Task.reject(1).bind(add_one_task).fork(lambda x: x, lambda y: y) == 1
    assert Task.of(1).bind(add_one_task).fork(lambda x: x, lambda y: y) == 2
    assert Task.of(1).bind(double_task).fork(lambda x: x, lambda y: y) == 2

# Generated at 2022-06-14 04:07:21.702271
# Unit test for method map of class Task

# Generated at 2022-06-14 04:07:28.342880
# Unit test for method map of class Task
def test_Task_map():
    # Create task with store some value
    initial_task = Task.of(1)

    # create mapper function
    def mapper_function(value):
        return value + 1

    # map created function on task
    mapped = initial_task.map(mapper_function)

    # get result of mapping
    result = mapped.fork(None, lambda a: a)

    # => 2
    assert(result == 2)
