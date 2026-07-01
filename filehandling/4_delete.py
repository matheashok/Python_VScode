# Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# Example: Remove the file "demofile2.txt":

'''import os
os.remove("demofile2.txt")'''

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example: Check if file exists, then delete it:

'''import os
if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
else:
  print("The file does not exist")'''

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example: Remove the folder "myfolder":

'''import os
os.rmdir("myfolder")'''

# Note: You can only remove empty folders.