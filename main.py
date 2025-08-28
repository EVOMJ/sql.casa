# 1. UPDATE – Aumentando salário
# A empresa decidiu aumentar o salário de todos os funcionários do departamento de TI em 10%.
# 👉 Escreva o comando UPDATE que faça essa alteração.

import sqlite3 as sql


mm = sql.connect('ricardaofather.db')

cursor = mm.cursor()

# cursor.execute("UPDATE funcionarios SET salario = salario * 1.10 WHERE departamento = 'TI' ")
# cursor.execute("UPDATE funcionarios SET telefone = '(11) 98888-7777'  WHERE  cpf=15967994960  ")
cursor.execute("UPDATE funcionarios SET cidade ='São Paulo' WHERE  id = 25;")
mm.commit()