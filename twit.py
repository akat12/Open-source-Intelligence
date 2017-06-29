import twitter,json

with open('config') as json_data:
    prof = json.load(json_data)

name = prof['person_1']['name']

api_key ="mynameajeff"
api_secret="XXXX"
access_token="XYZ"
access_secret="psyduck"
api = twitter.Api(api_key,api_secret,access_token,access_secret)
data = api.GetUsersSearch(name)
print(data)
user = api.GetUser(XXXX) #enter id num here
print (user)
