#!/usr/bin/env python3

from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tarball of the web_static directory."""
    now = datetime.utcnow()
    tarball_name = f"web_static_{now.year}{now.month:02}{now.day:02}{now.hour:02}{now.minute:02}{now.second:02}.tgz"
    tarball_path = f"versions/{tarball_name}"

    if not local("test -d versions").failed:
        local("mkdir -p versions")

    if local(f"tar -czvf {tarball_path} web_static").failed:
        return None

    return tarball_path
