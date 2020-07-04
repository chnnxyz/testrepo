def percentage(w,row):
    if w='wins':
        return row[1]/(row[1]+row[2]+row[3])
    elif w = 'losses':
        pass

with open(csvfile,'r') as csvdude:
    creader=csv.reader(csvdude)
    for row in creader:
        print(percentage('wins',row))

        #comment