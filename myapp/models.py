from django.db import models
import os, uuid
import re

class Document(models.Model):
    # def save(self):
    #     # self.docfile = re.sub("\W+", "", self.name.lower())
    #     self.comment = "Hello World"
    #     super(Document, self).save()

    def path_and_rename(instance, filename):
        upload_to = 'photos'
        ext = filename.split('.')[-1]
        # 1. Get Sub-Dir based on Home member.
        # 2. Get filename based on Person name.
        filename = '{}/{}.{}'.format(instance.home_member, instance.person_name, ext)
        # else:
        #     # set filename as random string
        #     filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    person_name = models.CharField(max_length=30, default='')
    list_home_members = [
        ('usr1', 'User1'),
        ('usr2', 'User2'),
        ('usr3', 'User3'),
    ]
    home_member = models.CharField(max_length=4,choices=list_home_members, default='')
    comment = models.CharField(max_length=200, default='')
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile = models.FileField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    print(f"Hello Priyesh")
