import lxml
import numpy as np
from requests import get
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1"
page = get(url)

html = BeautifulSoup(page.text, 'lxml')
movieCon = html.find_all("div", class_="lister-item mode-advanced")

def getMovieName(movieCon):
	movieNames = []
	movieRatings = []
	metaScores = []
	votes = []
	Grosses = []
	for i in range(len(movieCon)):
		movieName = movieCon[i].h3.a.text
		movieNames.append(movieName)
		
		movieRating = movieCon[i].strong.text
		movieRatings.append(movieRating)

		metaScore = movieCon[i].find("div", class_="ratings-bar")
		metaScore = metaScore.find_all("span")[-1].text.replace(" ", "")
		metaScores.append(metaScore)

		movieNG = movieCon[i].find(class_="sort-num_votes-visible")
		vote = movieNG.find_all("span")[1].text
		votes.append(vote)

		gross = movieNG.find_all("span")[-1].text
		grosses.append(gross)

	return movieNames, movieRatings, metaScores, votes, grosses

def cleanGross(gross):
	numGross = []
	for string in gross:
		string = string.replace("$", "")
		if "M" in string:
			string = string.replace("M", "")
			number = float(string)
			number = number*1000000
		else:
			string = string.replace(",", "")
			number = float(string)
		numGross.append(number)
	return numGross

def cleanVotes(vote):
	votes = []
	for string in vote:
		string = string.replace(",", "")
		votes.append(int(string))
	return votes

def cleanScore(score):
	scores = []
	for string in score:
		try:
			num = float(string)
			scores.append(num)
		except ValueError:
			nan_ = string.replace("X", str(np.nan))
			scores.append(float(nan_))
	return scores

def cleanRating(rating):
	return [float(x) for x in rating]

def cleanName(name):
	return [x for x in name]

def checkData(data):
	data = [MN, MR, MS, V, G]
	assert([len(x) for x in data])==[50,50,50,50,50]
	print("All datas are fine..")

def dataFrame(data):
	columnAttrib = ["Movie Name", "Movie Rating", "Movie Score", "Votes", "Gross"]
	df = pd.DataFrame(data=data, columns=columnAttrib)

def main():
	MN, MR, MS, V, G = getMovieName(movieCon)
	Data = [MN, MR, MS, V, G]
	Data[4] = cleanGross(G)
	Data[3] = cleanVotes(V)
	Data[2] = cleanScore(MS)
	Data[1] = cleanRating(MR)
	Data[0] = cleanName(MN)
	checkData(Data)

if __name__ == '__main__':
	main()
