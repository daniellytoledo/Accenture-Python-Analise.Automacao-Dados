import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # chama um algotimo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # frase para o usuário dizer
        print("Diga alguma coisa: ")

        # armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        # passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        elif "Fechar" in frase:
            print("Encerrando...")
            return True
    # se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi o que foi dito!")
        return False
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de voz.")
        
    return frase

while True:
    if ouvir_microfone():
        break

