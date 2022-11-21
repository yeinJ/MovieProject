import requests
import json

TMDB_API_KEY = '0be9f318e0cbbb471dd67369f3b2c1ca'

def get_movie_datas(N):
    total_data = []

    page = 1
    cnt = 0
    while cnt < N:
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={page}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            try:
                data = {
                    'id': movie['id'],
                    'title': movie['title'].strip(),
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'].strip(),
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                if (data['id'] and data['title'] and data['release_date'] and data['popularity'] and data['vote_count'] and data['vote_average'] and data['overview'] and data['poster_path'] and data['genres']):
                    cnt += 1
                    json = {
                        'model': 'movies.movie',
                        'fields': data
                    }
                    total_data.append(json)
                
                    if cnt >= N:
                        break
            
            except Exception as e:
                print(e)
                print(movie)
                print()

        page += 1
    
    return total_data


movie_list = get_movie_datas(1000)
print(len(movie_list))

with open("./movies/fixtures/movies_data.json", "w", encoding="utf-8") as w:
    json.dump(movie_list, w, indent=4, ensure_ascii=False)
