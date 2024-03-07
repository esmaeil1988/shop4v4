from django import forms


class fcontact(forms.Form):
    fname=forms.CharField(max_length=20, label="نام")
    lname=forms.CharField(max_length=20, label="نام خانوادگی")
    email=forms.EmailField(max_length=20, label="ایمیل")
    address=forms.CharField(max_length=30, label="آدرس")
    phonenumber=forms.CharField(max_length=11, label="شماره تماس")
    content=forms.CharField(max_length=500, label="متن درخواست",widget=forms.Textarea)
    def clean_phonenumber(self):
        p=self.cleaned_data["phonenumber"]
        if len(p)<11:
            raise forms.ValidationError("شماره موبایل باید 11 رقم باشد!")
        return p
