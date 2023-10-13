from django.db import models


class Ip(models.Model):
    fio = models.CharField(max_length=100)
    cabinet = models.IntegerField()
    department = models.IntegerField()
    user_name = models.CharField(max_length=30)
    pc_name = models.CharField(max_length=30)
    ip = models.GenericIPAddressField()

    def save(self, *args, **kwargs):
        if not self.pk:
            request = kwargs.pop('request', None)
            if request:
                self.user_name = request.user.username
                self.pc_name = request.pc_name
                self.ip = request.user_ip
        super().save(*args, **kwargs)
