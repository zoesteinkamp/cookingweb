from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    MEASUR = (
        ('Pinch', 'Pinch'),
        ('Pounds','Pounds'),
        ('Whole','Whole'),
        ('Teaspoon','Teaspoon'),
        ('Tablespoon','Tablespoon'),
        ('Cups','Cups')
    )
    type = models.CharField(max_length=20, choices=MEASUR)
    MEASURMENT= (
        ('Pinch',(
            ('1','1'),
        )),
        ('Teaspoon',(
            ('1/8','1/8'),('1/4','1/4'),('1/2', '1/2'),
             ('1','one'),('1 1/2','1 1/2'),('2','two'),
              )),
        ('Tablespoon',(
            ('1/2', 'half'),
             ('1','one'),('1 1/2', '1 1/2'),('2','two'),('2 1/2', '2 1/2'),('3','three'),
        )),
        ('Cup',(
            ('1/4','1/4'),('1/3','1/3'),('1/2','1/2'),('2/3','2/3'),('3/4','3/4'),('1','one'),
            ('1 1/4','1 1/4'),('1 1/3','1 1/3'),('1 1/2','1 1/2'),('1 2/3','1 2/3'),('1 3/4','1 3/4'),
            ('2','two'),('2 1/4','2 1/4'),('2 1/3','2 1/3'),('2 1/2','2 1/2'),('2 2/3','2 2/3'),('2 3/4','2 3/4'),
            ('3','three'), ('3 1/4','3 1/4'),('3 1/3','3 1/3'),('3 1/2','3 1/2'),('3 2/3','3 2/3'),('3 3/4','3 3/4'),
            ('4','four'), ('4 1/4','4 1/4'),('4 1/3','4 1/3'),('4 1/2','4 1/2'),('4 2/3','4 2/3'),('4 3/4','4 3/4'),
            ('5','five'), ('5 1/4','5 1/4'),('5 1/3','5 1/3'),('5 1/2','5 1/2'),('5 2/3', '5 2/3'),('5 3/4', '5 3/4'),
        )),
        ('Pounds',(
            ('1/4','1/4'),('1/3','1/3'),('1/2','1/2'),('2/3','2/3'),('3/4','3/4'),('1','one'),
            ('1 1/4','1 1/4'),('1 1/3','1 1/3'),('1 1/2','1 1/2'),('1 2/3','1 2/3'),('1 3/4','1 3/4'),
            ('2','two'),('2 1/4','2 1/4'),('2 1/3','2 1/3'),('2 1/2','2 1/2'),('2 2/3','2 2/3'),('2 3/4','2 3/4'),
            ('3','three'), ('3 1/4','3 1/4'),('3 1/3','3 1/3'),('3 1/2','3 1/2'),('3 2/3','3 2/3'),('3 3/4','3 3/4'),
            ('4','four'), ('4 1/4','4 1/4'),('4 1/3','4 1/3'),('4 1/2','4 1/2'),('4 2/3','4 2/3'),('4 3/4','4 3/4'),
            ('5','five'), ('5 1/4','5 1/4'),('5 1/3','5 1/3'),('5 1/2','5 1/2'),('5 2/3', '5 2/3'),('5 3/4', '5 3/4'),
        )),
        ('Whole Items',(
            ('1/2', '1/2'),('1','one'),('1 1/2','1 1/2'),('2','two'),('2 1/2', '2 1/2'),('3','three'),('3 1/2','3 1/2'),
            ('4','four'),('4 1/2', '4 1/2'),('5','five'),('5 1/2', '5 1/2'),('6', '6'),
        )),
    )
    amount = models.CharField(max_length=30, choices=MEASURMENT)
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=40)
    def __str__(self):
        return self.tag

class MainPhoto(models.Model):
    name = models.CharField(max_length=40)
    image_main = models.ImageField(upload_to="%Y/%m/%d")
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    short_des = models.TextField(max_length=200)
    long_des = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    servings = models.IntegerField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    date = models.DateField('date created', default=datetime.now)
    tags = models.ManyToManyField(Tag)
    vegan = models.NullBooleanField(default=False)
    vegeterian = models.NullBooleanField(default=False)
    glutten_free = models.NullBooleanField(default=False)
    dairy_free = models.NullBooleanField(default=False)
    photo = models.ForeignKey(MainPhoto)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.do_unique_slug()
        if not self.title:
            self.title = self.title
        super(Recipe, self).save(*args, **kwargs)

    def do_unique_slug(self):
        """
        Ensures that the slug is always unique for this post
        """
        if not self.id:
            # make sure we have a slug first
            if not len(self.slug.strip()):
                self.slug = slugify(self.title)

            self.slug = self.get_unique_slug(self.slug)
            return True

        return False

    def get_unique_slug(self, slug):
        """
        Iterates until a unique slug is found
        """
        orig_slug = slug
        counter = 1

        while True:
            posts = Recipe.objects.filter(slug=slug)
            if not posts.exists():
                return slug

            slug = '%s-%s' % (orig_slug, counter)
            counter += 1


class Comment(models.Model):
    name = models.CharField(max_length=30)
    body = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe)
    def __str__(self):
        return self.name




