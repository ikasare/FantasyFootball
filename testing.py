import unittest
import pandas 

from fantasy import get_team_midfielders, get_stats_for_game

class TestFileName(unittest.TestCase):
        
    def test_get_team_midfielders(self):
        # Test is our function returns a list of midfielders 
        self.assertTrue(type(get_team_midfielders()) is list)
        #Make sure that the list is not empty and has names and data of midfielder
        self.assertTrue(len(get_team_midfielders()) > 0)

    def test_get_stats_for_game(self):
        #Make sure the function returns a datframe with pandas
        self.assertTrue(type(get_stats_for_game()) is pandas.core.frame.DataFrame)
        #Make sure there is data in our dataFrame
        self.assertFalse(get_stats_for_game().empty)
        
        
        

if __name__ == '__main__':
    unittest.main()

