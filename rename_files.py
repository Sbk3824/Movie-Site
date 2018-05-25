import os

def rename_files():
    file_list = os.listdir("/Users/sbk/PythonUdacity/prank")
    curr_dir = os.getcwd()
    print curr_dir
    os.chdir("/Users/sbk/PythonUdacity/prank")
    print "Now in", os.getcwd()
    for file_name in file_list:
        print "Old File Name:", file_name
        print "New File Name:", file_name.translate(None,"0123456789")
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(curr_dir)
    print "Switched to", os.getcwd()
    

rename_files()
