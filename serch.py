import time,json
from threatlib import general,downloader


start = time.time()
list = general.readxsl("employee.xlsx")
link =general.encoder('http://webmii.com/people?n=\"'+list[2][0]+'\"')
webmii_search =downloader.download(link,'//div[@class="section"][@id="article"]//*')[0]
email_gsearch= downloader.google_search(str(list[2][2]),"AIzaSyAK8_nYtI5mV7hYMfAESMp5wk8FIoOc9eU" ,"000597688297972046908:wpcvmbousjm", num=10)
name_gsearch= downloader.google_search(str(list[2][0]),"AIzaSyAK8_nYtI5mV7hYMfAESMp5wk8FIoOc9eU" ,"000597688297972046908:wpcvmbousjm", num=10)
pastebin_search=downloader.google_search(str(list[2][3]),"AIzaSyDai2S6pC_VaDCfYsFYqjPk5Qf23_TwAYQ" ,"000597688297972046908:nfsxuyodqhe", num=10)
res={'a-name': list[2][0],'b-webmii':webmii_search,'c-email_google_search':email_gsearch,'d-name_search':name_gsearch,'e-paste_search':pastebin_search}
print json.dumps(res,sort_keys=True,indent=4,separators=(',',':'))


print (time.time()-start)
