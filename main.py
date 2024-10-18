from rich.console import Console
from rich.table import Table

# Инициализация консоли Rich
console = Console()

# Обозначения фигур
PIECES = {
    "R": "♜",  # Ладья (Rook)
    "N": "♞",  # Конь (Knight)
    "B": "♝",  # Слон (Bishop)
    "Q": "♛",  # Ферзь (Queen)
    "K": "♚",  # Король (King)
    "P": "♟︎",  # Пешка (Pawn)
}

# Стартовая позиция доски
START_POSITION = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]


# Вывод доски с помощью Rich
def print_board(board):
    table = Table(show_header=False, header_style="bold magenta")
    table.add_column("A")
    table.add_column("B")
    table.add_column("C")
    table.add_column("D")
    table.add_column("E")
    table.add_column("F")
    table.add_column("G")
    table.add_column("H")

    for row in board:
        table.add_row(*[PIECES.get(cell, " ") for cell in row])

    console.print(table)


# Функция для перемещения фигур
def move_piece(board, from_pos, to_pos):
    try:
        # Преобразуем позицию из формата A1 в координаты массива
        from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('A')
        to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('A')

        # Выполняем перемещение фигуры
        piece = board[from_row][from_col]

        # Если клетка пуста, сообщаем об ошибке
        if piece == " ":
            console.print("[bold red]На этой клетке нет фигуры![/bold red]")
            return

        board[from_row][from_col] = " "
        board[to_row][to_col] = piece

    except (IndexError, ValueError):
        console.print("[bold red]Неверный формат хода! Используйте, например, E2 E4.[/bold red]")


# Основной цикл игры
def play_game():
    board = [row[:] for row in START_POSITION]  # Копируем стартовую позицию
    print_board(board)

    while True:
        move = input("Введите ход (например, E2 E4): ").strip().upper()
        if len(move) == 5 and move[2] == ' ':
            from_pos, to_pos = move.split()
            move_piece(board, from_pos, to_pos)
            print_board(board)
        else:
            console.print("[bold red]Неверный ввод![/bold red] Попробуйте снова.")


if __name__ == "__main__":
    play_game()
