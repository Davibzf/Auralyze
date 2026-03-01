def transcribe_audio():
      # Importação da biblioteca Whisper (reconhecimento de fala da OpenAI)
      import whisper

      print("Versões do modelo Whisper disponíveis:")
      print("1 - tiny")
      print("2 - base")
      print("3 - small")
      print("4 - medium")
      while True:
            versao = int(input("\n⚡ Escolha a versão do modelo (1-4): "))
            if 1 <= versao <= 4:
                  break
            print("⚠️  Versão inválida. Tente novamente.")

      # Carrega o modelo "base" (equilibrado entre velocidade e precisão)
      # Outras opções: tiny, small, medium, large
      modelos = ["tiny", "base", "small", "medium"]
      modelo = whisper.load_model(modelos[versao-1])
      print(f"Modelo '{modelos[versao-1]}' carregado com sucesso!")

      resultado = modelo.transcribe("audioyt.m4a",   # Transcreve o arquivo de áudio "audioyt.m4a"
                                    fp16=False,      # fp16=False: desativa precisão reduzida (compatibilidade)
                                    language ="pt")  # language="pt": força o idioma português




      with open("transcricao.txt", "w", encoding="utf-8") as f:    
            f.write(resultado["text"])