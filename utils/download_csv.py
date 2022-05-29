import requests 
import os
import argparse 


parser = argparse.ArgumentParser(description='script to download csv files uploaded on GitHub')
parser.add_argument('-u', '--url', type=str, required=True, help='url of the csv file')
parser.add_argument('-n', '--name', type=str, required=True, help='Filename')
args = parser.parse_args()

def download_csv(url:str, name:str):
     
    res = requests.get(url, allow_redirects=True)

    with open(f'/home/adweeb/stat101/data/{name}.csv','wb') as file:
        file.write(res.content)

if __name__ == "__main__":

    download_csv(args.url, args.name)