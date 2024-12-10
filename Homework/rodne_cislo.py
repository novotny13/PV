import csv
import multiprocessing
import threading
import time
import hashlib

#Na nize uvedeny zdrojovy kod v uloze 12.6 nesahat !
def hledej(od, do, hash_rc):
    i = 0
    with open('dluznici.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  #preskoci prvni radek s hlavickou
        for row in reader:
            if i > od and i < do and hashlib.sha384(row[1].encode()).hexdigest() == hash_rc:
                print("Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(row[0],row[1], row[2]))
                break
            i = i+1
#Na vyse uvedeny zdrojovy kod v uloze 12.5 nesahat !


if __name__ == "__main__":

    hash_hledaneho_rc = "5275a2bd25897f396e5f1de8b1ede4fe94d960b20619c772a3b4eccd04430afdabc44e5d388f175aa72428e009ff927c"

    start = time.time()
    t1 = multiprocessing.Process(target=hledej,args=(0, 1_000_000, hash_hledaneho_rc))
    t2 = multiprocessing.Process(target=hledej,args=(1_000_001, 2_000_000, hash_hledaneho_rc))
    t3 = multiprocessing.Process(target=hledej,args=(2_000_001, 3_000_000, hash_hledaneho_rc))
    t2.start()
    t1.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end = time.time()

    print("Vypocet bez trval {:.6f} sec.".format((end - start)))
    # start = time.time()
    # t1 = multiprocessing.Process(target=hledej, args=(0, 1_000_000, hash_hledaneho_rc))
    # t2 = multiprocessing.Process(target=hledej, args=(1_000_001, 2_000_000, hash_hledaneho_rc))
    # t3 = multiprocessing.Process(target=hledej, args=(2_000_000, 3_000_000, hash_hledaneho_rc))
    # t2.start()
    # t1.start()
    # t3.start()
    # end = time.time()
    # print("Vypocet bez trval {:.6f} sec.".format((end - start)))