from django.test import TestCase
from .models import Pic,Location,Category
import datetime as dt

# Create your tests here.

class Test_Location(TestCase):
    def setUp(self):
       
        self.location=Location(name="location")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    def test_save(self):
        self.location.save_location()
        query=Location.objects.all()
        self.assertTrue(len(query)>0)
    def test_locationdelete(self):
        self.location.save_location()
        self.location.deletelocation()
        query=Location.objects.all()
        
        self.assertTrue(len(query)==0)
    
     
     
class Test_category(TestCase):
    
    
    def setUp(self):
         self.test_category=Category(name="category")
         
    def test_instance(self):
        self.assertTrue(isinstance(self.test_category,Category))
        
    def test_save(self):
        self.test_category.save_category()
        query=Category.objects.all()
        self.assertTrue(len(query)>0)
        
    def test_getAll(self):
        self.test_category.save_category()
        self.test_category.delete()
        query=Category.objects.all()
        
        self.assertTrue(len(query)==0)
        