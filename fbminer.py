import facebook
import oauth2,socket

socket.timeout(10)
app_id ="meep"
app_secret="kerokero"
link ="https://developers.facebook.com/tools/accesstoken/"
consumer = oauth2.Consumer(app_id,app_secret)
client = oauth2.Client(consumer)
req_token_url ="https://graph.facebook.com/oauth/access_token?client_id="+app_id+"&client_secret="+app_secret+"&grant_type=client_credentials"
resp, content = client.request(req_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response", resp['status'])
api_ver = resp['facebook-api-version']
content = eval(content)
req_token= content["access_token"]
print ("authenticate from the following ",link)
ua_token=input("enter the user access token")
graph = facebook.GraphAPI(ua_token)
fbid = input("enter the fbid")

data = graph.request(fbid+'?metadata=1')
print (data)
