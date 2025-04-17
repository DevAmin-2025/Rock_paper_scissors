import random

from utils import print_info, print_lose, print_win, print_yellow


class RockPaperScissors:
	"""
	Main class for Rock Paper Scissors game.
	"""
	def __init__(self, total_round=5):
		self.options = ['Rock', 'Paper', 'Scissors']
		self.total_round = total_round

	def generate_random_choice(self) -> str:
		"""
		Generate a random word from the list of options.

		:return: The chosen word from self.options.
		"""
		return random.choice(self.options)

	def get_user_choice(self) -> str:
		"""
        Prompt the user for an input.

        :return: User input.
        """
		return input('Enter your choice: (R -> Rock | P -> Paper | S -> Scissors) or q to exit: ')

	def validate_user_choice(self, user_choice: str) -> bool:
		"""
        Get user initial input and determine weather it is valid or not.

        :param user_choice: User initial input.
        :return: True if input is valid, False otherwise.
        """
		# 'r' -> Rock, 'p' -> Paper, 's' -> Scissors
		if not user_choice in ['r', 'p', 's']:
			return False
		return True

	def equate_user_choice(self, user_choice: str) -> str:
		"""
        Assign the user validated input to the proper option.

        :param user_choice: User validated input.
        :return: One of the game options according to the user input.
        """
		if user_choice == 'r':
			return 'Rock'
		elif user_choice == 'p':
			return 'Paper'
		else:
			return 'Scissors'

	def play_round(self, user_choice: str, computer_choice: str) -> str:
		"""
        Determine the winner.

        :param user_word: Input user choice.
        :param computer_choice: Input computer choice.
		:return: Tie if the result is a tie, win if user wins the round, lose otherwise.
        """
		if user_choice == computer_choice:
			return 'tie'
		# All scenarios which user can win
		win_combination = [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]
		for win_comb in win_combination:
			if user_choice == win_comb[0] and computer_choice == win_comb[1]:
				return 'win'
		return 'lose'

	def main(self):
		"""
		Run the whole game and put together other methods.
		"""
		user_count = 0
		computer_count = 0
		rounds = 0
		remaining_rounds = self.total_round

		while True:
			computer_choice = self.generate_random_choice()
			user_choice = self.get_user_choice()
			user_choice = user_choice.lower()

			if user_choice == 'q':
				print_info(' Goodbye! ')
				break
			elif not self.validate_user_choice(user_choice):
				print_info(' Invalid input. Please try again. ')
				continue

			user_choice = self.equate_user_choice(user_choice)
			round_result = self.play_round(user_choice, computer_choice)
			# Adding one to the total rounds of the game if the result of the round is not tie
			if not round_result == 'tie':
				rounds += 1

			if rounds != self.total_round:
				print_info(F' You choose: {user_choice} ')
				print_info(F' Computer choose: {computer_choice} ')
				print()

				if round_result == 'tie':
					print_info(f" That's a tie. Play again! ")
				elif round_result == 'win':
					print_win(' You win! ')
					user_count += 1
					remaining_rounds -= 1
				else:
					print_lose(f' You lost! ')
					computer_count += 1
					remaining_rounds -= 1

				print()
				print_info('Result:')
				print_yellow(F' You: {user_count} ')
				print_yellow(F' Computer: {computer_count} ')
				print_yellow(F' Remaining rounds: {remaining_rounds} ')
			else:
				if round_result == 'win':
					user_count += 1
				else:
					computer_count += 1

				if user_count > computer_count:
					print_win(' Congratulations! You beat the computer. ')
				else:
					print_lose(' Game over! ')

				print()
				print_info('Final result:')
				print_yellow(F' You: {user_count} ')
				print_yellow(F' Computer: {computer_count} ')
				break


if __name__ == '__main__':
	start = RockPaperScissors()
	start.main()
