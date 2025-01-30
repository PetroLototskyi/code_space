# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# https://github.com/mkleehammer/pyodbc/issues/517
# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows

# Output as input
# https://stackoverflow.com/questions/4744019/how-to-give-the-output-of-the-first-querywhich-has-two-values-as-the-input-to


import pyodbc
from tabulate import tabulate
# import csv

# import pandas as pd


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net'
# server = 'APPSERVER2\MISYS' # SQL instance
# server = '192.168.1.34\MISYS,1433' # SQL instance

# server = 'MISYS_Sandbox'
# database = 'ROANWELL'
# username = 'jantonik'
# password = 'sandbox'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; '
                      'SERVER=APPSERVER2\MISYS;'
                      'DATABASE=uniPoint_Roanwell;'
                      'PORT=49782;'
                      'UID=jantonik;'  # hq.roanwellcorp.com
                      'PWD=PigeonLandTree;'
                      # 'TrustServerCertificate=YES;'
                      # 'TrustServerCertificate=YES;'
                      'Encrypt=no;'
                      'Trusted_Connection=no;'
                      )

cursor = cnxn.cursor()
# cursor.execute("SELECT TOP 10 * FROM PT_InspectionSpecification_Measurement WHERE InspectionSpecification_No='10014'"
#                " ORDER BY Name") #  ORDER BY DOC_ID")
# cursor.execute("SELECT * FROM PT_Inspection WHERE InspectionSpecification_No='10014'") #  ORDER BY DOC_ID")
# Inspection_No 20035 20036
cursor.execute("SELECT * FROM PT_Todo") #  ORDER BY DOC_ID")


# df_request = pd.read_sql("SELECT * FROM PT_Request", cnxn)
# df_request.to_pickle('df_request.pickle')

# regarding the this general issue, I could ask for advice somebody from my previous company, check if they can advise something

# lastID = 12241
# cursor.execute("SELECT count(*) FROM PT_Address WHERE Notes='Added via script'")
# cursor.execute("SELECT * FROM PT_Customer WHERE Customer='VTG'")

# cursor.execute("SELECT * FROM PT_QC_Doc WHERE Doc_Num='990-202-001-10X_PRT'")
# cursor.execute("SELECT Doc_ID FROM PT_QC_Doc ORDER BY Doc_ID DESC")

# cursor.execute("SELECT Doc_Num, Doc_Name, Doc_Date, Revision, Doc_Status, Notes, Doc_Category, File_Path FROM PT_QC_Doc WHERE Doc_Num='494-413-001-XXX_PRT'")

# cursor.execute('UPDATE SystemOptions SET ItemValue=? WHERE ItemName=?', lastID, 'Doc_ID')
# cursor.commit()
# cursor.execute("SELECT TOP 10 * FROM PT_QC_Doc ORDER BY DOC_ID")
# cursor.execute("SELECT * FROM PT_Equip")
# cursor.execute("SELECT * FROM PT_Address WHERE AddressSource='GENTEX'")
# cursor.execute("SELECT * FROM PT_QC_Doc_Security ORDER BY ID")
# rows = cursor.execute("SELECT * FROM PT_NC")
# cursor.execute("SELECT * FROM PT_InspectionItem_Measurement_Log")

# # show all tables
# cursor.execute("SELECT table_name FROM information_schema.tables")
# #
# for table_name in cursor:
#    print(table_name[0])



# lastID = 11931
# cursor.execute('UPDATE SystemOptions SET ItemValue=? WHERE ItemName=?', lastID, 'Doc_ID')
# cursor.commit()

# cursor.execute("UPDATE PT_Customer SET Customer = 'VTG' WHERE Customer='VTGTES'")
# UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;

# cursor.execute("DELETE FROM PT_QC_Doc Where Doc_Category='PD'")
# cursor.execute("DELETE FROM PT_Address WHERE Notes='Added via script'")
# cursor.execute("DELETE FROM PT_Equip WHERE Equip_num='TEST1'")
# cursor.execute("DELETE FROM PT_QC_Doc WHERE Notes='Data added via script 8/24/2023'")
# cursor.commit()
# cursor.execute("SELECT * FROM PT_Vendor_Extended")

# should be cursor.execute


try:
    columns = [column[0] for column in cursor.description]
    print(tabulate(cursor.fetchall(), headers=columns, tablefmt='psql')) # , showindex='always'))
except:
    print('No columns')
    pass

# with open(r'PT_NC.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([x[0] for x in cursor.description])  # column headers
#     for row in rows:
#         writer.writerow(row)



# print(columns)
# print(100*'*')

# test_table = [[columns], [cursor.fetchall()]]
# print(tabulate(test_table, tablefmt='psql', showindex='always'))

cursor.close()
cnxn.close()
