import os,sys,shutil
from service import appsettingsedit as app
from service import getsettings as g
from service import manage as m
from service import unzip_file

def gisrao(project_name):
  print("INFO: Get settings from main section")
  config_main = g.get_all_settings('main')
  print("INFO: Get all settings for project %s" % project_name)
  config_dict = g.get_all_settings(project_name)

  target_directory = os.path.join(config_main.get('prefix_directory'),project_name)
  target_directory_site = os.path.join(target_directory,'site')
  target_service_name = os.path.join(target_directory_site,config_dict.get('target_service_name'))
  site_service_name = '%s.%s.service' % (project_name,config_dict.get('stand_name'))
  site_service_file = os.path.join('/etc/systemd/system/',site_service_name)
  site_user_name = 'www-data'
  site_run_directory = os.path.join('/var/lib',project_name,config_dict.get('stand_name'))
  zip_file = config_dict.get('site_zip_name')

  if os.path.isfile(zip_file) == False:
    print("ERROR: file %s not found" % zip_file)
    sys.exit(1)

  if os.path.isfile(site_service_file):
    print("INFO: Stop service %s" % site_service_name)
    m.service('stop',site_service_name)
    m.service('disable',site_service_name)

  if os.path.exists(target_directory_site):
    print("INFO: Remove target folder: %s" % target_directory_site)
    shutil.rmtree(target_directory_site)

  unzip_file.extract_all_with_permission(zip_file,target_directory_site)
  app.appsettings(project_name,target_directory_site,config_dict.get('connection_string'),config_dict.get('tileset1'),config_dict.get('tileset2'),config_dict.get('tileset3'),config_dict.get('tileset4'))
  m.setpermissions(target_directory_site,'www-data','www-data')

