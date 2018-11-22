from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

def post_image_path(instance, filename):
    return 'posts/{}/{}'.format(instance.pk, filename)

class Post(models.Model):
    image = ProcessedImageField(
                upload_to='posts/images',
                processors=[ResizeToFill(300,300)],
                format='JPEG',
                options={'quality':90},
            )
    content = models.TextField()
    
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk':self.pk})