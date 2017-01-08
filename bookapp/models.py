from django.db import models

class Contact(object):

    def __init__(self, id, name, surname, mail, phone_number):
        self.id=id
        self.name=name
        self.surname=surname
        self.mail=mail
        self.phone_number=phone_number
        
class Address(object):

    def __init__(self, id, street_name, street_number, zip_code, city):
        self.id = id
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city


# Create your models here.
