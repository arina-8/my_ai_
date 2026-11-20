from gigachat.models import (
        ChatMessage
)
from prompts import SYSTEM_PROMPT

dialog = [
    {"role": "system", "content": "Привет! Я помощник."},
    {"role": "user", "content": "Что ты умеешь?"},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "составь данный план по теме Поиск книг"},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "Задание 3 Составьте план диалога..."},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "Расскажи подробно, что это? ..."},
    {"role": "assistant", "content": "..."}
]

print("Длина списка:", len(dialog))

print("Роли:")
for message in dialog:
    print(message["role"])

    number_of_user_questions = 7      
if len(dialog) == number_of_user_questions:
    print(f"Количество элементов ({len(dialog)}) равно количеству вопросов пользователя.")
else:
    print(f"Количество элементов ({len(dialog)}) не равно количеству вопросов пользователя.")
