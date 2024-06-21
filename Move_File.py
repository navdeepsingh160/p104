import os
import shutil

list_of_files = os.listdir(from_dir)
print(list_of_files)

os.path.splitext() 
print()
list [ ‘.txt’, ‘.doc’, ‘.docx’, ‘.pdf’’]

if os.path.exists(path2):
  print("Moving" + file_name +".....")
  shutil.move(path1, path3)

else:
  os.makedirs (path2)
  print("Moving " + file_name + ".....")
  shutil.move(path1, path3)

else:
  os.makedirs (path3)
  print("Moving " + file_name + ".....")
  shutil.move(path1, path3)