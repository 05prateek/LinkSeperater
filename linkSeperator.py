import json
if __name__ == '__main__':
    name=[]
    link=[]
    
    data = []
    with open('input/file.txt', mode='r', encoding='utf8') as f:
        for line in f:
            #print(line)
            i=0
            x = line.split('https://')
            name.append(x[0])
            link.append('https://' + x[1])

with open('output/name.txt', mode='w',encoding='utf8') as fo:
    for i in name:
        fo.write(i+"\n")
    fo.close()

with open('output/links.txt', mode='w',encoding='utf8') as fo:
    for i in link:
        fo.write(i)
    fo.close()
    