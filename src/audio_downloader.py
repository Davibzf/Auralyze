def download_audio():
    # Importações
    from pytubefix import YouTube
    from pytubefix.cli import on_progress

    # Entrada do usuário
    while True:
        try:
            url = input("🔗 Digite a url: ")
            yt = YouTube(url, on_progress_callback=on_progress)
            break
        except:
            print("❌ URL inválida. Por favor, tente novamente.")
        

    # Exibição das informações do vídeo
    print(f"\n📹 Título: {yt.title}")
    duraçao = yt.length
    print(f"⏱️ Duração: {duraçao // 60} minutos e {duraçao % 60} segundos")
    print(f"👤 Autor: {yt.author}")

    # Download do áudio
    print("\n🔄 Iniciando download do áudio...")
    ys = yt.streams.get_audio_only()
    ys.download(filename="audioyt.m4a")
    print('✅ Download concluído!')