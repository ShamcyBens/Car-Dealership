from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

# Create your models here.
# models.py



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profile-pics/',blank=True, null=True,default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    fuel_type_choices = [
        ('lpg', 'LPG'),
        ('cng', 'CNG'),
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric')
    ]
    car_owner_choices = [
        ('first owner', 'First Owner'),
        ('second owner', 'Second Owner'),
        ('third owner', 'Third Owner'),
        ('fourth owner or more', 'Fourth Owner or More')
    ]
    insurance_type_choices = [
        ('comprehensive', 'Comprehensive'),
        ('third party', 'Third Party'),
        ('expired', 'Expired'),
    ]
    registration_type_choices = [
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('taxi', 'Taxi'),
    ]
    car_status_options = [
        ('active','Active'),
        ('deactive','Deactive'),
    ]
    vehicle_type_choices = [
        ('Car','Car'),
        ('Bike','Bike'),
        ('Truck','Truck'),
        ('Tractor','Tractor'),
        ('Auto Rickshaw','Auto Rickshaw'),
        ('Agriculture Instrument','Agriculture Instrument'),
    ]
    transmission_type_choices = [
		('automatic', 'Automatic'),
		('manual', 'Manual'),
    ]

    city_choices = [
		('Garhwa', 'Garhwa'),
		('Palamu', 'Palamu'),
		('Latehar', 'Latehar'),
		('Chatra', 'Chatra'),
		('Hazaribagh', 'Hazaribagh'),
		('Koderma', 'Koderma'),
		('Giridih', 'Giridih'),
		('Ramgarh', 'Ramgarh'),
		('Bokaro', 'Bokaro'),
		('Dhanbad', 'Dhanbad'),
		('Gumla', 'Gumla'),
		('Lohardaga', 'Lohardaga'),
		('Simdega', 'Simdega'),
		('Ranchi', 'Ranchi'),
		('Khunti', 'Khunti'),
		('West Singhbhum', 'West Singhbhum'),
		('Saraikela Kharsawan', 'Saraikela Kharsawan'),
		('East Singhbhum', 'East Singhbhum'),
		('Jamtara', 'Jamtara'),
		('Deoghar', 'Deoghar'),
		('Dumka', 'Dumka'),
		('Pakur', 'Pakur'),
		('Godda', 'Godda'),
		('Sahebganj', 'Sahebganj'),
		('Araria', 'Araria'),
		('Arwal', 'Arwal'),
		('Aurangabad', 'Aurangabad'),
		('Banka', 'Banka'),
		('Begusarai', 'Begusarai'),
		('Bhagalpur', 'Bhagalpur'),
		('Bhojpur', 'Bhojpur'),
		('Buxar', 'Buxar'),
		('Darbhanga', 'Darbhanga'),
		('East Champaran', 'East Champaran'),
		('Gaya', 'Gaya'),
		('Gopalganj', 'Gopalganj'),
		('Jamui', 'Jamui'),
		('Jehanabad', 'Jehanabad'),
		('Khagaria', 'Khagaria'),
		('Kishanganj', 'Kishanganj'),
		('Kaimur', 'Kaimur'),
		('Katihar', 'Katihar'),
		('Lakhisarai', 'Lakhisarai'),
		('Madhubani', 'Madhubani'),
		('Munger', 'Munger'),
		('Madhepura', 'Madhepura'),
		('Muzaffarpur', 'Muzaffarpur'),
		('Nalanda', 'Nalanda'),
		('Nawada', 'Nawada'),
		('Patna', 'Patna'),
		('Purnia', 'Purnia'),
		('Rohtas', 'Rohtas'),
		('Saharsa', 'Saharsa'),
		('Samastipur', 'Samastipur'),
		('Sheohar', 'Sheohar'),
		('Sheikhpura', 'Sheikhpura'),
		('Saran', 'Saran'),
		('Sitamarhi', 'Sitamarhi'),
		('Supaul', 'Supaul'),
		('Siwan', 'Siwan'),
		('Vaishali', 'Vaishali'),
		('West Champaran', 'West Champaran'),
		('Other', 'Other'),
	
    ]             

    car_id = models.AutoField
    car_title = models.CharField( max_length=100)
    make_year = models.IntegerField()
    make_month = models.CharField( max_length=100, blank=True, null = True )
    car_manufacturer = models.CharField( max_length=100)
    car_model = models.CharField( max_length=100)
    car_version = models.CharField( max_length=100, blank=True, null = True )
    car_color = models.CharField( max_length=100, blank=True, null = True )
    fuel_type = models.CharField(max_length=25, choices=fuel_type_choices, default= 'petrol')
    transmission_type = models.CharField(max_length=25, choices=transmission_type_choices, default= 'manual')
    car_owner = models.CharField(max_length=25, choices=car_owner_choices, default= 'first owner')
    kilometer_driven = models.IntegerField(blank=True, null = True )
    expected_selling_price = models.IntegerField()
    registration_type = models.CharField(max_length=25, choices=registration_type_choices, default= 'individual')
    insurance_type = models.CharField(max_length=25, choices=insurance_type_choices, default= 'expired')
    registration_number = models.CharField( max_length=30, blank=True, null = True )
    car_description = models.TextField(blank=True, null = True )
    car_post_date = models.DateField(default=datetime.now)
    car_photo = models.ImageField(upload_to='car-images/', default="car-images/default.jpeg", blank=True, null = True )
    car_status = models.CharField(max_length=25, choices=car_status_options, default= 'active')
    vehicle_type = models.CharField(max_length=25, choices=vehicle_type_choices, default= 'Car')


    # user , Many to One connection
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL
    # personal details

    car_owner_phone_number = models.IntegerField(default=0, blank=True, null = True )
    car_city = models.CharField( max_length=50, choices=city_choices, default= 'Patna')
    car_owner_name = models.CharField( max_length=100,default="-")


    class Meta:
        # order of cars in admin area
        # use -publish instead of publish , to reverse the order
        ordering = ('car_title',)

    def __str__(self):
        # responsible to show name of carin admin instead of object1
        # also look the authoradmin class in admin.py 
        return self.car_title

    

    

    