from django.shortcuts import render
import csv
from project_csv import settings
from .models import Csv_File_model
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import View
from django.contrib import messages


#this function is for uploading json file and return to read file and insert to database
def read_csv(self):
    #path of CSV_File in csvApp
    path = settings.CSVFILE+'/data.csv'
    #read CSV file split with comma
    reader=csv.DictReader(open(path))
    #get all row of CSV File and save in databases
    for row in reader:
        create = Csv_File_model(
            year=row['Year'],
            Industry_aggregation_NZSIOC=row['Industry_aggregation_NZSIOC'],
            Industry_code_NZSIOC=row['Industry_code_NZSIOC'],
            Industry_name_NZSIOC=row['Industry_name_NZSIOC'],
        )
        create.save(using='default')
        create.save(using='CSV_file_DB')
    return reverse('CSV:email')


 #email is just for show, you can get email from user information or get from a form
#request.user.email
class Send_mail(View):
 template_name='email.html'
 def get(self,request):
  myEmail = 'A@t.com'
  send_mail('subject', 'your file saved', 'a.b@gmail.com', [myEmail, ])
  messages.success(request,'email sent!')
  return render(request,self.template_name)

