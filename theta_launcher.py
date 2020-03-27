#!/usr/bin/python3

import sys
import os
import os.path as path


SNAPSHOT_DOWNLOAD_URL = 'https://mainnet-data.thetatoken.org/snapshot'
DEFAULT_CONFIG_FOLDER = '../mainnet/guardian'


def needsToDownloadSnapshot(config_folder):
  snapshot_exists = path.exists('{}/snapshot'.format(config_folder))
  needs_to_download_snapshot = not snapshot_exists
  return needs_to_download_snapshot

def downloadSnapshot(config_folder, snapshot_download_url):
  print("")
  print("====================== Downloading the latest snapshot... ======================")
  print("")
  cmd = 'curl -k --output {}/snapshot `curl -k {}`'.format(config_folder, snapshot_download_url)
  os.system(cmd)
  if needsToDownloadSnapshot(config_folder):
    return False
  else:
    return True

def launchTheta(config_folder, password):
  print("")
  print("============================== Launching Theta... ==============================")
  print("")
  if password == None:
    cmd = 'theta start --config={}'.format(config_folder)
  else:
    cmd = 'theta start --config={} --password={}'.format(config_folder, password)
  os.system(cmd)

if __name__ == '__main__':
  snapshot_download_url = SNAPSHOT_DOWNLOAD_URL
  password = None

  if len(sys.argv) > 3 or len(sys.argv) < 2:
    print('Usage: ./theta_launcher.py [path/to/config/folder] [password]')
  elif len(sys.argv) == 3:
    config_folder = sys.argv[1]
    password = sys.argv[2]
  elif len(sys.argv) == 2:
    config_folder = sys.argv[1]

  if needsToDownloadSnapshot(config_folder):
    success = downloadSnapshot(config_folder, snapshot_download_url)
    if not success:
      print("Failed to download the snapshot")
      exit(1)

  launchTheta(config_folder, password)

