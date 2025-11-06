from datetime import datetime

def get_date_today_iso_string():
    """
    Returns today's date in ISO 8601 format (YYYY-MM-DD).
    Example: '2025-11-01'
    """
    return datetime.today().date().isoformat()