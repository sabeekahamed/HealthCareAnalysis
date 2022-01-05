from django import forms

gend = [('male','Male'),('female','Female'),]
cd_ch = [('0','No'),('0','2-weeks'),('1','more than 2-weeks'),('0','less than 2-weeks')]
f_temp = [('0','No'),('0','exactly 100 F'),('1','above 100 F'),('0','below 100 F')]
pain = [('0','No'),('1','severe'),('0','occasional')]
sing = [('from birth','from birth'),('recently','recently'),('no','NO')]
yn = [('1','Yes'),('0','No')]
t = [('no','No'),('severe','severe'),('mild','mild')]
hab =[('1','Smoke'),('0','Alcohol'),('0','Other drugs'),('0','NO')]

#-----------------------------------------------------------------------------------------

class Doc_id(forms.Form):
    name = forms.CharField( widget = forms.TextInput( attrs = {'autofocus':'autofocus','autocomplete':'off'}))
    #reset = forms.CharField( widget = forms.TextInput( attrs = {'autocomplete':'off','type':'number'}))  create another class for reset

#-----------------------------------------------------------------------------------------

class Doctor_login(forms.Form):
    did = forms.CharField( widget = forms.TextInput( attrs = {'autofocus':'autofocus','placeholder':'      License number','autocomplete':'off'}))
    dpwd = forms.CharField( widget = forms.PasswordInput)
    #Gender = forms.ChoiceField(widget = forms.Select,choices = gender)

#-----------------------------------------------------------------------------------------

class Patient_login(forms.Form):
    pid = forms.CharField( widget = forms.TextInput( attrs = {'placeholder':'      Patient number','autocomplete':'off'}))
    ppwd = forms.CharField( widget = forms.PasswordInput)

#-----------------------------------------------------------------------------------------

class Reg(forms.Form):
    f_name = forms.CharField( widget = forms.TextInput( attrs = {'autofocus': 'autofocus','autocomplete':'off'}))
    l_name = forms.CharField(widget = forms.TextInput( attrs = {'autocomplete':'off'}))
    age = forms.CharField( widget = forms.TextInput(attrs = {'type':'date','autocomplete':'off'}))
    gender = forms.CharField( label='Gender',widget=forms.RadioSelect(choices = gend))

#-----------------------------------------------------------------------------------------

class Check(forms.Form):
    patient_id = forms.CharField( widget = forms.TextInput( attrs = {'autofocus':'autofocus','placeholder':'               P-***','autocomplete':'off'}))
    disease = forms.CharField(widget = forms.TextInput( attrs = {'placeholder':'   typhoid/dengue/TB/','autocomplete':'off'}))

#-----------------------------------------------------------------------------------------

class Questions(forms.Form):
    weight = forms.CharField( widget = forms.TextInput( attrs = {'type':'number'}))
    c_duration = forms.ChoiceField(choices=cd_ch, widget=forms.RadioSelect())
    f_temp = forms.ChoiceField(choices=f_temp, widget=forms.RadioSelect())
    chest = forms.ChoiceField(choices=pain, widget=forms.RadioSelect())
    breathing = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    vsing = forms.ChoiceField(choices=sing, widget=forms.RadioSelect())
    sweats = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    sleep = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    weightl = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    throat = forms.ChoiceField(choices=t, widget=forms.RadioSelect())
    nose = forms.ChoiceField(choices=yn,widget=forms.RadioSelect())
    skin = forms.ChoiceField(choices=yn,widget=forms.RadioSelect())
    habits = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=hab)#forms.ChoiceField(choices=hab,widget=forms.RadioSelect())
    textbox = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols':'105'}))
    #fd = forms.CharField(widget=forms.Textarea(attrs={'rows':'1', 'cols':'15'}))

#-----------------------------------------------------------------------------------------

class Iresult(forms.Form):
    sp = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    xr = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    gt = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    ct = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    hiv = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())
    cd4 = forms.ChoiceField(choices=yn, widget=forms.RadioSelect())

#-----------------------------------------------------------------------------------------
