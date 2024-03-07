from django.db import models
import datetime

# Create your models here.
class category(models.Model):
    title=models.CharField(max_length=30,verbose_name="عنوان طبقه")
    def __str__(self) -> str:
        return self.title
    def getprod(self):
        return product.objects.filter(category=self)
    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"


class product(models.Model):
    title=models.CharField(max_length=30,verbose_name="عنوان محصول")
    brand=models.CharField(max_length=30,null=True,verbose_name="برند")
    price=models.DecimalField(decimal_places=0,max_digits=10,verbose_name="قیمت")
    moshakhasat=models.CharField(max_length=500,null=True,verbose_name="مشخصات محصول")
    tozih=models.CharField(max_length=500,verbose_name="توضیحات محصول")
    garenty=models.CharField(max_length=100,null=True,verbose_name="وضعیت گارانتی")
    img=models.ImageField(upload_to='aks',verbose_name="عکس")
    category=models.ManyToManyField(category, verbose_name="طبقه بندی")
    is_special=models.BooleanField(null=True,verbose_name="ویژه")
    special_price=models.DecimalField(decimal_places=0,max_digits=10,verbose_name=" قیمت ویژه",null=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"
    



class contact(models.Model):
    fname=models.CharField(max_length=20,verbose_name="نام")
    lname=models.CharField(max_length=20,verbose_name="نام خانوادگی")
    email=models.EmailField(max_length=30,verbose_name="ایمیل")
    address=models.CharField(max_length=50,verbose_name="آدرس")
    phonenumber=models.CharField(max_length=11,null=True,verbose_name="شماره موبایل")
    content=models.CharField(max_length=500,verbose_name="متن پیام")
    def __str__(self) -> str:
        return self.fname + ' ' +self.lname
    class Meta:
        verbose_name_plural = "پیامها"
        verbose_name = "پیام"
    

  


class picture(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="aks")
    def __str__(self) -> str:
        return self.product.title
    class Meta:
        verbose_name_plural = "تصاویر"
        verbose_name = "تصویر"




class client(models.Model):
    firstname=models.CharField(max_length=20,verbose_name='نام')
    lastname=models.CharField(max_length=20,verbose_name='نام خانوادگی')
    username=models.CharField(max_length=20,verbose_name='نام کاربری')
    password=models.CharField(max_length=20,verbose_name='کلمه عبور')
    class Meta:
        verbose_name='مشتری'
        verbose_name_plural='مشتریان'
    def __str__(self) -> str:
        return self.firstname+" "+self.lastname



class cart(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qnt=models.IntegerField()
   


class faktor(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.datetime.now)
    totalprice=models.DecimalField(decimal_places=0,max_digits=10)
    class Meta:
        verbose_name='فاکتور'
        verbose_name_plural='فاکتورها'
    def __str__(self) -> str:
        return self.client



class faktor_details(models.Model):
    faktor=models.ForeignKey(faktor,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qnt=models.IntegerField()
