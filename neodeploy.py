import os
import argparse
from projects import gisrao


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Argument for neodeploy')
  parser.add_argument('-p','--project', help="Project name for deploy",required=True)
  args = parser.parse_args()

  gisrao.gisrao(args.project)
