import pandas as pd
import requests
from pprint import pprint
import requests
import time
import json

def drugconsumption(user_input):

    # credentials
    key = "14ec6574be9f7ef563bce7b554798152"
    Cookie = "38771cce9ac0f974522b34af498bfe66=56e404caec9315398b6da15a1e47abfc"

    url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/drugproduct?lang=en&type=json&status=1&user-key="
    url += key

    headers = {
      'user-key': key,
      'Cookie': Cookie
    }
    
    try:
    
        response = requests.request("GET", url, headers=headers)
        data = response.json()
    
    except:
        
        print("The website did not respond, please try again!")
        return
    
    drug_codes = []
    brand_names = []
    code_brands = []

    n = len(data)
    # print( (data[7]['drug_code'], data[7]['brand_name'] ) )
    for i in range(n):
        drug_codes.append(data[i]['drug_code'])
        brand_names.append(data[i]['brand_name'])
        code_brands.append((data[i]['drug_code'],data[i]['brand_name']))

    df = pd.DataFrame({'drug_code': drug_codes, 'brand_name': brand_names})

    #############################################################################################################
    # brand_names # used to check the branch names list
    #############################################################################################################


    # filtering drug ids and brand names

    #############################################################################################################
    # different user inputs
    # user_input = "AVONEX"
    # user_input = "ACETAMINOPHEN 325MG"
    # user_input = "CLONAZEPAM"
    # user_input = "BROMAZEPAM"
    # user_input = "LIP BALM SPF 15"
    # user_input = "EPHEDRINE SULFATE INJECTION USP"
    #############################################################################################################

    user_input = user_input.lower()
    filters = []

    # finding matching brand names
    for brand in brand_names:
        if user_input in brand.lower():
    #         print(brand_name.index(brand))
            filters.append(brand)

    filters = list(set(filters)) # removing duplicates

    # finding corresponding drug ids
    filters_ids = []
    for item in filters:
        k = brand_names.index(item)
        filters_ids.append(drug_codes[k])

    #############################################################################################################
    # to check drug ids and brand names that are filtered    
    # pprint(filters)
    # pprint(filters_ids)
    #############################################################################################################
    
    # data validation
    
    if not filters:
        print("There is no match for that brand name.")
        return
    else:
        
        # route of administration and form of the drug 

        # some empty declarations
        form_list = []
        route_list = []
        brand_namelist=[]

        # creating urls
        route_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/route?lang=en&type=json&id="
        form_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/form?lang=en&type=json&id="

        # inputting drug ids and retrieving results
        for drug_id in filters_ids:

            # creating url
            route_url += (str(drug_id) + "&active=yes")
            form_url += (str(drug_id) + "&active=yes")

            # getting responses
            route_response = requests.request("GET", route_url, headers=headers)
            time.sleep(1)
            form_response = requests.request("GET", form_url, headers=headers)

            # converting to list of dictionaries
            route_data = route_response.json()
            form_data = form_response.json()
            # extracting required information

            form_list.append(form_data[0]['pharmaceutical_form_name'])
            route_list.append(route_data[0]['route_of_administration_name'])
            brand_namelist.append(filters[filters_ids.index(drug_id)].title())
        
        print("Here are the results that we found:")
        ff_d = {'Brand Name':brand_namelist, 'Form': form_list, 'Administration Route': route_list}
        ff = pd.DataFrame(ff_d)
        return(ff)