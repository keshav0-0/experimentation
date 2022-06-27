import os, subprocess, sys
import importlib
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import inputs
# import add
add = importlib.import_module('add')

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
importlib.reload(add)
print(add.add(2,4))
inputs.testAdd(add.add,1,2)


osysNp("git checkout test")

importlib.reload(inputs)
importlib.reload(add)
print(add.add(2,4))
inputs.testAdd(add.add,1,2)
