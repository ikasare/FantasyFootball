import unittest
import pandas 

from fantasy import get_team_midfielders, get_stats_for_game


class TestFileName(unittest.TestCase):

    def test_get_team_midfielders(self):
        test = get_team_midfielders()
        # Test is our function returns a list of midfielders 
        self.assertTrue(type(test) is list)
        # Make sure that the list is not empty and has names and data of midfielder
        self.assertTrue(len(test) > 0)

    def test_get_stats_for_game(self):
        test = get_stats_for_game()
        # Make sure the function returns a datframe with pandas
        self.assertTrue(type(test) is pandas.core.frame.DataFrame)
        # Make sure there is data in our dataFrame
        self.assertFalse(test.empty)
        

if __name__ == '__main__':
    unittest.main()
