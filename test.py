import requests
# data = {
#         "user_id": 154824,
#         "no_watch_next":50,
#         "filter": {}
#     }
# path = "http://ai.sssmarket.com:8670/discovery_mall"

# res = requests.post(url=path,json=data)
# print(res.content)


data = {
        "user_id": 154824,
        "no_watch_next":50,
        "filter": {}
    }
path = "http://test.ai.sssmarket.com:8680/discovery_mall"

res = requests.post(url=path,json=data)
print(res.content)