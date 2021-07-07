import unittest
import pandas 

from fantasy import get_team_midfielders, get_stats_for_game

class TestFileName(unittest.TestCase):
        
    def test_is_not_None(self):
        self.assertIsNone(get_team_midfielders(), "Test value is not None")

    def test_instance(self):
        self.assertTrue(type(get_stats_for_game()) is pandas.core.frame.DataFrame)
        

if __name__ == '__main__':
    unittest.main()
