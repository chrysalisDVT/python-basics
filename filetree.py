import os

def calculate_file_size(path):
    """ Return the cumulative size of the directory path passes"""
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            total+=calculate_file_size(childpath)
    print('{0:<10}'.format(total),path)
    return total

print(calculate_file_size("C:\\_work\\docs"))



 