import requests

url="https://fakestoreapi.com/products/"

req=requests.get(url)
data=req.json()
#print(data)

for i in data:
    print(f'Product Name:{i["title"]}')
    print(f'Price:{i["price"]}')
    print(f"Rate:{i["rating"]["rate"]}")
