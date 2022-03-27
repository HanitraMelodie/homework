# Question 2
import requests
url ='https://opentdb.com/api.php?amount=10&category=11&difficulty=medium'
response = requests.get(url)
quizz = response.json()
result = quizz['results']
print(result)