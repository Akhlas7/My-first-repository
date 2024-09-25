import requests

def get_news():
     url = f"https://newsdata.io/api/1/latest?apikey=pub_544183a3aa834bb1808fbb00965944b6806dd&q=pizza"
     r = requests.get(url)
     content = r.json()
     print(content)


     get_news()





