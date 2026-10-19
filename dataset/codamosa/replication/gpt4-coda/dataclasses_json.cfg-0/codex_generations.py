

# Generated at 2024-03-18 05:12:31.055540
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:12:32.963092
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:12:34.919298
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:12:40.602514
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom encoder
    custom_encoder = lambda x: f"encoded_{x}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test with custom decoder
    custom_decoder = lambda x: f"decoded_{x}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test with custom Marshmallow field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test with custom letter case
    custom_letter_case = lambda x: x.upper()
    assert config(letter_case=custom_letter_case) == {'dataclasses_json': {'letter_case': custom_letter_case}}

    # Test with undefined parameter

# Generated at 2024-03-18 05:12:43.860617
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:12:49.114069
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()


# Generated at 2024-03-18 05:12:51.304487
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:12:53.146908
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:12:54.996952
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:12:56.888898
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:00.873722
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:02.716786
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:05.000384
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:06.764081
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:13:08.375050
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:09.999563
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:13:11.506827
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:13.248071
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:13:18.255827
# Unit test for function config
def test_config():    # Test default metadata
    default_metadata = config()
    assert 'dataclasses_json' in default_metadata
    assert default_metadata['dataclasses_json'] == {}

    # Test encoder
    def sample_encoder(value):
        return f"encoded_{value}"

    metadata_with_encoder = config(encoder=sample_encoder)
    assert 'encoder' in metadata_with_encoder['dataclasses_json']
    assert metadata_with_encoder['dataclasses_json']['encoder'] == sample_encoder

    # Test decoder
    def sample_decoder(value):
        return f"decoded_{value}"

    metadata_with_decoder = config(decoder=sample_decoder)
    assert 'decoder' in metadata_with_decoder['dataclasses_json']
    assert metadata_with_decoder['dataclasses_json']['decoder'] == sample_decoder

    # Test mm_field
    sample_mm_field = MarshmallowField()
    metadata_with_mm_field = config(mm_field=sample_mm_field)

# Generated at 2024-03-18 05:13:19.795721
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:13:24.746597
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:26.834250
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:29.002073
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:29.587825
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:13:31.530471
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:33.398630
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:35.257894
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:37.544276
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:13:40.487086
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:42.445174
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:47.782459
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:49.907599
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:13:51.747208
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:53.921979
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:55.798147
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:13:58.251978
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:13:59.858628
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:14:02.165658
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:14:04.678862
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:14:06.407033
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:14:11.070793
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:14:12.921505
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:14:35.282154
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:14:37.352662
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:14:39.529943
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:14:41.879497
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:14:43.895139
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:14:52.683028
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()


# Generated at 2024-03-18 05:14:55.520575
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:14:57.185480
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:02.987339
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:05.201668
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:07.454986
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:09.680557
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:11.566733
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:13.868032
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:15.556918
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:17.650391
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:19.475222
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:21.344287
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:15:26.232769
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:27.704258
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:29.689177
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:31.613523
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:35.975537
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:37.761762
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:39.723734
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:41.646096
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:43.202192
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:45.626000
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:50.938507
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:52.745741
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:15:54.031405
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:55.693656
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:15:56.945063
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:15:58.675814
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:00.329702
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:07.671310
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom encoder
    custom_encoder = lambda x: f"encoded_{x}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test with custom decoder
    custom_decoder = lambda x: f"decoded_{x}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test with custom Marshmallow field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test with custom letter case
    custom_letter_case = lambda x: x.upper()
    assert config(letter_case=custom_letter_case) == {'dataclasses_json': {'letter_case': custom_letter_case}}

    # Test with custom field name

# Generated at 2024-03-18 05:16:09.500505
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:16:11.650439
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:16:16.724762
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:18.040209
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:21.274709
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:22.890294
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:26.030909
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:29.484001
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:30.900920
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:32.426731
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:16:34.186137
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:16:40.378622
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom encoder
    custom_encoder = lambda x: f"encoded_{x}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test with custom decoder
    custom_decoder = lambda x: f"decoded_{x}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test with custom Marshmallow field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test with custom letter case
    custom_letter_case = lambda x: x.upper()
    assert config(letter_case=custom_letter_case, field_name='test') == {
        'dataclasses_json': {'letter_case': custom_letter_case}
    }

    # Test with undefined parameter


# Generated at 2024-03-18 05:16:45.262975
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:47.477413
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:50.452486
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:16:52.658286
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:01.468651
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder)['dataclasses_json']['encoder'] == custom_encoder

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder)['dataclasses_json']['decoder'] == custom_decoder

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field)['dataclasses_json']['mm_field'] == custom_mm_field

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()

# Generated at 2024-03-18 05:17:03.188907
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:04.995568
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:17:06.480651
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:17:09.965543
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:17:11.644710
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:17:16.885226
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:17:18.255975
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:17:24.175826
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()


# Generated at 2024-03-18 05:17:26.619600
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:29.873572
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:31.991489
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:33.943632
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:17:36.022236
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:17:41.358347
# Unit test for function config
def test_config():    # Test with default parameters
    default_metadata = config()
    assert 'dataclasses_json' in default_metadata
    assert default_metadata['dataclasses_json'] == {}

    # Test with custom encoder
    custom_encoder = lambda x: str(x)
    metadata_with_encoder = config(encoder=custom_encoder)
    assert metadata_with_encoder['dataclasses_json']['encoder'] == custom_encoder

    # Test with custom decoder
    custom_decoder = lambda x: int(x)
    metadata_with_decoder = config(decoder=custom_decoder)
    assert metadata_with_decoder['dataclasses_json']['decoder'] == custom_decoder

    # Test with custom mm_field
    custom_mm_field = MarshmallowField()
    metadata_with_mm_field = config(mm_field=custom_mm_field)
    assert metadata_with_mm_field['dataclasses_json']['mm_field'] == custom_mm_field

    # Test with custom letter_case
    custom_letter_case = lambda x: x.upper()
    metadata_with_letter

# Generated at 2024-03-18 05:17:43.413020
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:17:47.920027
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:17:49.861469
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:17:51.669622
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:52.995167
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:17:54.843503
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:17:56.433878
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:17:57.789825
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:00.929008
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:02.788332
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:04.909995
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:11.316607
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:13.184032
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:15.386421
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:16.979154
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:18:18.694622
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:21.023526
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:23.538262
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:18:26.935159
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:18:28.490445
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:30.669966
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:35.674864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:18:38.004487
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:18:41.057001
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:41.626387
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:18:44.329032
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:46.567721
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:18:53.368575
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder)['dataclasses_json']['encoder'] == custom_encoder

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder)['dataclasses_json']['decoder'] == custom_decoder

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field)['dataclasses_json']['mm_field'] == custom_mm_field

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()

# Generated at 2024-03-18 05:18:54.891119
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:56.974912
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:18:59.240359
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:04.867338
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:06.411018
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:08.182422
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:19:10.223446
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:12.341389
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:13.754923
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:15.730365
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:19:17.596555
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:18.111186
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:19:20.831355
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:25.961302
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:28.025974
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:30.502568
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:19:32.954158
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:34.927402
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:37.024943
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:19:39.027718
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:42.113483
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:42.683099
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:19:44.473835
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:19:49.811457
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:19:51.260998
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:19:54.191014
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:54.699789
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:19:56.861029
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:19:58.863561
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:19:59.389147
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:20:01.301393
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:20:08.445179
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom encoder
    custom_encoder = lambda x: f"encoded_{x}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test with custom decoder
    custom_decoder = lambda x: f"decoded_{x}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test with custom Marshmallow field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test with custom letter case
    custom_letter_case = lambda x: x.upper()
    assert config(letter_case=custom_letter_case, field_name='test') == {
        'dataclasses_json': {'letter_case': custom_letter_case}
    }

    # Test with undefined parameter


# Generated at 2024-03-18 05:20:10.540627
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:16.650512
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:18.741093
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:21.130178
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:20:22.877156
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:20:27.303517
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:30.968382
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:33.863831
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:20:36.536533
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:38.565846
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:20:40.394307
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any value") is False

# Generated at 2024-03-18 05:20:50.440769
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom metadata
    custom_metadata = {'custom_key': 'custom_value'}
    assert config(custom_metadata) == {'custom_key': 'custom_value', 'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder)['dataclasses_json']['encoder'] == custom_encoder

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder)['dataclasses_json']['decoder'] == custom_decoder

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field)['dataclasses_json']['mm_field'] == custom_mm_field

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()

# Generated at 2024-03-18 05:20:53.890404
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:20:56.133894
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:20:58.372902
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:21:00.186839
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:02.168092
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:04.112970
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:21:05.915922
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:08.059069
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:11.865061
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:16.683929
# Unit test for method NEVER of class Exclude

# Generated at 2024-03-18 05:21:18.645650
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:26.607524
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test with custom encoder
    def custom_encoder(value):
        return f"encoded_{value}"
    assert config(encoder=custom_encoder) == {'dataclasses_json': {'encoder': custom_encoder}}

    # Test with custom decoder
    def custom_decoder(value):
        return f"decoded_{value}"
    assert config(decoder=custom_decoder) == {'dataclasses_json': {'decoder': custom_decoder}}

    # Test with custom Marshmallow field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {'dataclasses_json': {'mm_field': custom_mm_field}}

    # Test with custom letter case
    def custom_letter_case(field_name):
        return field_name.upper()
    assert config(letter_case=custom_letter_case, field_name='test') == {
        'dataclasses_json': {'letter_case': custom_letter_case}
    }

    #

# Generated at 2024-03-18 05:21:28.564943
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:31.162582
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:32.926927
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:34.504930
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:38.130606
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:40.234697
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:42.126897
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:21:46.335506
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:48.352762
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:50.892393
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:53.070338
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:21:54.462687
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS(None) is True

# Generated at 2024-03-18 05:21:56.546846
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:22:04.607258
# Unit test for function config
def test_config():    # Test default metadata
    assert config() == {'dataclasses_json': {}}

    # Test encoder
    def custom_encoder(value):
        return f"encoded_{value}"

    assert config(encoder=custom_encoder) == {
        'dataclasses_json': {'encoder': custom_encoder}
    }

    # Test decoder
    def custom_decoder(value):
        return f"decoded_{value}"

    assert config(decoder=custom_decoder) == {
        'dataclasses_json': {'decoder': custom_decoder}
    }

    # Test mm_field
    custom_mm_field = MarshmallowField()
    assert config(mm_field=custom_mm_field) == {
        'dataclasses_json': {'mm_field': custom_mm_field}
    }

    # Test letter_case
    def custom_letter_case(field_name):
        return field_name.upper()


# Generated at 2024-03-18 05:22:06.451531
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any value") is True

# Generated at 2024-03-18 05:22:10.950228
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:22:13.825029
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:22:19.223139
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False

# Generated at 2024-03-18 05:22:21.161905
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:22:21.887739
# Unit test for method ALWAYS of class Exclude

# Generated at 2024-03-18 05:22:23.719194
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():    assert Exclude.ALWAYS("any_value") is True

# Generated at 2024-03-18 05:22:25.858430
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():    assert Exclude.NEVER("any_value") is False