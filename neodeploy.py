import os
import argparse
from projects import gisrao,cce,oak


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Argument for neodeploy')
  parser.add_argument('-p','--project', help="Project name for deploy",required=True)
  args = parser.parse_args()

  if args.project == 'gis-rao':
    gisrao.install('gis-rao')
  elif args.project == 'oak':
    oak.install('oak')
  elif args.project == 'cce':
    cce.install('cce')
  else:
    print("ERROR: Project not found")
