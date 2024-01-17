def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        print(f"Archive file {archive_path} not found.")
        return False

    archive_name = os.path.basename(archive_path)
    release_name = archive_name.split(".")[0]

    try:
        put(archive_path, f"/tmp/{archive_name}")
        run(f"rm -rf /data/web_static/releases/{release_name}/")
        run(f"mkdir -p /data/web_static/releases/{release_name}/")
        run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{release_name}/")
        run(f"rm /tmp/{archive_name}")
        run(f"mv /data/web_static/releases/{release_name}/web_static/* "
            f"/data/web_static/releases/{release_name}/")
        run(f"rm -rf /data/web_static/releases/{release_name}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{release_name}/ /data/web_static/current")
    except Exception as e:
        print(f"Error occurred during deployment: {e}")
        return False

    return True
