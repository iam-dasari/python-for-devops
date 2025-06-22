```
get(url,params,args): Sends a GET request to the specified URL
head(url,args): Sends a HEAD request to the specified url
post(url,data,json,args): Sends a POST request to the specified URL
put(url,data,args): Sends a PUT request to the specified URL
patch(url,data,args): Sends a PATCH request to the specified URL
delete(url,args): Sends a DELETE request to the specified URL
request(method,url,args): Sends a request of the specified method to the specified URL
```

```
get request
-----------
x = requests.get('url')
print(x.text)
```

```
head request
------------
x = requests.head('url')
print(x.headers)
```

```
post request
------------
url = 'url'
data = {'somekey': 'somevalue'}
x = requests.post(url, data=data)
print(x.text)
```

```
put request
------------
url = 'url'
data = {'somekey': 'somevalue'}
x = requests.put(url, data=data)
print(x.text)
```

```
delete request
------------
url = 'url'
data = {'somekey': 'somevalue'}
x = requests.delete(url, data=data)
print(x.text)
```
