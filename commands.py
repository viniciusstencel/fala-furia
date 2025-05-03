from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from furia_data import get_proximo_jogo, get_ultimo_jogo, get_redes_sociais
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Bem-vindo ao *Fala, FURIA*! Use /menu para ver os comandos.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 *Comandos disponíveis:*\n"
        "/ultimo_jogo - Último resultado\n"
        "/proximo_jogo - Próxima partida\n"
        "/torcida - Grito da torcida\n"
        "/redes_sociais - Redes sociais"
    )

async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_proximo_jogo())

async def ultimo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_ultimo_jogo())

async def torcida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    frases = [
        "🦁 VAMO FURIAAAA!",
        "🎯 KSCERATO vai carregar!",
        "🔥 ART no rush B é arte!",
        "💣 Domina esse bomb aí FURIA!"
    ]
    await update.message.reply_text(random.choice(frases))

async def redes_sociais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = get_redes_sociais()
    await update.message.reply_text(msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
