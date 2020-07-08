import os
import argparse
from projects import gisrao,cce,oak,oak_egisu,sguk


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Argument for neodeploy')
  parser.add_argument('-p','--project', help="Project name for deploy",required=True)
  args = parser.parse_args()

  if args.project == 'gis-rao':
    gisrao.install(args.project)
  elif args.project == 'oak':
    oak.install(args.project)
  elif args.project == 'cce':
    cce.install(args.project)
  elif args.project == 'oak-egisu':
    oak_egisu.install(args.project)
  elif args.project == 'sguk':
    sguk.install(args.project)
  else:
    print("ERROR: Project not found")
