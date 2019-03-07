from django.db import models
from user_profiles.models import Agent


class Client(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STATUS_OPTIONS = ((ACTIVE, 'Active'),
                      (INACTIVE, 'Inactive'))
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    wechat = models.CharField(max_length=255)
    comments = models.TextField(verbose_name='Comments')
    status = models.CharField(max_length=255,
                              choices=STATUS_OPTIONS,
                              default=ACTIVE)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImportRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    product_name = models.CharField(max_length=1000, verbose_name='Product Name')
    quantity = models.IntegerField(verbose_name='Quantity')
    comments = models.TextField(verbose_name='Comments')
    aeroshipment = models.BooleanField(default=False)
    export_agent = models.ForeignKey(Agent,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     verbose_name='Export Agent')


class ImportResponse(models.Model):
    import_request = models.ForeignKey(ImportRequest, on_delete=models.CASCADE)
    hs_code = models.CharField(max_length=255,
                               verbose_name='HS CODE')
    material = models.CharField(max_length=255,
                                verbose_name='Material')
    height = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Height')
    width = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Width')
    depth = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Depth')
    weight = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Weight')
    color = models.CharField(verbose_name='Color', max_length=255)
    time_production = models.IntegerField(verbose_name='Production Time(days)')
    moq = models.CharField(verbose_name='MOQ', max_length=255)
    total_pieces = models.IntegerField(verbose_name='TOTAL pcs')
    pieces_carton = models.IntegerField(verbose_name='PCS/carton')
    box_height = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Box Height')
    box_width = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Box Width')
    box_depth = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Box Depth')
    total_cbm = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total CBM')
    fob_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='FOB PRICE / USD')
    comments = models.TextField(verbose_name='Comments')
    supplier_information = models.TextField(verbose_name='Supplier Data')
    container_estimate = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Estimate', default=0)

    def fob_price_usd_pcs(self):
        return self.fob_price / self.total_pieces;


class Container(models.Model):
    cbm = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='CBM')
    measurements = models.CharField(max_length=255, verbose_name='Medidas')
    ton = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Ton')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price')
