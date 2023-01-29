import unittest
import pandas as pd
from ingredientVeterinarySpecies import ingredientVeterinarySpecies as ivs
from ingredientVeterinarySpecies import web_request as wr
from ingredientVeterinarySpecies import check_filter as cf

t1 = ivs("SULFAMETHAZINE")
t2 = ivs("")

class test_ingredientVeterinarySpecies(unittest.TestCase):
    
    def setUp(self):
        print("\n\033[1mThis is the setUp of test_jdrugconsumption.\n\n All good.")
        self.key = "9ec4bb641b31ddeeb9bfd84908c8dbb1"
        self.api1_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1/activeingredient?lang=en&type=json"
        self.wrong_api1_url = "https://dpd-hc-sc-apicast-production.api.canada.ca/v1"
        self.filters = ['SULFAMETHAZINE']
        self.filters_ids = [724]
        self.id_with_ingredients = [724]
        
    def tearDown(self):
        print("\nThis is the tearDown of test_jdrugconsumption")
        
    def test_ingredientVeterinarySpecies(self):
        self.assertEqual(t2, 'There is no match for that brand name.')
        
        self.assertEqual(str(type(t1)),"<class 'pandas.core.frame.DataFrame'>")
        self.assertEqual(wr(self.key, self.wrong_api1_url),"The website did not respond, please try again!")
        
        self.assertEqual(isinstance(cf(['SULFAMETHAZINE'],"9ec4bb641b31ddeeb9bfd84908c8dbb1",self.id_with_ingredients,self.filters_ids),pd.DataFrame), True)
        self.assertEqual(cf([],"9ec4bb641b31ddeeb9bfd84908c8dbb1",self.id_with_ingredients,self.filters_ids), "There is no match for that brand name.")
        
        self.assertEqual(isinstance(wr(self.key, self.api1_url), list), True)
        self.assertEqual(isinstance(wr(self.key, self.wrong_api1_url), list), False)
        # self.assertEqual(str(type(t2)),"<class 'NoneType'>")
        
        self.assertEqual(isinstance(t1, pd.DataFrame), True)
        self.assertEqual(isinstance(t2, pd.DataFrame), False)
        
        self.assertAlmostEqual(t1.iloc[0,0], "Sulfamethazine")
        self.assertAlmostEqual(t1.iloc[0,1], "Cattle")
        
        self.assertAlmostEqual(str(ivs("")), "There is no match for that brand name.")
        
        
unittest.main(argv=[''], verbosity=2, exit=False)