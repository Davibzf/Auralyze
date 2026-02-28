def summarize_text():
    # Importação da biblioteca Google Gemini AI
    from google import genai
    import time


    # Abre e lê o arquivo de transcrição criado anteriormente
    max_tentativas = 3
    for tentativa in range(max_tentativas):
        try:
            with open('transcricao.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                break
        except FileNotFoundError:
            if tentativa < max_tentativas - 1:
                print(f"❌ Arquivo 'transcricao.txt' não encontrado. Tentativa {tentativa + 1}/{max_tentativas}")
                print("⏳ Aguardando 2 segundos...")
                time.sleep(2)
            else:
                print("❌ Arquivo de transcrição não encontrado após 3 tentativas.")
                print("💡 Execute primeiro o download e a transcrição do áudio.")
                return
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return


    # Cria cliente com sua chave de API (autenticação)
    # Substitua "SUA_API_KEY_AQUI" pela sua chave real
    API_KEY = "SUA_API_KEY_AQUI"  # <-- COLOQUE SUA CHAVE AQUI
    genai.configure(api_key=API_KEY)

    # Criar o prompt
    pergunta = f"""
    Faça um resumo breve e conciso do seguinte conteúdo:
    
    {conteudo}
    
    Resumo:
    """

    print("\n🔄 Gerando resumo com Gemini...")

    try:
        # Escolher o modelo (nomes corretos dos modelos)
        modelo = genai.GenerativeModel('gemini-1.5-flash')  # ou 'gemini-pro'
        
        # Gerar o conteúdo
        response = modelo.generate_content(pergunta)
        
        # Extrair e exibir a resposta
        if response.text:
            print("\n📝 RESUMO GERADO:\n")
            print(response.text)
            
            # Salvar o resumo em arquivo
            with open("resumo.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("\n✅ Resumo salvo em 'resumo.txt'")
        else:
            print("❌ Resumo vazio ou bloqueado pela API")

    except Exception as e:
        print(f"❌ Erro ao gerar resumo: {e}")
        print("💡 Verifique sua chave de API e conexão com internet")
