import twitter,json

with open('config') as json_data:
    prof = json.load(json_data)

name = prof['person_1']['name']

api_key ="rID32Pp1AiyINX6saYB3L7Ver"
api_secret="Fs3tuAz69BvLnVP6faMsXGeb3zETZ4t7d4QNDlMxJUdXKxdIP2"
access_token="876043429905444864-wLthJ70dFKhHuHtekyn2whGcCleYhum"
access_secret="k9CDGjN7GfBvWMWbcXGRCcKpGeaPiIn8tvmrcGRWqzJNc"
api = twitter.Api(api_key,api_secret,access_token,access_secret)
data = api.GetUsersSearch(name)
print(data)
user = api.GetUser(68225924)
print (user)