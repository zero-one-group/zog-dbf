from dbfread import DBF


# Iterate over records
for record in DBF("users.dbf"):
    print(record)

