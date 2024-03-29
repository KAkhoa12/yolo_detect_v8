from djongo import models
class Image(models.Model):
    _id = models.ObjectIdField()
    urlImage = models.URLField()


class Users(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    birthDate = models.DateField()
    images = models.ArrayField( model_container=Image)
    isState = models.BooleanField(default=True)


class Model(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    modelName = models.CharField(max_length = 200)
    modelCategory = models.CharField(max_length = 100)
    modelImage = models.EmbeddedField(model_container = Image)
    modelDescription = models.TextField()
    slug = models.CharField(max_length = 100)

class Blog(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    blogName = models.CharField(max_length = 100)
    blogAuth = models.CharField(max_length = 50)
    blogDescription = models.CharField(max_length = 500)
    blogContent = models.TextField()
    slug = models.CharField(max_length = 50)