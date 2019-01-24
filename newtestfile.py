import dealinwithcsv
import testfile
a = open(r"filepath.txt","r")
#data stored in file using test .py  can be accesed using filevar
filevar = a.read()
a.close()
print(filevar)
#dealinwithcsv.write_csv()
exit()
