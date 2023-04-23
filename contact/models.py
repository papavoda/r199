from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class ContactModel(models.Model):
    """ Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to="icons/", null=True, blank=True)
    name = models.CharField(max_length=100)  # address, phone, email
    value = models.CharField(max_length=100, default='')  # Street, 903-1234567,
    font_awesome_icon = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name


class About(models.Model):
    """Класс модели страницы о нас"""
    keywords = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=300, default='')
    about_hero_image = models.ImageField(upload_to="about/", default='',
                                         help_text="about_hero_image 1920x1280")
    main_image = models.ImageField(upload_to="about/", default='',
                                   help_text="add main about img 1280x853")
    name = models.CharField(max_length=25)
    slogan = models.CharField(max_length=100)
    text = RichTextField(max_length=200)

    def get_first_image(self):
        # обращение к related_name="about_images" class ImageAbout line 48
        return self.about_images.first().image.url

    def get_first_alt(self):
        return self.about_images.first().alt

    def get_images(self):
        return self.about_images.order_by('id')

    def get_promo_title(self):
        return self.about_promo.order_by('id')

    def __str__(self):
        return str(self.id)


class PromoAbout(models.Model):
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_promo")
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class ImageAbout(models.Model):
    """Класс модели изображений страницы о нас"""
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=50)

    def __str__(self):
        return self.image.name


class Social(models.Model):
    """класс модели соц сетей сраницы о нас"""
    icon = models.FileField(upload_to="icons/social", default='', blank=True, null=True)
    font_awesome_code = models.CharField(max_length=12, default='', blank=True, null=True)
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name


class HomeHeroSlogans(models.Model):
    """
     Картинки для hero on home, главные лозунги с описанием
    """
    hero_section = models.PositiveSmallIntegerField(default=0)  # 1,2,3 сверху вниз
    small_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # images for main carousel 1920x1280
    title_image = models.ImageField(upload_to='about/home_hero', default='', blank=True, null=True)
    text = models.CharField(max_length=300, blank=True, null=True)

    # 4 рекламных описания, например видов работ (Construction, renovation etc)
    # +
    # 3 рекламных  - Высокое качество, Точно в срок, поможем в выборе стройматериалов
    # или акции + small image
    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    """
    Request A Quote, Contact Us form
    """
    name = models.CharField(_("Имя"), max_length=50)
    phone = PhoneNumberField(_('Телефон'), default='')
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(_('Тема'), max_length=200)
    message = models.TextField(_('Сообщение'), max_length=1000)

    def __str__(self):
        return f'{self.date} - {self.name} - {self.phone}'
