from django.db import models
from .utils import get_random_id
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='products', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    name = models.CharField(default='product', max_length = 200)
    description = models.TextField(default="no bio", max_length=300,blank=True)
    tags = models.TextField(default="no bio", max_length=300,blank=True)
    slug = models.SlugField(unique=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    owned = 'owned'
    listed = 'listed'
    status_choice = [(owned, 'Owned'), (listed, 'Listed')]

    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add = True)
    price = models.IntegerField(default=1)
    status = models.CharField(max_length = 9,choices = status_choice, default = 1)

    def __str__(self):
        return f"{self.name}"
        

    def save(self, *args, **kwargs):
        ex = True
        to_slug = "w"
        while ex:
            to_slug = slugify(to_slug + " " +str(get_random_id()))
            ex = Product.objects.filter(slug=to_slug).exists()
        self.slug = to_slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)