Ansible Role: deploy-user
=========================

Setup a user account with public key login and passwordless sudo.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see
defaults/main.yml).

    user_name: deploy

User's name.

    user_shell: /bin/bash

User's shell.

    user_groups: []

Additional groups beyond the default. **NB**: this role automatically creates
those groups if they do not exist in the system.

    public_keys:
      - ~/.ssh/id_rsa.pub

List of public keys to add to the user's `.ssh/authorized_keys` file.

    enable_passwordless_sudo: True

Enable passwordless sudo for the newly created the user.

Dependencies
------------

None.

Example Playbook
----------------

    - name: Create deploy user on all hosts.
      hosts: all
      roles:
         - { role: lnovara.deploy-user,
             user_groups: [foo, bar] }

License
-------

MIT

Author Information
------------------

Luca Novara
