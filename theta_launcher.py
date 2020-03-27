#!/usr/bin/python3

import os
import os.path as path

SNAPSHOT_DOWNLOAD_URL = 'https://mainnet-data.thetatoken.org/snapshot'
CONFIG_FOLDER = '../mainnet/guardian'

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

def launchTheta(config_folder):
  print("")
  print("============================== Launching Theta... ==============================")
  print("")
  cmd = 'theta start --config={}'.format(config_folder)
  os.system(cmd)

if __name__ == '__main__':
  config_folder = CONFIG_FOLDER
  snapshot_download_url = SNAPSHOT_DOWNLOAD_URL

  if needsToDownloadSnapshot(config_folder):
    success = downloadSnapshot(config_folder, snapshot_download_url)
    if not success:
      print("Failed to download the snapshot")
      exit(1)

  launchTheta(config_folder)

