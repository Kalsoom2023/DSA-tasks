import random

class Crossword:
    def __init__(self, grid_size, words):
        """
        Initialize the crossword grid and word list.
        :param grid_size: Size of the square grid (e.g., 10 for 10x10).
        :param words: List of words to place in the crossword.
        """
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.words = words

    def can_place_word(self, word, row, col, direction):
        """
        Check if a word can be placed on the grid.
        :param word: Word to place.
        :param row: Starting row.
        :param col: Starting column.
        :param direction: Direction to place the word ('H' for horizontal, 'V' for vertical).
        """
        if direction == 'H':
            if col + len(word) > self.grid_size:
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] not in (' ', word[i]):
                    return False
        elif direction == 'V':
            if row + len(word) > self.grid_size:
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] not in (' ', word[i]):
                    return False
        return True

    def place_word(self, word, row, col, direction):
        """
        Place a word on the grid.
        :param word: Word to place.
        :param row: Starting row.
        :param col: Starting column.
        :param direction: Direction to place the word ('H' or 'V').
        """
        if direction == 'H':
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]
        elif direction == 'V':
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]

    def generate_puzzle(self):
        """
        Generate the crossword puzzle using backtracking.
        """
        for word in self.words:
            placed = False
            for _ in range(100):  # Attempt 100 times to place the word
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)
                direction = random.choice(['H', 'V'])
                if self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True
                    break
            if not placed:
                print(f"Could not place the word: {word}")

    def display_grid(self):
        """
        Print the crossword grid.
        """
        for row in self.grid:
            print(' '.join(row))

# Example usage
if __name__ == "__main__":
    word_list = ["PYTHON", "JAVA", "ALGORITHM", "BACKTRACK", "DEBUG", "CODE"]
    crossword = Crossword(grid_size=10, words=word_list)
    crossword.generate_puzzle()
    print("Generated Crossword Puzzle:")
    crossword.display_grid()
