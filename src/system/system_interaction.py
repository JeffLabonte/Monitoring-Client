import subprocess

def __interact_with_bash(args):
    if not isinstance(args, list):
        raise AttributeError("args is supposed to be a list")
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if len(stderr) > 0:
        raise SystemError("Error with comms")
    return str(stdout, 'utf-8')
