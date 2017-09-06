from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    STAUTS_CHOICE = ( ('draft','Draft'),('published','Published'),)
    title =models.CharField(max_length =250)
    slug = models.SlugField(max_length =250)
    author = models.ForeignKey(User,related_name='blog_post')
    body = models.TextField()
    publish =models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    udated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length =250 , choices = STAUTS_CHOICE , default = 'draft')
    # objects = models.Manager
    # published = PublishedManager
    class Meta:
         ordering = ('-publish',)               
   
    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [self.slug, self.publish.year , self.publish.strftime('%m'), self.publish.strftime('%d')])  
    
    def __str__(self):
         return self.title
        