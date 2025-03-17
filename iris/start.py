import subprocess


def start() -> None:
    cmd = ['poetry', 'run', 'streamlit', 'run', 'iris/app.py']
    subprocess.run(cmd)