from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="photos/", verbose_name="Картинки")

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'


class Person(models.Model):
    person = models.ImageField(upload_to="photos/", verbose_name="Персонажи")

    class Meta:
        verbose_name = 'Персонажи'
        verbose_name_plural = 'Персонажи'


class UserCode(models.Model):
    user = models.TextField(verbose_name="Код пользователя")
    user_code = models.TextField(verbose_name="Код")
    user_image = models.IntegerField(verbose_name="Номер выбранного изображения")

    def __str__(self):
        return self.user_code

    class Meta:
        verbose_name = 'Код учеников'
        verbose_name_plural = 'Код учеников'
