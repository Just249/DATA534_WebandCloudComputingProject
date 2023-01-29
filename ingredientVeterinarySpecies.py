import pandas as pd
import requests
from pprint import pprint
import requests
import time

def ingredientVeterinarySpecies(user_input):

    # credentials
    key = "9ec4bb641b31ddeeb9bfd84908c8dbb1"

    url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/activeingredient?lang=en&type=json"
    url += key

    headers = {
      'user-key': key
    }
    
    try:
        response = requests.request("GET", url, headers=headers)
        data = response.json()
    
    except:
        print("The website did not respond, please try again!")
        return

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

    
    
    # print(df.head())
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
    filters_ids = []

    for ingredient in ingredient_name:
        if user_input == ingredient.lower():
            filters.append(ingredient)
            k = ingredient_name.index(ingredient)
            filters_ids.append(drug_codes[k])

    id_with_ingredients = list(set(filters_ids)) # removing duplicates
    # print(id_with_ingredients)


    #############################################################################################################
    # to check ingredents and corresponding drug ids that are filtered  
    # print(drug_codes[k]) #before
    # print(id_with_ingredients) #after
    #############################################################################################################
    
    # data validation
    
    if not filters:
        print("There is no match for that brand name.")
        # return "There is no match for that brand name."
    else:
        
        # route of administration and form of the drug 

        # some empty declarations
        veterinaryspecies_list = []
        ingredients_list = []

        # creating urls
        veterinaryspecies_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/veterinaryspecies?lang=en&type=json"
       
    
#         # inputting drug ids and retrieving results
        for drug_id in id_with_ingredients:

            # creating url
            veterinaryspecies_url += ("&id="+ str(drug_id))

#             # getting responses
            veterinaryspecies_response = requests.request("GET", veterinaryspecies_url, headers=headers)

            print(veterinaryspecies_url)
    
    
    
    
    
#             # converting to list of dictionaries
            veterinaryspecies_data = veterinaryspecies_response.json()

#             # extracting required information

            veterinaryspecies_list.append(veterinaryspecies_data[0]['vet_species_name'])

            ingredients_list.append(filters[filters_ids.index(drug_id)].title())
        
        print("Here are the results that we found:")
        ff_d = {'Ingredient Name':ingredients_list, 'Vet Species': veterinaryspecies_list}
        ff = pd.DataFrame(ff_d)
        return(ff)