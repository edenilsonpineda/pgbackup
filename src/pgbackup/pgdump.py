import subprocess
import sys


def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def dump_file(url: str, timestamp=None):
    db_name = url.split('/')[-1]  # postgres://demo:pass@ip:port/dbname (Removes any slashes and return the last item
    db_name = db_name.split('?')[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"
