# Unzipping a loop of zip files


import subprocess
import re
import os
filename = "37366.zip"

while 1:
  # Find password
  sub = subprocess.Popen('7z l ' + filename, shell=True, stdout=subprocess.PIPE)
  output = sub.stdout.read()

  newFile = re.findall("  [0-9]+.zip", output.decode("utf-8"))

  # Stop when there is no more zip file
  if len(newFile) == 0:
    break
  password = re.findall("[0-9]+", newFile[0])

  # Extract file and remove the old one
  os.system('7z e ' + filename + " -p" + password[0])
  os.system('rm ' + filename)
  
  # Create new loop
  filename = password[0] + ".zip"