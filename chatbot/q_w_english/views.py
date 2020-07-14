from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import module_chatbot

def index(request):
    return render(request,'home.html')
def huongdan(request):
    return render(request,'huongdan.html')
def chatbot(request):
    global cau_trl, cauhoi
    cauhoi = ""
    cau_trl = ""
    if request.method =="POST":
        cauhoi = request.POST.get("input_cauhoi")
        cauhoi = str(cauhoi)
        cau_trl = module_chatbot.response(cauhoi)
    cau_trl = str(cau_trl)
    conn=sqlite3.connect("db.sqlite3")
    cmd="INSERT INTO Ques_Ans_db(Question, Answer) Values(?,?)"
    cursor=conn.execute(cmd,(cauhoi, cau_trl))
    conn.commit()
    conn.close()
    context={
        'cauhoi': cauhoi,
        'cautraloi': cau_trl
    }
    return render(request,'form_cauhoi.html', context)