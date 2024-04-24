import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers


# Функция конфигурирования и запуска бота
async def main() -> None:

    # загружаем конфигурацию в переменную config
    config: Config = load_config()

    # Инициализируем бота и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # регистрируем роутеры в Диспетчере
    dp.include_router(user_handlers.router)

    # пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
