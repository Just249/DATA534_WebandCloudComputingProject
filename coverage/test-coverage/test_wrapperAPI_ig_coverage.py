import pandas as pd
import unittest
from jdrugingredient import jdrugingredient as jdg

t1 = jdg("LIP BALM SPF 15")  # Valid drug, two ingredient
t2 = jdg("") # empty drug name input
t3 = jdg("No such medicine") # invalid drug name
t4 = jdg("ISOPTO CARBACHOL 3%") # valid drug, one ingredient

class test_jdrugingredient(unittest.TestCase):
    
    def setUp(self):
        print("\n\033[1mThis is the setUp of test_jdrugingredient.\n\n All good.")
    
    def tearDown(self):
        print("\nThis is the tearDown of test_jdrugingredient")
        
    def test_DrugIngredient(self):
        # For t1
        self.assertEqual(str(type(t1)),"<class 'pandas.core.frame.DataFrame'>")
        self.assertEqual(isinstance(t1, pd.DataFrame), 1)
        self.assertEqual(len(t1), 2) # should return 2 ingredient df rows
        self.assertAlmostEqual(t1.iloc[0,0], "Lip Balm Spf 15") # ensure the name is correct
        self.assertAlmostEqual(t1.iloc[1,0], "Lip Balm Spf 15")
        self.assertAlmostEqual(t1.iloc[0,1], "OCTINOXATE") # verify the ingredient name 1
        self.assertAlmostEqual(t1.iloc[1,1], "OXYBENZONE") # verify the ingredient name 2

        # For t2
        self.assertEqual(str(type(t2["Brand Name"])),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(str(type(t2)),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(t2.empty, 0)
  
        # For t3
        self.assertEqual(str(type(t3["Brand Name"])),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(str(type(t3)),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(t3.empty, 0)
    
        # For t4
        self.assertEqual(str(type(t4)),"<class 'pandas.core.frame.DataFrame'>")
        self.assertEqual(isinstance(t4, pd.DataFrame), 1)
        self.assertEqual(len(t4), 1) # should return 1 ingredient df rows
        self.assertAlmostEqual(t4.iloc[0,0], "Isopto Carbachol 3%") # ensure the name is correct
        self.assertAlmostEqual(t4.iloc[0,1], "CARBACHOL") # verify the ingredient name        

            
unittest.main(argv=[''], verbosity=2, exit=False)