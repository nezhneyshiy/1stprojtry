# Логика учёта расходов
# Функции:
# - parse_expense_message
# - categorize_expense
# - save_expense_to_db
# core/finance.py

def parse_expense_message(text: str):
    """
    Пример: 'кофе 250' → ('кофе', 250)
    """
    parts = text.strip().split()
    if len(parts) < 2:
        return None, None
    try:
        amount = float(parts[-1])
        category = " ".join(parts[:-1])
        return category, amount
    except ValueError:
        return None, None

def categorize_expense(category: str):
    """
    Простейшее правило. Потом можно прикрутить NLP.
    """
    mapping = {
        "кофе": "еда",
        "метро": "транспорт",
        "такси": "транспорт",
    }
    return mapping.get(category.lower(), "другое")

def save_expense_to_db(user_id: int, category: str, amount: float):
    """
    Заглушка — пока без реальной базы.
    """
    print(f"[SAVE] User: {user_id}, Category: {category}, Amount: {amount}")
