from datetime import datetime
import requests
import json
import sys



sub = str(sys.argv[1])
today = datetime.now().strftime('%d-%b-%Y %H:%M:%S')

def getPushshiftData(sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='+ str(sub) +'&after=7d&sort_type=num_comments&sort=desc&domain=i.redd.it&size=1'
    r = requests.get(url)
    data = json.loads(r.text)

    return data['data']


post = getPushshiftData( sub )
if( len(post) > 0 ):
    post = post[0]
    print('[time: ' + today + ']')
    print( post['author'] )
    print( post['title'] )
    print( post['url'] )
    print( post['full_link'] )

    f = open('README.md', 'w')
    content = f"""### Hey, what's up?
<img align="right" alt="Pedro's GitHub Top Languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=PedrosUsername&exclude_repo=HW2&layout=compact" />

I'm Pedro. Interested in coding, animation, witch-house and video games.<br>
I like different, creative and original stuff.<br><br>
Welcome to my profile!

### More about me
- **Currently working on:**  
&nbsp;&nbsp;&nbsp;&nbsp;My web development skills
- **Currently learning:**  
&nbsp;&nbsp;&nbsp;&nbsp;Spring and Angular
- **Favorite song:**  
&nbsp;&nbsp;&nbsp;&nbsp;DEVILNOTCRY — NotEnoughOfYou
___
[<img align="right" alt="LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
&nbsp;&nbsp;
[<img align="right" alt="Email" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />][gmail]
___

### Bonus info +

<p align="left"><sub>last updated at: {today}</sub></p>

|   |
| --- |
| <sub>[Posted by: u/{post['author']}][source]</sub> |
| **{post['title']}** | 
|<p align="center"> <img alt="image" src="{post['url']}" width="550" /> </p>|
|   |

  



  
  
  
[linkedin]: https://linkedin.com/in/pedro-h-r-gomes-8a487b14a/
[gmail]: mailto:pilique11@gmail.com
[source]: {post['full_link']}
[PushshiftAPI]: https://github.com/pushshift/api"""

    f.write( content )
    f.close()

else:
    print('Error')
    print('The subreddit r/'+ sub +' might not exist')
    print('or')
    print('No pictures were found')
