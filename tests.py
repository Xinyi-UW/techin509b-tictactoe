import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_get_winner_1(self):
        board = [
            ['O', None, 'X'],
            [None, 'O', None],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

if __name__ == '__main__':
    unittest.main()
