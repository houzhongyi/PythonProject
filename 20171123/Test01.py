import requests

top250 = requests.get("https://api.douban.com/v2/movie/top250")
for movie in top250.json()['subjects']:
    movie_id = movie['id']
    movie_url = "https://api.douban.com/v2/movie/subject/" + movie_id
    movie_req = requests.get(movie_url).json()
    ratings_count = movie_req["ratings_count"]
    movie_name = movie_req["title"]
    print(movie_name, ratings_count)