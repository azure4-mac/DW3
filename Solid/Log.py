class Notificacao:
    def __init__(self, mensagem, recipient_email):
        self.mensagem = mensagem
        self.recipient_email = recipient_email

    def send(self):
        print(f"Enviando notificação para {self.recipient_email}: {self.mensagem}")

    def enviar(self):
        print(f"Notificação: {self.mensagem}") 

class Logger:
    def __init__(self, notificacao: Notificacao):
        self.notificacao = notificacao
    
    def save(self):
        with open("log.txt", "a") as log_file:
            log_file.write(f"{self.notificacao.mensagem}\n")

notificacao = Notificacao("Este é um log de teste.")
notificacao.send()

logger = Logger(notificacao)
logger.save()