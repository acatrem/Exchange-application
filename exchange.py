import requests
import json


api_key = "064d349f354643c8661660f0"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz: ").upper() #USD
alinacak_doviz = input("Alinacak döviz: ").upper()#TRY
miktar = float(input(f"Miktar {bozulan_doviz}: ")) #1000

sonuc = requests.get(api_url + bozulan_doviz)

sonuc_json = json.loads(sonuc.text)

#print(sonuc_json["conversion_rates"][alinacak_doviz])

print(f"{miktar} {bozulan_doviz} = {miktar * sonuc_json['conversion_rates'][alinacak_doviz]} {alinacak_doviz}")
