import zipfile
import sys
archive = zipfile.ZipFile(sys.argv[1], 'r')


infolist = archive.infolist()
for info in infolist:
    print(info.comment)