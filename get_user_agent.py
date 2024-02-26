import requests

data = requests.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending")

print(data.request.headers)