from django.http import HttpResponse


def index(request):
    import sqlite3
    conn =sqlite3.connect('DjangoFramework.db')
    conn.close()
    return HttpResponse('Hello world! You are at the polls index.')