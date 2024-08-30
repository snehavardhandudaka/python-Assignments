from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
ftp.retrbinary('RETR test.txt', open('test.txt', 'wb').write)
ftp.quit()
