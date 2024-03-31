import requests

def fetch_joke_content():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]    
        content = user_data["content"]
        return content
    else:
        raise Exception("Jokes are not available now!!")


def main():
    try:
        content = fetch_joke_content()
        print(f"Latest Joke:\n{content}")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()