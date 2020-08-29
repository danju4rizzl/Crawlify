import requests
from bs4 import BeautifulSoup


url = "https://stackoverflow.com/questions"
responce = requests.get(url)

soup = BeautifulSoup(responce.text, "html.parser")

questions = soup.select(".question-summary")
votes = soup.select(".vote-count-post ")

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
