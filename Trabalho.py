import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")


myresult = mycursor.fetchall()


i = 1
for registro in myresult:   
    print(i ,"-"  , registro[0])
    i = i + 1


print("Escolha uma tabela")
tabela = input()


mycursor2 = mydb.cursor()

mycursor2.execute(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabela}' and table_schema = 'northwind'")

myresult2 = mycursor2.fetchall()

i = 1
for registro2 in myresult2:
    print(i, "-" , registro2[0])
    i = i + 1

print("Escolha o campo que deseja pesquisar.")
campo = input()
print("")
print("Digite sua pesquisa.")
pesquisa = input() 



cursor = mydb.cursor()
cursor.execute('SELECT * FROM {}').format(tabela)
result = cursor.fetchall()
for r in result:
    print(result)




