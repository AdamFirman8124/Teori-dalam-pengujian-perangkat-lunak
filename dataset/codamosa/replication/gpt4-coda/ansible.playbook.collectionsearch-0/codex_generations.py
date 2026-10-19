

# Generated at 2024-03-18 02:49:54.627666
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:50:03.518991
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:50:11.228174
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections are provided."

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when collections are provided."

    # Test with both default and builtin collections provided
    cs_with_builtin = CollectionSearch(collections=['ansible.builtin', 'my_namespace.my_collection'])
    assert cs_with_builtin._collections == ['ansible.builtin', 'my_namespace.my_collection', 'ansible.legacy'], "ansible.legacy not appended when ansible.builtin is provided."

    # Test with templated collection name
    cs_with_templated_name = CollectionSearch(collections=['{{ my_collection_var }}'])
    assert cs_with_templated_name

# Generated at 2024-03-18 02:50:20.094941
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections list not handled correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
   

# Generated at 2024-03-18 02:50:31.600792
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:50:37.828672
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always in the list
    cs_builtin_legacy = CollectionSearch()
    cs

# Generated at 2024-03-18 02:50:43.651943
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_test_collections = CollectionSearch()
    cs_test_collections._collections = test_collections
    assert cs_test_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always in the list
    cs_builtin_legacy = CollectionSearch()
   

# Generated at 2024-03-18 02:50:48.621340
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Create an instance of CollectionSearch with no collections specified
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are specified."

    # Create an instance of CollectionSearch with specific collections specified
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are specified."

    # Create an instance of CollectionSearch with a templated collection name
    templated_collections = ['{{ my_namespace.my_collection }}']
    cs_templated_collections = CollectionSearch()
    cs_templated_collections._collections = templated_collections

# Generated at 2024-03-18 02:50:54.846797
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test that 'ansible.legacy' is added if not present
    cs_legacy_check = CollectionSearch()

# Generated at 2024-03-18 02:51:03.931438
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.builtin', 'ansible.legacy'], \
        "Default collections should include 'ansible.builtin' and 'ansible.legacy'"

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == ['my_namespace.my_collection', 'ansible.builtin', 'ansible.legacy'], \
        "Custom collections should be prepended with the default collection and 'ansible.legacy'"

    # Test with default collection already included
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default

# Generated at 2024-03-18 02:51:19.615398
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection should be 'ansible.legacy' when no collections are provided"

    # Test with default collection provided
    AnsibleCollectionConfig.default_collection = 'my_namespace.my_collection'
    cs_default_collection = CollectionSearch()
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection should be included along with 'ansible.legacy'"

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == ['my_namespace.my_collection', 'another_namespace.another_collection', 'ansible.legacy'], "Custom collections should be included along with 'ansible.legacy'"

    # Test with 'ansible

# Generated at 2024-03-18 02:51:25.283188
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with empty collections list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections list not set correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
    cs

# Generated at 2024-03-18 02:51:31.296403
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:51:36.624410
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always in the list
    cs_builtin_legacy = CollectionSearch()
    cs

# Generated at 2024-03-18 02:51:44.872451
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:51:52.378972
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:51:58.739797
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:52:05.424362
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections are provided."

    # Test with default collection provided
    AnsibleCollectionConfig.default_collection = 'my_namespace.my_collection'
    cs_default_collection = CollectionSearch()
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when default is set."

    # Reset default collection for further tests
    AnsibleCollectionConfig.default_collection = None

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch(collections=custom_collections)
    assert cs_custom_collections._collections == custom_collections + ['ansible.legacy'], "Custom collections not set correctly."

    # Test with custom collections provided including ansible.builtin
    custom_collections_with_builtin

# Generated at 2024-03-18 02:52:11.214788
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:52:19.954932
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Default collections not added to custom collections list."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch

# Generated at 2024-03-18 02:52:40.693399
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Create an instance of CollectionSearch with no collections specified
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are specified."

    # Create an instance of CollectionSearch with specific collections specified
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are specified."

    # Create an instance of CollectionSearch with a templated collection name
    templated_collections = ['{{ my_namespace.my_collection }}']
    cs_templated_collections = CollectionSearch()
    cs_templated_collections._collections = templated_collections

# Generated at 2024-03-18 02:52:47.298370
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:52:52.959205
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
    cs_custom

# Generated at 2024-03-18 02:52:57.978785
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly when default collection is not in the list."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom

# Generated at 2024-03-18 02:53:04.686918
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.builtin', 'ansible.legacy'], \
        "Default collections should include 'ansible.builtin' and 'ansible.legacy'"

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == ['ansible_collections.my_namespace.my_collection', 'ansible.builtin', 'ansible.legacy'], \
        "Custom collections should be prefixed with 'ansible_collections.' and include 'ansible.builtin' and 'ansible.legacy'"

    # Test with default collection set in AnsibleCollectionConfig
    AnsibleCollectionConfig.default_collection = 'my_default.collection'
    cs_default_collection = CollectionSearch()

# Generated at 2024-03-18 02:53:10.896686
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:53:16.174086
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
    cs_custom

# Generated at 2024-03-18 02:53:22.014366
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always in the list

# Generated at 2024-03-18 02:53:30.326873
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.builtin', 'ansible.legacy'], \
        "Default collections should include 'ansible.builtin' and 'ansible.legacy'"

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch(collections=custom_collections)
    assert cs_custom_collections._collections == ['ansible.builtin', 'my_namespace.my_collection', 
                                                  'another_namespace.another_collection', 'ansible.legacy'], \
        "Custom collections should be prefixed with 'ansible.builtin' and suffixed with 'ansible.legacy'"

    # Test with default collection provided
    AnsibleCollectionConfig.default_collection = 'default.namespace.default_collection'
    cs_default_collection = CollectionSearch()

# Generated at 2024-03-18 02:53:38.427566
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy']

    # Test with default collection provided
    cs_default_collection = CollectionSearch()
    cs_default_collection._collections = ['my_namespace.my_collection']
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy']

    # Test with multiple collections provided
    cs_multiple_collections = CollectionSearch()
    cs_multiple_collections._collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    assert cs_multiple_collections._collections == ['my_namespace.my_collection', 'another_namespace.another_collection', 'ansible.legacy']

    # Test with 'ansible.builtin' provided
    cs_builtin_collection = CollectionSearch()
    cs_builtin_collection._collections = ['ansible.builtin']
    assert cs_builtin_collection._collections == ['ansible.builtin', 'ansible.legacy']

    # Test with 'ansible.legacy'

# Generated at 2024-03-18 02:54:15.159661
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test with default collection in the list
    test_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default_collection

# Generated at 2024-03-18 02:54:25.443629
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always present
    cs_with_builtin_legacy = CollectionSearch()
    cs

# Generated at 2024-03-18 02:54:31.633663
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:54:38.539778
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly when an empty list is provided."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
   

# Generated at 2024-03-18 02:54:44.630457
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:54:53.358490
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections with 'ansible.builtin' should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:55:00.259783
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always present

# Generated at 2024-03-18 02:55:07.234006
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly for an empty collections list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test that 'ansible.builtin' or 'ansible.legacy' is always in the list

# Generated at 2024-03-18 02:55:15.687790
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.builtin', 'ansible.legacy'], \
        "Default collections should include 'ansible.builtin' and 'ansible.legacy'"

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == ['my_namespace.my_collection', 'ansible.builtin', 'ansible.legacy'], \
        "Custom collections should be prepended with the default collection and appended with 'ansible.legacy'"

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default

# Generated at 2024-03-18 02:55:24.107927
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections are provided."

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when other collections are provided."

    # Test with both default and builtin collections provided
    cs_with_builtin = CollectionSearch(collections=['ansible.builtin', 'my_namespace.my_collection'])
    assert cs_with_builtin._collections == ['ansible.builtin', 'my_namespace.my_collection', 'ansible.legacy'], "ansible.legacy not appended when ansible.builtin is provided."

    # Test with templated collection name
    cs_templated_name = CollectionSearch(collections=['{{ my_collection_var }}'])
    assert cs_templated_name._

# Generated at 2024-03-18 02:56:35.250202
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections provided"

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when collections provided"

    # Test with both default and builtin collections provided
    cs_with_builtin = CollectionSearch(collections=['ansible.builtin', 'my_namespace.my_collection'])
    assert cs_with_builtin._collections == ['ansible.builtin', 'my_namespace.my_collection', 'ansible.legacy'], "ansible.legacy not appended when ansible.builtin is present"

    # Test with templated collection name
    cs_with_templated_name = CollectionSearch(collections=['{{ my_collection_var }}'])
    assert cs_with_templated_name._collections

# Generated at 2024-03-18 02:56:42.680082
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections provided"

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when collections provided"

    # Test with both default and builtin collections provided
    cs_with_builtin = CollectionSearch(collections=['ansible.builtin', 'my_namespace.my_collection'])
    assert cs_with_builtin._collections == ['ansible.builtin', 'my_namespace.my_collection', 'ansible.legacy'], "ansible.legacy not appended when ansible.builtin is present"

    # Test with templated collection name
    cs_templated_name = CollectionSearch(collections=['{{ my_collection }}'])

# Generated at 2024-03-18 02:56:51.829719
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection should be 'ansible.legacy' when no collections are provided"

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection should be included along with 'my_namespace.my_collection'"

    # Test with multiple collections provided
    cs_multiple_collections = CollectionSearch(collections=['my_namespace.my_collection', 'another_namespace.another_collection'])
    assert cs_multiple_collections._collections == ['my_namespace.my_collection', 'another_namespace.another_collection', 'ansible.legacy'], "Both specified collections should be included along with 'ansible.legacy'"

    # Test with ansible.builtin provided
    cs_builtin_collection = CollectionSearch(collections=['ansible.builtin'])
   

# Generated at 2024-03-18 02:56:59.939815
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with custom collections provided
    custom_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with default collection in the list
    collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default
    assert cs_with_default._collections == collections_with_default, \
        "Collections list with default collection should not be modified."

    # Test with legacy collection in the list

# Generated at 2024-03-18 02:57:08.055236
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection not set correctly when no collections are provided."

    # Test with default collection provided
    cs_default_collection = CollectionSearch()
    cs_default_collection._collections = ['my_namespace.my_collection']
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection not included when other collections are provided."

    # Test with multiple collections provided including the default
    cs_multiple_collections = CollectionSearch()
    cs_multiple_collections._collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    assert cs_multiple_collections._collections == ['my_namespace.my_collection', 'another_namespace.another_collection', 'ansible.legacy'], "Default collection not included with multiple collections."

    # Test with ansible.builtin in the list
    cs_with_builtin = CollectionSearch()
    cs_with_builtin

# Generated at 2024-03-18 02:57:13.835512
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with custom collections list without default collection
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == _ensure_default_collection(custom_collections), \
        "Custom collections not set correctly."

    # Test with custom collections list including default collection
    custom_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_custom_with_default = CollectionSearch()
    cs_custom

# Generated at 2024-03-18 02:57:20.190928
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection(), \
        "Default collections not set correctly when no collections are provided."

    # Test with empty collections list
    cs_empty_collections = CollectionSearch()
    cs_empty_collections._collections = []
    assert cs_empty_collections._collections == _ensure_default_collection([]), \
        "Default collections not set correctly with an empty list."

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections), \
        "Collections not set correctly when specific collections are provided."

    # Test to ensure 'ansible.builtin' or 'ansible.legacy' is always in the list
    cs_builtin_legacy = CollectionSearch()
    cs

# Generated at 2024-03-18 02:57:28.379757
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection should be 'ansible.legacy' when no collections are provided"

    # Test with default collection provided
    cs_default_collection = CollectionSearch(collections=['my_namespace.my_collection'])
    assert cs_default_collection._collections == ['my_namespace.my_collection', 'ansible.legacy'], "Default collection should be included along with 'my_namespace.my_collection'"

    # Test with multiple collections provided
    cs_multiple_collections = CollectionSearch(collections=['my_namespace.my_collection', 'another_namespace.another_collection'])
    assert cs_multiple_collections._collections == ['my_namespace.my_collection', 'another_namespace.another_collection', 'ansible.legacy'], "Both specified collections should be included along with 'ansible.legacy'"

    # Test with ansible.builtin provided
    cs_builtin_collection = CollectionSearch(collections=['ansible.builtin'])
   

# Generated at 2024-03-18 02:57:33.967876
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Test with no collections provided
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == _ensure_default_collection()

    # Test with empty list provided
    cs_empty_list = CollectionSearch()
    cs_empty_list._collections = []
    assert cs_empty_list._collections == _ensure_default_collection([])

    # Test with specific collections provided
    test_collections = ['my_namespace.my_collection', 'another_namespace.another_collection']
    cs_with_collections = CollectionSearch()
    cs_with_collections._collections = test_collections
    assert cs_with_collections._collections == _ensure_default_collection(test_collections)

    # Test with default collection included
    test_collections_with_default = ['ansible.builtin', 'my_namespace.my_collection']
    cs_with_default_collection = CollectionSearch()
    cs_with_default_collection._collections = test_collections_with_default
    assert cs_with_default_collection._collections == test_collections_with_default

    # Test with legacy collection included
    test_collections

# Generated at 2024-03-18 02:57:40.838549
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():    # Create an instance of CollectionSearch with no collections specified
    cs_no_collections = CollectionSearch()
    assert cs_no_collections._collections == ['ansible.legacy'], "Default collection should include 'ansible.legacy'"

    # Create an instance of CollectionSearch with a specific collection list
    custom_collections = ['my_namespace.my_collection']
    cs_custom_collections = CollectionSearch()
    cs_custom_collections._collections = custom_collections
    assert cs_custom_collections._collections == ['my_namespace.my_collection', 'ansible.legacy'], \
        "Custom collection list should be appended with 'ansible.legacy'"

    # Create an instance of CollectionSearch with default collection in the list
    collections_with_default = ['ansible.builtin']
    cs_with_default = CollectionSearch()
    cs_with_default._collections = collections_with_default