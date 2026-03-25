# Глобальные счетчики побед
scores = {'X': 0, 'O': 0}
custom_symbols = {'X': 'X', 'O': 'O'}

def customize_symbols():
    """Кастомизация символов игроков"""
    print("\n" + "=" * 40)
    print("НАСТРОЙКА СИМВОЛОВ")
    print("=" * 40)
    
    x_sym = input("Введите символ для первого игрока (Enter для X по умолчанию): ").strip()
    if x_sym:
        custom_symbols['X'] = x_sym
    
    o_sym = input("Введите символ для второго игрока (Enter для O по умолчанию): ").strip()
    if o_sym:
        custom_symbols['O'] = o_sym
    
    print(f"\nСимволы установлены: Игрок 1: {custom_symbols['X']}, Игрок 2: {custom_symbols['O']}")

def print_board(board):
    """Вывод игрового поля"""
    print("\n   0   1   2")
    for i, row in enumerate(board):
        display_row = [custom_symbols[cell] if cell in custom_symbols else cell for cell in row]
        print(f"{i}  {' | '.join(display_row)}")
        if i < 2:
            print("  ---+---+---")

def check_win(board, player):
    """Проверка победы"""
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Проверка, заполнено ли поле"""
    return all(cell != ' ' for row in board for cell in row)

def show_stats():
    """Показ статистики"""
    print("\n" + "=" * 40)
    print("СТАТИСТИКА ИГР")
    print("=" * 40)
    print(f"Игрок {custom_symbols['X']}: {scores['X']} побед")
    print(f"Игрок {custom_symbols['O']}: {scores['O']} побед")
    print(f"Всего сыграно: {scores['X'] + scores['O']} игр")
    print("=" * 40)

def play_game():
    """Основная функция игры"""
    # Выбор режима
    print("\n" + "=" * 40)
    print("ИГРА КРЕСТИКИ-НОЛИКИ v2.0")
    print("=" * 40)
    
    # Спросить о кастомизации
    customize = input("Хотите настроить символы? (y/n): ").lower()
    if customize == 'y':
        customize_symbols()
    
    while True:
        # Создаем пустое поле
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        
        print("\n" + "=" * 40)
        print(f"НОВАЯ ИГРА! Счет: {custom_symbols['X']}:{scores['X']} | {custom_symbols['O']}:{scores['O']}")
        print("=" * 40)
        
        while True:
            print_board(board)
            current_symbol = custom_symbols[current_player]
            print(f"\nХод игрока {current_symbol}")
            
            try:
                row = int(input("Введите номер строки (0-2): "))
                col = int(input("Введите номер столбца (0-2): "))
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Ошибка! Введите числа от 0 до 2")
                    continue
                
                if board[row][col] != ' ':
                    print("Ошибка! Эта клетка уже занята")
                    continue
                
                board[row][col] = current_player
                
                if check_win(board, current_player):
                    print_board(board)
                    print(f"\n{'=' * 40}")
                    print(f"ПОБЕДИЛ ИГРОК {current_symbol}!")
                    print(f"{'=' * 40}")
                    scores[current_player] += 1
                    break
                
                if is_board_full(board):
                    print_board(board)
                    print(f"\n{'=' * 40}")
                    print("НИЧЬЯ!")
                    print(f"{'=' * 40}")
                    break
                
                current_player = 'O' if current_player == 'X' else 'X'
                
            except ValueError:
                print("Ошибка! Введите целое число")
        
        show_stats()
        
        # Спросить о продолжении
        play_again = input("\nСыграть еще? (y/n): ").lower()
        if play_again != 'y':
            print("\nСпасибо за игру!")
            break

if __name__ == "__main__":
    play_game()