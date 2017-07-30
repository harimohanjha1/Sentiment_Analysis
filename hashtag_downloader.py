from requests_oauthlib import OAuth1Session
import json
import sys
KEY = "mtPa0sN2Y9qDvfrgAKb4ISBai"
SECRET = "2wPmc3gm9sj9uIB2S41v5jYnOTiP0OEyhffkIqHcBx5fpSZNcR"
TOKEN = " 2685173118-L6TmM5UW1vSwSiQfp0IRhsHtka1ncelL0tCuOgs"
TOKEN_SECRET = " sTtL8Mz642wLi04hqhN6lZLfwSWU2zpiJMHmX2ESkdBOO"
def stream(hashtag):
    twitter = OAuth1Session(KEY, client_secret=SECRET,
                            resource_owner_key=TOKEN,
                            resource_owner_secret=TOKEN_SECRET)

    r = twitter.post(
        'https://stream.twitter.com/1.1/statuses/filter.json',
        data={
            'track': hashtag
            },
        stream=True
    )

    for line in r.iter_lines():
        if line:
            print line

if __name__ == '__main__':
    hashtag = 'twitter'
    if len(sys.argv) >= 2:
        hashtag = sys.argv[1]
    stream(hashtag)
