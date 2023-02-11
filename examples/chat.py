from cdj_minecraft import Bot, wanneer

bot = Bot(naam="albert", server="localhost")


@wanneer("bericht")
def bericht(gebruikersnaam: str, bericht: str):
    # We willen niet dat de robot antwoord op zijn eigen berichten.
    if gebruikersnaam == bot.naam:
        return

    print(f"{gebruikersnaam}: {bericht}")


    if bericht.strip().lower() == "hallo":
        bot.zeg(f"Hallo {gebruikersnaam}!")


@wanneer("login")
def login():
    print(f"Ingelogd op {bot.server} als {bot.naam}.")
    bot.zeg(f"Hallo, ik ben {bot.naam}!")


bot.start()
