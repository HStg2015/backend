from django.db import models

class RefugeeCamp(models.Model):
    # Location
    city = models.CharField(max_length=64)
    postcode = models.CharField(max_length=16)
    street = models.CharField(max_length=128)
    streetnumber = models.CharField(max_length=32)

    def __str__(self):
        return "{0} {1}: {2} {3}".format(self.postcode, self.city,
                                         self.street, self.streetnumber)

class ObjectCategory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class SimpleOffer(models.Model):
    category = models.ForeignKey(ObjectCategory, null=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4096)
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='api.UploadedFile/bytes/filename/mimetype',
                              blank=True, null=True)

    # Owner's info
    city = models.CharField(max_length=64)
    telephone = models.CharField(max_length=64)
    email = models.CharField(max_length=128)

class HelpTimeSearch(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    camp = models.ForeignKey(RefugeeCamp)

class UploadedFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
