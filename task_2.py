time = int(input('Vvedite vremya v secundah: '))

if time < 60:
    print (f'Vremya 00:00:{time:02}')
elif time <3600:
    print (f'Vremya 00:{time//60}:{time:02}-{time//60}')
else:
    print (f'Vremya {time//36000:02}//3600:{time//60::02}:{time:02}-{time//60:02}')