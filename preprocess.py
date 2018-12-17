f = open("climate_data_miyako.csv")
for l in f:
    l.replace('）', '')
    print(l)
