from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_by_dealer_bust_and_user_not_bust(self, input_mock, randint_mock):
        '''
        Dealer receives cards that end up to bust.
        The user wins by having a hand of less than or equal to 21.
        '''
        output = run_test([4, 6, 9], ['y', 'n'], [1, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_by_higher_hand(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([4, 6, 9], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_by_user_bust_and_dealer_not_bust(self, input_mock, randint_mock):
        '''
        User receives cards that end up to bust.
        The dealer wins.
        '''
        output = run_test([1, 1], ['n'], [1, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_by_higher_hand(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([3, 5, 10], ['y', 'n'], [4, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "Dealer has 10.\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_by_same_cards_without_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that do not bust and are equal.
        Push.
        '''
        output = run_test([4, 6, 9], ['y', 'n'], [4, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "Dealer has 10.\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_by_same_cards_that_both_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive same cards that bust.
        Dealer wins.
        '''
        output = run_test([1,1], ['n'], [1,1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_by_same_cards_that_blackjack(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that blackjack and are equal.
        Push.
        '''
        output = run_test([4, 6, 1], ['y'], [4, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "Dealer has 10.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_by_blackjack_and_dealer_less_than_21(self, input_mock, randint_mock):
        '''
        User receive cards that blackjack but dealer has less than 21 cards.
        User wins.
        '''
        output = run_test([4, 6, 1], ['y'], [4, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "Dealer has 10.\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_by_blackjack_and_user_less_than_21(self, input_mock, randint_mock):
        '''
        Dealer receive cards that blackjack but user has less than 21 cards.
        User wins.
        '''
        output = run_test([4, 6, 9], ['y', 'n'], [4, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "Dealer has 10.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_by_blackjack_and_dealer_bust(self, input_mock, randint_mock):
        '''
        User receive cards that blackjack but dealer busts.
        User wins.
        '''
        output = run_test([4, 6, 1], ['y'], [1,1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
