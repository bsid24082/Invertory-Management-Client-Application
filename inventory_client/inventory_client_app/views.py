from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def product_detail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            try:
                api_url = f'http://localhost:8000/items/{name}/'  # Construct API URL with item name
                response = requests.get(api_url)
                if response.status_code == 200:
                    item = response.json()
                    return render(request, 'product_detail.html', {'item': item})
                else:
                    return render(request, 'home.html', {'message': 'Item not found'})
            except Exception as e:
                return render(request, 'home.html', {'message': 'Error fetching item data'})
        else:
            return render(request, 'home.html', {'message': 'Please enter an item name'})
    return render(request, 'home.html')
