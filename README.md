# Data-Scraping-IMDB-Movie-Site-using-Python
Data Scraping and Data Wrangling using Python BeautifulSoup

## Data Scraping the TOP 100 most popular videos in IMDb in 2019
<b>Data Scraping</b> from a website is one of the way to get <b>valuable data</b> about present trends especially because most of the data in this age really comes from the datas coming from different website especially <i>Youtube, Facebook, Twitter</i> and other <i>Social Media sites</i>.<br>
Now, if one wants to analyze what's the trend movie currently and use that data for personal or business reasons, scraping data from the popular movie website like <b>IMDb</b> is the way to go.

# Data Scraping using PYTHON
We use <b>Python</b> because it is one of the most used languages in data science and also because it is the language that I am most <b>familiar</b> with.
## Install Important Packages 
(If you already done this part, you can skip this part)
<br>
### On Windows
Open <i>Command Prompt</i> or cmd<br>
Type the following:
```
pip install lxml
pip install numpy
pip install pandas
pip install bs4
pip install requests
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

## Authors

* **Reljod T. Oreta**- [**Reljod**](https://github.com/Reljod)

