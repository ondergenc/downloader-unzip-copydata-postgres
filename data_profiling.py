import pandas as pd
import glob

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

def get_file_data_profiling():
    tsv_files = glob.glob("./data/*.tsv", recursive = False)
    tsv_files_df = pd.DataFrame(tsv_files, columns=['file_name'])

    for index, file in tsv_files_df.iterrows():
        data = pd.read_csv(file["file_name"], sep="\t")
        print(file["file_name"])
        print(data.head())
