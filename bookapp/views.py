from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from bookapp.models import Contact
from mysql.connector import connect



class NewContact(View):

    def get(self, request):
        return render(request, "new_contact.html")

    def post(self, request):
        new_contact_name = request.POST.get("contact_name")
        new_contact_surname = request.POST.get("contact_surname")
        new_contact_mail = request.POST.get("contact_mail")
        new_contact_phone_number = request.POST.get("contact_phone_number")

        query = """
            INSERT INTO Contacts (id, name, surname, mail, phone_number)
                VALUES (0, '%s', '%s', '%s', '%s');
                """ % (new_contact_name, new_contact_surname, new_contact_mail, new_contact_phone_number)

        print(query)
        try:
            cnx = connect(user="root", password="coderslab", host="127.0.0.1", database="contactbook")
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
        except:
            raise 

        cursor.close()
        cnx.close()

        return HttpResponseRedirect("/")

class ModifyContact(View):
    def get(self,request):
        return HttpResponse("ModifyContact")
class DeleteContact(View):
    def get(self,request):
        return HttpResponse("DeleteContact")

class ShowContact(View):
    def get(self,request,contact_id):
        
        sql = '''select * from Contacts where id={}'''.format(contact_id)
        username= "root"
        passwd= "coderslab"
        hostname= "localhost"
        db_name= "contactbook"
        
        print(sql)
       
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cursor = cnx.cursor()
        cursor.execute(sql)

        contact_for_cursor=cursor.fetchone()
        
        contact = Contact(
        
            contact_for_cursor[0],
            contact_for_cursor[1],
            contact_for_cursor[2],
            contact_for_cursor[3],
            contact_for_cursor[4]    
                )
        
        
        cursor.close()
        cnx.close()
        
        ctx={"contact":contact}
        return render(request, "show_contact.html",ctx)


class ShowContactList(View):
    def get(self, request):
        query = """SELECT id, name, surname, mail, phone_number 
                FROM Contacts;"""
        try:
            cnx = connect(user="root", password="coderslab", host="127.0.0.1", database="contactbook")
            cursor = cnx.cursor()
            cursor.execute(query)
        except:
            raise 

        contacts = []
        for row in cursor:
            contact = Contact(row[0],row[1],row[2],row[3],row[4])
            contacts.append(contact)

        ctx = { 'contact_list' : contacts}

        return render(request, "contact_list.html", ctx)
