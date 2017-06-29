from googleapiclient.discovery import build
import json

def google_search(search_term,api_key, cse_id, **kwargs):
    service = build("customsearch", "v1",developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id).execute()
    results= res['items']
    gsearch={}
    i=0
    for result in results:
        gsearch[i] = result['title']+":- "+result['link']
        i+=1
    return gsearch

api_key="nyahahaha"
cse_id="kerokero"

query = raw_input("Enter query parameter")

pastebin_search=google_search(query,api_key ,cse_id, num=10)

res={'paste_search':pastebin_search}
print json.dumps(res,sort_keys=True,indent=4,separators=(',',':'))

