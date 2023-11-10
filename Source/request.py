import requests

def get_data(query):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    try:
        response = requests.get(api_url + query, headers={'X-Api-Key': '0KA/BoNRh0XFVZp2Ur7CUA==EAoYhhyLWtkeWN2k'})
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the HTTP request:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))