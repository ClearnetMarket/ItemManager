from app import db
from app.item.models import marketItem


def changeending():
    getitems = db.session.query(marketItem).all()
    for f in getitems:

        if f.imageone.endswith(".jpg"):
            newname = f.imageone[:-4]
            print(newname)
            f.imageone = newname
            db.session.add(f)

    db.session.commit()

changeending()
