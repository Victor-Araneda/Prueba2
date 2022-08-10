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


def info_nodo():
    url = sandbox + "/api/class/mgmtMgmtIf.json?rsp-subtree-class=eqptIngrBytes5min"
    cabecera = {
        "Content-Type": "application/json"
    }
    variables = {
        "APIC-Cookie": token
    }
    respuesta = requests.get(url, headers=cabecera, cookies=variables, verify=False)
    print(respuesta.json())


info_nodo()