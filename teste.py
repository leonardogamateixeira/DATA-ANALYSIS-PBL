casos =[['23/04', 'Tomba', '2', '2'],
        ['23/04', 'Papagaio', '2', '2'],
        ['23/04', 'Cis', '2', '2'],
        ['24/04', 'Tomba', '1', '1'],
        ['24/04', 'Papagaio', '1', '1'],
        ['24/04', 'Cis', '1', '1']]

confSoma1 = sum([int(row[2]) for row in casos if row[0] == data1])
confSoma2 = sum([int(row[2]) for row in casos if row[0] == data2])
negSoma1 = sum([int(row[3]) for row in casos if row[0] == data1])
negSoma2 = sum([int(row[3]) for row in casos if row[0] == data2])
