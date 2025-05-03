Fala FURIA 🎮🦁
Desafio 1 do processo seletivo da FURIA
Um bot do Telegram que fornece informações sobre os jogos da equipe FURIA de CS:GO, incluindo o próximo jogo, o último resultado, gritos da torcida e links para redes sociais oficiais.

📦 Estrutura do Projeto
O projeto está organizado nos seguintes arquivos:

bot.py: Arquivo principal que inicializa o bot e registra os comandos.

commands.py: Contém as funções que respondem aos comandos do bot.

furia_data.py: Responsável por obter dados sobre os jogos da FURIA.

requirements.txt: Lista de dependências necessárias para executar o projeto.

🚀 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/viniciusstencel/fala-furia.git
cd fala-furia
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
🔧 Configuração
Variáveis de ambiente:

Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Telegram:

env
Copiar
Editar
FURIA_BOT_TOKEN= *Token Enviado na aba de observações do Formulário*
Ou defina diretamente no terminal:

bash
Copiar
Editar
export FURIA_BOT_TOKEN= *Token Enviado na aba de observações do Formulário* # No Windows: set FURIA_BOT_TOKEN= *Token Enviado na aba de observações do Formulário*

bash
Copiar
Editar
python bot.py
📚 Comandos Disponíveis
/start: Mensagem de boas-vindas.

/menu: Lista os comandos disponíveis.

/proximo_jogo: Exibe informações sobre o próximo jogo da FURIA.

/ultimo_jogo: Mostra o resultado do último jogo da FURIA.

/torcida: Exibe um grito de torcida aleatório.

/redes_sociais: Fornece links para as redes sociais oficiais da FURIA.

🤖 Tecnologias Utilizadas
Python

python-telegram-bot

requests

beautifulsoup4

lxml

dotenv

📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

