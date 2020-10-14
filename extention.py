import os
file_name=input("Enter the file name:")
x=os.path.splitext(file_name)
print("Extention of the file :",x[1])
