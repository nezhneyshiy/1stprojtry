# Логика анализа эмоций и настроения
# Функции:
# - analyze_mood
# - save_mood_to_db
# - detect_keywords
# core/mood.py

def analyze_mood(text: str) -> str:
    """
    Заглушка: возвращает 'позитив', 'нейтрально' или 'негатив'.
    Позже прикрутим настоящую модель.
    """
    bad_words = ["устал", "плохо", "тяжело"]
    good_words = ["рад", "хорошо", "доволен"]

    text = text.lower()
    if any(word in text for word in bad_words):
        return "негатив"
    elif any(word in text for word in good_words):
        return "позитив"
    else:
        return "нейтрально"

def save_mood_to_db(user_id: int, mood: str, text: str):
    """
    Заглушка — пока без базы.
    """
    print(f"[MOOD] User: {user_id}, Mood: {mood}, Text: {text}")
