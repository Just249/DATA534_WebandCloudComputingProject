import pandas as pd
import requests
from pprint import pprint
import requests
import time
import json

def jdrugingredient(user_input):
    
    # credentials
    key = "257eb29dc538a64a9e9d3fdc69758cce"
#    Cookie = "38771cce9ac0f974522b34af498bfe66=56e404caec9315398b6da15a1e47abfc"

    url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/drugproduct?lang=en&type=json&status=1&user-key="
    url += key

    headers = {
      'user-key': key #,
 #     'Cookie': Cookie
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

    #############################################################################################################
    # this code chunk is for testing purposes, please ignore
    # to check drug ids and brand names that are filtered
    # pprint(filters)
    # pprint(filters_ids)
    # print(filters)

    #############################################################################################################

#    form_list = []
#    route_list = []
    ingredient_list = []
    brand_namelist=[]

    # creating urls to get response from form and route APIs
#    route_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/route?lang=en&type=json&id="
#    form_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/form?lang=en&type=json&id="
    ingredient_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/activeingredient?lang=en&type=json&id="
    
    # inputting drug ids and retrieving results
    for drug_id in filters_ids:

        # creating url specific to a drug
#        route_url += (str(drug_id) + "&active=yes")
#        form_url += (str(drug_id) + "&active=yes")
        ingredient_url += (str(drug_id) + "&active=yes")

        # getting responses
#        route_response = requests.request("GET", route_url, headers=headers)
#       time.sleep(1)
#        form_response = requests.request("GET", form_url, headers=headers)
        ingredient_response = requests.request("GET", ingredient_url, headers=headers)

        # converting to list of dictionaries using .json()
#        route_data = route_response.json()
#        form_data = form_response.json()
        ingredient_data = ingredient_response.json()
        
        # extracting required information
#        form_list.append(form_data[0]['pharmaceutical_form_name'])
#        route_list.append(route_data[0]['route_of_administration_name'])
        for i in ingredient_data :
            ingredient_list.append(i['ingredient_name'])
            brand_namelist.append(filters[filters_ids.index(drug_id)].title())

#        ingredient_list.append(ingredient_data[0]['ingredient_name'])
#        brand_namelist.append(filters[filters_ids.index(drug_id)].title())

        
    # printing/returning output 
    print("Here are the results that we found:")
#    ff_d = {'Brand Name':brand_namelist, 'Form': form_list, 'Administration Route': route_list}
    ff_d = {'Brand Name':brand_namelist, 'Ingredient': ingredient_list}
    ff = pd.DataFrame(ff_d)
    return (ff)