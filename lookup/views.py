#view lookup.py

from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zipcode) + "&distance=5&API_KEY=0A6DDA1B-E65B-4979-AF58-0E708993F9A5")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...' 
        #rochona = "Air quality : " + api[0]['Category']['Name']
        
        
        return render(request, 'home.html', {'api': api, 'rochona': "fwkjfiw", 'zipcode': zipcode})

        pass
    else :
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94304&distance=5&API_KEY=0A6DDA1B-E65B-4979-AF58-0E708993F9A5")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...' 
        rochona = "Air quality : " + api[0]['Category']['Name']
        #api.0.Category.Name
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94304&distance=5&API_KEY=0A6DDA1B-E65B-4979-AF58-0E708993F9A5
        return render(request, 'home.html', {'api': api, 'rochona': rochona})

def about(request):
    return render(request, 'about.html', {})