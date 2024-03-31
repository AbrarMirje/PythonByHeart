import requests
import random

def youtube_title():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        
        random_index = random.randint(0, 10)
        # print(random_index)
        title = user_data["data"][random_index]["items"]["snippet"]["title"]
        return title
    else:
        raise Exception("Title not found!!!")


def main():
    try:
        title = youtube_title()
        print(f"Title: {title}")
    except Exception as e:
        print(str(e))


if  __name__ == '__main__':
    main()