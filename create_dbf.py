import dbf

# Create a new DBF file
table = dbf.Table('users.dbf', 'ID C(10); Name C(50); Age N(3, 0)')
table.open(mode=dbf.READ_WRITE)

# Add records
table.append(('1', 'John Doe', 30))
table.append(('2', 'Jane Smith', 25))

# Commit and close
table.close()

# Read the records
with dbf.Table('users.dbf') as table:
    for record in table:
        print(f"ID: {record.ID}, Name: {record.Name}, Age: {record.Age}")

