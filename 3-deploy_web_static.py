def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Unpack and move the files to the appropriate directories
    try:
        put(archive_path, f"/tmp/{file}")
        run(f"rm -rf /data/web_static/releases/{name}/")
        run(f"mkdir -p /data/web_static/releases/{name}/")
        run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/")
        run(f"rm /tmp/{file}")
        run(f"mv /data/web_static/releases/{name}/web_static/* "
            f"/data/web_static/releases/{name}/")
        run(f"rm -rf /data/web_static/releases/{name}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current")
    except Exception as e:
        print(f"Error occurred during deployment: {e}")
        return False

    return True
