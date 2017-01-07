from django.db import models

class Contact(object):

    def __init__(self, id, name, surname, mail, phone_number):
        self.id=id
        self.name=name
        self.surname=surname
        self.mail=mail
        self.phone_number=phone_number
        
    

# Create your models here.
