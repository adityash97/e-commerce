from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    on_created = models.DateTimeField(auto_now_add=True)
    on_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductClass(BaseModel):
    product_class = models.CharField(max_length=255)
    
    def __str__(self):
        return self.product_class


CLASSIFICATION = (
    ("Men", "men"),
    ("Women", "women"),
    ("unisex", "Unisex"),
    ("girl_kid", "Girl Kid"),
    ("boy_kid", "Boy Kid"),
    ("unisex_kid", "Unisex Kid"),
)


class ProductBelongsTo(BaseModel):
    classification = models.CharField(
        max_length=55, choices=CLASSIFICATION, default="unisex"
    )
    def __str__(self):
        return self.classification

class RatingChoices(models.IntegerChoices):
    ONE = 1, "★☆☆☆☆"
    TWO = 2, "★★☆☆☆"
    THREE = 3, "★★★☆☆"
    FOUR = 4, "★★★★☆"
    FIVE = 5, "★★★★★"


class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    rating = models.IntegerField(choices=RatingChoices.choices)
    order_count = models.IntegerField()
    total_item = models.IntegerField()
    out_of_stock = models.BooleanField(default=False)
    item_belongs_to = models.ManyToManyField(
        ProductBelongsTo, related_name="belongs_to"
    )
    item_class = models.ForeignKey(
        ProductClass, on_delete=models.DO_NOTHING, related_name="item_class"
    )
    
    def __str__(self):
        classfications = ", ".join([obj.classification for obj in self.item_belongs_to.all()])
        return f"{self.name} - {classfications}"
        