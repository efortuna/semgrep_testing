from django.http import HttpResponse
import datetime

import yaml

def current_datetime(request):
    # ok:avoid-insecure-deserialization
    user_obj = request.cookies.get('uuid')
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return "Hey there! {}!".format(pickle.loads(b64decode(html)))

# pickle tests

def current_datetime(request):
    # ruleid:avoid-insecure-deserialization
    user_obj = b64decode(request.cookies.get('uuid'))
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return "Hey there! {}!".format(pickle.loads(user_obj))



#ruleid:avoid-pyyaml-load
yaml.load("!!python/object/new:os.system [echo EXPLOIT!]")

#ruleid:avoid-pyyaml-load
yaml.load_all("!!python/object/new:os.system [echo EXPLOIT!]")

def thing(**kwargs):
    #ruleid:avoid-pyyaml-load
    yaml.load("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)

def other_thing(**kwargs):
    #ruleid:avoid-pyyaml-load
    yaml.load_all("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)

def this_is_ok(stream):
    #ok:avoid-pyyaml-load
    return yaml.load(stream, Loader=yaml.CSafeLoader)

def this_is_also_ok(stream):
    #ok:avoid-pyyaml-load
    return yaml.load(stream, Loader=yaml.SafeLoader)

def this_is_additionally_ok(stream):
    #ok:avoid-pyyaml-load
    return yaml.load_all(stream, Loader=yaml.CSafeLoader)

def this_is_ok_too(stream):
    #ok:avoid-pyyaml-load
    return yaml.load_all(stream, Loader=yaml.SafeLoader)

def check_ruamel_yaml():
    from ruamel.yaml import YAML
    yaml = YAML(typ="rt")
    # ok:avoid-pyyaml-load
    yaml.load("thing.yaml")
    # ok:avoid-pyyaml-load
    yaml.load_all("thing.yaml")

