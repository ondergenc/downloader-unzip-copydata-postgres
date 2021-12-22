import os
import zipfile
import gzip
import shutil

def unzip_file():
    files = get_files("./data")
    
    for file in files:
        extension = os.path.splitext(file) 
        if extension == 'zip':
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall("./data")
        else:
            with gzip.open(file, 'rb') as f_in:
                with open(file.replace('.gz', ''), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

def get_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

