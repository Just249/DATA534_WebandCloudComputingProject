# Group information
Government of Canada Drug Product Database Wrapper API (GC DPD)
Source API : https://hc-sc.api.canada.ca/en/detail?api=dpd

## Description and Motivation of the API

The current GC API provided useful information (e.g. Drug Information, ingredients, pharmaceutical companies, etc) but the current APIs are generic and primitive :
* The calling interface and parameters are mostly done via internal ID.  The current APIs are not very user-friendly with restraining input parameters,  and results are also not readily usable.
* Currently, different drug details are stored and disseminated via several different individual APIs, which require tedious and routine operation to have a consolidated and integrated view of the drug information. 
* The current API returns results in json format which will need further parsing, reorganizing and manipulation before they can be used in the respective programming languages.

Therefore, we have decided to provide user-friendly wrapper functions on a few most frequently used scenarios.  The wrapper target to achieve :

* Our wrapper would greatly simplify the API calling procedure and enhance usability by providing user-friendly api interfaces.  Instead of using original “Internal IDs” (which most users should not be familiar with) as the search parameters, our wrapper adopts drug/ingredient names as the input variables, increasing usage convenience.
* Our wrapper would be implemented in Python, the Python user community could be benefited in terms of efficiency and usability by retrieving the relevant data in a direct python-native and cleaned format for their further analysis.  
* The wrapper will also try to provide a consolidated view which integrates different data sources, saving users’ efforts from performing unnecessary data wrangling and joining.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pandas
pip install requests
pip install json
pip install IPython
pip install unittest
```

## Usage

```python
from api_wrapper.JCingredientVeterinarySpecies import ingredientVeterinarySpecies as ivs
from api_wrapper.jdrugingredient import jdrugingredient as dg
from api_wrapper.Vim_jdrugconsumption import jdrugconsumption as jdg

from IPython import display

#Return data frame containing Veterinary Specie and Drug id that contains ingredient "SULFAMETHAZINE"
display.display(ivs("SULFAMETHAZINE", api_token ))

#Return data frame containing drug name and the ingredient that it contain
display.display(dg("TUINAL PULVULE 303", api_token))

#Return data frame containing Drug Form & Route of Administration that were linked to the drug
display.display(jdg("LIP BALM SPF 15", api_token))

```

## Intended users and outcome:

Description of the intended users: Pharmacists and Doctors.

Description of the outcome: Since different patients have different symptoms, allergic ingredients and preferences, Pharmacists and Doctors can use this API wrapper to quickly search through the database and determine the most suitable drugs that could be prescribed to their patients. Due to the original API suffering from being too generic and primitive, having an API wrapper that could search drug ingredients and intended users by product name instead of product id could result in a faster searching time and reduced error rate.

## License

[MIT](https://choosealicense.com/licenses/mit/)