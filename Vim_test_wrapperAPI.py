import pandas as pd
import unittest
from jdrugconsumption import jdrugconsumption as jdg

t1 = jdg("LIP BALM SPF 15", "14ec6574be9f7ef563bce7b554798152")
t2 = jdg("", "14ec6574be9f7ef563bce7b554798152")

class test_jdrugconsumption(unittest.TestCase):
    
    def setUp(self):
        print("\n\033[1mThis is the setUp of test_jdrugconsumption.\n\n All good.")
    
    def tearDown(self):
        print("\nThis is the tearDown of test_jdrugconsumption")
        
    def test_DrugConsumption(self):
        self.assertEqual(str(type(t1)),"<class 'pandas.core.frame.DataFrame'>")
        self.assertEqual(isinstance(t1, pd.DataFrame), 1)
        self.assertAlmostEqual(t1.iloc[0,0], "Lip Balm Spf 15")
        self.assertNotEqual(isinstance(t1, pd.DataFrame), 0)
        self.assertAlmostEqual(t1.iloc[0,1], "Ointment")
        self.assertEqual(str(type(t2["Brand Name"])),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(str(type(t2)),"<class 'pandas.core.series.Series'>")
        self.assertNotEqual(t2.empty, 0)
  
            
unittest.main(argv=[''], verbosity=2, exit=False)