import os,shutil
import subprocess

def service(operation,service):
  if os.path.isfile('/etc/systemd/system/' + service):
    try:
      print('WARN: %s service %s' % (operation,service))
      subprocess.run(['systemctl',operation,service])
    except Exception as e:
      print('ERROR: %s' % str(e))

def setpermissions(path,user,group):
  print("INFO: Update permissions. Set %s to %s" % (user,path))
  for root, dirs, files in os.walk(path):
    shutil.chown(root, user, group)
    for item in dirs:
      shutil.chown(os.path.join(root, item), user, group)
    for item in files:
      shutil.chown(os.path.join(root, item), user, group)