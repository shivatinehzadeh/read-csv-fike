from django.test import TestCase,Client
from django.core.mail import send_mail
from django.core import mail
from .models import Csv_File_model


class Test_for_view(TestCase):
#check that read CSV file and check that it saved or not
 def test_Insert_CSV_in_db(self):
     create_file = Csv_File_model(
         year='2019',
         Industry_aggregation_NZSIOC='Level 1',
         Industry_code_NZSIOC='BB',
         Industry_name_NZSIOC='Agriculture, Forestry and Fishing',
     )
     select_saved_file=Csv_File_model.objects.filter(year=2019,Industry_code_NZSIOC='BB')
     for row in select_saved_file:
      self.assertEqual(create_file.Industry_code_NZSIOC,row['Industry_code_NZSIOC'])


# send email and check that this email sent or not
 def test_email(self):
         send_mail('subject', 'body.', 'a@b.com', ['a@gmail.com'])
         assert len(mail.outbox) == 1

# check for create some row in model
class Test_model(TestCase):
    def test_for_model(self):
        create_model = Csv_File_model.objects.using('CSV_file_DB').create(year="2019")
        self.assertEqual(str(create_model), "2019")





