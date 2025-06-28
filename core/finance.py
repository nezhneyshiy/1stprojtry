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
    mapping = {
        "кофе": "еда",
        "обед": "еда",
        "такси": "транспорт",
        "метро": "транспорт",
        "транспорт": "транспорт",
    }
    return mapping.get(category.lower(), "другое")
