import os,shutil
from service import appsettingsedit as app
from service import getsettings as g
from service import manage as m
from service import create_unit as c

def install(project_name):
  #--------------------------------------------------------------------------------------------------
  print("INFO: Get settings from main section")
  config_main = g.get_all_settings('main')
  print("INFO: Get all settings for project {}".format(project_name))
  config_dict = g.get_all_settings(project_name)

  stand_name = config_dict.get('stand_name')
  target_directory = os.path.join(config_main.get('prefix_directory'),project_name,stand_name)
  target_directory_site = os.path.join(target_directory,'Site')
  target_service_name = os.path.join(target_directory_site,config_dict.get('target_service_name'))
  site_user_name = 'www-data'
  site_service_name = '{}.{}.service'.format(project_name,config_dict.get('stand_name'))
  site_service_file = os.path.join('/etc/systemd/system/',site_service_name)
  site_run_directory = os.path.join('/var/lib',project_name,stand_name)
  zip_file = config_dict.get('main_zip_name')
  #--------------------------------------------------------------------------------------------------

  m.check_file(zip_file)
  if os.path.isfile(site_service_file):
    m.service('stop',site_service_name)
    m.service('disable',site_service_name)

  if os.path.exists(target_directory):
    print("INFO: Remove target folder: {}".format(target_directory))
    shutil.rmtree(target_directory)

  m.extract_all_with_permission(zip_file,target_directory_site)
  app.gisrao(target_directory_site,config_dict.get('connection_string'),config_dict.get('tileset1'),config_dict.get('tileset2'),config_dict.get('tileset3'),config_dict.get('tileset4'))
  m.setpermissions(target_directory_site,'www-data','www-data')

  c.unit(project_name,stand_name,target_directory_site,target_service_name,site_user_name,site_run_directory,config_dict.get('port_site'),site_service_file)
  if not os.path.exists(site_run_directory):
    os.makedirs(site_run_directory)
  m.setpermissions(site_run_directory,'www-data','www-data')
  os.chmod(target_service_name, 0o0777)
  m.service('enable',site_service_name)
  m.service('start',site_service_name)