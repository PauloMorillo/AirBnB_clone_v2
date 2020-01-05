#!/usr/bin/python3
""" full deployment """

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["35.237.238.105", "34.74.131.167"]
env.user = "ubuntu"


def do_pack():
    """ pack webstatic and save the file inside versions dir """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date + ".tgz"

    try:
        if path.exists("versions") is False:
            local("mkdir versions")
        local("tar -zcvf {} web_static".format(name))
        return name
    except:
        return None


def do_deploy(archive_path):
    """ Deploy the file in specific folders in the servers """
    if path.isfile(archive_path) is False:
        return False
    # With .tgz
    filetgz = archive_path.split("/")[-1]
    # No .tgz
    filename = filetgz.replace('.tgz', '')

    newdir = "/data/web_static/releases/" + filename

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir {}/".format(newdir))
        run("sudo tar -xzf /tmp/{} -C {}/".format(filetgz, newdir))
        run("sudo rm /tmp/{}".format(filetgz))
        run("sudo mv {}/web_static/* {}/".format(newdir, newdir))
        run("sudo rm -rf {}/web_static".format(newdir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newdir))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ Full deploy the servers """
    try:
        path = do_pack()
    except:
        return False

    return do_deploy(path)
