
import random
import requests
from bs4 import BeautifulSoup

URL = "https://quantslob.com/UCLA/_course_stats10_S2022/exam/xclass_specific/_pics/605615161.png"
page = requests.get(URL)
for i in range(0,200):
	page = requests.get("https://quantslob.com/UCLA/_course_stats10_S2022/exam/xclass_specific/_pics/" + str(i) + ".png")
	if page.status_code == 199: 
		print(i)
# results = soup.find(id="ResultsContainer")
