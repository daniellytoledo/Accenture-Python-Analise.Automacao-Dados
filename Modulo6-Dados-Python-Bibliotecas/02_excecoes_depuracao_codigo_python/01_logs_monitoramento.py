# Logs e Monitoramento
# Em sistemas reais usamos logs para registrar eventos no sistema. 

# Módulo logging
# Python possui um módulo chamado logging para registrar eventos que acontecem durante a execução de um programa.
# Ao invés de usar print(), é recomendado usar logging, pois ele permite:

# exibir mensagens de diferentes níveis de importância
# salvar mensagens em arquivos
# controlar quais mensagens serão exibidas
# facilitar a identificação de erros

import logging

logging.basicConfig(level=logging.INFO) # Essa linha configura o comportamento do logger. Significa: "Mostre todas as mensagens de nível INFO ou superior."
logging.info("Programa iniciado.") # Como o nível configurado é INFO, essa mensagem será exibida.

# Níveis     |  Valor  |  Quando usar

# DEBUG      |   10    |  Informações detalhadas para desenvolvimento
# INFO       |   20    |  Informações normais sobre o funcionamento
# WARNING    |   30    |  Algo inesperado aconteceu, mas o programa continua
# ERROR      |   40    |  Ocorreu um erro que impediu parte do programa
# CRITICAL   |   50    |  Erro grave que pode interromper o programa

logging.debug("Entrando na função")       
logging.info("Programa iniciado")         
logging.warning("Pouco espaço em disco")  
logging.error("Erro ao abrir o arquivo")  
logging.critical("Sistema encerrado")

# Saída

# INFO:root:Programa iniciado
# WARNING:root:Pouco espaço em disco
# ERROR:root:Erro ao abrir o arquivo
# CRITICAL:root:Sistema encerrado

# Perceba que a mensagem DEBUG não aparece, porque o nível mínimo configurado foi INFO.