# %%
from genmono import greeting, log

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)
# %%
logger.error("hi")
# %%
from genmono.hello_api import core

print(core.app.routes)
# %%
from components.genmono.greeting.core import hello_world
hello_world() + "!"
# %%
