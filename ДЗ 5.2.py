inp = int(input())

days = inp // 60 // 60 // 24

razn_d = inp - (days * 24 * 60 * 60)
hours = razn_d // 60 // 60

razn_m = razn_d - (hours * 60 * 60)
minutes = razn_m // 60

razn_s = razn_m - (minutes * 60)
sec = razn_s

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if sec < 10:
    sec = '0' + str(sec)
    
if days == 1 or days in list(range(21, 100, 10)):   
    print(f'{days} день, {hours}:{minutes}:{sec}')
elif days > 21 and str(days)[1] in '234' or 1 < days < 5:   
    print(f'{days} дня, {hours}:{minutes}:{sec}')
else:
    print(f'{days} дней, {hours}:{minutes}:{sec}')

