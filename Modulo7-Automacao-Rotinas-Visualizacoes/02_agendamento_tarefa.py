# Agendamento de Tarefas
# Scripts programados
# Em sistemas reais, scripts podem ser executados automaticamente em horários específicos.

import datetime

agora = datetime.datetime.now()
print("Script executado em: ", agora)

def executar_relatorio():
    agora = datetime.datetime.now()
    print("Gerando relatório...")
    print("Horário: ", agora)

executar_relatorio()

# ---------------------------------------------------------------------------------------

# Cron Jobs
# Em sistemas Linux, utilizamos Cron Jobs para agendar tarefas. Exemplo:
# Executar um script todos os dias Às 8h:
# 0 8 * * * python script.py

def gerar_relatorio():
    vendas = [120, 200, 150, 300]
    total  = sum(vendas)
    agora = datetime.datetime.now()

    print("Relatório gerado em: ", agora)
    print("Total de vendas: ", total)

gerar_relatorio()

# ---------------------------------------------------------------------------------------

# Como isso funciona na prática:

# Fluxo real de automação:

# 1º criamos um script Python (ex. relatorio.py)
# 2º adicionamos um cron job no servidor como o exemplo acima 0 8 * * * python script.py
# 3º o sistema executará o script automaticamente todos os dias às 08:00.

# ---------------------------------------------------------------------------------------

# Monitoramento
# Quando automatizamos processos, precisamos monitorar se os scripts estão funcionando corretamente. Uma forma comum de fazer isso é usando logs.

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Script de automação iniciado!")