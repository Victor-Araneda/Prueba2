import requests
import json

sandbox = "https://10.10.20.14"
def obtener_token(usuario, clave):
    url = sandbox + "/api/aaaLogin.json"
    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

token = obtener_token("admin", "C1sco12345")


def top_level_system():
    url = sandbox + "/api/class/topSystem.json"
    cabecera = {
        "Content-Type": "application/json"
    }
    galletas = {
        "APIC-Cookie": token
    }
    respuesta = requests.get(url, headers=cabecera, cookies=galletas, verify=False)
    print(respuesta.json())


top_level_system()