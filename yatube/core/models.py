from django.db import models


class CreatedModel(models.Model):
    """Модель добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
