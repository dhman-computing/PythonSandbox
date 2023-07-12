# pylint: disable=missing-module-docstring
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# for line in fhand:
#     print(line.decode().strip())

# print(dir(fhand))
print(fhand.getheaders)
