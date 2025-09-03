import pytest


def test_redis_package(host):
    pkg = host.package("redis-server")
    assert pkg.is_installed


def test_redis_user_group(host):
    user = host.user("redis")
    group = host.group("redis")
    assert user.exists
    assert group.exists
    assert user.group == "redis"


def test_redis_service(host):
    svc = host.service("redis-server")
    assert svc.is_enabled
    assert svc.is_running


def test_redis_listening(host):
    sock = host.socket("tcp://127.0.0.1:6379")
    assert sock.is_listening


def test_redis_ping(host):
    cmd = host.run("redis-cli ping")
    assert cmd.rc == 0
    assert "PONG" in cmd.stdout


@pytest.mark.parametrize(
    "path,mode,user,group",
    [
        ("/var/lib/redis", 0o750, "redis", "redis"),
        ("/var/log/redis", 0o2750, "redis", "adm"),
        ("/run/redis", 0o2755, "redis", "redis"),
    ],
)
def test_directories(host, path, mode, user, group):
    d = host.file(path)
    assert d.exists
    assert d.is_directory
    assert d.user == user
    assert d.group == group
    assert d.mode == mode


def test_redis_conf(host):
    f = host.file("/etc/redis/redis.conf")
    assert f.exists
    assert f.user == "redis"
    assert f.group == "redis"
    assert f.mode == 0o640
    assert f.contains(r"^bind 127\.0\.0\.1 ::1$")
    assert f.contains(r"^supervised systemd$")
    assert f.contains(r"^daemonize no$")


def test_override_conf(host):
    f = host.file("/etc/systemd/system/redis-server.service.d/override.conf")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    assert f.contains(r"^ProtectSystem=full$")
