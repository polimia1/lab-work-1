def print_board(board):
    """Вывод игрового поля"""
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  {' | '.join(row)}")
        if i < 2:
            print("  ---+---+---")

def check_win(board, player):
    """Проверка победы"""
    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Проверка, заполнено ли поле"""
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    """Основная функция игры"""
    # Создаем пустое поле
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("=" * 30)
    print("ИГРА КРЕСТИКИ-НОЛИКИ")
    print("=" * 30)
    print("Игрок X ходит первым")
    print()
    
    while True:
        print_board(board)
        print(f"\nХод игрока {current_player}")
        
        # Ввод координат
        try:
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            
            # Проверка корректности ввода
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Ошибка! Введите числа от 0 до 2")
                continue
            
            # Проверка, свободна ли клетка
            if board[row][col] != ' ':
                print("Ошибка! Эта клетка уже занята")
                continue
            
            # Ставим символ
            board[row][col] = current_player
            
            # Проверка победы
            if check_win(board, current_player):
                print_board(board)
                print(f"\n{'=' * 30}")
                print(f"ПОБЕДИЛ ИГРОК {current_player}!")
                print(f"{'=' * 30}")
                break
            
            # Проверка ничьей
            if is_board_full(board):
                print_board(board)
                print(f"\n{'=' * 30}")
                print("НИЧЬЯ!")
                print(f"{'=' * 30}")
                break
            
            # Смена игрока
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Ошибка! Введите целое число")

if __name__ == "__main__":
    play_game()
