from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='default')
    neighbourhood = models.ForeignKey("Neighbourhood", blank=True, null=True, related_name='community', on_delete=models.CASCADE)
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
class Neighbourhood(models.Model):
    COUNTY_CHOICES = (
('Baringo','Baringo County'),
('Bomet','Bomet County'),
('Bungoma','Bungoma County'),
('Busia','Busia County'),
('Elgeyo Marakwet','Elgeyo Marakwet County'),
('Embu','Embu County'),
('Garissa','Garissa County'),
('Homa Bay','Homa Bay County'),
('Isiolo','Isiolo County'),
('Kajiado','Kajiado County'),
('Kakamega','Kakamega County'),
('Kericho','Kericho County'),
('Kiambu','Kiambu County'),
('Kilifi','Kilifi County'),
('Kirinyaga','Kirinyaga County'),
('Kisii','Kisii County'),
('Kisumu','Kisumu County'),
('Kitui','Kitui County'),
('Kwale','Kwale County'),
('Laikipia','Laikipia County'),
('Lamu','Lamu County'),
('Machakos','Machakos County'),
('Makueni','Makueni County'),
('Mandera','Mandera County'),
('Meru','Meru County'),
('Migori','Migori County'),
('Marsabit','Marsabit County'),
('Mombasa','Mombasa County'),
('Muranga','Muranga County'),
('Nairobi','Nairobi County'),
('Nakuru','Nakuru County'),
('Nandi','Nandi County'),
('Narok','Narok County'),
('Nyamira','Nyamira County'),
('Nyandarua','Nyandarua County'),
('Nyeri','Nyeri County'),
('Samburu','Samburu County'),
('Siaya','Siaya County'),
('Taita Taveta','Taita Taveta County'),
('Tana River','Tana River County'),
('Tharaka Nithi','Tharaka Nithi County'),
('Trans Nzoia','Trans Nzoia County'),
('Turkana','Turkana County'),
('Uasin Gishu','Uasin Gishu County'),
('Vihiga','Vihiga County'),
('Wajir','Wajir County'),
('West Pokot','West Pokot County'),
   
    )
    neighbourhood_name = models.CharField(max_length = 100)
    neighbourhood_image = models.ImageField(upload_to='neighbourhoods/', default='neighbourhoods/default.png')
    admin = models.ForeignKey("Profile", related_name='hood', on_delete=models.CASCADE)
    neighbourhood_location = models.CharField(max_length = 100,choices=COUNTY_CHOICES)
    police_info = models.TextField(default="911")
    health_department_info = models.TextField(default="911")
    occupants_count= models.PositiveIntegerField()

    def __str__(self):
        return f'{self.neighbourhood_name} Neighbourhood'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    @classmethod
    def find_neighbourhood_id(cls,id):
        neighbourhood = cls.objects.get(id=id)
        return neighbourhood