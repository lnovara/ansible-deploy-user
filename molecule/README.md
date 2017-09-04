Testing with molecule
=====================

This role uses [molecule](https://molecule.readthedocs.io/en/latest/) to
implement automatic testing of its functionalities.

Requirements
------------

* Ansible >= 2.2
* molecule v2
* docker

Execute the tests
-----------------

```bash
ansible-galaxy install lnovara.deploy-user -p .

cd lnovara.deploy-user

# test all the scenarios
molecule test --all
```
