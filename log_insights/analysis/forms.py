# log_matcher/forms.py
from django import forms

class LogForm(forms.Form):
    file = forms.FileField()
    test_name = forms.CharField()
    speed = forms.IntegerField(label='Speed')
    mtu = forms.IntegerField(label='MTU')
    frame_size = forms.IntegerField(label='Frame Size')
    use_udp = forms.CharField(label='use_udp')
    use_tcp = forms.CharField(label='use_tcp')
