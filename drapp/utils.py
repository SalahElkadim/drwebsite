import requests

def get_country_from_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/country_name/')
        if response.status_code == 200:
            return response.text
    except:
        pass
    return "unknown"