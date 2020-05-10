TOKEN = ''
GROUPE_ID = ''


INTENTS = [
    {
        'name': 'Дата проведения',
        'tokens': ('когда', 'сколько', 'даты', 'дату'),
        'scenario': None,
        'answer': 'Конференция проводится 15 апреля, регистрация начнется в 10 утра'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро'),
        'scenario': None,
        'answer': 'Конференция пройдет в павильоне 18Г в Экспоцентре'
    },
    {
        'name': 'Регистрация',
        'tokens': ('регистр', 'добавь', 'зарегистр'),
        'scenario': 'registration',
        'answer': None
    }
]

SCENARIOS = {
    'registration':{
        'first_step': 'step1',
        'steps':{
            'step1':{
                'text': 'Чтобы зарегистрироваться введите Ваше имя.',
                'failure_text': 'Имя должно состоять из 3-40 букв и дефиса',
                'handler': 'handle_name',
                'next_step': 'step2'
            },
            'step2':{
                'text': 'Введите email',
                'failure_text': 'Введенный адрес содержит ошибку',
                'handler': 'handle_mail',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Спасибо за регистрацию! {name} Мы отправили билет на {email}',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
   }
}

DEFAULT_ANSWER = 'Не знаю как на это отвечать.' \
    ' Могу сказать когда и где пройдет конференция, а также зарегистрировать Вас!'

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='',
    host='localhost',
    database='vk_chat_bot'
)
