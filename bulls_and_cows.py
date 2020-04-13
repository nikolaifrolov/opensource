import bulls_and_cows_engine


print('Игра быки и коровы')
answers = bulls_and_cows_engine.get_all_answes()
player = bulls_and_cows_engine.input_number()
enemy = bulls_and_cows_engine.get_one_answer(answers)

while True:
    print('=' * 15, 'Ход игрока', '=' * 15)
    print('Угадайте число компьютера')
    number = bulls_and_cows_engine.input_number()
    bulls, cows = bulls_and_cows_engine.check(number, enemy)
    print('Быки:', bulls, 'Коровы:', cows)
    if bulls == 4:
        print('Вы победили')
        print('Компьютер загадал число: ', enemy)
        break

    print('=' * 15, 'Ход компьютера', '=' * 15)
    enemy_try = bulls_and_cows_engine.get_one_answer(answers)
    print('Компьютер считает, что вы загадали число: ', enemy_try)
    bulls, cows = bulls_and_cows_engine.check(enemy_try, player)
    print('Быки:', bulls, 'Коровы:', cows)
    if bulls == 4:
        print('Победил компьютер')
        print('Компьютер загадал число: ', enemy)
        break
    else:
        answers = bulls_and_cows_engine.del_bad_answer(answers, enemy_try, bulls, cows)
