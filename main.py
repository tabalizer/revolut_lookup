import requests

def get_user_profile(username):
    url = f"https://revolut.me/api/web-profile/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("API Response:")
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print("HTTP error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Connection error:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout error:", errt)
    except requests.exceptions.RequestException as err:
        print("Unknown error:", err)

if __name__ == "__main__":
    user_input = input("Enter Revolut username: ").strip()
    get_user_profile(user_input)
