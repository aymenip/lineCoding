from django.shortcuts import render, redirect
from .forms import EncoderForm
from Utils import generator, encode_and_plot


def index(request):
    return render(request, 'encoder/home.html')


def encode(request):
    form = EncoderForm()
    if request.method == "POST":
        form = EncoderForm(request.POST)
        if form.is_valid():
            request.session['temp_data'] = form.cleaned_data
            pos = form['pos_logic'].data
            custom = form['custom'].data
            if custom:
                seq = list(map(int, list(form['custom_bits'].value())))
            else:
                bit_size = int(form['bit_size'].data)
                seq = generator.generate(bit_size)
            scheme = form['scheme_choice'].data
            if scheme == 'AMI':
                uri = encode_and_plot.plot_ami(seq, pos)
            else:
                if scheme == 'Unipolar':
                    uri = encode_and_plot.plot_unipolar(seq, pos)
                elif scheme == 'NRZ-L':
                    uri = encode_and_plot.plot_nrz_l(seq, pos)
                elif scheme == 'NRZ-I':
                    uri = encode_and_plot.plot_nrz_i(seq, pos)
                elif scheme == 'Manchester':
                    uri = encode_and_plot.plot_manchester(seq, not pos)
                elif scheme == 'Polar RZ':
                    uri = encode_and_plot.plot_rz(seq)
                elif scheme == 'Unipolar RZ':
                    uri = encode_and_plot.plot_unipolar_rz(seq)
                else:
                    uri = encode_and_plot.plot_differential_manchester(
                        seq, pos)
            pal_img = {}
            pal_img['uri'] = uri
            pal_img['palindrome'] = generator.manachers_algorithm(seq)
            request.session['data_img'] = pal_img
            return redirect('results', scheme=scheme)
        else:
            print("Error! Check Form Validation!")
    return render(request, 'encoder/encode.html', {'title': "Encode", 'form': form})


def decode(request):
    return render(request, 'encoder/decode.html', {'title': "Decode"})


def about(request):
    return render(request, 'encoder/about.html', {'title': "About"})


def results(request, scheme):
    data = request.session.get('temp_data')
    pal = (request.session.get('data_img'))['palindrome']
    pal = [str(i) for i in pal]
    data['palindrome'] = "".join(pal)
    data['uri'] = (request.session.get('data_img'))['uri']
    return render(request, 'encoder/result.html', data)
