from audio_downloader import download_audio
from transcriber import transcribe_audio
from llm_client import summarize_text
import os
import time

def verificar_arquivo(nome_arquivo, tempo_espera=2):
    """Verifica se um arquivo existe e aguarda se necessário"""
    for _ in range(3):  # 3 tentativas
        if os.path.exists(nome_arquivo):
            return True
        print(f"⏳ Aguardando arquivo '{nome_arquivo}'...")
        time.sleep(tempo_espera)
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("🎵 PIPELINE DE PROCESSAMENTO DE ÁUDIO 🎵".center(60))
    print("=" * 60)
    
    # Etapa 1: Download
    print("\n📥 ETAPA 1: Download do áudio")
    print("-" * 40)
    download_audio()
    
    # Verificar se o áudio foi baixado
    if not verificar_arquivo("audioyt.m4a"):
        print("❌ Arquivo de áudio não encontrado. Abortando.")
        exit(1)
    
    # Etapa 2: Transcrição
    print("\n📝 ETAPA 2: Transcrição do áudio")
    print("-" * 40)
    transcribe_audio()
    
    # Verificar se a transcrição foi gerada
    if not verificar_arquivo("transcricao.txt"):
        print("❌ Arquivo de transcrição não encontrado. Abortando.")
        exit(1)
    
    # Etapa 3: Resumo
    print("\n🤖 ETAPA 3: Geração de resumo")
    print("-" * 40)
    summarize_text()
    
    print("\n" + "=" * 60)
    print("✅ PROCESSO CONCLUÍDO COM SUCESSO!".center(60))
    print("=" * 60)