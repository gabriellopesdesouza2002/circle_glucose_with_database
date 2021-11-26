from datetime import datetime

import mysql.connector
from time import strptime, strftime

# PEGA O ID E O NOME DO USUÁRIO
nome = ''
id = 0


def pega_id(email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f"SELECT id FROM usuarios WHERE email = '{email}'")
    # SQL CODE
    for id_tuple in cur:
        for id_num in id_tuple:
            global id
            id = id_num
        # SQL CODE
        cur.execute(f'SELECT nome FROM usuarios WHERE id = "{id}"')
        # SQL CODE
        for nome_tuple in cur:
            for nome_dado in nome_tuple:
                global nome
                nome = nome_dado
    cur.close()
    conexao.commit()
    conexao.close()


# PEGA O NOME E O ID DO USUÁRIO


# FUNÇÃO PARA ADICIONAR NOVO USUARIO AO BANCO DE DADOS EM CASO DE CADASTRO
def adiciona_usuario(nome, email, senha):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f"insert into usuarios(nome, email, senha) values('{nome}', '{email}', '{senha}')")
    # SQL CODE
    cur.close()
    conexao.commit()
    conexao.close()


# FUNÇÃO PARA ADICIONAR NOVO USUÁRIO AO BANCO DE DADOS EM CASO DE CADASTRO


# pegar emails dos usuários para validação
emails = []


def recupera_emails():
    global emails
    emails = []
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute('SELECT email FROM usuarios')
    # SQL CODE
    for emails_tuple in cur:
        for email in emails_tuple:
            emails.append(email)
    else:
        emails = tuple(emails)

    cur.close()
    conexao.commit()
    conexao.close()


# pegar emails dos usuários para validação


senhas = []


def recupera_senhas():
    global senhas
    senhas = []
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute('SELECT senha FROM usuarios')
    # SQL CODE
    for senha_tuple in cur:
        for senha in senha_tuple:
            senhas.append(senha)
    else:
        senhas = tuple(senhas)
    cur.close()
    conexao.commit()
    conexao.close()


def altera_email(email_antigo, email_novo):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f'UPDATE usuarios SET email = "{email_novo}" where email = "{email_antigo}"')
    # SQL CODE
    cur.close()
    conexao.commit()
    conexao.close()


def altera_senha(senha_atual, senha_nova):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f'UPDATE usuarios SET senha = "{senha_nova}" where senha = "{senha_atual}"')
    # SQL CODE
    cur.close()
    conexao.commit()
    conexao.close()


# Dados das glicemias e Dados dos horários para serem colocados no gráfico.

# OPERAÇÕES NA TABELA DE [AO LEVANTAR] (INSERÇÃO E CONSULTA DE DADOS)
def envia_glic_ao_levant(id_user, glicemia, data, hora):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f'INSERT INTO glicemias_ao_levant_users(id_usuario, glicemia, data_glicemia, hora_glicemia) '
                f'VALUES({id_user}, {glicemia}, "{data}", "{hora}")')
    # SQL CODE
    cur.close()
    conexao.commit()
    conexao.close()


glicemias_01 = []
glicemias_01_hora = []
#
# for hora in glicemias_01_hora:
#         if strptime(hora, '%H:%M:S'):
#             return datetime.strptime(data_str, '%d/%m/%y').date()
#     except ValueError:
#         return False
glicemias_01_data = []


def recupera_glicemia_glic_ao_levant():
    global id
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='bolarede792',
        database='circle_glucose',
        port='3306'
    )
    cur = conexao.cursor(buffered=True)
    # SQL CODE
    cur.execute(f'select glicemia from glicemias_ao_levant_users where id_usuario = "{id}"')
    for glicemia_tuple in cur:
        for glicemia in glicemia_tuple:
            global glicemias_01
            glicemias_01.append(glicemia)
    cur.execute(f'select hora_glicemia from glicemias_ao_levant_users where id_usuario = "{id}"')
    for hora_glicemia_tuple in cur:
        for hora in hora_glicemia_tuple:
            global glicemias_01_hora
            glicemias_01_hora.append(hora)
    cur.execute(f'select data_glicemia from glicemias_ao_levant_users where id_usuario = "{id}"')
    for data_glicemia_tuple in cur:
        for data in data_glicemia_tuple:
            global glicemias_01_data
            glicemias_01_data.append(data)
    # SQL CODE
    cur.close()
    conexao.commit()
    conexao.close()


glicemias_02 = []
glicemias_02_hora = []
glicemias_03 = []
glicemias_03_hora = []
glicemias_04 = []
glicemias_04_hora = []
glicemias_05 = []
glicemias_05_hora = []
glicemias_06 = []
glicemias_06_hora = []
glicemias_07 = []
glicemias_07_hora = []
glicemias_08 = []
glicemias_08_hora = []
glicemias_09 = []
glicemias_09_hora = []

dicio_glicemia = {'Ao levantar': glicemias_01,
                  'Antes do almoço': glicemias_02,
                  'Depois do almoço': glicemias_03,
                  'Antes do lanche': glicemias_04,
                  'Depois do lanche': glicemias_05,
                  'Antes do jantar': glicemias_06,
                  'Depois do jantar': glicemias_07,
                  'Ao dormir': glicemias_08,
                  'Sem Período Especificado': glicemias_09,
                  }

recupera_senhas()
recupera_emails()


###################### validação e conversão da data e hora p/ o banco de dados ###########
def valida_data(data_str):
    try:
        if type(data_str) == str:
            strptime(data_str, '%d/%m/%y')  # se a data que vir for desse formato, irá retornar True

            d_u = int(data_str[:2])
            d_valid = int(strftime('%d'))
            m_u = int(data_str[3:5])
            m_valid = int(strftime('%m'))
            y_u = int(data_str[6:])
            y_valid = int(strftime('%y'))
            if d_u <= d_valid and m_u <= m_valid and y_u <= y_valid:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


def convert_data(data_str):
    try:
        if strptime(data_str, '%d/%m/%y'):
            return datetime.strptime(data_str, '%d/%m/%y').date()
    except ValueError:
        return False


# validação e conversão da data p/ o banco de dados


# validação e conversão da hora p/ o banco de dados
def valida_hora(hora_str):
    try:
        if type(hora_str) == str:
            strptime(hora_str, '%H:%M')  # se a data que vir for desse formato, irá retornar True
            h_u = int(hora_str[:2])
            m_u = int(hora_str[3:])
            # h_valid = int(strftime('%H'))
            # m_valid = int(strftime('%M'))

            if h_u <= 23 and m_u >= 00 and m_u <= 59:
                return True
            else:
                return False
    except ValueError:
        return False
# validação e conversão da hora p/ o banco de dados
