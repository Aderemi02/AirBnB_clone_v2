#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""

from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """script that creates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        new_file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(new_file))
        return new_file
    except:
        return None
