import requests

r = requests.get("http://localhost:8080/api/videos").json()
print(f'{r}')
