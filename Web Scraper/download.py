import requests

url = input("URL : ")
filename = input("File Name : ")

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Error occurred while downloading the file.")
