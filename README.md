Apache 
===
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-smbambling.apache-blue.svg)](https://galaxy.ansible.com/smbambling/apache/)
[![Build Status](https://travis-ci.org/smbambling/ansible-role-apache.svg?branch=master)](https://travis-ci.org/smbambling/ansible-role-apache)
[![CodeClimate](https://codeclimate.com/github/smbambling/ansible-role-apache/badges/gpa.svg)](https://codeclimate.com/github/smbambling/ansible-role-apache)
[![IssueCount](https://codeclimate.com/github/smbambling/ansible-role-apache/badges/issue_count.svg)](https://codeclimate.com/github/smbambling/ansible-role-apache)

Table of Contents
-----------------
1. [Overview](#overview)
1. [Requirements](#requirements)
1. [Variable Overrides](#variable-overrides)
1. [Role Variables](#role-variables)
1. [Dependencies](#dependencies)
1. [Examples](#example-playbooks)
1. [Development / Contributing](#development--contributing)
1. [License](#license)
1. [Author Information](#author-information)

Overview
--------
This role installs and manages the Apache HTTPD Web Server

Requirements
------------
This role requires Ansible 2.1 or higher and platform requirements are listed in the [metadata](meta/main.yml) file.

If you are using SSL/TLS you should provided your own certificate and key files.  By default it will use the localhost certificate and key created by the system.

Variable Overrides
------------------

Varibles listed as a key with no values in `defaults/main.yml` can be overriden via group or extra variables yet still set a default value via OS-specific variable includes ( see `vars/*.yml` ).

This is accomplished via the `set_overrides.yml` task file which determines if a value is passed to the role or if the value is `None` and then initializes the variable with a default value from the OS-specific variable includes

Role Variables
--------------
The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

> See [Variable Overrides](#variable-overrides) for information on variables not listed with a default value and the ability to override them via pass-ins.

```yaml
apache_packages:
```
The set of packages to be installed. 

```yaml
apache_service:
```
The service name for the apache daemon to run on the system.

```yaml
apache_state:
```
The Apache daemon state to be enforced. This should generally remain the default value.

```yaml
apache_enabled:
```
Weather the apache service should start on boot. This should generally remain the default value.

### VirtualHosts

All default Apache VirtualHost entries are removed during the running of this play and at least one entry must be passed



Dependencies
------------
None

Example Playbook(s)
-------------------

Development / Contributing
--------------------------
See [Contributing](.github/CONTRIBUTING.md).

Note: This role is currently only tested against the following OS and Ansible versions:

#### Operating Systems / version
- CentOS 6.x
- CentOS 7.x

#### Ansible Versions
- 2.1.0
- 2.2.2
- latest

License
-------
Licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Author Information
------------------
- Steven Bambling
