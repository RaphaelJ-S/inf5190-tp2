import unittest
from unittest.mock import MagicMock
from app.src.service.service_msg import Service_Msg
from app.src.message.messagerie import Messagerie

msgrie = MagicMock()
service = Service_Msg(msgrie)


# class Test_Service_Msg(unittest.TestCase):
