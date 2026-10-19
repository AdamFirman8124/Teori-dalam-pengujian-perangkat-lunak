

# Generated at 2022-06-14 00:05:56.886417
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    pass

# Generated at 2022-06-14 00:06:08.931021
# Unit test for method __getattr__ of class Generic

# Generated at 2022-06-14 00:06:15.850844
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider method of class Generic.
    """
    # Arrange
    class Provider():
        class Meta():
            name = "provider"
    obj = Generic()
    # Act
    obj.add_provider(Provider)
    # Assert
    assert "provider" in dir(obj)


# Generated at 2022-06-14 00:06:19.339349
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    g.add_provider(Person)
    g.add_provider(Datetime)
    assert g.person
    assert g.datetime
    assert g.person.full_name()
    assert g.datetime.month()



# Generated at 2022-06-14 00:06:21.698825
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    g.add_provider(Code)
    assert g.code.is_md5()


# Generated at 2022-06-14 00:06:30.996876
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    d = Generic()
    # set the first argument to "en-US"
    d._person = Person
    d._address = Address
    d._datetime = Datetime
    d._business = Business
    d._text = Text
    d._food = Food
    d._science = Science

    # test person
    assert d.person.__class__ == Person(locale="en-US", seed=None)
    assert d.person.full_name() == "Karen Petit"
    # test address
    assert d.address.__class__ == Address(locale="en-US", seed=None)
    assert d.address.country() == "Kazakhstan"
    assert d.address.address() == "84471 Jana Square"
    assert d.address.city() == "Midland"
    assert d.address

# Generated at 2022-06-14 00:06:40.284400
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    item = Generic()
    assert callable(item.person)
    assert callable(item.address)
    assert callable(item.datetime)
    assert callable(item.business)
    assert callable(item.text)
    assert callable(item.food)
    assert callable(item.science)
    assert callable(item.transport)
    assert callable(item.code)
    assert callable(item.unit_system)
    assert callable(item.file)
    assert callable(item.numbers)
    assert callable(item.development)
    assert callable(item.hardware)
    assert callable(item.clothing)
    assert callable(item.internet)
    assert callable(item.path)


# Generated at 2022-06-14 00:06:46.197013
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # define a custom provider
    class Test(BaseProvider):
        class Meta:
            name = 'test'
        def test(self):
            return 'a test'
    # add provider
    generic = Generic()
    generic.add_provider(Test)
    assert isinstance(generic.test, Test)
    assert generic.test.test() == 'a test'


# Generated at 2022-06-14 00:06:48.833337
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    gender = Generic().person.gender()
    assert gender in ['Male', 'Female']

# Generated at 2022-06-14 00:06:50.749098
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    obj = Generic()
    assert obj._person is not None
