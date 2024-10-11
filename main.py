import requests
import plotly.express as px

import http.client

conn = http.client.HTTPSConnection("football-web-pages1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "45dfc4c064msh14441388a82d595p138ec2jsn29e66be3c434",
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
}

conn.request("GET", "/appearances.json?comp=1&team=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))