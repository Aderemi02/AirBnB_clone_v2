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
        put(archive_path, '/tmp/')
        arcFile = archive_path.split("/")[-1]
        arcFile_no_ext = arcFile.split(".")[0]
        loc = "/data/web_static/releases/"
        run('mkdir -p {}{}/'.format(loc, arcFile_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arcFile, loc, arcFile_no_ext))
        run('rm /tmp/{}'.format(arcFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(arcFile, arcFile_no_ext))
        run('rm -rf {}{}/web_static'.format(arcFile, arcFile_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(loc, arcFile_n_ext))
        return True
    except Exception:
        return False
