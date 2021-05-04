# Amtega wso2am role

This is an [Ansible](http://www.ansible.com) role to deploy WSO2 API Manager

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

The role setups the following facts:

- `wso2am_latest_version`: latest version of wso2am available on the web. This fact is only available if you are downloading from the official site.
- `wso2am_needs_restart`: when variable `wso2am_manage_service_state` is set to false this fact indicates if wso2am service needs to be restarted after changes.

## Example Playbook

This is an example playbook:

``` yaml
---
- hosts: localhost
  roles:  
    - amtega.wso2am
  vars:
    wso2am_state: present
    wso2am_version: latest
```

## Testing

Tests are based on [molecule with docker containers](https://molecule.readthedocs.io/en/latest/installation.html).

```shell
cd amtega.wso2am

molecule test --all
```

## License

Copyright (C) 2020 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
