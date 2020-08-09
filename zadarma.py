import re
import csv 

# функция суммирования
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return round(theSum, 2)

# функция подсчета статистики
def statistic(name, list_ring):
    summ_answered = [] # сумма по отвеченным
    time_answered = [] # длительность по отвеченным
    name = str(name)   # название страны
    for line in list_ring:
        if line[6] == 'answered' and line[-2] != '0.0000':
            summ_answered.append(float(line[-2]))
            time_answered.append(float(line[-4]))
    all_ring = len(time_answered)
    print(name, ': всего отвеченных звонков:', all_ring, 'на сумму',
          listsum(summ_answered), 'руб.', 'Длительность:',
          listsum(time_answered)/60, 'минут(ы)' )
     
    
# инициализируем cписки направлений
ukr_zadarma=[]
uzb_zadarma=[]
bel_zadarma=[]
kaz_zadarma=[]
usa=[]
russia=[]
germany=[]
kyrg=[]
moldova=[]
uk=[]

# Открываем файл и делим на направления
with open ('stat_zadarma.csv',encoding='utf8', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for line in csv_reader:
        for i in line:
            if re.search(r'Ukraine', i):
                ukr_zadarma.append(line)
            elif re.search(r'Uzbekistan', i):
                uzb_zadarma.append(line)
            elif re.search(r'Belarus', i):
                bel_zadarma.append(line)
            elif re.search(r'KAZAKHSTAN', i) or re.search(r'Kazakhstan', i):
                kaz_zadarma.append(line)
            elif re.search(r'Kyrgyzstan', i) or re.search(r'KYRGYZSTAN', i):
                kyrg.append(line)
            elif re.search(r'Usa', i):
                usa.append(line)
            elif re.search(r'Russia', i):
                russia.append(line)
            elif re.search(r'Germany', i):
                germany.append(line)
            elif re.search(r'Moldova', i) or re.search(r'MOLDOVA', i):
                moldova.append(line)
            elif re.search(r'United Kingdom', i):
                uk.append(line)

#Выводим статистику

statistic('Узбекистан', uzb_zadarma)
statistic('Украина', ukr_zadarma)
statistic('Беларусь', bel_zadarma)
statistic('Казахстан', kaz_zadarma)
statistic('США', usa)
statistic('Россия', russia)
statistic('Германия', germany)
statistic('Кыргызстан', kyrg)
statistic('Молдова', moldova)
statistic('Великобритания', uk)


        
