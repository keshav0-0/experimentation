import os, subprocess, sys
import importlib, imp
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import inputs

def osysNp(cmd, suppress_stderr=False):
    if suppress_stderr:
        stderr_pipe = subprocess.PIPE
    else:
        stderr_pipe = None
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=stderr_pipe, shell=True)
    os.waitpid(process.pid, 0)
    output = process.stdout.read().strip().decode('utf-8')
    error = ''
    if process.stderr is not None:
        error = process.stderr.read().strip().decode('utf-8')
    return output,error


osysNp("git checkout master")

importlib.reload(inputs)

inputs.testAdd(1,2)


osysNp("git checkout test")

importlib.reload(inputs)

inputs.testAdd(1,2)
