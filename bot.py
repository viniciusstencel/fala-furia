import os
import asyncio
import nest_asyncio
nest_asyncio.apply()
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import start, menu, proximo_jogo, ultimo_jogo, torcida, redes_sociais

# Carrega o token da variável de ambiente
TOKEN = os.getenv("FURIA_BOT_TOKEN")

if not TOKEN:
    raise ValueError("⚠️ A variável de ambiente FURIA_BOT_TOKEN não está definida.")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("proximo_jogo", proximo_jogo))
    app.add_handler(CommandHandler("ultimo_jogo", ultimo_jogo))
    app.add_handler(CommandHandler("torcida", torcida))
    app.add_handler(CommandHandler("redes_sociais", redes_sociais))

    print("🤖 Bot Fala, FURIA iniciado...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
