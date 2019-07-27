from django import forms
from django.forms.widgets import RadioSelect
from django.forms import extras
from bootstrap_datepicker_plus import DatePickerInput
from multiselectfield import MultiSelectFormField
from django.contrib.admin.widgets import AdminDateWidget


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    father_name = forms.CharField(
        label='Father Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Father Name'
            }
        )
    )
    mother_name = forms.CharField(
        label='Mother Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mother Name'
            }
        )
    )
    sal = forms.IntegerField(
        label='Salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Salary'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile'
            }
        )
    )

    color = forms.CharField(
        label='Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Color'
            }
        )
    )

    weight = forms.IntegerField(
        label='Weight',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Weight'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'
            }
        )
    )
    #
    # years = range(2000, 1970, -1)
    # dob = forms.DateField(
    #     label='Date of Birth',
    #     widget=forms.extras.SelectDateWidget(years=years))

    # dob = forms.DateField(
    #     widget=DatePickerInput(
    #         options={
    #             "format": "mm/dd/yyyy",
    #             "autoclose": True
    #         }
    #     )
    # )
    years = range(2000, 1970, -1)
    dob = forms.DateField(
        widget=forms.extras.SelectDateWidget(years=years)

    )

    hgt = [4.5,4.6,4.7,4.8,4.9,4.10,4.11,5.0, 5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.10,5.11,6,6.1,6.2]

    HEIGHT_CHOICES = [tuple([x, x]) for x in hgt]
    #   
    # height = forms.FloatField(label="Height",
    #                             widget=forms.Select(choices=HEIGHT_CHOICES,
    #                                                 attrs={
    #                                                     'class':'form-control'
    #                                                 }))
    height = forms.FloatField(
        label='Height',
        widget=forms.Select(
            choices=HEIGHT_CHOICES,
            attrs={
                'class':'form-control'
            }
        )
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(
        ), choices=GENDER_CHOICES)

    LOCATION_CHOICES = (
        ('Hyd', 'Hyderabad'),
        ('Bang', 'Bangalore'),
        ('Chen', 'Chennai'),
        ('Mum', 'Mumbai')
    )
    preffered_location = MultiSelectFormField(choices=LOCATION_CHOICES)

    JOB_CHOICES = (
        ('Govt', 'Govt Job'),
        ('S/W', 'Software'),
        ('Trainers', 'Teachers'),
        ('Doctor', 'Doctors'),
        ('Police', 'Police')
    )
    jobtype = MultiSelectFormField(choices=JOB_CHOICES)

    LOOKING_CHOICES = (
        ('Male', 'GROOM'),
        ('Female', 'BRIDE')
    )
    looking_for = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=LOOKING_CHOICES
    )


    address = forms.CharField(
        label='Address',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Address'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter Your Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your pasword',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )


class PasswordForm(forms.Form):
    username = forms.CharField(
        label='Enter UserName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password1 = forms.CharField(
        label='Enter New Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'New Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Enter Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'
            }
        )
    )
