import http.server
import socketserver
import socket
import subprocess
import os
import shutil

def all_subdirs_of(b='.') -> list:
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd): result.append(bd)
  return result



ip = "0.0.0.0"
port = 8080


# Execute GL - Patcher

current_path = os.getcwd() # backing this up for later use

os.chdir(current_path + "\\Patch")
print("Please wait until the patcher finishes running")
os.system(os.getcwd() + '"/GL - Patcher.exe"')
print("Done!")


# Copy the output to the correct folder
patch_folder = max(all_subdirs_of("Patchs"), key=os.path.getctime) # select the newest created folder

latest_finger = patch_folder + "\\fingerprint.json"

parent = os.path.dirname(current_path) # classic brawl parent dir

shutil.copy(latest_finger, parent + "\\GameAssets") 


os.chdir(current_path) # get back to the original folder
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((ip, port), handler) as httpserver:
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name)
    
    print(f"Patching HTTP server started at URL \nhttp://{host_ip}:{port}/Patchs/\n")
    print("Do not close this window and restart your Classic Brawl server for changes to take effect")
    httpserver.serve_forever()