import requests
from bs4 import BeautifulSoup
import json
import csv
    
def get_all_eps(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    epsodes = soup.find_all('h2',class_ = 'font-size-18 text-white mb-2')

    all_eps = []
    for eps in epsodes:
        try:
            one_eps = eps.find('a').get('href')
            all_eps.append(one_eps)
        except:
            continue

    return all_eps

def title(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.find('h1',class_='entry-title font-size-28 font-weight-bold text-white mb-0').text   

def one_eps(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    download_first = soup.find('a',class_='link-btn link-download d-flex align-items-center px-3').get('href')


    return download_first

def download(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    download_first = soup.find('a',class_='font-size-16 text-muted').get('href')
    return download_first

    

def bot(url):
    titles = title(url)
    all_epsods = get_all_eps(url)

    all_epsods_2 = []

    for elem in all_epsods:
        one_elem = one_eps(elem)
        all_epsods_2.append(one_elem)

    all_download_links = []
    for element in all_epsods_2:
        download_eps = download(element)
        all_download_links.append(download_eps)

    with open(f"{titles}.txt", "w") as txt_file:
        for line in all_download_links:
            txt_file.write(line + "\n")


    





if __name__ == "__main__":
    bot('https://old.akwam.net/148324/%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D8%A7%D8%B3%D8%B7%D9%88%D8%B1%D8%A9-%D8%A7%D9%84%D8%A8%D8%AD%D8%B1-%D8%A7%D9%84%D8%A7%D8%B2%D8%B1%D9%82-%D8%A7%D9%84%D9%85%D9%88%D8%B3%D9%85-%D8%A7%D9%84%D8%A7%D9%88%D9%84-%D9%85%D8%AF%D8%A8%D9%84%D8%AC')


