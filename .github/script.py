from datetime import date
import requests
import json
import sys



sub = str(sys.argv[1])
today = date.today().strftime('%d-%b-%Y')

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

    f = open('README.md', 'w')
    content = f"""### Hey, what's up?
<img align="right" alt="GIF" src="https://github.com/PedrosUsername/PedrosUsername/blob/main/aha.gif?raw=true" width="500" height="320" />

Name's Pedro Henrique, but you can call me Pedro. I'm a simple man, I'm
interested in coding, animation, witch-house and video games.
I like the different. When I'm working on something I try to be as creative and original as Possible.

### More about me
- **Currently working on:**  
&nbsp;&nbsp;&nbsp;&nbsp;My web development skills
- **Currently learning:**  
&nbsp;&nbsp;&nbsp;&nbsp;Spring, Django and Angular
- **Looking to collaborate on:**  
&nbsp;&nbsp;&nbsp;&nbsp;Creative projects
- **Favorite song:**  
&nbsp;&nbsp;&nbsp;&nbsp;DEVILNOTCRY — NotEnoughOfYou
___
[<img align="right" alt="LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
&nbsp;&nbsp;
[<img align="right" alt="Email" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />][gmail]
<p align="center">
<img alt="Pedro's GitHub Top Languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=PedrosUsername&exclude_repo=HW2&layout=compact" />
</p>

___

<p align="left"><sub>last updated at: {today}</sub></p>

|   |
| --- |
| <sub>[Posted by: u/{post['author']}][source]</sub> |
| **{post['title']}** | 
|<p align="center"> <img alt="image" src="{post['url']}" width="550" /> </p>|
|   |

<sub>[Reddit] r/{sub}'s most commented post in 7 days</sub>  
  



  
  
  
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