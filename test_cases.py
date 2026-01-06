import unittest
from Ten_Pin_Bowling_score import validate_input, calculate_score

class TestBowlingScore(unittest.TestCase):

    def test_all_open_frames(self):
        game = "9-9-9-9-9-9-9-9-9-9-"
        scores = validate_input(game)
        self.assertIsNotNone(scores)
        self.assertEqual(calculate_score(scores), 90)

    def test_all_strikes(self):
        game = "XXXXXXXXXXXX"
        scores = validate_input(game)
        self.assertIsNotNone(scores)
        self.assertEqual(calculate_score(scores), 300)

    def test_all_spares(self):
        game = "5/5/5/5/5/5/5/5/5/5/5"
        scores = validate_input(game)
        self.assertIsNotNone(scores)
        self.assertEqual(calculate_score(scores), 150)

    def test_mixed_game(self):
        game = "72X221/1212121/1212"
        scores = validate_input(game)
        self.assertIsNotNone(scores)
        self.assertEqual(calculate_score(scores), 64)

    def test_invalid_input(self):
        game = "73X2212121212121212"
        scores = validate_input(game)
        self.assertIsNone(scores)
        
    def test_spare_without_first_roll(self):
        game = "/9-----------------"
        scores = validate_input(game)
        self.assertIsNone(scores)

    def test_too_many_rolls(self):
        game = "9-9-9-9-9-9-9-9-9-9-9"
        scores = validate_input(game)
        self.assertIsNone(scores)


if __name__ == "__main__":
    unittest.main()