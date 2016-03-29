from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=25,
        unique=True,
    )

    def __str__(self):
        return "#{tag_name}".format(
            tag_name=self.name
        )
