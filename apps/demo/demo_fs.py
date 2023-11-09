import common.fs as fs

list = fs.read_csv("d:/output/test/test_read_csv.csv")
for row in list:
    print(row)
