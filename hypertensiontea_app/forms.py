from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, help_text='Please, enter your fullname.')
    phone_no = forms.IntegerField(help_text='Please, enter your phone number.')
    email = forms.EmailField(help_text='Please, enter a valid email address.')
    address = forms.CharField(widget=forms.Textarea, help_text='Please enter your delivery address.')
    CHOICES = (('Please select', 'Please select'),('1 tea pack ₦12,500', '1 tea pack ₦12,500'),('2 tea packs ₦20,000', '2 tea packs ₦20,000'),
     ('3 tea packs ₦30,000', '3 tea packs ₦30,000'), ('4 tea packs ₦40,000', '4 tea packs ₦40,000'),
     ('5 tea packs ₦50,000', '5 tea packs ₦50,000'))
    quantity = forms.ChoiceField(choices=CHOICES)
    
