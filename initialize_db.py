import os
import django
from django.core.management import call_command

def initialize_database():
    # إعداد بيئة Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
    django.setup()

    print("إنشاء الجداول في قاعدة البيانات...")
    call_command('makemigrations')
    call_command('migrate')

    print("إنشاء حساب المشرف...")
    username = input("اسم المستخدم لحساب المشرف: ")
    email = input("البريد الإلكتروني لحساب المشرف: ")
    password = input("كلمة المرور لحساب المشرف: ")

    from django.contrib.auth.models import User
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("تم إنشاء حساب المشرف بنجاح!")
    else:
        print("حساب المشرف موجود بالفعل.")

if __name__ == "__main__":
    initialize_database()