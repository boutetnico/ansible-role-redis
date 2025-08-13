[![tests](https://github.com/boutetnico/ansible-role-redis/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-redis/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.redis-blue.svg)](https://galaxy.ansible.com/boutetnico/redis)

ansible-role-redis
==================

This role installs and configures redis.

Requirements
------------

Ansible 2.15 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                           | Choices   | Comments                    |
|------------------------------|----------|-----------------------------------|-----------|-----------------------------|
| redis_packages               | true     |                                   | list      | See `defaults/main.yml`.    |
| redis_packages_state         | true     | `present`                         | string    | Use `latest` to update.     |
| redis_user                   | true     | `redis`                           | string    |                             |
| redis_group                  | true     | `redis`                           | string    |                             |
| redis_bind                   | true     | `127.0.0.1 -::1`                  | string    |                             |
| redis_protected_mode         | true     | `yes`                             | string    |                             |
| redis_port                   | true     | `6379`                            | int       |                             |
| redis_daemonize              | true     | `yes`                             | string    |                             |
| redis_supervised             | true     | `systemd`                         | string    |                             |
| redis_pidfile                | true     | `/run/redis/redis-server.pid`     | string    |                             |
| redis_loglevel               | true     | `notice`                          | string    |                             |
| redis_logfile                | true     | `/var/log/redis/redis-server.log` | string    |                             |
| redis_databases              | true     | `16`                              | int       |                             |
| redis_dir                    | true     | `/var/lib/redis`                  | string    |                             |
| redis_systemd_overrides      | true     |                                   | list      | See `defaults/main.yml`.    |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-redis

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
