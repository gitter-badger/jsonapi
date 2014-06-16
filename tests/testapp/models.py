""" Models definition.

Model relationship:

      Author
       ||
       ||
       ||-----@ Post ----> PostWithPicture
       |  ______/
       |  |
       @  @
       Comment

"""


from django.db import models


class Author(models.Model):
    big_integer = models.BigIntegerField()
    # binary = models.BinaryField()
    boolean = models.BooleanField()
    char = models.CharField(max_length=100)
    comma_separated_integer = models.CommaSeparatedIntegerField(max_length=5)
    date = models.DateField()
    datetime = models.DateTimeField()
    email = models.EmailField()
    authorfile = models.FileField(upload_to='.')
    filepath = models.FilePathField()
    floatnum = models.FloatField()
    # image = models.ImageField()  # Avoid Pillow
    integer = models.IntegerField()
    ip = models.IPAddressField()
    generic_ip = models.GenericIPAddressField(protocol='ipv6')
    nullboolean = models.NullBooleanField()
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    small_integer = models.SmallIntegerField()
    text = models.TextField()
    time = models.TimeField()
    url = models.URLField()

    @property
    def integer_next(self):
        return self.integer + 1


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)

    @property
    def title_uppercased(self):
        return self.title.upper()


class PostWithPicture(Post):
    picture_url = models.URLField()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(Author)