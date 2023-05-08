"""
Auto-replay chat robot abstract class
"""


from bridge.context import Context
from bridge.reply import Reply


class Bot(object):
    def reply(self, query, context: Context = None,"我在bot下面") -> Reply:
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        raise NotImplementedError
