from app.item.models import marketItem, BannedISN, ItemtoDelete
from app import db
from config import storagelocation
import os
from app.common.functions import itemlocation
import sys


def deletefromdb():
    """
    This function looks for new items to delete in db table.
     Will ban amazon id..deletes image folder
    """
    itemnumber = db.session.query(ItemtoDelete).all()
    for f in itemnumber:
        itemidb = db.session.query(marketItem).filter(marketItem.id == f.itemid).first()
        if itemidb is not None:
            # if its amazon item delete item
            if itemidb.amazonid != '':
                addnewban = BannedISN(ISNid=itemidb.amazonid)
                db.session.add(addnewban)
            getimagesubfolder = itemlocation(itemidb.id)
            # try tro delete image..sometimes it doesnt have an image

            try:
                thepath = os.path.join(storagelocation, str(getimagesubfolder), str(itemidb.id))
                print(thepath)
                sys.stdout.flush()
                os.remove(thepath)
            except:
                pass

            print("deleting item")
            sys.stdout.flush()
            print(itemidb.id)
            sys.stdout.flush()
            print(itemidb.itemtitlee)
            sys.stdout.flush()
            db.session.delete(itemidb)
        else:
            # was already flagged..remove isbn
            print("item already deleted ...")
            isnindb = db.session.query(ItemtoDelete).filter(ItemtoDelete.id == f.id).first()
            print(isnindb.id)
            db.session.delete(isnindb)
        print("*" * 10)
    db.session.commit()

