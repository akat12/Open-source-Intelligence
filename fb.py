import facebook,oauth2,socket,json

socket.timeout(10)
app_id ="166897523846833"
app_secret="1b05d5874eb955ee7f75435decc59844"
link ="https://developers.facebook.com/tools/accesstoken/"

with open('config') as json_data:
    data = json.load(json_data)

consumer = oauth2.Consumer(app_id,app_secret)
client = oauth2.Client(consumer)
req_token_url ="https://graph.facebook.com/oauth/access_token?client_id="+app_id+"&client_secret="+app_secret+"&grant_type=client_credentials"
resp, content = client.request(req_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response", resp['status'])
content = eval(content)
req_token= content["access_token"]
print ("authenticate from the following ",link)
ua_token=input("enter the user access token")
graph = facebook.GraphAPI(ua_token)
query ="https://graph.facebook.com/search?q=akshat%20pradhan&type=user"
name = data['person_1']['name']
data = graph.request('search',{'q':name,'type':'user'})
print (data)





