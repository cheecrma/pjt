from operator import methodcaller
from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Movie
from rest_framework import status
from rest_framework.response import Response
import requests
import random



## 필요한 API 받아오기 ##
# 날씨 API
def weather(reg):
    # URL 및 요청변수 설정
    BASE_URL = 'https://api.openweathermap.org'
    path = '/data/2.5/weather'
    region = str(reg)
    params = {'q': region, 'appid': '94d20dbf59c21d77835234930c8cfae2'}
    
    # 결과를 받아서 json형식의 data변수로 저장
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    # 날씨 데이터 반환
    name = data.get('name')
    weather = data.get('weather')
    main = weather[0].get('main')
    icon = weather[0].get('icon')
    description = weather[0].get('description')
    return [name, main, icon, description]

# 누적 인기 영화 API
def movie_popular(page):
    # URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    page = int(page)
    params = {
        'api_key': '7065898125e3c5540c241eebabdd426e',
        'language': 'ko-KR',
        'page': page,
        'region': 'KR',
        }
    
    # 결과를 받아서 json형식의 data변수로 저장
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    movie_popular_list = []
    for i in range(len(data.get('results'))):
        title = data.get('results')[i]['title']
        overview = data.get('results')[i]['overview']
        release_date = data.get('results')[i]['release_date']
        poster_path = data.get('results')[i]['poster_path']
        genre_ids = data.get('results')[i]['genre_ids']
        vote_average = data.get('results')[i]['vote_average']

        movie_popular_list.append([title, overview, release_date, poster_path, genre_ids, vote_average])
    
    return movie_popular_list

# 영화 리스트 생성
# if __name__ == '__main__':
#     movie_list = []
#     for i in range(1,11):
#         movie_list.extend(movie_popular(i))


## Create your views here. ##
@require_safe
def index(request):
    return render(request, 'movies/index.html')

@login_required
@require_http_methods(['GET', 'POST'])
def result_on(request):
    # 싫어하는 장르는 not in으로 필터 & 날씨는 우리의 리스트를 만들어서 해당 장르의 영화 추천
    person = request.user
    # 한글로 받은 지역을 영어로 변환시키기!
    dict_region = {'서울': 'Seoul', '대전': 'Daejeon', '대구': 'Daegu', '부산': 'Busan', '구미': 'Gumi',}
    weather_now = weather(dict_region[person.region])
    
    genre_list = []
    if weather_now[1] == 'Clear':
        genre_list = [14, 36, 10770, 16, 10751, 35, 10749]
    elif weather_now[1] == 'Clouds':
        genre_list = [36, 12, 18, 878, 10752]
    elif weather_now[1] == 'Drizzle':
        genre_list = [9648, 37, 35]
    elif weather_now[1] == 'Rain':
        genre_list = [99, 10402, 53, 80]
    elif weather_now[1] == 'Thunderstorm':
        genre_list = [14, 53, 10752, 27]
    elif weather_now[1] == 'Snow':
        genre_list = [10770, 12, 10749]
    else:
        genre_list = [99, 10752, 28]


    dict_genre = {'액션': 28, '애니메이션': 16, '코미디': 35, '범죄': 80, '공포': 27, '드라마': 18, '로맨스': 10749, 'SF': 878, '가족': 10751, '기타': 12,}
    genre_code_like = random.choice(genre_list)
    genre_code_dislike = dict_genre[person.genre_dislike]
    

    
    movie_list = []
    for i in range(1,6):
        movie_list.extend(movie_popular(i))
    
    suggest_list = []
    for i in range(len(movie_list)):
        if (genre_code_dislike not in movie_list[i][4]) and (genre_code_like in movie_list[i][4]):
            suggest_list.append(movie_list[i])

    # 추천해줄 영화 없음
    if len(suggest_list) == 0:
        context = {
            'region_here': person.region,
            'weather_now': weather_now[0:2],
            'weather_icon': weather_now[2],
            'weather_description': weather_now[3],
            'poster_path' : '/fWJuBBzXPJAVQqktXRWPXdLyflS.jpg',
            'title': '다시 진행해 주세요.',
            'vote_average': '0.0',
            'release_date': '0000-00-00',
            'overview': '해당하는 영화를 찾지 못했습니다.',
        }
        return render(request, 'movies/result_on.html', context)
    else:
        num = random.randint(0, len(suggest_list)-1)
        context = {
            'region_here': person.region,
            'weather_now': weather_now[0:2],
            'weather_icon': weather_now[2],
            'weather_description': weather_now[3],
            'like' : genre_code_like,
            'dislike': genre_code_dislike,
            'title': suggest_list[num][0],
            'overview': suggest_list[num][1],
            'release_date':suggest_list[num][2],
            'poster_path': suggest_list[num][3],
            'vote_average': suggest_list[num][5],
            
        }
        return render(request, 'movies/result_on.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def result_off(request):
    person = request.user
    # 한글로 받은 지역을 영어로 변환시키기!
    dict_genre = {'액션': 28, '애니메이션': 16, '코미디': 35, '범죄': 80, '공포': 27, '드라마': 18, '로맨스': 10749, 'SF': 878, '가족': 10751, '기타': 12,}
    genre_code_like = dict_genre[person.genre_like]
    genre_code_dislike = dict_genre[person.genre_dislike]


    # 좋아하는장르와 싫어하는 장르를 같게 선택한 경우
    if genre_code_like == genre_code_dislike:
        context = {
            'poster_path' : '/s5Ihagz0cOWYyys1VMeN5SXKhqz.jpg',
            'title': '장르를 바꿔주세요.',
            'vote_average': '0.0',
            'release_date': '0000-00-00',
            'overview': '현재 좋아하는 장르와 싫어하는 장르가 같습니다:(',
        }
        return render(request, 'movies/result_off.html', context)

    else:
        movie_list = []
        for i in range(1,6):
            movie_list.extend(movie_popular(i))

        suggest_list = []
        for i in range(len(movie_list)):
            if (genre_code_dislike not in movie_list[i][4]) and (genre_code_like in movie_list[i][4]):
                suggest_list.append(movie_list[i])

        # 추천해줄 영화 없음
        if len(suggest_list) == 0:
            context = {
                'poster_path' : '/eziqqKVysxen1gRlZX2wbb5BUDq.jpg',
                'title': '장르를 바꿔주세요.',
                'vote_average': '0.0',
                'release_date': '0000-00-00',
                'overview': '현재 추천 가능한 장르의 영화가 없습니다:(',
            }
            return render(request, 'movies/result_off.html', context)
        else:
            num = random.randint(0, len(suggest_list)-1)
            context = {
                'like' : genre_code_like,
                'dislike': genre_code_dislike,
                'title': suggest_list[num][0],
                'overview': suggest_list[num][1],
                'release_date':suggest_list[num][2],
                'poster_path': suggest_list[num][3],
                'vote_average': suggest_list[num][5],
            }
            return render(request, 'movies/result_off.html', context)
