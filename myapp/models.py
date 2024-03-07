from djongo import models


from djongo import models

class Image(models.Model):
    _id = models.ObjectIdField()
    urlImage = models.URLField()


class Users(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthDate = models.DateField()
    images = models.ArrayField( model_container=Image)
    isState = models.BooleanField(default=True)


