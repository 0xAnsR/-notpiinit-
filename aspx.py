import requests

url = "https://www.ppsc.gop.pk/(S(oxicsm3utyrfa3nfxn0c3tws))/jobs.aspx"
headers = {'User-Agent': 'Mozilla/5.0'}

for _ in range(3):  # Retry 3 times
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("Page fetched successfully")
            break
    except requests.exceptions.RequestException as e:
        print(f"Retrying due to error: {e}")
