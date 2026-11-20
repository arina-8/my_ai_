import os
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import (
    ChatCompletionRequest, ChatMessage, ChatModelOptions,
)
from prompts import SYSTEM_PROMPT

load_dotenv()

model_options = ChatModelOptions(
    temperature=0.2,
    max_tokens=400,
    top_p=0.8,
)

question = input("Какую книгу вы ищете? ").strip()
genre = input("Какой жанр вам интересен? ").strip()
mood = input("Под какое настроение ищем книгу? ").strip()
details = input("Какие детали сюжета вам интересны? ").strip()
format = input("Какой формат ответа?").strip()

if genre == "" or mood == "":
    print("Укажите жанр и настроение.")
else:
    user_prompt = (
        f"Подбери книгу по запросу: {question}.\n"
        f"Жанр: {genre}.\n"
        f"Настроение: {mood}.\n"
        f"Детали сюжета: {details}.\n"
        f"Выбор формата: {format}."
    )

    request = ChatCompletionRequest(
        messages=[
            ChatMessage(role="system", content=SYSTEM_PROMPT),
            ChatMessage(role="user", content=user_prompt),
        ],
        model_options=model_options
    )

    try:
        with GigaChat(
            credentials=os.getenv("GIGACHAT_CREDENTIALS"),
            scope=os.getenv("GIGACHAT_SCOPE"),
            model="GigaChat-2",
            ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
            timeout=60,
        ) as client:
            response = client.chat.create(request)
            answer = response.messages[0].content[0].text
            print("Ответ:")
            print(answer)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

messages = [{"role": "system", "content": "Привет! Я помощник."}]

from gigachat import GigaChat
from prompts import SYSTEM_PROMPT

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

with GigaChat() as client:
    while True:
        user_input = input("Введите сообщение (или 'выход' для завершения): ")
        cleaned_input = user_input.strip()

        if cleaned_input.lower() == "выход":
            print("Цикл завершён по команде пользователя.")
            break

        if not cleaned_input:
            print("Введена пустая строка. Пожалуйста, введите текст.")
            continue

        messages.append({"role": "user", "content": cleaned_input})

        response = client.chat.completions.create(
            model="GigaChat",
            messages=messages
        )
        assistant_reply = response.choices[0].message.content

        messages.append({"role": "assistant", "content": assistant_reply})

        print(f"Ответ помощника: {assistant_reply}")