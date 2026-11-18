from database.connection import conectar
def criar_banco():
 c=conectar();cur=c.cursor()
 cur.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY,nome TEXT,telefone TEXT,email TEXT,data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
 cur.execute("CREATE TABLE IF NOT EXISTS profissionais(id INTEGER PRIMARY KEY,nome TEXT,especialidade TEXT)")
 cur.execute("CREATE TABLE IF NOT EXISTS servicos(id INTEGER PRIMARY KEY,nome TEXT,duracao INTEGER,valor REAL)")
 cur.execute("CREATE TABLE IF NOT EXISTS agendamentos(id INTEGER PRIMARY KEY,cliente_id INTEGER,profissional_id INTEGER,servico_id INTEGER,data_agendamento TEXT,horario TEXT,status TEXT DEFAULT 'Agendado')")
 c.commit();c.close()
