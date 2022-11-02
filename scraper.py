import requests
from bs4 import BeautifulSoup
def get_citations_needed_count(url):
    """
    funtion that take url as argrument and return number of citations needed as integer 

    Args:
        url (string):the url of the website

    Returns:
        int: number of citations needed
    """
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    all=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    return len(all)

URL='https://en.wikipedia.org/wiki/History_of_Mexico'
print(get_citations_needed_count(URL))


def get_citations_needed_report(url):
    """ 
    funtion that take url as argrument and return number of citations needed report as strting 

    Args:
        url (stirng): the url of the website
    Returns:
        string:report of citations needed
    """
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    for tag in soup.find_all(['p']): 
        if tag.find(class_='noprint Inline-Template Template-Fact'):
            print (tag.text)
    return

print(get_citations_needed_report(URL))
