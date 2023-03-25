import requests as req

#product_code = input("POdaj kod produktu: ")
product_code = "100361771"

url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

response = req.get(url)
print(response.status_code)