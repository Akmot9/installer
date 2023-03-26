import subprocess

print("Installation ...")

# Check for Firefox
try:
    output = subprocess.check_output(['firefox', '--version'], stderr=subprocess.STDOUT)
    print('Firefox is installed on your computer.')
except (subprocess.CalledProcessError, FileNotFoundError):
    print('Firefox is not installed on your computer.')

# Check for 7-Zip
try:
    output = subprocess.check_output(['7z', '--version'], stderr=subprocess.STDOUT)
    print('7-Zip is installed on your computer.')
except (subprocess.CalledProcessError, FileNotFoundError):
    print('7-Zip is not installed on your computer.')

# Check for ElasticSearch
try:
    output = subprocess.check_output(['elasticsearch', '--version'], stderr=subprocess.STDOUT)
    print('ElasticSearch is installed on your computer.')
except (subprocess.CalledProcessError, FileNotFoundError):
    print('ElasticSearch is not installed on your computer.')

# Check for Kibana
try:
    output = subprocess.check_output(['kibana', '--version'], stderr=subprocess.STDOUT)
    print('Kibana is installed on your computer.')
except (subprocess.CalledProcessError, FileNotFoundError):
    print('Kibana is not installed on your computer.')
