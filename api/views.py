from django.shortcuts import render

import requests
from django.http import JsonResponse
from datetime import datetime, timezone

# Create your views here.
def me(request):
    try:
        response = requests.get('https://catfact.ninja/fact', timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get('fact', 'No cat fact found.')
    except requests.RequestException:
        cat_fact = f"Could not fetch cat fact: {str(e)}"

    data = {
        "status": "success",
        "user": {
            "email": "your_email@example.com",
            "name": "Oduduabasi Usoro",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data)