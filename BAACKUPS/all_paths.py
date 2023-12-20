import os
dir = os.path.dirname(__file__)

filename = os.path.join(dir, '/relative/path/to/file/you/want')
  
Picture_path = os.path.join(dir,"No_Virus_Found.png")

icon_path = os.path.join(dir,"Antivirus_Logo.png")

#First time run paths  

username_file_path = os.path.join(dir,"./User_credn/usernames.txt")

password_file_path = os.path.join(dir,"./User_credn/password.txt")

email_file_path = os.path.join(dir,"./User_credn/email.txt")

purchase_file_path = os.path.join(dir,"User_credn/purchase.txt")

multi_scan_path =  os.path.join(dir,"scan/dire.py")

directory_scan_path =  os.path.join(dir,"scan/multi.py")

enigne_scan_path = os.path.join(dir,"scan/engine.py")