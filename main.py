import requests
import datetime

date = datetime.datetime.now()
date = date.strftime("%Y%m%d")
username = "hicham093"
token = "mlkengf5mkeqf"
params= {"quantity":"5"}
headers={
    'X-USER-TOKEN': token,
}
     
response = requests.delete(url=f'https://pixe.la/v1/users/{username}/graphs/graph1/{date}',headers=headers)
print(response.text)
