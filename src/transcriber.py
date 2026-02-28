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
      modelo = whisper.load_model(f"{['tiny', 'base', 'small', 'medium'][versao-1]}")


      resultado = modelo.transcribe("audioyt.m4a",   # Transcreve o arquivo de áudio "audioyt.m4a"
                                    fp16=False,      # fp16=False: desativa precisão reduzida (compatibilidade)
                                    language ="pt")  # language="pt": força o idioma português




      with open("transcricao.txt",         # Salva a transcrição em um arquivo de texto
            "w",                       # "w": modo escrita
            encoding="utf-8") as f:    # encoding="utf-8": suporte a caracteres especiais
      # resultado["text"] contém o texto transcrito
            f.write(resultado["text"])