from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.views.generic import TemplateView
from ipage.forms import Reg,Patient_login,Doctor_login,Questions,Doc_id,Check,Iresult
from django.http import HttpResponse
from ipage.Medical_data_analysis import rec
from ipage import reg

# Create your views here.

#-----------------------------------------------------------------------------------------

class admin(TemplateView):
    template_name = "admin.html"

    def get(self,request):
        form = Doc_id()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = Doc_id(request.POST)
        if form.is_valid():
            dn = form.cleaned_data['name']
            a = reg.docid(dn)
            form = Doc_id()
            return render(request,self.template_name,{'form':form,'id': 'The generated id is : '+a})

#-----------------------------------------------------------------------------------------

class login(TemplateView):
    template_name = "exthome.html"

    def get(self,request):
        form1 = Doctor_login()
        form2 = Patient_login()
        form3 = Reg()
        return render(request,self.template_name,{'form1':form1,'form2':form2,'form3':form3})

    def post(self,request):
        form1 = Doctor_login(request.POST)
        form2 = Patient_login(request.POST)
        form3 = Reg(request.POST)
        if form1.is_valid():
            doid = form1.cleaned_data['did']
            dopwd = form1.cleaned_data['dpwd']
            form1 = Doctor_login()
            a = reg.dlogin(doid)
            request.session['Doctor_name'] = a
            if a != dopwd:
                return render(request,self.template_name,{'form1':form1,'form2':form2,'form3':form3,'w':'... Incorrect Id or Password ...'})
            else:
                return redirect(reverse('search'))
        elif form2.is_valid():
            patid = form2.cleaned_data['pid']
            patpwd = form2.cleaned_data['ppwd']
            form2 = Patient_login()
            b = reg.plogin(patid)
            re = b['fname'] + b['lname']
            if re != patpwd:
                return render(request,self.template_name,{'form1':form1,'form2':form2,'form3':form3,'w':'... Incorrect Id or Password ...'})
            else:
                dob = b['Dob']
                gen = b['Gender']
                reg.dtt(patid)
                return render(request,"patient_page.html",{'f':re,'dob':dob,'g':gen,'b':b,'download':patid})
        elif form3.is_valid():
            fn = form3.cleaned_data['f_name']
            ln = form3.cleaned_data['l_name']
            dob = form3.cleaned_data['age']
            g = form3.cleaned_data['gender']
            a = reg.registration(fn,ln,dob,g)
            form3 = Reg()
            return render(request,self.template_name,{'form1':form1,'form2':form2,'form3':form3,'w':'Your registered id is : '+a})

#-----------------------------------------------------------------------------------------

class search(TemplateView):
    template_name = "extdlogin.html"
    def get(self,request):
        a = request.session['Doctor_name']
        return redirect(reverse('dr'))

#-----------------------------------------------------------------------------------------

class ppage(TemplateView):
    template_name = "patient_page.html"

#-----------------------------------------------------------------------------------------

class questions(TemplateView):
    template_name = "dr1.html"
    def get(self,request):
        form2 = Questions()
        a = request.session['Doctor_name']
        return render(request,self.template_name,{'form2':form2,'f':a})
    def post(self,request):
        form2 = Questions(request.POST)
        a = request.session['Doctor_name']
        pid = request.session['patient_id']
        d = request.session['dcease']
        if form2.is_valid():
            w = form2.cleaned_data['weight']
            c = form2.cleaned_data['c_duration']
            f = form2.cleaned_data['f_temp']
            cp = form2.cleaned_data['chest']
            brp = form2.cleaned_data['breathing']
            wz = form2.cleaned_data['vsing']
            ns = form2.cleaned_data['sweats']
            sl = form2.cleaned_data['sleep']
            wl = form2.cleaned_data['weightl']
            t = form2.cleaned_data['throat']
            n = form2.cleaned_data['nose']
            sr = form2.cleaned_data['skin']
            h = form2.cleaned_data['habits']
            o = form2.cleaned_data['textbox']
            r = reg.basiq(a,pid,d,w,c,f,cp,brp,wz,ns,sl,wl,t,n,sr,h,o)
            form2 = Questions()
            print(r)
        if r == '1':
            return render(request,"c.html",{'f':a})
        elif r == '0':
            return render(request,"c1.html",{'f':a})
#-----------------------------------------------------------------------------------------

class iresult(TemplateView):
    template_name = "dr2.html"
    def get(self,request):
        form = Iresult()
        a = request.session['Doctor_name']
        return render(request,self.template_name,{'f':a,'form':form})
    def post(self,request):
        form = Iresult(request.POST)
        a = request.session['Doctor_name']
        
        if form.is_valid():
            sp = form.cleaned_data['sp']
            xr = form.cleaned_data['xr']
            gt = form.cleaned_data['gt']
            ct = form.cleaned_data['ct']
            hiv = form.cleaned_data['hiv']
            cd4 = form.cleaned_data['cd4']
            r = reg.ran1(sp,xr,gt,ct,hiv,cd4)
        return render(request,"dr3.html",{'f':a,'res':r})
       # return render(request,self.template_name,{'f':a,'form':form})

#-----------------------------------------------------------------------------------------

class dr(TemplateView):
    template_name = "dr.html"
    def get(self,request):
        a = request.session['Doctor_name']
        form1 = Check()
        return render(request,self.template_name,{'form1':form1,'f':a})
    def post(self,request):
        form1 = Check(request.POST)
        a = request.session['Doctor_name']
        if form1.is_valid():
            d = form1.cleaned_data['disease']
            pid = form1.cleaned_data['patient_id']
            request.session['patient_id'] = pid
            request.session['dcease'] = d
            k = reg.chek(pid,d,a)
            form1 = Check()
        if k == '... The Requested person does not have Health Care account ...':
            return render(request,self.template_name,{'form1':form1,'w':k,'f':a})
        elif k is True:
            return redirect(reverse('iresult'))
        elif k is False:
            return redirect(reverse('questions'))

#-----------------------------------------------------------------------------------------
class final_ans():
     template_name = "dr3.html"
     
