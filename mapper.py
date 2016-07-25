#!/usr/bin/python3.4
#funzione che mi permette di aprire e leggere il file
def openFile():
    with open('hotelworld-sample-data.txt', 'r') as f:
        return f.readlines()
#funzione che legge i dati nel file
def getData(x):
#ciclo for per ogni linea del file
    for line in x:
#divido le linee
        i = line.split(';')

        print i[0].strip() + "\t" + i[1].strip() + "\t" + i[2].strip() + "\t" + i[3].strip()

if __name__ == "__main__":
    x = openFile()
    getData(x)
    # closeFile(x)
