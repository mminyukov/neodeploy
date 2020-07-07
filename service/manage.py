import os,shutil,sys
import subprocess
import zipfile

def service(operation,service):
  if os.path.isfile('/etc/systemd/system/' + service):
    try:
      print('WARN: %s service %s' % (operation,service))
      subprocess.run(['systemctl',operation,service])
    except Exception as e:
      print('ERROR: %s' % str(e))

def exec(workdir,command):
  try:
    print('WARN: Try to run command: {}'.format(command))
    os.chdir(workdir)
    subprocess.call(command, shell=True)
  except Exception as e:
    print('ERROR: %s' % str(e))

def check_file(c_file):
  if os.path.isfile(c_file) == False:
    print("ERROR: file {} not found".format(c_file))
    sys.exit(1)

def setpermissions(path,user,group):
  print("INFO: Update permissions. Set %s to %s" % (user,path))
  for root, dirs, files in os.walk(path):
    shutil.chown(root, user, group)
    for item in dirs:
      shutil.chown(os.path.join(root, item), user, group)
    for item in files:
      shutil.chown(os.path.join(root, item), user, group)

def extract_all_with_permission(zf, target_dir):
  print("INFO: Unpack %s in %s" % (zf,target_dir))
  with zipfile.ZipFile(zf, 'r') as zf:
    for info in zf.infolist():
      extracted_path = zf.extract(info, target_dir)
      unix_attributes = info.external_attr >> 16
      if unix_attributes:
        os.chmod(extracted_path, unix_attributes)