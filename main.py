import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

headers = {
    'authority': 'api.fanbox.cc',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'cookie': os.getenv('COOKIE'),
    'dnt': '1',
    'origin': 'https://www.fanbox.cc',
    'referer': 'https://www.fanbox.cc/',
    'sec-ch-ua': '^\\^.Not/A)Brand^\\^;v=^\\^99^\\^, ^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# Example : 4185163
postId = input("Enter Fanbox Post ID : ")

params = (
    ('postId', postId),
)

def main():
    r = requests.get('https://api.fanbox.cc/post.info', headers=headers, params=params)
    title = r.json()['body']['title']
    publishedDatetime = r.json()['body']['publishedDatetime']
    updatedDatetime = r.json()['body']['updatedDatetime']
    results = r.json()['body']['body']['images']
    try:
        os.mkdir(os.path.join(os.getcwd(), title))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), title))

    # Convert time
    formatPublishedtime = datetime.strptime(publishedDatetime, '%Y-%m-%dT%H:%M:%S%z')
    formatUpdatedTime = datetime.strptime(updatedDatetime, '%Y-%m-%dT%H:%M:%S%z')

    # Create descriptions
    lines = [f"title : {title}", f"Publish Date : {formatPublishedtime}", f"Update Date : {formatUpdatedTime}"]
    with open('Post Description.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(lines))

    for result in results:
        imgId = result['id']
        imgUrl = result['originalUrl']
        with open(imgId+'.jpeg', 'wb') as f:
            im = requests.get(imgUrl)
            f.write(im.content)
            print('Writing : ', imgId)

if __name__ == "__main__":
    main()
