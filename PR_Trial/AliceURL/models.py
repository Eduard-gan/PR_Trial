from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Основая таблица в которой хранятся сопоставления ссылок и их авторы
class ShortURL(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    target_link = models.URLField(validators=[RegexValidator(regex=r'^https://.*')]) # Валидатор протокола.

    def __str__(self):
        return '{0} ({1})'.format(self.code, self.target_link)


# Дополнительная таблица в которой фиксируются время и IP-адрес с которого был переход по ссылке.
class URLPass(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    code = models.ForeignKey(ShortURL, to_field='code', on_delete=models.CASCADE)
    visitor = models.GenericIPAddressField()

    def __str__(self):
        return '{0} ({1})'.format(self.code.code, self.visitor)
