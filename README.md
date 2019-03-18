# Python Data Scraping IMDb Movie site using BeautifulSoup
Data Scraping and Data Wrangling using Python BeautifulSoup

## Data Scraping the TOP 100 most popular videos in IMDb in 2019
<b>Data Scraping</b> from a website is one of the way to get <b>valuable data</b> about present trends especially because most of the data in this age really comes from the datas coming from different website especially <i>Youtube, Facebook, Twitter</i> and other <i>Social Media sites</i>.<br>
Now, if one wants to analyze what's the trend movie currently and use that data for personal or business reasons, scraping data from the popular movie website like <b>IMDb</b> is the way to go.

# Data Scraping using PYTHON
We use <b>Python</b> because it is one of the most used languages in data science and also because it is the language that I am most <b>familiar</b> with.
## Install Important Packages 
(If you're already done in this part, just <b>skip this</b>)
<br>
### On Windows
**Note:** Make sure that you already installed the Python before pip-installing the following packages.<br>

Open <i>Command Prompt</i> or cmd<br>
Type the following:
```
pip install lxml
pip install numpy
pip install pandas
pip install bs4
pip install requests
```

### On Linux
**Note:** Make sure that you already installed the Python before aptget-installing the following packages.<br>

Open the <i>Terminal</i><br>
Type the following:
```
apt-get install lxml
apt-get install numpy
apt-get install pandas
apt-get install bs4
apt-get install requests
```

# Going to IMDb Website
![image](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/imdbmain.png)
1. Go to [IMDb](https://www.imdb.com/?ref_=nv_home) movie website
2. Hover your mouse to the <b>Watchlist</b>
3. Click the <b>Popular Movies</b> section

If you want to use my Jupyter notebook, use this link:
[IMDb-most-popular-2019](https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2)
![image](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/imdbweb.png)
## Use Google Chrome Developer Tools
Use Google Chrome Developer Tools to inspect <b>elements</b> or the data of the website.
Right Click mouse then Inspect
![right-click](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/right-click-inspect.png)
Find the Elements that correspond to the data we're getting
![hover-mouse-content](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/highlight-elements.png)
![hover-mouse-movie](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/highlight-firstmovie.png)
![hover-mouse-title](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/hightlight-target-text.png)
<b>Keep in mind</b> that one need to find the source of the data before getting it. In the case of the IMDb movie website, the structure of the data of the 1st movie is similar to the structure of those remaining 99 movies. We can take advantage of that later.
#### Take note of the TAGS as well as the Attributes like class, id, etc. We'll use that later.

## CODE (Click the jupyter notebook link to continue)
[Step-by-Step-Jupyter-Notebook-Code](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/jupyter-notebook/IMDBwebscraping.ipynb)
### IMDb class jupyter notebook code (full):
[Full-code](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/jupyter-notebook/IMDb-Web-Scraping-Full-Code.ipynb)
## Step-by-Step python code
**Import modules**
```
import pandas as pd
import numpy as np
import re
import lxml

from bs4 import BeautifulSoup
from requests import get
%matplotlib inline
```
**Get the page link**
```
url= "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"
```
<dl>
  <dt><b>Get page data</b></dt>
  <dd>- Get page using requests.get<br></dd>
  <dd>- Parse page using BeautifulSoup and lxml</dd>
</dl>

```
page = get(url)
soup = BeautifulSoup(page.content, 'lxml') 
```

<b>Get the Element or tag that holds the <i>movie</i> contents</b><br>
![id-main-image](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/idmain.png)
```
content = soup.find(id="main")
```
### Get Article Title
soup.find("h1", class_="header")** finds the first line that has **h1** tag and has a **class** header.<br>
.text** gets the text of that line or that element.<br>
.replace("\n","")** just erases **\n**.
```
articleTitle = soup.find("h1", class_="header").text.replace("\n","")
```
### Get the contents of one movie content
![movie-frame](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/highlight-movie-frame.png)
Find_all returns a <b>list</b> of all instances that has the <b>tags</b> specified (i.e. "div", "class")<br>
To get the first movie only, use movieFrame[0]
```
movieFrame = content.find_all("div", class_="lister-item mode-advanced")
```
### Getting the Movie Title and Movie Date
![first-line](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/first-line.png)<br>
We need to first get the line where the title and the date contains because the tags that holds those values are too <b>common</b> and using find might not get it to <b>appear</b>.<br>
<b>.find("a")</b> returns the first line that has a <b>tag "a"</b><br>
<b>.find_all("span")</b> returns all lines that has a tag of "span". Because we only want the date, we only return the second line denoted by ("span")[-1]<br>
<b> .text</b> returns the <b>text value</b> of that line.<br>
```
movieFirstLine = movieFrame[0].find("h3", class_="lister-item-header")
movieTitle = movieFirstLine.find("a").text
movieDate = re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text)
```
### Getting the Runtime, genre, rating, score and movie description
Find the other datas are just the same as what we did with the first ones. Just take note that <b>be more specific</b> in describing the <b>attributes</b> (i.e. class, id, etc.) so that the it will directly return the line that we want to get. 
```
movieRunTime = movieFrame[0].find("span", class_="runtime").text[:-4]
movieGenre = movieFrame[0].find("span", class_="genre").text.rstrip().replace("\n","").split(",")
movieRating = movieFrame[0].find("strong").text
movieScore = movieFrame[0].find("span", class_="metascore unfavorable").text.rstrip()
movieDesc = movieFrame[0].find_all("p", class_="text-muted")[-1].text.lstrip()
```
### Getting the movie casts and directors
Movies w/o including the directors are troublesome and we need to anticipate that by making that missing value into NaN using np.nan.
Getting the movie casts is a bit tricky because there is an indefinite number of casts that can be included in each movie, sometimes none, sometimes a few. That is the reason why we need to anticipate those three scenarios.<br>
Take a look at the <b>code</b>:
```
#Movie Director and Movie Stars
try:
    casts = movieCast.text.replace("\n","").split('|')
    casts = [x.strip() for x in casts]
    casts = [casts[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
    movieDirector = casts[0]
    movieStars = [x.strip() for x in casts[1].split(",")]
except:
    casts = movieCast.text.replace("\n","").strip()
    movieDirector = np.nan
    movieStars = [x.strip() for x in casts.split(",")]
```
##### Same scenario with the votes and gross
We can get an attribute by including it to the attrs dictionary and adding its value to it.
```
movieNumbers = movieFrame[0].find_all("span", attrs={"name": "nv"})
if len(movieNumbers) == 2:
    movieVotes = movieNumbers[0].text
    movieGross = movieNumbers[1].text
else:
    movieVotes = movieNumbers[0].text
    movieGross = np.nan
```
### Full code
```
'''
Author: Reljod T. Oreta PUP-Manila
BSECE 5th year
'''
import lxml
import re
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from requests import get

url1 = "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"

class IMDB(object):
	"""docstring for IMDB"""
	def __init__(self, url):
		super(IMDB, self).__init__()
		page = get(url)

		self.soup = BeautifulSoup(page.content, 'lxml')

	def articleTitle(self):
		return self.soup.find("h1", class_="header").text.replace("\n","")

	def bodyContent(self):
		content = self.soup.find(id="main")
		return content.find_all("div", class_="lister-item mode-advanced")

	def movieData(self):
		movieFrame = self.bodyContent()
		movieTitle = []
		movieDate = []
		movieRunTime = []
		movieGenre = []
		movieRating = []
		movieScore = []
		movieDescription = []
		movieDirector = []
		movieStars = []
		movieVotes = []
		movieGross = []
		for movie in movieFrame:
			movieFirstLine = movie.find("h3", class_="lister-item-header")
			movieTitle.append(movieFirstLine.find("a").text)
			movieDate.append(re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text))
			try:
				movieRunTime.append(movie.find("span", class_="runtime").text[:-4])
			except:
				movieRunTime.append(np.nan)
			movieGenre.append(movie.find("span", class_="genre").text.rstrip().replace("\n","").split(","))
			try:
				movieRating.append(movie.find("strong").text)
			except:
				movieRating.append(np.nan)
			try:
				movieScore.append(movie.find("span", class_="metascore unfavorable").text.rstrip())
			except:
				movieScore.append(np.nan)
			movieDescription.append(movie.find_all("p", class_="text-muted")[-1].text.lstrip())
			movieCast = movie.find("p", class_="")

			try:
				casts = movieCast.text.replace("\n","").split('|')
				casts = [x.strip() for x in casts]
				casts = [casts[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
				movieDirector.append(casts[0])
				movieStars.append([x.strip() for x in casts[1].split(",")])
			except:
				casts = movieCast.text.replace("\n","").strip()
				movieDirector.append(np.nan)
				movieStars.append([x.strip() for x in casts.split(",")])

			movieNumbers = movie.find_all("span", attrs={"name": "nv"})

			if len(movieNumbers) == 2:
				movieVotes.append(movieNumbers[0].text)
				movieGross.append(movieNumbers[1].text)
			elif len(movieNumbers) == 1:
				movieVotes.append(movieNumbers[0].text)
				movieGross.append(np.nan)
			else:
				movieVotes.append(np.nan)
				movieGross.append(np.nan)

		movieData = [movieTitle, movieDate, movieRunTime, movieGenre, movieRating, movieScore, movieDescription,
							movieDirector, movieStars, movieVotes, movieGross]
		return movieData
```
### Check the result using the IMDB class
```
id1 = IMDB(url1)
#Get Article Title
print(id1.articleTitle())
#Get the first 5 movie data using for loop
for i in range(5):
	print(movieData[i][:5])
```
Result should be:
![imdbData](https://github.com/Reljod/Data-Scraping-IMDB-Movie-Site-using-Python/blob/master/imdb/imdbData.png)

## What's next?
The data we extracted from the website should be <b>cleaned</b> first before using it for <b>data analyzation</b> or <b>machine learning</b> but it will be done on my next project using exactly the data that we've been extracted so far.

## Thank You!!

## Author

* **Reljod T. Oreta**- [**Reljod**](https://github.com/Reljod)

