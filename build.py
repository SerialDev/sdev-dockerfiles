import os, subprocess, pickle
from hashlib import sha512

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# Python script to run a command line

def execute(cmd, working_directory=os.getcwd()):
    """
        Purpose  : To execute a command and return exit status
        Argument : cmd - command to execute
        Return   : exit_code
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd = working_directory)
    (result, error) = process.communicate()

    rc = process.wait()

    if rc != 0:
        print ("Error: failed to execute command:", cmd)
        print (error)
    return result


def save_file(data, path, flag='wb'):
    with open(path, flag) as f:
        f.write(data)
    return True

def load_file(path, flag='rb'):
    with open(path, flag) as f:
        temp = f.read()
    return temp

def load_or_create(path, flag='rb'):
    try:
        result = pickle.load(open(path, "rb"))
    except (OSError, IOError) as e:
        result = {}

    return result

def to_pickle(data, path, flag='wb'):
    with open(path, flag) as f:
        pickle.dump(data, f)
        
DOCKERHUB = "serialdev/"

for name, dirs, files in walklevel(os.getcwd(), 1):
    if files == []:
	    continue
    if files[0] == 'Dockerfile':
        dockerfile_name = name.split(os.sep)[-1]
        dockerfile_hash_dict = load_or_create("dockerfile-hash/dockerfile_hash.plk")
        dockerfile = load_file(os.path.join(name, 'Dockerfile'))
        dockerfile_hash = sha512(dockerfile).hexdigest()
        try:
            if dockerfile_hash == dockerfile_hash_dict[dockerfile_name]:
                continue
        except:
            pass
        dockerfile_hash_dict[dockerfile_name] = dockerfile_hash
        to_pickle(dockerfile_hash_dict, "dockerfile-hash/dockerfile_hash.plk")

        build = execute('docker build ./ -t {}'.format(dockerfile_name), name)
        tag = execute('docker tag {} {}'.format(dockerfile_name,
                                                DOCKERHUB + dockerfile_name), name)
        deploy = execute('docker push {}'.format(DOCKERHUB + dockerfile_name), name)

        print(build)
        print(tag)
        print(deploy)
