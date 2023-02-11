# We importeren onze minecraft robot code
from cdj_minecraft import Bot

# We willen dat onze robot “albert” noemt dus kunnen we de naam gelijk zetten aan albert, ook willen we dat albert
# verbind met `<domain here>`, dus kunnen we hetzelfde doen voor server
bot = Bot(naam="albert", server="<domain here>")

# Onze laatste stap is onze robot opstarten, dit zal ervoor zorgen dat “albert” op minecraft gaat in in de `<domain
# here>` server in logged.
bot.start()
