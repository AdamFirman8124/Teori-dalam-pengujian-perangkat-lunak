

# Generated at 2022-06-14 00:06:02.912269
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Test(BaseProvider):
        """Test provider."""

        class Meta:
            """Class for metadata."""

            name = 'test'

        def example(self) -> str:
            """Test method."""
            return 'Hello, test!'

    generic = Generic()
    generic.add_provider(Test)
    assert generic.test._example() == 'Hello, test!'
    assert generic.test.example() == 'Hello, test!'


# Generated at 2022-06-14 00:06:12.750076
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
  g = Generic()
  print(g.person.full_name())
  print(g.address.address())
  print(g.datetime.date())
  print(g.business.company())
  print(g.text.sentence())
  print(g.food.dish())
  print(g.science.chemical_element())
  print(g.transport.vehicle())
  print(g.code.ipv4())
  print(g.unit_system.weight())
  print(g.file.mime_type())
  print(g.numbers.decimal())
  print(g.development.password())
  print(g.hardware.cpu())
  print(g.clothing.clothe())
  print(g.internet.url())
  print(g.path.path())
  print

# Generated at 2022-06-14 00:06:17.768050
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """
    unit test for method add_provider of class Generic
    """
    provider = Generic()
    provider.add_provider(Address)
    assert 'address' in dir(provider)
    provider.add_provider(Business)
    assert 'business' in dir(provider)

# Generated at 2022-06-14 00:06:22.940059
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person is g.__dict__['_person'](g.locale, g.seed)
    assert g.address is g.__dict__['_address'](g.locale, g.seed)
    assert g.datetime is g.__dict__['_datetime'](g.locale, g.seed)


# Generated at 2022-06-14 00:06:27.066004
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import mimesis.providers.education as education

    g = Generic()
    g.add_provider(education.Education)
    assert isinstance(g.education, education.Education)



# Generated at 2022-06-14 00:06:37.642312
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    obj = Generic()
    assert obj.person
    assert obj.address
    assert obj.datetime
    assert obj.business
    assert obj.text
    assert obj.food
    assert obj.science
    assert obj.transport
    assert obj.code
    assert obj.unit_system
    assert obj.file
    assert obj.numbers
    assert obj.development
    assert obj.hardware
    assert obj.clothing
    assert obj.internet
    assert obj.path
    assert obj.payment
    assert obj.cryptographic
    assert obj.structure
    assert obj.choice
    assert obj.choice


# Generated at 2022-06-14 00:06:43.340293
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test method add provider."""
    from mimesis.providers.person import PersonalInfo
    gen = Generic()
    gen.add_provider(PersonalInfo)
    value = gen.personal_info.name(gender='female')
    assert value
    assert hasattr(gen, 'personal_info')



# Generated at 2022-06-14 00:06:48.833333
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.code import Code
    g = Generic()

    g.add_provider(Code)
    assert g.code.code() == 'T9F93X'



# Generated at 2022-06-14 00:06:50.626646
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    assert generic.person.full_name() == 'Jean-Louis Salaun'


# Generated at 2022-06-14 00:06:52.994608
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        pass

    g = Generic()
    g.add_provider(MyProvider)
    assert g.myprovider is not None

