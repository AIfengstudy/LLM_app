import time
import subprocess

def run_command_with_timeout(command, timeout):
    process = subprocess.Popen(command)
    time.sleep(timeout)
    process.terminate()