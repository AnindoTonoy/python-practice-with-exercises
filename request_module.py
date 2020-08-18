import requests

r = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     'p1' : 1,
#     'p2' : 5
# }
# r2 = requests.post(url = url, data= data)