# Определяем исключения
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

# Функция для определения победителя в игре "Камень-Ножницы-Бумага"
def rps_game_winner(game):
    # Проверка количества игроков
    if len(game) != 2:
        raise WrongNumberOfPlayersError

    # Проверка корректности ходов
    valid_moves = {'R', 'P', 'S'}
    for player, move in game:
        if move not in valid_moves:
            raise NoSuchStrategyError

    # Извлечение информации о ходах игроков
    player1, move1 = game[0]
    player2, move2 = game[1]

    # Логика игры
    if move1 == move2:
        return f"{player1} {move1}"
    elif (move1 == 'R' and move2 == 'S') or \
            (move1 == 'S' and move2 == 'P') or \
            (move1 == 'P' and move2 == 'R'):
        return f"{player1} {move1}"
    else:
        return f"{player2} {move2}"


# Тесты
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  # => WrongNumberOfPlayersError
except Exception as e:
    print(type(e).__name__)
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  # => NoSuchStrategyError
except Exception as e:
    print(type(e).__name__)

print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # => 'player1 P'