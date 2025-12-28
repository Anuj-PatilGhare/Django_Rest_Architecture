from django.db import models


class Studnets(models.Model):
    student_id = models.CharField(max_length=10)
    studnet_name = models.CharField(max_length=50)
    student_class =models.CharField(max_length=20)

    def __str__(self):
        return self.studnet_name
