# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from toml import dumps, TomlEncoder

class AnsibleTomlEncoder(TomlEncoder):
    """TomlEncoder taht supports ansible AnsibleUnsafeText"""

    def __init__(self, _dict=dict, preserve=False):
        """Constructor"""
        super(AnsibleTomlEncoder, self).__init__(_dict, preserve)

        self.dump_funcs[AnsibleUnsafeText] = self.dump_funcs[str]

def wso2am_to_toml(data):
    """Convert the value to TOML"""
    return dumps(data, encoder=AnsibleTomlEncoder())

class FilterModule(object):
    """Ansible filters."""

    def filters(self):
        return {
            "wso2am_to_toml": wso2am_to_toml
        }
