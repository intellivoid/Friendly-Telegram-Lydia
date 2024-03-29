from .. import loader, utils
import logging, random

logger = logging.getLogger(__name__)

def register(cb):
    cb(MockMod())

class MockMod(loader.Module):
    """mOcKs PeOpLe"""
    def __init__(self):
        self.commands = {'mock':self.mockcmd}
        self.config = {}
        self.name = "Mocker"

    async def mockcmd(self, message):
        """Use in reply to another message"""
        if message.is_reply:
            text = list((await message.get_reply_message()).message)
        else:
            text = list(utils.get_args_raw(message.message))
        n = 0
        rn = 0
        for c in text:
            if n % 2 == random.randint(0, 1):
                text[rn] = c.upper()
            else:
                text[rn] = c.lower()
            if c.lower() != c.upper():
                n += 1
            rn += 1
        text = "".join(text)
        logger.debug(text)
        await message.edit(text)


