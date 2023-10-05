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
        arcFilename = archive_path.split("/")[-1]
        arcFilename_no_ext = arcFilename.split(".")[0]
        loc = "/data/web_static/releases/"
        run('mkdir -p {}{}/'.format(loc, arcFilename_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arcFilename, loc, arcFilename_no_ext))
        run('rm /tmp/{}'.format(arcFilename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(arcFilename, arcFilename_no_ext))
        run('rm -rf {}{}/web_static'.format(arcFilename, arcFilename_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(loc, arcFilename_n_ext))
        return True
    except:
        return False
