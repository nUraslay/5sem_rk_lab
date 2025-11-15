from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8379388382:AAF2ZSJ1BgJ6wPMjCaA4u_KyhmYUiIKJBEc"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        ["Мужская одежда", "Женская одежда"],
        ["Аксессуары", "Контакты"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f"Привет, {user.first_name}! \nДобро пожаловать в наш магазин Brandshop",
        reply_markup=reply_markup
    )

# Обработка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Мужская одежда":
        await update.message.reply_text("В разделе мужской одежды: футболки, джинсы, куртки.")
    elif text == "Женская одежда":
        await update.message.reply_text("В разделе женской одежды: платья, юбки, блузки.")
    elif text == "Аксессуары":
        await update.message.reply_text("Аксессуары: шапки, ремни, часы, сумки.")
    elif text == "Контакты":
        await update.message.reply_text("Наш сайт: brandshop.ru\nТелефон: +7 (922) 442-45-67")
    else:
        await update.message.reply_text("Выберите раздел из меню")

# Основная функция
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен! Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
