from tkinter import CASCADE
from django.db import models

from users.models import User

# TODO: CONTRIBUTORS: setup les permissions
# TODO: Certains fields demandes des choix
# TODO: max_lenght aux charfields

class Contributors(models.Model):

    user_id = models.IntegerField()
    project_id = models.IntegerField()
    role = models.CharField()

    def __str__(self):
        return "%s %s" % (self.user_id, self.project_id)


class Projects(models.Model):

    title = models.CharField()
    description = models.CharField()
    type = models.CharField()
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Issues(models.Model):

    title = models.CharField()
    desc = models.CharField()
    tag = models.CharField()
    priority = models.CharField()
    project_id = models.IntegerField()
    status = models.CharField()
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):

    description = models.CharField(max_length=120)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

