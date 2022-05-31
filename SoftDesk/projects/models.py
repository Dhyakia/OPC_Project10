from django.conf import settings
from django.db import models

from users.models import User


class Projects(models.Model):

    WEBSITE = 'WEB'
    ANDROID = 'ADR'
    IOS = 'IOS'

    TYPE_CHOICES = (
        (WEBSITE, "Website"),
        (ANDROID, "Android"),
        (IOS, "IOS"),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributors(models.Model):

    AUTHOR = 'AUT'
    CONTRIBUTORS = 'CTB'

    PERMISSIONS_CHOICES = (
        (AUTHOR, 'Auteur'),
        (CONTRIBUTORS, 'Collaborateur'),
    )

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    permission = models.CharField(max_length=30, choices=PERMISSIONS_CHOICES, default=CONTRIBUTORS)
    role = models.CharField(max_length=30)

    def __str__(self):
        return 'name: {} role: {}'.format(self.user_id.last_name, self.role)


class Issues(models.Model):

    LOW = 'LOW'
    MIDDLE = 'MID'
    HIGH = 'HIG'

    BUG = 'BUG'
    TASK = 'TSK'
    UPGRADE = 'UPG'

    PRIORITY_CHOICES = (
        (LOW,'Basse priorité...'),
        (MIDDLE,'Moyenne priorité.'),
        (HIGH, 'Haute priorité !')
    )

    TAG_CHOICES = (
        (BUG, 'Bug'),
        (TASK, 'Tâche'),
        (UPGRADE, 'Amélioration')
    )

    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=120)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)

    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='rel_author_user')
    assigne_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='rel_assigne_user')
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):

    description = models.CharField(max_length=255)

    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)