#!/usr/bin/env python3
import argparse
import json
import os
'''
parser = argparse.ArgumentParser(description='appsettings.json editing script')
parser.add_argument('-p','--filePath', help="Path to appsettings.json file without / at the end",required=True)
parser.add_argument('-cstrdb','--connStringDb', help="Database connection string",required=False)
parser.add_argument('-cstrusr','--connStringUser', help="Database connection string",required=False)
parser.add_argument('-cstrsch','--connStringScheduler', help="Scheduler connection string",required=False)
parser.add_argument('-cstrschhgf','--connStringSchedulerHangfire', help="Scheduler Hangfire connection string",required=False)
parser.add_argument('-ssurl','--SSURL', help="url of SS",required=False)
parser.add_argument('-cstrcci','--connStringCCI', help="CCI connection string",required=False)
args = parser.parse_args()
'''

def read_json(path,file_name):
  with open(os.path.join(path,file_name), "r") as f:
    jsonMod = json.load(f)
    return jsonMod

def write_json(path,jsonMod,file_name):
  with open(os.path.join(path,file_name), "w") as f:
    json.dump(jsonMod, f, indent=2, sort_keys=False)


def appsettings(path,**connstrings):
  jsonMod = read_json(path,'appsettings.json')
  if 'UserConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['UserConnectionString'] = connstrings.get('stringuser')

  write_json(path,jsonMod,'appsettings.json')

'''
if 'ConnectionString' in jsonMod['Data']['PostgreSql']:
  jsonMod['Data']['PostgreSql']['ConnectionString'] = args.connStringApp
for tileset in jsonMod['tilesets']:
  if tileset['name'] == 'saintspbWiki15':
    tileset['source'] = args.tileSetSaintspbWiki15
  if tileset['name'] == 'saintspb':
    tileset['source'] = args.tileSetSaintspb
  if tileset['name'] == 'saintpgoolge':
    tileset['source'] = args.tileSetSaintpgoolge
  if tileset['name'] == 'route':
    tileset['source'] = args.tileSetRoute


  if 'ConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['ConnectionString'] = stringdb
  if 'DefaultConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['DefaultConnectionString'] = stringdb
  if 'HangfireConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['HangfireConnectionString'] = stringschedulerhangfire
  if 'SchedulerUrlConstants' in jsonMod['Data']:
    if 'BaseAddress' in jsonMod['Data']['SchedulerUrlConstants']:
      jsonMod['Data']['SchedulerUrlConstants']['BaseAddress'] = stringscheduler
  if 'cci' in jsonMod:
    if 'connection_string' in jsonMod['cci']:
      jsonMod['cci']['connection_string'] = stringcci
'''
'''
  if ssurl != None:
    jsonOriginal = ""
    jsonMod = ""
    with open(str(path) + "/settings.json", "r") as f:
      lines = f.readlines()
      for line in lines:
        if line.strip().strip("\n")[0:2] != "//":
          jsonOriginal = jsonOriginal + line
    jsonMod = json.loads(jsonOriginal)
    if 'BaseUrl' in jsonMod['SS']:
        jsonMod['SS']['BaseUrl'] = ssurl

    with open(str(path) + "/settings.json", "w") as f:
        json.dump(jsonMod, f, indent=2, sort_keys=False)
'''