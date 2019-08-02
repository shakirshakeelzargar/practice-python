from ftplib import FTP
import pandas as pd

#Connecting to FTP server
host = 'hostname'
ftp = FTP(host)

# Login to ftp

ftp.login("username","password")

#sourcefolder

ftp.cwd('sourcefolder')
print(ftp.retrlines('LIST'))

#Destination folder
out = 'destinationpath'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'sales.csv', f.write)
    f.close()
    
df=pd.read_csv("./ftp/salesfile.csv")
df.head()