import unittest
import pandas 

from fantasy import get_team_midfielders, get_stats_for_game

class TestFileName(unittest.TestCase):
        
    def test_is_not_None(self):
        #self.assertIsNone(get_team_midfielders(), "Test value is not None")
        self.assertTrue(type(get_team_midfielders()) is list)
        self.assertTrue(len(get_team_midfielders()) > 0)

    def test_instance(self):
        self.assertTrue(type(get_stats_for_game()) is pandas.core.frame.DataFrame)
        self.assertFalse(get_stats_for_game().empty)
        

if __name__ == '__main__':
    unittest.main()

