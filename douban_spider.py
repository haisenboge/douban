import requests


result = requests.get("https://movie.douban.com/top250")

print(result.text)