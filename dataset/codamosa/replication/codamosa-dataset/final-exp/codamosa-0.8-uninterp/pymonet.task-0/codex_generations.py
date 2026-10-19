

# Generated at 2022-06-14 03:57:57.759941
# Unit test for method bind of class Task
def test_Task_bind():
    # a function with side effect
    def side_effect(value):
        print('called side_effect')
        return 0

    # set up expected result
    expected_result = 0
    # create Task with side effect
    task = Task(side_effect)
    # execute task
    result = task.bind(lambda arg: Task.of(arg)).fork(lambda _: 1, lambda arg: arg)
    # assert result is expected
    assert result == expected_result




# Generated at 2022-06-14 03:58:03.535210
# Unit test for method map of class Task
def test_Task_map():
    def resolve_add(number):
        return Task.of(number + 1)

    task = Task(lambda _, resolve: resolve(5))

    assert task.map(lambda arg: arg + 1).fork(lambda _: None, lambda arg: arg) == 6
    assert task.bind(resolve_add).fork(lambda _: None, lambda arg: arg) == 6


# Generated at 2022-06-14 03:58:08.909715
# Unit test for method map of class Task
def test_Task_map():
    source = Task.of(1)

    def double(value):
        return value * 2

    expect = Task.of(2)
    actual = source.map(double)

    assert (
        actual.fork(lambda _: False, lambda arg: arg == expect.fork(lambda _: False, lambda arg: arg))
    )


# Generated at 2022-06-14 03:58:11.587325
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda reject, resolve: resolve(2)).map(
        lambda x: x + 2
    ).fork(lambda reject: None, lambda resolve: resolve) == 4


# Generated at 2022-06-14 03:58:24.236540
# Unit test for method map of class Task
def test_Task_map():
    def add_one(arg):
        return arg + 1

    def test_map_resolve(resolve, reject):
        resolve("value")

    def test_map_reject(resolve, reject):
        reject("value")

    # test for reject
    assert Task(test_map_reject).map(add_one).fork(
        lambda arg: arg == "value",
        lambda arg: arg == 2
    )
    # test for resolve
    assert Task(test_map_resolve).map(add_one).fork(
        lambda arg: arg == "value",
        lambda arg: arg == "value1"
    )


# Generated at 2022-06-14 03:58:36.556573
# Unit test for method bind of class Task
def test_Task_bind():
    def id(value):
        return value

    def a(value):
        return Task.of(value + 'a')

    def b(value):
        return Task.of(value + 'b')

    def c(value):
        return Task.of(value + 'c')

    task = Task.of('a').bind(a).bind(b).bind(c)
    fork_result = task.fork(id, id)

    assert fork_result == 'abc'

if __name__ == '__main__':
    test_Task_bind()

# Generated at 2022-06-14 03:58:41.398380
# Unit test for method bind of class Task
def test_Task_bind():
    t1 = Task.of(1)
    t2 = t1.bind(lambda a: Task.of(a + 1))
    assert(hasattr(t1, 'fork'))
    assert(hasattr(t2, 'fork'))
    assert(t1.fork(lambda a: 0, lambda a: a) == 1)
    assert(t2.fork(lambda a: 0, lambda a: a) == 2)


# Generated at 2022-06-14 03:58:45.416796
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task(lambda reject, resolve: resolve(value * 2))

    result = Task.of(2).bind(fn)
    assert result.fork(
               lambda reject: 'Failed with {}'.format(reject),
               lambda resolve: 'Success with {}'.format(resolve)) == 'Success with 4'

# Generated at 2022-06-14 03:58:50.170339
# Unit test for method bind of class Task
def test_Task_bind():
    def foo(reject, _):
        reject("42")

    task = Task(foo)
    value = task.bind(lambda _: Task.of("bar"))
    assert value == Task.reject("42")



# Generated at 2022-06-14 03:58:58.484828
# Unit test for method bind of class Task
def test_Task_bind():
    def reject_func(value):
        return Task.reject(value)

    def resolve_func(value):
        return Task.of(value)

    def bind_func(value):
        return Task(lambda _, resolve: resolve(value + 10))

    def test():
        task = Task.of(100)
        task = task.bind(reject_func)
        task = task.map(bind_func)
        assert task.fork(lambda a: a, lambda a: a) == 110

    test()



# Generated at 2022-06-14 03:59:07.052244
# Unit test for method map of class Task
def test_Task_map():
    def test(fn, expect_result):
        value = any()
        result = Task.of(value).map(fn)
        assert result.fork(None, lambda result: result) == expect_result
    test(lambda arg: arg, any())
    test(lambda arg: arg + '!', any() + '!')
    test(lambda arg: arg * 2, any() * 2)


# Generated at 2022-06-14 03:59:16.169617
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task(lambda reject, resolve: resolve(value))

    assert Task.of(10).bind(fn).fork(None, lambda value: value) == 10
    assert Task.of(10).bind(fn).bind(fn).fork(None, lambda value: value) == 10
    assert Task.reject(10).bind(fn).fork(lambda value: value, None) == 10
    assert Task.reject(10).bind(fn).bind(fn).fork(lambda value: value, None) == 10
    assert Task.of(10).map(lambda value: value).bind(fn).map(lambda value: value).fork(None, lambda value: value) == 10



# Generated at 2022-06-14 03:59:23.881138
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test method Task.bind 
    """
    mock_reject = mock.MagicMock()
    mock_resolve = mock.MagicMock()

    assert Task.of(5).bind(lambda x: Task.of(x * 2)).fork(mock_reject, mock_resolve) == True
    mock_resolve.assert_called_once_with(10)
    mock_reject.assert_not_called()


# Generated at 2022-06-14 03:59:27.890390
# Unit test for method map of class Task
def test_Task_map():
    @task
    def work(resolve):
        time.sleep(2)
        resolve('result')

    result = work.map(lambda value: value + ' is good')

    assert result.fork(None, lambda value: value) == 'result is good'


# Generated at 2022-06-14 03:59:31.446043
# Unit test for method bind of class Task
def test_Task_bind():
    test_case = Task.of(1)

    assert test_case.bind(lambda arg: Task.of(arg ** 2)) == \
        Task.of(1 ** 2)

    assert test_case.bind(lambda arg: Task.reject(arg ** 2)) == \
        Task.reject(1 ** 2)



# Generated at 2022-06-14 03:59:42.711552
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Case when we have function which return rejected Task and function is called
    on the Task which is resolved.
    """
    def func(value):
        return Task.reject({'msg': value})


# Generated at 2022-06-14 03:59:48.182496
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for bind method of class Task
    """
    def resolve(value):
        assert False

    def reject(value):
        assert value == 42

    def result(reject, resolve):
        assert False

    Task.reject(42).bind(lambda r: Task(result)).fork(reject, resolve)

test_Task_bind()


# Generated at 2022-06-14 03:59:51.424813
# Unit test for method map of class Task
def test_Task_map():
    def mul_2(arg):
        return arg * 2

    def check(arg):
        assert arg == 10


# Generated at 2022-06-14 03:59:57.319043
# Unit test for method map of class Task
def test_Task_map():
    def concat(value):
        return '%s %s' % (value, 'world')

    def resolve(value):
        assert value == 'hello world'

    def reject(value):
        assert False

    Task.of('hello').map(concat).fork(reject, resolve)


# Generated at 2022-06-14 04:00:05.059693
# Unit test for method map of class Task
def test_Task_map():
    def exception_fn(par):
        raise Exception()

    def fn(par):
        return par + 1

    assert Task(lambda _, resolve: resolve(1)).map(exception_fn).fork(
        lambda par: False,
        lambda par: par == 2
    )

    assert Task(lambda _, resolve: resolve(1)).map(fn).fork(
        lambda par: False,
        lambda par: par == 2
    )


# Generated at 2022-06-14 04:00:12.015303
# Unit test for method map of class Task
def test_Task_map():
    def async_generator():
        def result(reject, resolve):
            reject("Error")
            resolve("Resolved")
            nonlocal reject, resolve

        return Task(result)

    task = async_generator()
    assert len(task.map(lambda _: "Hey!")) == 1


# Generated at 2022-06-14 04:00:23.032584
# Unit test for method map of class Task
def test_Task_map():
    def resolve_function(value):
        def result(_, resolve):
            resolve(value)
        return result

    def reject_function(value):
        def result(reject, _):
            reject(value)
        return result

    def result_function(reject, resolve):
        resolve(10)

    def mapper_function(value):
        return value + 1

    reject_task = Task(reject_function(100))
    resolve_task = Task(resolve_function(100))

    reject_task_map = reject_task.map(mapper_function)
    resolve_task_map = resolve_task.map(mapper_function)

    assert success(reject_task_map.fork(lambda x: 0, lambda x: 1)) == 0

# Generated at 2022-06-14 04:00:32.731319
# Unit test for method map of class Task
def test_Task_map():
    def mapper(arg):
        return arg ** 2

    def fork0(reject, resolve):
        resolve(2)

    def fork1(reject, resolve):
        reject(100)

    task0 = Task(fork0).map(mapper)
    assert task0.fork(reject=lambda arg: arg, resolve=lambda arg: arg) == 4

    task1 = Task(fork1).map(mapper)
    assert task1.fork(reject=lambda arg: arg, resolve=lambda arg: arg) == 100


# Generated at 2022-06-14 04:00:42.215718
# Unit test for method bind of class Task
def test_Task_bind():
    t = Task.reject(1).bind(
        lambda arg: Task.reject(arg+1)
    )

    assert t.fork(
        lambda reject: 'reject'
    ) == 'reject'

    t = Task.reject(1).bind(
        lambda arg: Task.of(arg+1)
    )

    assert t.fork(
        lambda reject: 'reject'
    ) == 'reject'

    t = Task.of(1).bind(
        lambda arg: Task.reject(arg+1)
    )

    assert t.fork(
        lambda reject: reject,
        lambda _: 'not reject'
    ) == 2

    t = Task.of(1).bind(
        lambda arg: Task.of(arg+1)
    )


# Generated at 2022-06-14 04:00:50.456638
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Resolved Task with passed value (1)
    then call bind with function that return Task of add value to passed argument
    and finally call bind with function that return Task of square value.
    """
    def add(x):
        return Task(lambda _, resolve: resolve(x + 1))

    def square(x):
        return Task(lambda _, resolve: resolve(x**2))

    task = Task.of(1)
    task = task.bind(add).bind(square)
    t.eq(task.fork(None, lambda v: v), 4)


# Generated at 2022-06-14 04:00:58.232222
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task

    :returns: None
    :rtype: None
    """
    def func(arg):
        return arg * 2

    task = Task(lambda _, resolve: resolve(2))
    new_task = task.map(func)

    assert new_task.fork(lambda arg: arg, lambda arg: arg) == 2 * 2


# Generated at 2022-06-14 04:01:07.177921
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    """
    def fork_add(reject, resolve):
        resolve(7)

    def fork_mul(reject, resolve):
        resolve(8)

    task_add = Task(fork_add)
    task_mul = Task(fork_mul)

    def mapper(value):
        return task_mul

    def check(value):
        assert value == 8

    task = task_add.bind(mapper)
    task.fork(lambda _: None, lambda value: check(value))


# Example for method map of class Task

# Generated at 2022-06-14 04:01:12.543285
# Unit test for method bind of class Task
def test_Task_bind():
    @typecheck
    def test(x: int) -> Task[int]:
        return Task.of(x * 2)

    result = Task.of(1).bind(test).fork(
        lambda error: "rejected",
        lambda result: result
    )

    assert result == 2

    result = Task.reject(1).bind(test).fork(
        lambda error: "rejected",
        lambda result: result
    )

    assert result == "rejected"


# Generated at 2022-06-14 04:01:22.290360
# Unit test for method bind of class Task
def test_Task_bind():
    task_one = Task.of(1)
    task_two = Task.of(2)
    task_three = Task.of(3)
    task_four = Task.of(4)
    task_five = Task.of(5)
    task_six = Task.of(6)


# Generated at 2022-06-14 04:01:28.352644
# Unit test for method map of class Task
def test_Task_map():
    for i in range(100):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        c = random.randint(0, 1000)
        d = random.randint(0, 1000)

        assert Task(lambda _, resolve: resolve(a * b * c * d)).map(lambda arg: arg + 1).fork(None, lambda arg: arg) \
               == a * b * c * d + 1



# Generated at 2022-06-14 04:01:36.366354
# Unit test for method map of class Task

# Generated at 2022-06-14 04:01:47.064066
# Unit test for method map of class Task
def test_Task_map():
    """
    Task.map
    """
    def inc(value):
        return value + 1

    def is_unary_callable_function(value):
        return isinstance(value, types.FunctionType) and len(signature(value).parameters) == 1

    assert task.fork(lambda _, resolve: resolve(1)).map(inc).map(inc).fork(lambda _: False, lambda arg: arg == 3)
    assert task.fork(lambda _, resolve: resolve(1)).map(inc).map(is_unary_callable_function).fork(lambda _: False, lambda arg: arg)
    assert not task.fork(lambda reject, _: reject(1)).map(inc).map(is_unary_callable_function).fork(lambda _: True, lambda _: False)

# Generated at 2022-06-14 04:01:50.916482
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task.map(lambda x: x + 1).fork(
        lambda x: 1 / 0,
        lambda x: x == 2
    )



# Generated at 2022-06-14 04:01:58.381607
# Unit test for method bind of class Task
def test_Task_bind():
    def assert_task(
        task,
        attr_name,
        value,
        not_assigned_value=None,
        expected_type=Task
    ):
        """
        :param task: task to test
        :type task: Task
        :param attr_name: name of attribute in task
        :type attr_name: str
        :param value: assigned value (for right type)
        :type value: Any
        :param not_assigned_value: not assigned value (for wrong type)
        :type not_assigned_value: Any
        :param expected_type: expected type of task
        :type expected_type: type
        """
        def error_handler(_):
            """
            :param e: exception
            :type e: Exception
            """
            pass


# Generated at 2022-06-14 04:02:03.613755
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Given fn is function that returns Task with mapped value.
    When bind is called with fn.
    Then return Task with mapped value.
    """

    def fn(value):
        return Task.of(value + 1)

    task = Task.of(0)
    assert task.bind(fn).fork(lambda x: x, lambda x: x) == 1


# Generated at 2022-06-14 04:02:14.727582
# Unit test for method bind of class Task
def test_Task_bind():

    # Unit test for method bind of class Task
    Task.of('a').bind(lambda param: Task.of(param + 'b')).fork(
        lambda reject: setattr(test_Task_bind, 'reject', reject),
        lambda resolve: setattr(test_Task_bind, 'resolve', resolve)
    )
    assert test_Task_bind.resolve == 'ab'

    # Unit test for method bind of class Task
    Task.of(None).bind(lambda _: Task.of('a')).fork(
        lambda reject: setattr(test_Task_bind, 'reject', reject),
        lambda resolve: setattr(test_Task_bind, 'resolve', resolve)
    )
    assert test_Task_bind.resolve == 'a'



# Generated at 2022-06-14 04:02:24.985380
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda val: Task.of(val + 1)).fork(
        lambda val: False,
        lambda val: val == 2
    )

    assert Task.reject(1).bind(lambda val: Task.of(val + 1)).fork(
        lambda val: val == 1,
        lambda val: False
    )

#    assert Task.of(1).bind(lambda val: Task.reject(val + 1)).fork(
#        lambda val: val == 2,
#        lambda val: False
#    )

#    assert Task.reject(1).bind(lambda val: Task.reject(val + 1)).fork(
#        lambda val: val == 2,
#        lambda val: False
#    )



# Generated at 2022-06-14 04:02:34.346806
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map function of class Task.

    :returns: None
    :rtype: NoneType
    """
    assert Task(lambda _, resolve: resolve(2)).map(lambda value: value ** 2).fork(
        lambda value: print("rejected: %d" % value),
        lambda value: print("resolved: %d" % value)
    ) == None

    assert Task(lambda reject, _: reject(2)).map(lambda value: value ** 2).fork(
        lambda value: print("rejected: %d" % value),
        lambda value: print("resolved: %d" % value)
    ) == None

# Generated at 2022-06-14 04:02:38.332483
# Unit test for method map of class Task
def test_Task_map():
    def some_fn(x):
        return x + 1

    def fork(reject, resolve):
        resolve(4)

    t = Task(fork)
    mapped = t.map(some_fn)

    assert mapped.fork(lambda x: x, lambda x: x) == 5


# Generated at 2022-06-14 04:02:41.200667
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)
    task.map(add(2)).fork(print, print)
    task.bind(add(3)).map(divide(2)).fork(print, print)


# Generated at 2022-06-14 04:02:55.963590
# Unit test for method bind of class Task
def test_Task_bind():
    # given
    task = Task.of(5)

    # when
    bind_task = task.bind(lambda x: Task.of(x * 10))

    # then
    assert bind_task.fork(lambda x: x, lambda x: x) == 50



# Generated at 2022-06-14 04:03:07.497068
# Unit test for method bind of class Task
def test_Task_bind():
    def async_success_fn(value):
        def async_call(reject, resolve):
            resolve(value)

        return Task(async_call)

    def async_error_fn(value):
        def async_call(reject, resolve):
            reject(value)

        return Task(async_call)

    def async_call_with_two_resolve(reject, resolve):
        resolve(1)
        resolve(10)

    assert Task(async_call_with_two_resolve)\
        .bind(async_success_fn)\
        .map(lambda arg: f"test({arg})")\
        .fork(lambda arg: arg, lambda result: result)\
        == "test(1)"


# Generated at 2022-06-14 04:03:15.478555
# Unit test for method bind of class Task
def test_Task_bind():
    def first_task(reject, resolve):
        resolve(1)

    def second_task(reject, resolve):
        resolve(2)

    def third_task(reject, resolve):
        resolve(3)

    assert Task(first_task).bind(
        lambda first: Task(second_task).bind(
            lambda second: Task(third_task).map(
                lambda third: [first, second, third]
            )
        )
    ).fork(None, lambda value: value) == [1, 2, 3]

# Generated at 2022-06-14 04:03:20.166594
# Unit test for method bind of class Task
def test_Task_bind():
    def task1_fork(reject, resolve):
        return resolve(1)

    def task2_fork(reject, resolve):
        return resolve(2)

    def fn(v):
        return Task(task2_fork)

    task1 = Task(task1_fork)
    result = task1.bind(fn)
    assert result.fork(lambda r: r, lambda r: r) == 2

# Generated at 2022-06-14 04:03:27.621546
# Unit test for method map of class Task
def test_Task_map():
    def test_map_resolve_set_value(resolve, reject):
        def fn(x):
            return x * 10

        resolve(10)

        return Task(test_map_resolve_set_value).map(fn)


# Generated at 2022-06-14 04:03:32.467888
# Unit test for method map of class Task
def test_Task_map():
    def to_str(value):
        return str(value)

    input = Task.of(42)
    output = input.map(to_str)
    expected = Task.of('42')

    assert output.fork(
        lambda _: False,
        lambda arg: arg == expected.fork(
            lambda _: None,
            lambda _: arg
        )
    ) == True


# Generated at 2022-06-14 04:03:37.141935
# Unit test for method bind of class Task
def test_Task_bind():
    @Task
    def fork(reject, resolve):
        resolve('foo')

    @Task
    def bind_fork(reject, resolve):
        resolve('bar')

    value = fork.bind(lambda value: bind_fork)
    assert value == 'bar', 'test_Task_bind for bind() return not correct value'

# Generated at 2022-06-14 04:03:47.911591
# Unit test for method map of class Task
def test_Task_map():
    def resolve(value):
        print("| - Resolving task with: " + str(value))
        return value

    def reject(value):
        print("| - Rejecting task with: " + str(value))
        return value

    task = Task.of(10)
    print("| - Testing map on task: " + str(task))
    task1 = task.map(lambda x: x + 10)
    print("| - Task result: " + str(task1))
    task2 = task.map(lambda x: x + 10).map(lambda x: x + 10)
    print("| - Task result: " + str(task2))
    assert task1.fork(reject, resolve) == 20
    assert task2.fork(reject, resolve) == 30
    print("* - Success.\n")




# Generated at 2022-06-14 04:03:56.534763
# Unit test for method bind of class Task
def test_Task_bind():
    class SomeClass:
        """
        Some class for test binding.
        """

        def __init__(self, value=0):
            self.value = value

        def addValue(self, value):
            self.value += value

    def someFn(value):
        """
        some function for test binding.

        :param value: `SomeClass` with value
        :type value: `SomeClass`
        """
        assert value is not None
        assert type(value) is SomeClass

        sc = SomeClass(value.value)
        sc.addValue(1)
        return sc

    def someFnErr(value):
        if value:
            return Task.reject(value)
        return Task.reject("Some error")

    def testFn(reject, resolve):
        resolve("value")

   

# Generated at 2022-06-14 04:04:08.094284
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test function bind with Task[reject, mapped_value] as result
    """
    def fn(value):
        return Task.of(value + ' mapped')
    task = Task.of('value').bind(fn)
    assert task.fork(lambda err: 'Failed', lambda val: val) == 'value mapped'


    def fn(value):
        return Task.reject(value + ' rejected')
    task = Task.of('value').bind(fn)
    assert task.fork(lambda err: err, lambda _: 'Failed') == 'value rejected'


    def fn(value):
        return Task.reject(value + ' rejected')
    task = Task.reject('value').bind(fn)
    assert task.fork(lambda err: err, lambda _: 'Failed') == 'value rejected'



# Generated at 2022-06-14 04:04:38.296940
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('test').map(lambda arg : arg).fork({}, {}) == 'test'
    assert Task.of('test').map(lambda arg : arg + '_test').fork({}, {}) == 'test_test'
    assert Task.of('test').map(lambda arg : arg + '_test').map(lambda arg : arg + '_test').fork({}, {}) == 'test_test_test'
    assert Task.of('test').map(lambda arg : arg + '_test').map(lambda arg : arg + '_test').map(lambda arg : 'test').fork({}, {}) == 'test'

# Generated at 2022-06-14 04:04:44.460372
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.reject(0).bind(lambda x: Task.reject(1)).fork(
        lambda a: a == 0,
        lambda a: a == 1
    )

    assert Task.of(0).bind(lambda x: Task.of(1)).fork(
        lambda a: a == 0,
        lambda a: a == 1
    )


# Generated at 2022-06-14 04:04:52.109738
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value*10)

    task = Task.of(10)
    result = task.bind(mapper).fork(lambda arg: arg, lambda arg: arg)

    assert result == 100

    task = Task.reject("test")
    result = task.bind(mapper).fork(lambda arg: arg, lambda arg: arg)

    assert result == "test"


# Generated at 2022-06-14 04:04:56.818806
# Unit test for method map of class Task
def test_Task_map():
    """Test for map method of Task class."""

    def test_fn(value):
        return 2 * value

    task = Task.of(1)
    task_result = task.map(test_fn)
    assert task_result.fork(lambda reject: None, lambda resolve: resolve) == 2


# Generated at 2022-06-14 04:05:05.430345
# Unit test for method map of class Task
def test_Task_map():
    from mock import Mock
    task = Task(Mock(return_value=None))

    mapper = Mock(return_value=10)
    result = task.map(mapper)

    assert result.fork.called
    assert mapper.called

    task.fork.assert_called_once_with(result.fork.return_value,
                                      result.fork.call_args[0][1])
    mapper.assert_called_once_with(task.fork.call_args[0][1].return_value)

    task.fork.reset_mock()
    mapper.reset_mock()

    def inner_mapper(arg):
        assert arg == 100
        return 1

    inner_task = Task(Mock(return_value=None))
    inner_task.fork.return_value = 100

    result

# Generated at 2022-06-14 04:05:12.136609
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Example of using bind method.
    """

    task = Task.of(2)
    task_b = task.bind(lambda x: Task.of(x*x))

    def fork(reject, resolve):
        return task_b.fork(reject, resolve)

    result = fork(lambda value: 'Rejected: %s' % value, lambda value: 'Resolved: %s' % value)
    assert result == 'Resolved: 4'



# Generated at 2022-06-14 04:05:20.783052
# Unit test for method bind of class Task
def test_Task_bind():
    def inc(arg):
        return arg + 1

    def er(arg):
        return Task.of(0)

    def oth(arg):
        return Task.of(arg + 1)

    assert Task.of(0).bind(er) == Task.of(0)
    assert Task.reject(0).bind(er) == Task.of(0)
    assert Task.of(0).bind(oth) == Task.of(1)



# Generated at 2022-06-14 04:05:30.913813
# Unit test for method map of class Task
def test_Task_map():
    def addOne(x): return x + 1
    def addTwo(x): return x * 2

    assert Task.of(1).map(addOne).map(addTwo).fork(None, None) == 4
    assert Task.of(2).map(addOne).map(addTwo).fork(None, None) == 6
    assert Task.of(3).map(addOne).map(addTwo).fork(None, None) == 8
    assert Task.of(4).map(addOne).map(addTwo).fork(None, None) == 10
    assert Task.of(5).map(addOne).map(addTwo).fork(None, None) == 12
    print('test_Task_map OK')


# Generated at 2022-06-14 04:05:34.418500
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda _, resolve: resolve(42)) \
        .map(lambda x: x * 2) \
        .fork(lambda e: e, identity) == 84


# Generated at 2022-06-14 04:05:36.901517
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(a):
        return Task.of(a * a)

    assert Task.of(10).bind(mapper).fork(lambda reject: 0, lambda resolve: resolve) == 100


# Generated at 2022-06-14 04:06:34.335608
# Unit test for method map of class Task
def test_Task_map():
    # Returns 10
    def add(value):
        return value + 10

    assert Task.of(1).map(add).fork(lambda _: None, lambda arg: arg) == 11

    # Returns 1
    def sub(value):
        return value - 1

    assert Task.of(10).map(sub).fork(lambda _: None, lambda arg: arg) == 9


# Generated at 2022-06-14 04:06:44.104744
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    def test_normal_case():
        """
        Test bind method in normal case
        """
        state = {
            'count': 0,
            'value': None,
        }

        def test_function(value):
            """
            Test function, increment state.count and return
            Task of result with stored value argument.
            """
            state['count'] += 1
            return Task.of(value)

        def set_value(value):
            """
            Set state.value with value argument.
            """
            state['value'] = value

        t_task = Task.of(1)
        t_task.bind(test_function).bind(set_value)

        assert state == {'count': 2, 'value': 1}


# Generated at 2022-06-14 04:06:54.193447
# Unit test for method bind of class Task
def test_Task_bind():
    def task_of(value):
        return Task.of(value)

    def inc(num):
        return num + 1

    # Task[resolve, resolve] -> Task[reject, resolve] -> Task[reject, resolve]
    # Task.of(10) -> Task.of(11) -> Task.of(12)
    result = Task.of(10).bind(task_of).bind(task_of)
    assert result.fork(lambda reject: "reject", lambda resolve: resolve) == 12

    # Task[reject, resolve] -> reject
    # Task.reject(10) -> reject(11)
    result = Task.reject(10).bind(lambda reject: task_of(reject + 1))
    assert result.fork(lambda reject: reject, lambda resolve: "resolve") == 11

    # Task

# Generated at 2022-06-14 04:07:04.586745
# Unit test for method bind of class Task
def test_Task_bind():
    def double(x):
        return x * 2

    def square(x):
        return x ** 2

    def plus(x, y):
        return x + y

    assert Task.of(5).bind(lambda x: Task.of(double(x))).bind(lambda x: Task.of(square(x))).fork(None, lambda x: x) == 100
    assert Task.of(5).bind(lambda x: Task.reject(x + 1)).fork(lambda x: x, None) == 6
    assert Task.reject(5).bind(lambda x: Task.reject(x + 1)).fork(lambda x: x, None) == 5

# Generated at 2022-06-14 04:07:14.735301
# Unit test for method bind of class Task
def test_Task_bind():
    def throw(x):
        raise Exception('Test error')

    def fn(x):
        return x + 10

    def fn2(x):
        return Task.reject(x + 20)

    def fn3(x):
        return Task.of(x + 30)

    assert Task.of(5).bind(fn).fork(throw, lambda resolved: resolved == 15)
    assert Task.of(5).bind(fn2).fork(lambda rejected: rejected == 15, throw)
    assert Task.of(5).bind(fn3).fork(throw, lambda resolved: resolved == 35)
    assert Task.reject(5).bind(fn).fork(lambda rejected: rejected == 5, throw)
    assert Task.reject(5).bind(fn2).fork(lambda rejected: rejected == 5, throw)

# Generated at 2022-06-14 04:07:18.354771
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)

# Generated at 2022-06-14 04:07:22.523542
# Unit test for method map of class Task
def test_Task_map():
    TASK_TO_TEST = Task(lambda reject, resolve: resolve(1))
    assert TASK_TO_TEST.map(lambda x: x + 1).fork(None, None) == 2


# Generated at 2022-06-14 04:07:27.951562
# Unit test for method bind of class Task
def test_Task_bind():
    fork = lambda r, s: s(20)
    task = Task(fork)
    task2 = task.bind(lambda x: Task.of(x + 20))

    def resolve(_):
        return True

    def reject(__):
        return False

    assert task2.fork(reject, resolve) == True



# Generated at 2022-06-14 04:07:30.908097
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        return resolve(42)
    
    task = Task(fork)
    mapped_task = task.map(lambda x: x + 6)

    assert mapped_task.fork(lambda x: None, lambda x: x) == 48


# Generated at 2022-06-14 04:07:37.616714
# Unit test for method bind of class Task
def test_Task_bind():
    # Setup a reject Task
    first_task = Task.reject(None)

    # Setup a resolve Task
    second_task = Task.of(None)

    # Call bind on that task and check if results are the same
    def fn(arg):
        return Task.of(1)
    assert first_task.bind(fn) == second_task.bind(fn)
