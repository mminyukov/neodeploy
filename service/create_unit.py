def unit(project_name,stand_name,target_directory_site,target_service_name,site_user_name,site_run_directory,port_site,site_service_file):
  # template unit file
  unit = [
  '[Unit]',
  'Description={}.{}'.format(project_name,stand_name),
  '[Service]',
  'WorkingDirectory={}'.format(target_directory_site),
  'ExecStart={}'.format(target_service_name),
  'Restart=always',
  'RestartSec=30',
  'SyslogIdentifier={}.{}'.format(project_name,stand_name),
  'User={}'.format(site_user_name),
  'Environment=ASPNETCORE_ENVIRONMENT=Production',
  'Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false',
  'Environment=HOME={}'.format(site_run_directory),
  'Environment=ASPNETCORE_URLS=http://*:{}/'.format(port_site),
  '[Install]',
  'WantedBy=multi-user.target']

  print("INFO: Try to create unit file {}".format(site_service_file))
  f = open(site_service_file, 'w')
  for u in unit:
    f.write(u + '\n')
  f.close()
  print("INFO: File is created")

def unit_cce(project_name,stand_name,target_directory_site,target_service_name,site_service_file):
  # template unit file
  unit = [
  '[Unit]',
  'Description={}.{}'.format(project_name,stand_name),
  '[Service]',
  'WorkingDirectory={}'.format(target_directory_site),
  'ExecStart=/usr/bin/dotnet {}'.format(target_service_name),
  'Restart=always',
  'RestartSec=30',
  'SyslogIdentifier={}.{}'.format(project_name,stand_name),
  'User=root',
  'Environment=ASPNETCORE_ENVIRONMENT=Production',
  'CPUQuota=80%',
  '[Install]',
  'WantedBy=multi-user.target']

  print("INFO: Try to create unit file {}".format(site_service_file))
  f = open(site_service_file, 'w')
  for u in unit:
    f.write(u + '\n')
  f.close()
  print("INFO: File is created")