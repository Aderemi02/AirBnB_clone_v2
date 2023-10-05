#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from os.path import exists
from fabric.api import put, env, run
env.hosts = ['100.26.154.225', '54.209.218.5']


def do_deploy(archive_path):
    """this distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        arcFile = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")
        loc = "/data/web_static/releases/"
        run('mkdir -p {}{}/'.format(loc, arcFile))
        run('tar -xzf /tmp/{}.tgz -C {}{}/'.format(arcFile, loc, arcFile))
        run('rm -rf /tmp/{}.tgz'.format(arcFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(loc, arcFile))
        run('rm -rf {}{}/web_static'.format(loc, arcFile))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(loc, arcFile))
        return True
    except Exception:
        return False
