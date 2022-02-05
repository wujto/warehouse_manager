from django.db import models

class ProductModel(models.Model):
    id_number = models.CharField(unique=True, max_length=9) #Number to identify product in database
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, default="")
    category = models.ForeignKey("CategoryModel", on_delete= models.DO_NOTHING, blank=False, null=False)
    localization = models.ForeignKey("LocalizationModel", on_delete = models.DO_NOTHING, blank=False, null=False)
    photo = models.FileField()
    product_set = models.ForeignKey("ProductSetModel",on_delete = models.DO_NOTHING, null=True, blank=False)
    product_user = models.ForeignKey("User",on_delete = models.DO_NOTHING, blank=False, null=True)

    def __str__(self):
        return f'{self.id_number} {self.name}'

    def get_info(self):
        info = {
            'id_number':self.id_number,
            'name':self.name,
            'description':self.description,
            'category':self.category,
            'localization':self.localization,
            'photo':self.photo,
            'product_set':self.product_set,
            'product_user':self.product_user
        }

        return info
