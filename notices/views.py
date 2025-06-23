from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def diploma_notices(request):
    target_url = 'https://bteb.gov.bd/site/page/7cd7fa7f-4960-483c-b4e2-5404721ac62b/ডিপ্লোমা-পর্যায়'
    try:
        response = requests.get(target_url)
        response.raise_for_status()
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

    soup = BeautifulSoup(response.content, 'html.parser')
    printable_area = soup.find(id='printable_area')
    if not printable_area:
        return JsonResponse({'error': 'printable_area not found'}, status=404)

    data = []
    # -- find all rows inside the table -
    for tr in printable_area.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) >= 2:
            date_text = tds[0].get_text(strip=True)
            link_tag = tds[1].find('a')
            if link_tag and link_tag.get('href'):
                href = link_tag.get('href')
                text = link_tag.get_text(strip=True)
                data.append({
                    'date': date_text,
                    'title': text,
                    'url': href,
                })
    return JsonResponse(
        data,
        safe=False,
        json_dumps_params={'ensure_ascii': False},  # -- show Bangla properly
    )