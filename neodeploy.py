import configparser
import os
import sys
import zipfile
import subprocess
import shutil

def get_config(path):
  if not os.path.exists(path):
    print("ERROR: file %s not found" % path)
    sys.exit(1)

  config = configparser.ConfigParser()
  config.read(path)
  return config

def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    return value

def manage_service(operation,service):
  if os.path.isfile('/etc/systemd/system/' + service):
    try:
      print('WARN: %s service %s' % (operation,service))
      subprocess.run(['systemctl',operation,service])
    except Exception as e:
      print('ERROR: %s' % str(e))

def extract_all_with_permission(zf, target_dir):
  for info in zf.infolist():
    extracted_path = zf.extract(info, target_dir)
    unix_attributes = info.external_attr >> 16
    if unix_attributes:
      os.chmod(extracted_path, unix_attributes)

if __name__ == "__main__":
  try:
    print("INFO: Get variables from settings.ini")
    setting_file = 'settings.ini'
    project_name = 'gis-rao'
    stand_name = get_setting(setting_file,project_name,'stand_name')
    prefix_directory = get_setting(setting_file,'main','prefix_directory')
    target_directory = os.path.join(prefix_directory,project_name)
    target_directory_site = os.path.join(target_directory,'site')
    target_service_name = os.path.join(target_directory_site,get_setting(setting_file,project_name,'target_service_name'))
    site_service_name = '%s.%s.service' % (project_name,stand_name)
    site_service_file = os.path.join('/etc/systemd/system/',site_service_name)
    site_user_name = 'www-data'
    site_file_owner = 'www-data:www-data'
    site_run_directory = os.path.join('/var/lib',project_name,stand_name)
    zip_file = get_setting(setting_file,project_name,'site_zip_name')
  except Exception as e:
    print('ERROR: %s' % str(e))

  if os.path.isfile(zip_file) == False:
    print("ERROR: file %s not found" % zip_file)
    sys.exit(1)

  if os.path.isfile(site_service_file):
    print("INFO: Stop service %s" % site_service_name)
    manage_service('stop',site_service_name)
    manage_service('disable',site_service_name)

  if os.path.exists(target_directory_site):
    print("INFO: Remove target folder: %s" % target_directory_site)
    shutil.rmtree(target_directory_site)

  print("INFO: Unpack %s in %s" % (zip_file,target_directory_site))
  with zipfile.ZipFile(zip_file, 'r') as zf:
    extract_all_with_permission(zf,target_directory_site)
