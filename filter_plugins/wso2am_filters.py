# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.parsing.yaml.objects import AnsibleMapping
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

from re import sub
from toml import dumps, TomlEncoder


class AnsibleTomlEncoder(TomlEncoder):
    """TomlEncoder taht supports ansible AnsibleUnsafeText"""

    def __init__(self, _dict=AnsibleMapping, preserve=False):
        """Constructor"""
        super(AnsibleTomlEncoder, self).__init__(_dict, preserve)
        self.dump_funcs[AnsibleUnsafeText] = self.dump_funcs[str]

    def dump_sections(self, o, sup):
        return super(AnsibleTomlEncoder, self).dump_sections(o, sup)


def wso2am_mix_deployment(target_deployment, source_deployment):
    """Mix two deployment dicts

    Args:
        target_deployment (dict): dict with the target deployment
        source_deployment (dict): dict with the source deployment to mix

    Returns:
        dict: dict with the deployments mixed
    """
    result = AnsibleMapping(target_deployment.items())

    for k in source_deployment.keys():
        if k not in result.keys():
            result[k] = source_deployment[k]
        else:
            if isinstance(result[k], dict):
                result[k] = wso2am_mix_deployment(result[k],
                                                  source_deployment[k])
            elif isinstance(result[k], list):
                unique_list = list()
                for x in result[k] + source_deployment[k]:
                     if x not in unique_list:
                         unique_list.append(x)

                result[k] = unique_list
            else:
                result[k] = source_deployment[k]

    return result


def wso2am_to_toml(data):
    """Convert the value to TOML"""
    toml = dumps(data, encoder=AnsibleTomlEncoder())
    result = sub('"(.*)" = (.*)', '\\1 = \\2', toml)
    result = sub('\n\[.*\]\n(\[.*\])', '\n\\1', result)

    return result


class FilterModule(object):
    """Ansible filters."""

    def filters(self):
        return {
            "wso2am_mix_deployment": wso2am_mix_deployment,
            "wso2am_to_toml": wso2am_to_toml
        }
