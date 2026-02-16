# 🎙️ Sonarize - Audio Intelligence

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=plastic&logo=python)](https://python.org)
[![Whisper](https://img.shields.io/badge/Whisper-OpenAI-black?style=plastic&logo=openai)](https://openai.com)
[![Gemini](https://img.shields.io/badge/Gemini-Google-blue?style=plastic&logo=google)](https://deepmind.google)
[![PyTubeFix](https://img.shields.io/badge/PyTubeFix-YouTube-red?style=plastic&logo=youtube)](https://pytubefix.github.io/)
[![Status](https://img.shields.io/badge/status-V1--Ativo-brightgreen?style=plastic)]()
[![Licença](https://img.shields.io/badge/licença-MIT-blue?style=plastic)](LICENSE)

**Transforme vídeos do YouTube em resumos inteligentes com IA**

Pipeline completo: **download de áudio → transcrição → resumo com Google Gemini**

---

## 📋 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Pipeline do Sistema](#-pipeline-do-sistema)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Limitações Atuais](#-limitações-atuais-v1)
- [Roadmap](#-próximas-melhorias-roadmap)
- [Autor](#-autor)

---

## 🎯 Sobre o Projeto

**Sonarize** é uma ferramenta que automatiza a extração de conhecimento de vídeos do YouTube:

- 📥 **Baixa** o áudio de qualquer vídeo do YouTube
- 📝 **Transcreve** o áudio para texto usando Whisper (OpenAI)
- 🧠 **Resume** o conteúdo com Google Gemini AI
- 📄 **Gera** um resumo inteligente e salva a transcrição completa

> 💡 *"Como um sonar que mapeia o fundo do mar, o Sonarize mapeia o conteúdo do seu áudio e traz à tona apenas o que importa."*

---

## 🔄 Pipeline do Sistema

```
🔗 URL do YouTube
    ↓
📥 Download do Áudio (PyTubeFix)
    ↓
📝 Speech-to-Text (Whisper)
    ↓
📄 Transcrição Completa (.txt)
    ↓
🧠 Resumo Inteligente (Gemini AI)
    ↓
✨ Resumo Final + Transcrição
```

---

## 🛠️ Tecnologias

| Categoria | Tecnologia | Função |
|-----------|------------|--------|
| **Linguagem** | Python 3.11 | Base do projeto |
| **Download** | PyTubeFix | Baixa áudio do YouTube |
| **STT** | Whisper (OpenAI) | Transcrição áudio → texto (modelo 'base') |
| **LLM** | Google Gemini API | Geração de resumos inteligentes |
| **Formato** | M4A / TXT | Áudio e texto processados |

---

## ⚙️ Pré-requisitos

### Dependências de Sistema
- **FFmpeg** (necessário para Whisper processar áudio)

### Dependências Python
```bash
pytubefix
openai-whisper
google-generativeai
```

---

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sonarize.git

# Entre no diretório
cd sonarize

# Instale as dependências
pip install -r requirements.txt
```

### 🔑 Configuração da API Key

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Gere sua chave da API Gemini
3. Substitua no código:

```python
client = genai.Client(api_key="SUA_API_KEY_AQUI")
```

---

## 🚀 Como Usar

Execute as células do notebook sequencialmente no Google Colab ou Jupyter:

| Etapa | Ação |
|-------|------|
| **1** | Digite a URL do YouTube quando solicitado |
| **2** | Aguarde o download do áudio |
| **3** | Whisper transcreve automaticamente |
| **4** | Gemini gera o resumo |
| **5** | Pronto! Resumo exibido na tela |

---

## 📊 Estrutura do Projeto

O notebook `Sonarize.ipynb` contém 3 células principais:

```python
# 1. DOWNLOAD DO ÁUDIO
- Recebe URL do YouTube
- Baixa apenas o áudio em formato M4A
- Salva como 'audioyt.m4a'

# 2. TRANSCRIÇÃO COM WHISPER
- Carrega modelo Whisper 'base'
- Transcreve áudio para texto (português)
- Salva transcrição em 'transcricao.txt'

# 3. RESUMO COM GEMINI
- Lê arquivo de transcrição
- Envia para API Gemini com prompt de resumo
- Exibe resumo inteligente
```

---

## 💡 Exemplo de Uso

**Entrada:**
```
Digite a url do youtube: https://youtu.be/exemplo-aula-programacao
```

**Processamento:**
```python
# PyTubeFix baixa o áudio
yt.title = "Aula Completa de Python para Iniciantes"

# Whisper transcreve (modelo 'base', idioma 'pt')
transcricao = "Olá pessoal, hoje vamos aprender Python... [30 minutos de aula]"

# Gemini resume
resumo = "Nesta aula, o instrutor aborda conceitos básicos de Python..."
```

**Saída:**
```
📝 RESUMO DO VÍDEO:
Nesta aula de 30 minutos, o instrutor apresenta os fundamentos do Python...
```

---

## ⚠️ Limitações Atuais (V1)

| Limitação | Descrição |
|-----------|-----------|
| ❌ **YouTube apenas** | Não suporta outras fontes de áudio |
| ❌ **Arquivo fixo** | Sempre sobrescreve 'audioyt.m4a' |
| ❌ **Sem interface gráfica** | Apenas linha de comando/notebook |
| ❌ **Dependência de internet** | Download e API Gemini requerem conexão |
| ❌ **Processamento sequencial** | Bloqueante durante execução |

---

## 🔮 Próximas Melhorias (Roadmap)

### 🟢 V2 – Melhorias Imediatas
- [ ] Suporte a arquivos locais (MP3, WAV, M4A)
- [ ] Nome único para cada arquivo (timestamp)
- [ ] Tratamento de erros robusto
- [ ] Barra de progresso visual

### 🟡 V3 – Funcionalidades Avançadas
- [ ] Resumo em múltiplos idiomas
- [ ] Extração de tópicos principais (bullet points)
- [ ] Detecção automática de idioma do áudio
- [ ] Interface web simples (Streamlit)

### 🔴 V4 – Arquitetura Profissional
- [ ] Processamento em lote (múltiplos vídeos)
- [ ] Banco de dados para histórico
- [ ] API REST para integrações
- [ ] Exportação para PDF/DOCX

---

## 🧪 Desafios Técnicos Enfrentados

### 1. **Download de Áudio do YouTube**
```python
# Solução: PyTubeFix com get_audio_only()
ys = yt.streams.get_audio_only()
ys.download(filename="audioyt.m4a")
```

### 2. **Performance do Whisper**
- Modelo 'base' escolhido (equilíbrio entre velocidade e precisão)
- Configuração `fp16=False` para compatibilidade
- Idioma fixo 'pt' para melhor acurácia

### 3. **Integração Gemini**
```python
# Prompt estruturado para resumo breve
pergunta = f"""
Faça um resumo breve do
conteúdo: {conteudo}
"""
```

### 4. **Processamento em Notebook**
- Adaptação para execução célula a célula
- Arquivos intermediários salvos em disco

---

## 👨‍💻 Autor

**Davi Bezerra Fraga**  
Estudante de desenvolvimento backend e Inteligência Artificial

- 🔗 [LinkedIn](https://www.linkedin.com/in/davi-bezerra-fraga-319a49363/)
- 🐙 [GitHub](https://github.com/Davibzf)
- 📧 [Email](mailto:davibezerrafraga@gmail.com)
- 🌐 [Portfólio](https://davibezerrafraga.vercel.app)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- [OpenAI Whisper](https://github.com/openai/whisper) pelo modelo de transcrição
- [Google Gemini](https://deepmind.google/technologies/gemini/) pela API de IA
- [PyTubeFix](https://github.com/JuanBindez/pytubefix) pela biblioteca de download

---

> 🌟 **Se este projeto te ajudou, dê uma estrela no GitHub!**  
> 💬 *Sugestões e contribuições são muito bem-vindas*

---

## 📌 Configurações Técnicas

```python
# Whisper
modelo = "base"  # Modelo utilizado
idioma = "pt"    # Idioma fixo para transcrição
fp16 = False     # Compatibilidade com CPU/GPU

# Gemini
modelo_gemini = "gemini-flash-lite-latest"  # Modelo leve e rápido
```

---

Este README está pronto para ser colocado no seu repositório **Sonarize**! Quer que eu ajuste alguma seção ou crie algo mais específico?
