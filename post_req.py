import requests

host_ip = #ip da maquina
port = #porta do servidor

url = f'http://{host_ip}:{port}/'

req = requests.post(url)

print(req.status_code)
