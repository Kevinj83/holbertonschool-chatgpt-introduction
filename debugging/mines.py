def play(self):
    non_mine_cells = self.width * self.height - len(self.mines)
    revealed_cells = 0

    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break
            revealed_cells += 1
            if revealed_cells == non_mine_cells:
                print("Congratulations! You've won the game.")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

