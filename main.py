"""
Tutorials:

Game
Part 1: https://www.youtube.com/watch?v=vnd3RfeG3NM&list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3&index=1&t=0s
Part 2: https://www.youtube.com/watch?v=LSYj8GZMjWY&list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3&index=2
Part 3: https://www.youtube.com/watch?v=_kOXGzkbnps&list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3&index=3

AI:
Part 1: https://www.youtube.com/watch?v=RjdrFHEgV2o&list=PLwI0K_u0moiUOE1oozIA3ynZ1kPiKL0vM&index=10&t=44s
part 2: https://www.youtube.com/watch?v=mYbrH1Cl3nw

"""
import pygame
from checkers_again.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers_again.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col

def main():
	run = True
	clock = pygame.time.Clock()
	game = Game(WIN)

	while run:
		clock.tick(FPS)

		if game.turn == WHITE:
			value, new_board = minimax(game.get_board(), 3, WHITE, game)
			game.ai_move(new_board)

		if game.winner() != None:
			print(game.winner(), "won")
			run = False
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = get_row_col_from_mouse(pos)

				game.select(row, col)

		game.update()

	pygame.quit()

if __name__ == "__main__":
	main()