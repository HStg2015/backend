from django.db import models

class RefugeeCamp(models.Model):
    # Location
    city = models.CharField(max_length=64)
    postcode = models.CharField(max_length=16)
    street = models.CharField(max_length=128)
    streetnumber = models.CharField(max_length=32)

class ObjectCategory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class SimpleOffer(models.Model):
    category = models.ForeignKey(ObjectCategory, null=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='api.UploadedFile/bytes/filename/mimetype',
                              blank=True, null=True)

    # Owner's info
    city = models.CharField(max_length=64)
    telephone = models.CharField(max_length=64)
    email = models.CharField(max_length=128)

class UploadedFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
