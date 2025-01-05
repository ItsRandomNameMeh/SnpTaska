'''
Метод нормальной игры
player_1 = ход первого игрока
player_2 = ход второго игрока
'''
def normal_game(massi):
    player_1 = massi[0][1]
    player_2 = massi[1][1]
    #обработка всех случаев победы первого игрока
    if (player_1 == 'P' and player_2 == 'R') or\
        (player_1 == 'S' and player_2 == 'P') or\
        (player_1 == 'R' and player_2 == 'S'):
        print(massi[0][0],massi[0][1])
    else:#остальные случаи - победа игока 2
        print(massi[1][0],massi[1][1])
'''
Основной вызываемый метод, в нем мы обрабатываем ошибки из ТЗ 
А так же ситуацию "ничья", если все это не выполнилось
Тогда вызываем метод нормальной игры
'''
def rps_game_winner(massi):
    for players in massi: #сначала пытаемся найти исключение
        if int(players[0][6])>2:#Если номер игрока в списке данных об игре больше 2-исключение
            print("Exception: WrongNumberOfPlayersError")
            return
        elif players[1] not in ['P','S','R']:#Исключение 'несуществующего' хода
            print("Exception: NoSuchStrategyError")
            return
    if(massi[0][1] == massi[1][1]):
        print(massi[0][0], massi[0][1])
        return
    normal_game(massi)


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
#=> WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
#=> NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
#=> 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) #
#=> 'player1 P'