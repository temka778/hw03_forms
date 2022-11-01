from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='текст',
        help_text='текст публикации')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='группа',
        help_text='выберите группу публикаций')

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        default_related_name= 'posts'

    def __str__(self):
        return self.text[:200]


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title
