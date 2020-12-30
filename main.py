# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def requestDataIp(stringRequest):
    stringRequest = stringRequest.split('/')
    ip = stringRequest[0]
    cidr = stringRequest[1]
    count = 0
    arrayBinarioForMascara = []
    while count < 32:
        if count < int(cidr):
            arrayBinarioForMascara.append(1)
        else:
            arrayBinarioForMascara.append(0)
        count = count + 1
    bloque = stringBinarioToFormatIp(arrayBinarioForMascara)
    octetos_ip = ip.split(".")
    binario_ip = []
    resultado_aux = 0
    string_pivote = ""
    piv_exp = 7
    contador_ip = 0
    print("---------")
    for i in octetos_ip:
        resultado_aux = int(i)
        while piv_exp >= 0:
            if resultado_aux < pow(2,piv_exp):
                string_pivote = string_pivote + "0"
            else:
                string_pivote = string_pivote + "1"
                resultado_aux = resultado_aux - pow(2,piv_exp)
            piv_exp = piv_exp - 1
        piv_exp = 7
        binario_ip.append(string_pivote)
        string_pivote = ""
    bit_host = 32 - int(cidr)
    string_binario = binario_ip[0] + binario_ip[1] + binario_ip[2] + binario_ip[3]
    string_host = string_binario[int(cidr): 32]
    binario_red = string_binario[0:int(cidr)]
    aux_bit_host = bit_host
    while aux_bit_host > 0:
        binario_red = binario_red + "0"
        aux_bit_host = aux_bit_host - 1
    binario_first_host= binario_red[0:31]
    binario_first_host = binario_first_host + "1"
    aux_bit_host = bit_host
    binario_broadcast = string_binario[0:int(cidr)]
    while aux_bit_host > 0:
        binario_broadcast = binario_broadcast + "1"
        aux_bit_host = aux_bit_host - 1
    binario_last_host = binario_broadcast[0:31]
    binario_last_host = binario_last_host + "0"
    ip_req = stringBinarioToFormatIp(string_binario)
    ip_network = stringBinarioToFormatIp(binario_red)
    ip_first_host = stringBinarioToFormatIp(binario_first_host)
    ip_last_host = stringBinarioToFormatIp(binario_last_host)
    ip_broadcast = stringBinarioToFormatIp(binario_broadcast)

    item = {
        "data":[
            {
                "ip_request": ip,
                "cidr": cidr,
                "netmask": bloque,
                "binary_ip": string_binario,
                "ip": ip_req,
                "binary_network":binario_red,
                "ip_network":ip_network,
                "binary_first_host": binario_first_host,
                "ip_first_host": ip_first_host,
                "binary_last_host": binario_last_host,
                "ip_last_host": ip_last_host,
                "binary_broadcast": binario_broadcast,
                "ip_broadcast": ip_broadcast,
            }
        ]
    }
    return item

def stringBinarioToFormatIp(stringBinario):
    pivote = 0
    aux = 7
    suma = 0
    decimal = 0
    bloque = []
    for i in stringBinario:
        i = int(i)
        if pivote == 8 or pivote == 16 or pivote == 24:
            aux = 7
            bloque.append(suma)
            suma = 0
        if i > 0:
            decimal = pow(2,aux)
        else:
            decimal = 0
        suma = suma + decimal
        if pivote == 31:
            bloque.append(suma)
        pivote = pivote + 1
        aux = aux - 1
    ip = str(bloque[0])+"."+str(bloque[1])+"."+str(bloque[2])+"."+str(bloque[3])
    return ip

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(requestDataIp('45.231.169.89/29'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
