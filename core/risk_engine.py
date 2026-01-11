from datetime import date, timedelta
from core.database import history

def check_risk(name: str) -> str:
    rows = history(name, limit=30)

    # Not enough data to judge
    if len(rows) < 3:
        return "NOT ENOUGH DATA"

    today = date.today()
    logged_days = {date.fromisoformat(d) for d, _, _ in rows}

    missed = 0
    for i in range(1, 4):  # check last 3 days (excluding today)
        if (today - timedelta(days=i)) not in logged_days:
            missed += 1

    if missed >= 2:
        return "HIGH RISK"
    elif missed == 1:
        return "MEDIUM RISK"
    return "LOW RISK"
