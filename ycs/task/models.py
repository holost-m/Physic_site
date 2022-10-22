from django.db import models

# Темы задач по физике
class Topic(models.Model):
    topic = models.CharField(max_length=255, verbose_name="Тема физики")
    def __str__(self):
         return self.topic

    class Meta:
        verbose_name_plural = 'Темы по физике'
        verbose_name = 'Тема'
        ordering = ['id']

# Задачи по физике
class Task(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name="Название задачи", default="Задача")
    text = models.TextField(verbose_name="Текст задачи")
    file = models.FileField(verbose_name="Картинка к задаче")
    variables_and_si = models.CharField(max_length=255, verbose_name="Список переменных и СИ")
    to_find = models.CharField(max_length=255, verbose_name="Найти")
    solving = models.CharField(max_length=255, verbose_name="Решение")
    answer = models.CharField(max_length=255, verbose_name="Ответ")

    def __str__(self):
         return f'Тема "{self.topic}" {self.name}'

    class Meta:
        verbose_name_plural = 'Задачи по физике'
        verbose_name = 'Задача'
        ordering = ['id']
