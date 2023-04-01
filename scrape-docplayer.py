from bs4 import BeautifulSoup
import requests
import time
#import concurrent.futures

#words = ["sundhedsplatform"];
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
baseUrl ="https://docplayer.dk/search/?q="


#MAX_THREADS = 5


#def start_download(words):
#	threads = min(MAX_THREADS, len(words))    
#	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
#		executor.map(download_word_links, words)
	


def findOgGem(word, num):
    result = requests.get("https://docplayer.dk/search/?q="+word+"&page="+num, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")
    searchResults = doc.find_all('h4')
    mylinks =[]
    count = 0
    for x in doc.find_all('h4'):
        count = count+1
        mylinks = x.find_next('a')
        print(mylinks)
        with open("word-links.html", "a") as file:
            file.write(str("<a href='https://docplayer.dk"+ str(mylinks['href']) +"' target='_blank'>https://docplayer.dk"+ str(mylinks['href']) +"</a><br>\n"))
        pass




#lav kun ændringer herunder


# range(antal) bestemmer hvor mange sider du skal bladre igennem
for x in range(20):
    print(x)
    # skift "ordet" her for ny søgning
    findOgGem("sundhedsplatformen", str(x))
    time.sleep(0.5)
    pass

