# Runs to an error after the system runs out of resource to open more files
files = []
for i in range(10000):
    files.append(open(r"F:\Udacity\python_beg\file_to_read.txt", "r"))
    print(i)
                 
                 
