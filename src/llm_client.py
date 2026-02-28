def summarize_text():
    # Importação da biblioteca Google Gemini AI
    from google import genai


    # Abre e lê o arquivo de transcrição criado anteriormente
    with open('transcricao.txt', 'r') as arquivo:
        conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
        # Cria uma pergunta/prompt para a IA
        pergunta = f"""
    Faça um resumo breve do
    contedudo: {conteudo}
    """

    # Cria cliente com sua chave de API (autenticação)
    # Substitua "SUA_API_KEY_AQUI" pela sua chave real
    genai.Client(api_key="SUA_API_KEY_AQUI")

    # Envia a pergunta para o modelo Gemini
    # model='gemini-flash-lite-latest': modelo rápido e leve
    # contents=pergunta: o prompt que criamos
    response = genai.GenerativeModel('gemini-flash-lite-latest').generate_content(       
        contents=pergunta                       
    )


    # Extrai e exibe a resposta gerada
    resp = response.text                 # Pega o texto da resposta
    print(resp)                          # Mostra o resumo no terminal