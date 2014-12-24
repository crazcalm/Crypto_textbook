import subprocess


print('Python3 tests')
subprocess.call('python3 -m unittest discover tests/', shell=True)
print('\n\nPython2.7 tests')
subprocess.call('python -m unittest discover tests/', shell=True)
