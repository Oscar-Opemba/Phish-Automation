def risk_score(events: dict) -> float:
    clicks = events.get("clicks", 0)
    reported = events.get("reported", 0)
    if clicks + reported == 0:
        return 0.0
    return round(clicks / (clicks + reported), 2)
