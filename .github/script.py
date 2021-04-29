import requests
import json
import sys



sub = str(sys.argv[1])

def getPushshiftData(sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='+ str(sub) +'&after=7d&sort_type=num_comments&sort=desc&domain=i.redd.it&domain=i.imgur.com&size=1'
    r = requests.get(url)
    data = json.loads(r.text)

    return data['data']


post = getPushshiftData( sub )
if( len(post) > 0 ):
    post = post[0]
    print( post['author'] )
    print( post['title'] )
    print( post['url'] )
    print( post['full_link'] )
else:
    print('Error')
    print('The subreddit r/'+ sub +' might not exist')
    print('or')
    print('No pictures were found')