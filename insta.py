import urllib.request,json

client_id ="6e46a9d928914100a8b0ed0659511da5"
client_secret="c673cf7d18b44f1bac876bc93e0b9cd2"
redirect_uri="https://127.0.0.1"
scope="public_content"
req_url="https://api.instagram.com/oauth/authorize/?client_id="+client_id+"&redirect_uri="+redirect_uri+"&response_type=token&scope="+scope
print(req_url)
access_token = input("input the access_token at the end of the url:")
search_data = json.load(urllib.request.urlopen("https://api.instagram.com/v1/users/1938315455/media/recent/?access_token="+access_token))
print(search_data)