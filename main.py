import gzip
import re

regexMain = '(.{3}\s{1,10}\d\s\d{1,2}\:\d{1,2}\:\d{1,2})\s{1,10}(.+?)\s(.+?)\s(.+?\s.+?)\s(.+?)\s-\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(\".+?")\s-\s(.+?)\s(.+)$'
regexSecond = '(.{3}\s{1,10}\d\s\d{1,2}\:\d{1,2}\:\d{1,2})\s{1,10}(.+?)\s(.+?)\s(.+?\s.+?)\s(.+?)\s-\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+?)\s(.+)$'
with open('output.csv', 'w') as output:
    with gzip.open('csv_example.csv.gz', 'rt') as f:
        for line in f:
            m = re.match(regexMain, line)
            if not m:
                m2 = re.match(regexSecond, line)
                if not m2:
                    print('ERROR: ' + line)
                else:
                    out = ''
                    for j in range(len(m2.groups())):
                        if j + 1 == 6 or j + 1 == 7:
                            #Тут должен был быть метод (GET/POST) либо протокол, но их не оказалось, так что ставим прочерк (-)
                            out = out + "-;" + m2.group(j+1) + ';'
                        else:
                            out = out + m2.group(j+1) + ';'
                    output.write(out)
                    #print(out)
            else:
                out = ''
                for j in range(len(m.groups())):
                    out = out + m.group(j+1) + ";"
                output.write(out)
                #print(out)