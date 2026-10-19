

# Generated at 2022-06-13 04:06:17.927279
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    _LinuxVirtual = LinuxVirtual()
    facts = _LinuxVirtual.get_virtual_facts()
    assert facts['is_virtual'] is True


# Generated at 2022-06-13 04:06:20.719487
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    if not module.check_mode:
        linux_virtual = LinuxVirtual(module)
        linux_virtual.get_virtual_facts()


# Generated at 2022-06-13 04:06:31.795622
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    linux_virtual = LinuxVirtual()
    # FIXME:
    # - Add tests for data in systemd_container
    # - Add tests for data in openvz
    # - Add tests for data in xen
    # - Add tests for data in powervm_lx86
    # - Add tests for data in uml
    # - Add tests for data in vdsm
    # - Add tests for data in parallels
    # - Add tests for data in pseries
    # - Add tests for data in openstack
    # - Add tests for data in virtio
    # - Add tests for data in VirtualPC
    # - Add tests for data in KubeVirt
    # - Add tests for data in linux_vserver
    # - Add tests for data in containers
    # - Add tests for data in RHEV
    # - Add tests for data in dm

# Generated at 2022-06-13 04:06:40.079670
# Unit test for method get_virtual_facts of class LinuxVirtual

# Generated at 2022-06-13 04:06:41.670044
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    lv = LinuxVirtualCollector()
    assert lv._fact_class is LinuxVirtual
    assert lv._platform == 'Linux'
    assert lv.virtual_facts is None

# Generated at 2022-06-13 04:06:46.704746
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    # get_virtual_facts is a method of LinuxVirtual class
    set_module_args(dict(
        gather_subset='all'
    ))
    # Will fail but lets us continue
    #p = module.params
    obj = LinuxVirtual(module)

    # Testing virtualization facts
    virtual = obj.get_virtual_facts()
    for k, v in dict(virtualization_type="NA",
                     virtualization_role="NA",
                     virtualization_tech_guest=set(['NA']),
                     virtualization_tech_host=set(['NA'])).items():
       assert virtual[k] == v


# Generated at 2022-06-13 04:06:47.357341
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    assert(LinuxVirtualCollector is not None)



# Generated at 2022-06-13 04:06:52.570018
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    l = LinuxVirtual(None)
    with mock.patch("os.path.exists", return_value=True):
        # Found vserver
        with mock.patch("__main__.get_file_content", return_value="10"):
            with mock.patch("os.access", return_value=True):
                with mock.patch("__main__.get_file_lines", return_value=[
                    "Vendor: xVM",
                    "VxID: 0",
                ]), mock.patch("__main__.get_bin_path", return_value=True):
                    virtual_facts = l.get_virtual_facts()
                    assert virtual_facts['virtualization_type'] == 'Linux_VServer'
                    assert virtual_facts['virtualization_role'] == 'host'

        # Found vserver

# Generated at 2022-06-13 04:06:53.386130
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    virtual = LinuxVirtual()
    return virtual.get_virtual_facts()

# Generated at 2022-06-13 04:06:55.781479
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():

    collector = LinuxVirtualCollector("foo")
    assert collector._platform == "Linux"
    assert collector._fact_class == LinuxVirtual