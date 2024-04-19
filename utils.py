from datetime import datetime
from datetime import timezone


def get_current_datetime() -> datetime:
    """
    Получение текущего времени и даты.

    :return: Объект datetime с текущими временем и датой.
    """
    return datetime.now(timezone.utc)
