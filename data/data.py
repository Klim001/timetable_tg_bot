def weather():
    from bs4 import BeautifulSoup
    import requests
    url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    weat = soup.find('div', class_ = 't_0')
    symb = ' °C'
    return weat.text + symb

def dollar():
    from bs4 import BeautifulSoup
    import requests
    url = 'https://www.rbc.ru/quote/ticker/72413'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    curse = soup.find('span', class_ = 'chart__info__sum')
    symb = curse.text[0]
    return curse.text[1:-2] + symb

def timetable(url, number):
    import requests
    from bs4 import BeautifulSoup
    day_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table', class_='inner_table')
    while len(table) < 7:
        table.append('В этот день расписания нет')
    try:
        table_day = table[number].find_all('tr')
        table_day = table_day[1:]
        return_str = day_of_week[number] + '\n\n'
        for i in range(len(table_day)):
            table_day[i] = table_day[i].text.split('\n')
            table_day[i] = table_day[i][1:-1]
            if str(table_day[i][4]) == 'все':   table_day[i][4] = 'ВСЕ'
            if str(table_day[i][4]) == 'чёт':   table_day[i][4] = 'четная'
            if str(table_day[i][4]) == 'нечет':   table_day[i][4] = 'НЕчётная'

            if str(table_day[i][2]) == ' ' and str(table_day[i][3]) == ' ':
                para = str(table_day[i][0]) + '  ' + str(table_day[i][1]) + '\n' + ' ' + '\n' + ' ' + '\n' + '<b>'+str(table_day[i][4])+'</b>' + '\n'
            elif str(table_day[i][2]) == ' ':
                para = str(table_day[i][0]) + '  ' + str(table_day[i][1]) + '\n' + ' ' + '\n' + str(table_day[i][3]) + '\n' + '<b>'+str(table_day[i][4])+'</b>' + '\n'
            elif str(table_day[i][3]) == ' ':
                para = str(table_day[i][0]) + '  ' + str(table_day[i][1]) + '\n' + str(table_day[i][2]) + '\n' + ' ' + '\n' + '<b>'+str(table_day[i][4])+'</b>' + '\n'
            else:
                para = str(table_day[i][0]) + '  ' + str(table_day[i][1]) + '\n' + str(table_day[i][2]) + '\n' + str(table_day[i][3]) + '\n' + '<b>'+str(table_day[i][4])+'</b>' + '\n'
            return_str += para
            return_str += '\n'
    except Exception as e:
        return_str = day_of_week[number] + '\n'
        return_str += table[number]

    return return_str

if __name__ == '__main__':
    from config import URL_O745B
    print(timetable(URL_O745B, 4))