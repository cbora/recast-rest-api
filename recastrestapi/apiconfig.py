import os
import pkg_resources
import yaml

def default_config():
    return yaml.load(open(pkg_resources.resource_filename('recastrestapi', 'resources/defaultconfig.yaml')))

def mk_config():
    the_config = default_config()
    if os.environ.has_key('RECASTCONTROLCENTER_CONFIG'):
        custom_config = yaml.load(open(os.environ['RECASTCONTROLCENTER_CONFIG']))
        the_config_update(**custom_config)
    return the_config

config = mk_config()
