from Utils.Writer import Writer
from Database.DataBase import DataBase
import random

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        if (self.player.room_id == 0):
            self.player.room_id = random.randint(0, 2147483647)
            self.writeInt(self.player.room_id)
            DataBase.replaceValue(self, 'roomID', self.player.room_id)

        else:
           self.writeInt(self.player.room_id)

        self.writeVint(1557129593)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(15)
        self.writeVint(self.player.map_id) # map ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # high id
        self.writeInt(1)  # low id
        self.writeVint(16)
        self.writeVint(self.player.brawler_id)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(99999)
        self.writeVint(1)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.name) # player name
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(23)
        self.writeVint(self.player.starpower)
        if self.player.useGadget == 1:
            self.writeVint(23)
            self.writeVint(self.player.gadget)
        else:
           self.writeVint(0)
           self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(6)
        self.writeHexa('''FF-FF-00-00-00-00-00''')

