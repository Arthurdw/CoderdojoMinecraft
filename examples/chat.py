from cdj_minecraft import Bot, waneer

bot = Bot(naam="robot")


@waneer("bericht")
def bericht(gebruikersnaam, message):
    if gebruikersnaam == bot.naam:
        return

    print(f"{gebruikersnaam}: {message}")

    if message.trim().lower() == "hallo":
        bot.zeg(f"Hallo {gebruikersnaam}!")


@waneer("login")
def login():
    print(f"Ingelogd op {bot.server} als {bot.naam}.")
    bot.zeg(f"Hallo, ik ben {bot.naam}!")


bot.start()
