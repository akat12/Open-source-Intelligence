# Open-source-Intelligence
Scrapes data from paste sites,facebook,twitter,Indtagram,Google-searching,webmii

GOOGLE SEARCH
steps
1. create an account by accessing this https://cse.google.com/cse/all
2. click on new search engine. Add a random site name in the site to search for box for now. fill the rest of the form
and click create
3. go to settings->basics->site to search and input the sites you want to be in scope.
4. go to search feature->advanced->websearch restricts->result size and enter 20.
5. go to setup-> details and note down the search engine id. This will be used in your python program.
6. go to https://developers.google.com/custom-search/json-api/v1/introduction to get your api key for your search engine.

refference
https://developers.google.com/custom-search/json-api/v1/reference/ api refference.

warning : do not leave the api key and cse id hardcoded into the project.

WEBSITE SCRAPING
WEBMII
parses the html data to xml and generate an element tree from it(tag : value). iterate through the tree for matching
regex and return the matched attribute's value.

PASTEBIN SEARCHING

pastebin's api doesn't allow searching for public posts. The sit itself uses Google with limited scope to search for public
posts with specific keywords. Implemented the same.

FACEBOOK API
steps to create your own application.
1. login to https://developers.facebook.com with your facebook id.
2. go to MyApps and click add a new app. fill in the form and click create App id.
3. Go to App review and enable make testing public.
4. choose the cattegory you want. I took entertainment
5. Go to settings and you will see your app id and app secret. this is required in the program to make api calls.
6.Click on tools and support.
7. Click on access token tool and select create user token for your app. This token is used in calls related to user profile data.
if you need to search for pages or posts, you require a page access token.
8. Click on Tools & support->graph api explorer and test out your api calls.

Refferences.
https://developers.facebook.com/docs/graph-api #graph api doc
https://developers.facebook.com/docs/graph-api/reference/ #API calls refferences

Usage of code:-
1. use fb.py to search for a person's fb id. (still unable to filter results, will try to figure out reason) or use
https://findmyfbid.com/ to get the person's fbid.
2. input the fbid into fbminer.py

Note: Since fql expired on august 8 2016, users have more control over their public data. The data mined by fbminer
depends on their 3 party app settings. Possible workaround: send the targets a fb quiz,form etc. with a catchy name and
run this app in the background.





 LINKEDIN

 unable to perform profile searching as that method is registered for partner programs. still need to figure it out.
 client_id = ''
client_secret = ''

# OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix

linkedin = OAuth2Session(client_id, redirect_uri='https://127.0.0.1')
linkedin = linkedin_compliance_fix(linkedin)

# Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print ('Please go here and authorize,', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

 # Fetch the access token
# Fetch a protected resource, i.e. user profile
r = linkedin.get('https://api.linkedin.com/v1/people/~')
print (r.content)

INSTAGRAM

log in to instagram https://www.instagram.com/developer with your instagram account.
click on manage clients->register a new client.Fill in the form and click register
Note down the client_id and client_secret for your app. You will be using this in the program.
by default apps run in sandbox mode with the dataset restricted to 10 test users that need to be invited and 20 of their
most recent media.
to move from sand box mode to live mode, apply for review and permisssions in the "manage clients" option.
the list of permisssions required are documented here;- https://www.instagram.com/developer/review/
once approved by Instagram, you app will move on to live mode.

REFFERENCES

list of endpoints https://www.instagram.com/developer/endpoints/
api overview https://www.instagram.com/developer/

TWITTER

setting up twitter searching is farily easy:
1. login with your twitter account to https://dev.twitter.com/ -> Join
2. click on My Apps->create new app, after registering.
3. Fill in the details and then click create new application.
4.Note your api_key and api_secret from keys and access token in your app settings.
5. scroll down on the same page and click on genereate access token.
6. Note down your access_token and access_secret.

all twitter api request are made through one user.

REFFERENCES

python-twitter documentation http://python-twitter.readthedocs.io/en/latest/twitter.html
api overview https://dev.twitter.com/overview/api
