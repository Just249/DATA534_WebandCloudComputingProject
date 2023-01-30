import pandas as pd
import requests
from pprint import pprint
from IPython import display
import requests
import time
# from helper_functions import web_request as wr
# from helper_functions import check_filter as cf

# key = "9ec4bb641b31ddeeb9bfd84908c8dbb1"
api1_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/activeingredient?lang=en&type=json"


def web_request(key,url):
    if url == api1_url:
        url += key
    headers = {'user-key': key}
    try:
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        return data
    except:
        return "The website did not respond, please try again!"
    
    
def check_filter(filters,key,id_with_ingredients,filters_ids):
    headers = {'user-key': key}
    if not filters:
        return "There is no match for that brand name."
    else:
        veterinaryspecies_list = []
        ingredients_list = []
        veterinaryspecies_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/veterinaryspecies?lang=en&type=json"
        # inputting drug ids and retrieving results
        for drug_id in id_with_ingredients:
            veterinaryspecies_url += ("&id="+ str(drug_id))
            # getting responses
            veterinaryspecies_data = web_request(key,url = veterinaryspecies_url)
            veterinaryspecies_list.append(veterinaryspecies_data[0]['vet_species_name'])
            ingredients_list.append(filters[filters_ids.index(drug_id)].title()) 
    print("Here are the results that we found:")
    ff_d = {'Ingredient Name':ingredients_list, 'Vet Species': veterinaryspecies_list}
    ff = pd.DataFrame(ff_d)
    
    return(ff)

def ingredientVeterinarySpecies(user_input,key):
    data = web_request(key,api1_url)
    
    ingredient_name = []
    drug_codes = []
    code_ingredient = []
    vet_species_name = []
    n = len(data)
    
    for i in range(n):
        drug_codes.append(data[i]['drug_code'])
        ingredient_name.append(data[i]['ingredient_name'])
        code_ingredient.append((data[i]['drug_code'],data[i]['ingredient_name']))

    df = pd.DataFrame({'drug_codes': drug_codes, 'ingredient_name': ingredient_name, 'code_ingredient': code_ingredient})
    
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
    filters_ids = []

    for ingredient in ingredient_name:
        if user_input == ingredient.lower():
            filters.append(ingredient)
            k = ingredient_name.index(ingredient)
            filters_ids.append(drug_codes[k])

    id_with_ingredients = list(set(filters_ids)) # removing duplicates

    #############################################################################################################
    # to check ingredents and corresponding drug ids that are filtered  
    # print(drug_codes[k]) #before
    # print(id_with_ingredients) #after
    #############################################################################################################
    result = check_filter(filters,key,id_with_ingredients,filters_ids)
    
    return result