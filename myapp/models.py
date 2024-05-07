from djongo import models

class Post(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def get_id(self):
        return str(self._id)  # Make sure this is correctly returning the _id as a string

    class Meta:
        db_table = 'posts'
