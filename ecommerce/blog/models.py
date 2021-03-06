from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)



    #def get_absolute_url(self): We will replace it using reverse method with minor change
    #    return "/blog/%s/"%(self.id)

    def get_absolute_url(self):
        #return reverse('detail', kwargs={"id": self.id})
        return reverse('blog:detail', kwargs={"id": self.id}) #referring to the name space assigned to master urls.py