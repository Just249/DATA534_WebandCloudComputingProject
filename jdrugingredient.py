import pandas as pd
import requests
from pprint import pprint
import requests
import time
import json

def jdrugingredient(user_input):
    
    # credentials
    key = "257eb29dc538a64a9e9d3fdc69758cce"

    url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/drugproduct?lang=en&type=json&status=1&user-key="
    url += key

    headers = {
      'user-key': key
    }
    
    # reading json response from drugproduct API call
    data = pd.read_json("response.json")
    drug_codes = []
    brand_names = []
    code_brands = []

    # converting response to dictionary and creating a lsit of drug_codes and brand_names
    datadict = data.to_dict(orient='records')
    datadict
    n = len(datadict)
    # print( (datadict[7]['drug_code'], datadict[7]['brand_name'] ) )
    for i in range(n):
        drug_codes.append(datadict[i]['drug_code'])
        brand_names.append(datadict[i]['brand_name'])
        code_brands.append((datadict[i]['drug_code'],datadict[i]['brand_name']))
    df = pd.DataFrame({'drug_code': drug_codes, 'brand_name': brand_names})

    user_input = user_input.lower()
    filters = []

    # finding matching brand names for user_input
    for brand in brand_names:
        if user_input == brand.lower():
            filters.append(brand)
            
    # removing duplicates
    filters = list(set(filters)) 

    # finding drug id(s) corresponding to user-input
    filters_ids = []
    for item in filters:
        k = brand_names.index(item)
        filters_ids.append(drug_codes[k])

    ingredient_list = []
    brand_namelist=[]

    # creating urls to get response from form and route APIs
    ingredient_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/activeingredient?lang=en&type=json&id="
    
    # inputting drug ids and retrieving results
    for drug_id in filters_ids:

        ingredient_url += (str(drug_id) + "&active=yes")
        # time.sleep(1)
        ingredient_response = requests.request("GET", ingredient_url, headers=headers)
        # converting to list of dictionaries using .json()
        ingredient_data = ingredient_response.json()
        
        # extracting required information
        for i in ingredient_data :
            ingredient_list.append(i['ingredient_name'])
            brand_namelist.append(filters[filters_ids.index(drug_id)].title())

    print("Here are the results that we found:")
    ff_d = {'Brand Name':brand_namelist, 'Ingredient': ingredient_list}
    ff = pd.DataFrame(ff_d)
    return (ff)