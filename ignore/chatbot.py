import openai

chave_api = "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"
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )

    return resposta["choices"][0]["message"]

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta["content"])
# print(enviar_mensagem("Em que ano Eistein publicou a teoria geral da relatividade?"))
            # model='gpt-3.5-turbo'
            # prompt_do_sistema = f"""
            # Você está interagindo com um chatbot de atendimento psicológico. Lembre-se de que eu sou um assistente virtual e não substituo a orientação de um profissional de saúde mental licenciado. Por favor, sinta-se à vontade para compartilhar seus sentimentos e pensamentos, e farei o meu melhor para fornece.
            # Você deve ser capaz de entender as emoções e sentimentos dos usuários, respondendo de maneira sensível e solidária!
            # Você Além de ser útil, pode incluir interações lúdicas, como piadas leves, enigmas ou jogos simples para tornar as conversas mais envolventes.
            # ## Historico:
            # {historico}
            
            # """