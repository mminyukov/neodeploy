import os
import zipfile

def extract_all_with_permission(zf, target_dir):
  print("INFO: Unpack %s in %s" % (zf,target_dir))
  with zipfile.ZipFile(zf, 'r') as zf:
    for info in zf.infolist():
      extracted_path = zf.extract(info, target_dir)
      unix_attributes = info.external_attr >> 16
      if unix_attributes:
        os.chmod(extracted_path, unix_attributes)