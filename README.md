# xvfb

[![Build Status](https://travis-ci.org/infOpen/ansible-role-xvfb.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-xvfb)

Install xvfb package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Installation
xvfb_packages: "{{ _xvfb_packages }}"
xvfb_repository_cache_valid_time: 3600
xvfb_repository_update_cache: True
xvfb_binary_path: "{{ _xvfb_binary_path }}"

# Service
xvfb_service_name: 'xvfb'
xvfb_service_enabled: True
xvfb_service_state: 'started'

# Configuration
xvfb_options: ':99 -screen 0 1x1x24 -ac +extension GLX +render -noreset'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.xvfb }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
