def getRootDir():
    from pathlib import Path
    import os
    path = Path(os.getcwd())

    last_path = None

    while path != last_path:
        if path.name == "src":
            return str(path.parent.absolute())
        
        last_path = path
        path = path.parent.absolute()

    raise Exception("Root of repository not found!")