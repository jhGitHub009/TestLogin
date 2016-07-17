from django import forms

class outgoingForm(forms.Form):
	zone = forms.CharField(label = 'Zone ID', max_length = 20)
	pallet = forms.CharField(label = 'Pallet ID', max_length = 20)
	material_code = forms.CharField(label ='Material Code', max_length = 20)
	unit = forms.CharField(label ='Unit', max_length = 10)
	count = forms.IntegerField(label ='Count')