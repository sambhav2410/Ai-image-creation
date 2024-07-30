def parse_crontab(crontab: str):
    try:
        parts = crontab.split()
        minute = parts[0] if len(parts) > 0 else "*"
        hour = parts[1] if len(parts) > 1 else "*"
        dom = parts[2] if len(parts) > 2 else "*"
        dow = parts[3] if len(parts) > 3 else "*"
    except IndexError as e:
        raise ValueError("Invalid crontab", crontab) from e

    return {
        "minute": minute,
        "hour": hour,
        "day_of_month": dom,
        "day_of_week": dow,
    }
