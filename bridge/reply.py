# encoding:utf-8

from enum import Enum


class ReplyType(Enum):
    TEXT = 1  # 文本
    VOICE = 2  # 音频文件
    IMAGE = 3  # 图片文件
    IMAGE_URL = 4  # 图片URL

    INFO = 9
    ERROR = 10

    def __str__(self):
        return self.name


class Reply:
    def __init__(self, type: ReplyType = None, content=None , sostfix_message=None):
        self.type = type
        self.content = content
        sostfix_message = "关注我 我在chatgpt-on-wechat/bridge/reply.py"

    def __str__(self):
        return "Reply(type={}, content={})".format(self.type, self.content, sostfix_message)
