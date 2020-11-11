#region Description: task8
query1='خشکی دریاچه هامون'
query2='کاهش گردشگری سیستان و زابل'
######################################################################################
#pip install google
#pip install beautifulsoup4
#pip install google-api-python-client
#link for tutorials: https://linuxhint.com/google_search_api_python/
#                    https://www.geeksforgeeks.org/performing-google-search-using-python-code/

from googlesearch import search
from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

my_api_key = '...'
my_cse_id = "..."

query12=query1+" "+query2
query21=query2+" "+query1

result_query1 = google_search(query1, my_api_key, my_cse_id)
result_query2 = google_search(query2, my_api_key, my_cse_id)
result_query12 = google_search(query12, my_api_key, my_cse_id)
result_query21 = google_search(query21, my_api_key, my_cse_id)

hits_query1=int(result_query1['searchInformation']['totalResults'])
hits_query2=int(result_query2['searchInformation']['totalResults'])

hits_query12=int(result_query12['searchInformation']['totalResults'])
hits_query21=int(result_query21['searchInformation']['totalResults'])

jsim12=hits_query12/(hits_query1+hits_query2-hits_query12)
jsim21=hits_query21/(hits_query1+hits_query2-hits_query21)

print(jsim21*100)
print(jsim12*100)

#pause should be 2 because your IP would be blocked
#stope=None loop forever till ends
'''
for url in search(query12, num=10,tld="com", pause=2, start=0, stop=10):
    print(url)

for url in search(query21, num=10,tld="com", pause=2, start=0, stop=10):
    print(url)
'''
#endregion
