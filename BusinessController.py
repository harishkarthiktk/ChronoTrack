from time import ctime, time
import json

def getTimeStr(time_epoch):
    time_str = ctime(time_epoch)
    return time_str

class Item:
    def __init__(self, id, item_name = "WaterCan", item_type="WaterCan", create_date=time()):
        self.id = id
        self.item_name = item_name
        self.item_type = item_type
        self.create_date = create_date

        """
        Purpose: 
        Each item added as a row will be of this class type.
        There will be one static classification of WaterCans, because I want to track that first.
        Further item categorization will be added later.
        """
    
    def createItemJSON(self):
        j_object = {"id": self.id,
                    "item_name": self.item_name,
                    "item_type": self.item_type,
                    "self.create_date" : self.create_date 
                    }

        return json.dumps(j_object)
    
