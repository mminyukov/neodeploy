#!/usr/bin/env python3
import json
import os

def read_json(path,file_name):
  print("INFO: Read file {}".format(file_name))
  with open(os.path.join(path,file_name), "r") as f:
    jsonMod = json.load(f)
    return jsonMod

def write_json(path,jsonMod,file_name):
  print("INFO: Write changes in file {}".format(file_name))
  with open(os.path.join(path,file_name), "w") as f:
    json.dump(jsonMod, f, indent=2, sort_keys=False)

def gisrao(path,*connstrings):
  jsonMod = read_json(path,'appsettings.json')
  if 'ConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['ConnectionString'] = connstrings[0]
  for tileset in jsonMod['tilesets']:
    if tileset['name'] == 'saintspbWiki15':
      tileset['source'] = connstrings[1]
    if tileset['name'] == 'saintspb':
      tileset['source'] = connstrings[2]
    if tileset['name'] == 'saintpgoolge':
      tileset['source'] = connstrings[3]
    if tileset['name'] == 'route':
      tileset['source'] = connstrings[4]
  write_json(path,jsonMod,'appsettings.json')

def cce(path,*connstrings):
  jsonMod = read_json(path,'settings.json')
  if 'cci' in jsonMod:
    if 'connection_string' in jsonMod['cci']:
      jsonMod['cci']['connection_string'] = connstrings[0]
  if 'ConnectionStrings' in jsonMod:
    if 'cci_database' in jsonMod['ConnectionStrings']:
      jsonMod['ConnectionStrings']['cci_database'] = connstrings[0]
  if 'ConnectionStrings' in jsonMod:
    if 'cci_hangfire' in jsonMod['ConnectionStrings']:
      jsonMod['ConnectionStrings']['cci_hangfire'] = connstrings[0]
  write_json(path,jsonMod,'settings.json')

def oak(path,*connstrings):
  jsonMod = read_json(path,'appsettings.json')
  if 'ConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['ConnectionString'] = connstrings[0]
  if 'UserConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['UserConnectionString'] = connstrings[1]
  if 'HangfireConnectionString' in jsonMod['Data']['PostgreSql']:
    jsonMod['Data']['PostgreSql']['HangfireConnectionString'] = connstrings[2]
  if 'SchedulerUrlConstants' in jsonMod['Data']:
    if 'BaseAddress' in jsonMod['Data']['SchedulerUrlConstants']:
      jsonMod['Data']['SchedulerUrlConstants']['BaseAddress'] = connstrings[3]
  if 'cci' in jsonMod:
    if 'connection_string' in jsonMod['cci']:
      jsonMod['cci']['connection_string'] = connstrings[4]
  write_json(path,jsonMod,'appsettings.json')

  if connstrings[5] != None:
    jsonMod = read_json(path,'settings.json')
    if 'BaseUrl' in jsonMod['SS']:
        jsonMod['SS']['BaseUrl'] = connstrings[5]
    write_json(path,jsonMod,'settings.json')
