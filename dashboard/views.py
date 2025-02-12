# # dashboard/views.py
# import requests
# from django.shortcuts import render

# def weather_dashboard(request):
#     api_key = 'd60abc7e526f05648f7d61bab95e40ca'  # ใส่ API Key จาก OpenWeatherMap
#     city = request.GET.get('city', 'Bangkok').replace(" ", " ")  # รับค่า city จาก Form หรือใช้ 'Bangkok' เป็นค่าเริ่มต้น
#     api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = {
#             'city': data['name'],
#             'temperature': data['main']['temp'],
#             'description': data['weather'][0]['description'],
#             'icon': data['weather'][0]['icon']
#         }
#     else:
#         weather_data = None

#     return render(request, 'dashboard/index.html', {'weather_data': weather_data, 'city': city})

# dashboard/views.py
import requests
from django.shortcuts import render

def weather_dashboard(request):
    api_key = 'd60abc7e526f05648f7d61bab95e40ca'  # ใส่ API Key จาก OpenWeatherMap

    # รายชื่อเมืองที่สามารถเลือกได้
    cities = {
        'Bangkok': 'Bangkok',
        'Salaya': 'Salaya, TH',
        'Nakhon Pathom': 'Nakhon Pathom',
        'Chiang Mai': 'Chiang Mai'
    }

    # รับค่า city จาก Dropdown หรือใช้ 'Bangkok' เป็นค่าเริ่มต้น
    city = request.GET.get('city', 'Bangkok')
    city_query = cities.get(city, 'Bangkok').replace(" ", " ")
    
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_query}&appid={api_key}&units=metric'    

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        weather_data = None

    return render(request, 'dashboard/index.html', {
        'weather_data': weather_data,
        'city': city,
        'cities': cities
    })
