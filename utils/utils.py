from lexicon import lexicon
from random import choice

# инициализируем словарик, где будут данные юзеров, ключами
# будут айди юзеров, а значением словарь с данными по играм
users: dict = {}


# функция для проверки, есть ли юзер в нашей базе, если нет -
# то он инициализируется
def chek_user(user_id: str) -> None:
    if user_id not in users:
        users[user_id] = {
            'total_games': 0,
            'wins': 0,
            'loses': 0,
            'draws': 0
            }


# функция возвращающая строку со статистикой игрока
def stat_func(user_id: str) -> str:
    stat_string = (
        f"Всего игр  🎲:  {users[user_id]['total_games']}\n"
        f"Побед  🍾:  {users[user_id]['wins']}\n"
        f"Поражений  😢:  {users[user_id]['loses']}\n"
        f"Ничьих  🤨:  {users[user_id]['draws']}")
    return stat_string


# функция сброса статистики игрока
def reset_stat(user_id: str) -> str:
    users[user_id]['total_games'] = 0
    users[user_id]['wins'] = 0
    users[user_id]['loses'] = 0
    users[user_id]['draws'] = 0
    return choice(lexicon.LEXICON_RU['reset_stat_phrases'])


# функция генерации ответа на выбор инструмента игроком + обновление
# его статистики по играм
def generate_answer(user_answer: str, bot_answer: str, user_id: str) -> str:
    users[user_id]['total_games'] += 1
    if (user_answer, bot_answer) in lexicon.win_combinations:
        rand_ans = choice(lexicon.win_combinations[(user_answer, bot_answer)])
        users[user_id]['wins'] += 1
        return f'{choice(lexicon.LEXICON_RU['bot_choice'])} {bot_answer}. {rand_ans}'
    elif (user_answer, bot_answer) in lexicon.lose_combianations:
        rand_ans = choice(lexicon.lose_combianations[(user_answer, bot_answer)])
        users[user_id]['loses'] += 1
        return f'{choice(lexicon.LEXICON_RU['bot_choice'])} {bot_answer}. {rand_ans}'
    else:
        users[user_id]['draws'] += 1
        return f'{choice(lexicon.LEXICON_RU['bot_choice'])} {bot_answer}. {choice(lexicon.LEXICON_RU['draw_phrases'])}'
