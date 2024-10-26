from django.shortcuts import render
from .forms import LogForm

def home(request):
    result = None 
    if request.method == "POST":
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            speed = form.cleaned_data['speed']
            mtu = form.cleaned_data['mtu']
            frame_size = form.cleaned_data['frame_size']
            use_udp = form.cleaned_data['use_udp']
            use_tcp = form.cleaned_data['use_tcp']
            # Read and match data in CSV
            csv_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(csv_file)
            for row in reader:
                if (row['name'] == name and 
                    int(row['speed']) == speed and 
                    int(row['mtu']) == mtu and 
                    int(row['framesize']) == framesize and 
                    row['use_udp'].capitalize() == use_udp and 
                    row['use_tcp'].capitalize() == use_tcp):
                        result = 'Pass'
                        break
                else:
                    result = 'Fail'

    else:
        form = LogForm()


    return render(request,'analysis/home.html', {'form': form, 'result': result})
