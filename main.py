import downloader
import unzip
import pandas as pd
import data_profiling
import data_import_to_postgresql as data_imp

file_path = 'url_list.csv'
downloader.download_file(file_path)
unzip.unzip_file()
data_profiling.get_file_data_profiling()
data_imp.copy_data_to_postgres()
