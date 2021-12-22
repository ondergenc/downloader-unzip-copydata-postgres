import requests
import pandas as pd

def get_url(file_path):
    return pd.read_csv(file_path, header=None)


def download_file(file_path):
    chunk_size=128
    urls = pd.read_csv(file_path)
    url_df = pd.DataFrame(urls, columns=['url'])
    
    for index, row in url_df.iterrows():
        url = row.url
        if url != 'url':
            save_path = './data/' + url.split('/')[-1]
            r = requests.get(url, stream=True)
            
            with open(save_path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    fd.write(chunk)
            