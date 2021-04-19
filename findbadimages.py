from app import db
from app.item.models import marketItem
from config import storagelocation
import os


# this will delete if there isnt an image
def getallitems():

    getitems = db.session.query(marketItem).all()
    for item in getitems:
        itempath = os.path.join(storagelocation,
                                item.stringnodeid,
                                str(item.id),
                                item.imageone)

        x = (os.path.exists(itempath))

        if x is not True:
            if item.imageone != '0':
                print("Item id", item.id)
                print(itempath)
                print("it doesnt exist")
                db.session.delete(item)

    db.session.commit()

getallitems()