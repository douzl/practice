import os
import yaml

def read_file(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('%s not exists' % (filename))
    with open(filename,encoding='utf-8') as f:
        content = yaml.safe_load(f)
    f.close
    return content

conf = read_file('pool.yaml')

print(conf['name'])