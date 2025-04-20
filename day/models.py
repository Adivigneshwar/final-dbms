from django.db import models
class Cate(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self) :
        return self.name
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

    @property
    def description(self):
        return self.content

    def __str__(self) :
        return self.title
