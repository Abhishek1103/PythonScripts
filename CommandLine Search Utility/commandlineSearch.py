import webbrowser,sys,requests,bs4


#proxy = {"http": "http://username:password@<proxy_IP>:<Port>/",
#                "https": "http://username:password@<proxy_IP>:<Port>/"}
if len(sys.argv) > 1:
    srch =' '.join(sys.argv[1:])
else:
    print("Enter the search query: ", end="")
    srch = input()
if len(srch)>1:
    query = srch
    #res=requests.get('https://www.google.co.in/search?q='+query, proxies=proxy)
    res=requests.get('https://www.google.co.in/search?q='+query)
    try:
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"html5lib")
        topresults=soup.select(".r a")

        numOpen = min(5, len(topresults))
        try:
            webbrowser.open('https://www.google.co.in/search?q='+query)
        except Exception as ex:
            print("Some error occured: "+str(ex))
        for i in range(numOpen):
            try:
                webbrowser.open('http://google.com'+topresults[i].get('href'))
            except Exception as ex:
                print("Some error occured: "+str(ex))
    except Exception as exc:
        print('There was a problem: %s' % (exc))
else :
    print("enter a search query")
