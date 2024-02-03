import requests
from bs4 import BeautifulSoup

def get_top_links(query, num_links):
    links = []
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('a')
    for result in search_results:
        link = result.get('href')
        if link.startswith('/url?q=https://'):
            #print(result)
            link = link[7:]
            links.append(link.split("&")[0])
            if len(links) == num_links:
                break
    return links[1:]

# query = "test quert"
# num_links = 4

# top_links = get_top_links(query, num_links)
# for link in top_links:
#     print(link)
