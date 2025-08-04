import pywhatkit
import time
import random

# ===== CONFIGURAÇÕES ===== 
numeros = [
    "+559987878787"   # Segundo melhor telefone
]

# Tempo de espera entre mensagens (em segundos)
intervalo_resposta = random.randint(180, 300)  # 3 a 5 minutos
intervalo_final = random.randint(180, 360)     # 3 a 6 minutos

def enviar_mensagens():
    for numero in numeros:
        try:
            print(f"\nEnviando mensagem para {numero}...")

            # PRIMEIRA MENSAGEM (Olá, tudo bem?)
            pywhatkit.sendwhatmsg_instantly(
                phone_no=numero,
                message="Olá, boa tarde. Tudo bem?",
                tab_close=True
            )
            print("✔ Mensagem 1 enviada!")

            # AGUARDA RESPOSTA (3-5 minutos)
            print(f" Aguardando {intervalo_resposta // 60} minutos...")
            time.sleep(intervalo_resposta)

            # SEGUNDA MENSAGEM (Pedido de contato com o responsável)
            pywhatkit.sendwhatmsg_instantly(
                phone_no=numero,
                message="Então, eu precisava falar com quem cuida da agenda do responsável e decisor de vocês na área de infraestrutura/energia, pois meu diretor gostaria de uma reunião com ele. Pode me ajudar?",
                tab_close=True
            )
            print("✔ Mensagem 2 enviada!")

            # AGUARDA RESPOSTA (3-6 minutos)
            print(f" Aguardando {intervalo_final // 60} minutos...")
            time.sleep(intervalo_final)

            # TERCEIRA MENSAGEM (Caso a pessoa pergunte "Quem são vocês?")
            pywhatkit.sendwhatmsg_instantly(
                phone_no=numero,
                message="Nós somos uma empresa que está investindo, ao todo, mais de 1,2 bilhões no nordeste, em regiões onde vocês atuam, e seria muito importante essa conversa.",
                tab_close=True
            )
            print("✔ Mensagem 3 enviada!")

        except Exception as erro:
            print(f" Erro ao enviar para {numero}: {erro}")

# ===== INICIAR O BOT ===== #
if __name__ == "__main__":
    print("- - - - BOT WHATSAPP INICIADO - - - -")
    enviar_mensagens()
    print("✔ Todas as mensagens foram enviadas!")