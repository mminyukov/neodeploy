import os
import sys
import configparser

def get_config(path):
  if not os.path.exists(path):
    print("ERROR: file %s not found" % path)
    sys.exit(1)

  config = configparser.ConfigParser()
  config.read(path)
  return config

def get_setting(section, setting):
  setting_file = 'settings.ini'
  config = get_config(setting_file)
  value = config.get(section, setting)
  return value

def get_all_settings(section):
  config_dict = {}
  setting_file = 'settings.ini'
  config = get_config(setting_file)
  for name, value in config.items(section):
    config_dict[name] = value
  return config_dict