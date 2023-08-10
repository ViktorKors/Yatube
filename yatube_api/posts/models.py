from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Group(models.Model):
    """Модель для групп."""

    title = models.CharField(max_length=200, verbose_name=_("Groups title"))
    slug = models.SlugField(unique=True, verbose_name=_("Groups slug"))
    description = models.TextField(verbose_name=_("Groups description"))

    def __str__(self):
        """Для показа заголовока группы"""
        return self.title

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField(
        verbose_name=_("Posts text"),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Publication date"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Posts author"),
        related_name="posts",
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name=_("Posts image"),
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name=_("Group"),
    )

    def __str__(self):
        """Для показа текста поста"""
        return self.text

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Comment(models.Model):
    """Модель для комментариев."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Comments author"),
        related_name="comments",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_("Comments post"),
        related_name="comments",
    )
    text = models.TextField(verbose_name=_("Comments text"))
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name=_("Comment creation time"),
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Follow(models.Model):
    """Модель для подписчиков и подписок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Followers"),
        related_name="followers",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Subscription"),
        related_name="following",
    )

    class Meta:
        unique_together = [["user", "following"]]
        verbose_name = _("Follow")
        verbose_name_plural = _("Follows")
