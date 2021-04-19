from app import db
# models
from app.profile.models import \
    StatisticsUser, \
    StatisticsVendor
# End Models
from app.achievements.c import howmanyitemsbought_customer, howmanytrades_customer
from app.achievements.v import howmanyitemssold_vendor, howmanytrades_vendor

from datetime import datetime
from decimal import Decimal

now = datetime.utcnow()



def addtotalItemsSold(userid, howmany):
    # how many items a customer sold
    itemssold = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()

    a = itemssold.totalsales
    x = int(a) + int(howmany)
    itemssold.totalsales = x
    db.session.add(itemssold)
    db.session.commit()
    howmanyitemssold_vendor(userid=userid, number=x)


def addtotalItemsBought(userid, howmany):
    # how many items a customer bought
    itemsbought = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()

    a = itemsbought.totalitemsbought
    x = a + howmany
    itemsbought.totalitemsbought = x
    db.session.add(itemsbought)
    db.session.commit()

    howmanyitemsbought_customer(userid=userid, number=x)


def addtotaltradesuser(userid):
    # how many trades a customer did
    userstats = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    useramount = userstats.totaltrades
    usernewamount = useramount + 1
    userstats.totaltrades = usernewamount
    db.session.add(userstats)
    db.session.commit()

    # achievement
    howmanytrades_customer(userid=userid, number=usernewamount)



def addtotaltradesVendor(userid):
    # how many trades a customer did
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    # add total trades to vendor
    amount = vendorstats.totaltrades
    newamount = amount + 1
    vendorstats.totaltrades = newamount
    db.session.add(vendorstats)
    db.session.commit()

    howmanytrades_vendor(userid=userid, number=newamount)




def reviewsgiven(userid):
    """
    # adds a review given by user
    :param userid:
    :return:
    """

    reviewsstats = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    y = reviewsstats.totalreviews
    x = y + 1
    reviewsstats.totalreviews = x
    db.session.add(reviewsstats)
    db.session.commit()


def reviewsrecieved(userid):
    """
    # adds a review recieved as a vendor
    :param userid:
    :return:
    """

    reviewsstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    y = reviewsstats.totalreviews
    x = y + 1
    reviewsstats.totalreviews = x
    db.session.add(reviewsstats)
    db.session.commit()


def addflag(userid):
    # adds a flag to user stats
    reviewsstats = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    y = reviewsstats.itemsflagged
    x = y + 1
    reviewsstats.itemsflagged = x
    db.session.add(reviewsstats)
    db.session.commit()


def vendorflag(userid):
    # adds a flag to vendor stats
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    # add total trades to vendor
    amount = vendorstats.beenflagged
    newamount = amount + 1
    vendorstats.beenflagged = newamount
    db.session.add(vendorstats)
    db.session.commit()


def totalspentonitems(userid, amount, howmany):
    # USER
    # how much money a user has spent of physical items
    # bitcoin
    itemsbought = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    a = itemsbought.totalbtcspent
    totalamt = (Decimal(amount) * int(howmany))
    x = (Decimal(a + totalamt))
    itemsbought.totalbtcspent = x
    db.session.add(itemsbought)
    db.session.commit()


def totalrecbyusers(userid, amount, howmany):
    # how much money a user has spent of physical items
    # bitcoin
    itemsbought = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    a = itemsbought.totalbtcrecieved
    totalamt = (Decimal(amount) * int(howmany))
    x =  (Decimal(a + totalamt))
    itemsbought.totalbtcrecieved = x
    db.session.add(itemsbought)
    db.session.commit()


def vendortotalmade(userid, amount):
    # vendor
    # how much money a user has spent of physical items
    # bitcoin
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    a = vendorstats.totalbtcrecieved
    x = (Decimal(a + amount))
    vendorstats.totalbtcrecieved = x
    db.session.add(vendorstats)
    db.session.commit()


def vendortotalsent(userid, amount):
    # how much money a user has spent of physical items
    # bitcoin
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    a = vendorstats.totalbtcspent
    x = (Decimal(a + amount))
    vendorstats.totalbtcspent = x
    db.session.add(vendorstats)
    db.session.commit()





def totalspentonitems_btccash(userid, amount, howmany):
    # USER
    # how much money a user has spent of physical items
    # bitcoin cash
    itemsbought = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    a = itemsbought.totalbtccashspent
    totalamt = (Decimal(amount) * int(howmany))
    x = (Decimal(a + totalamt))
    itemsbought.totalbtccashspent = x
    db.session.add(itemsbought)
    db.session.commit()


def totalrecbyusers_btccash(userid, amount, howmany):
    # USER
    # how much money a user has spent of physical items
    # bitcoin cash
    itemsbought = db.session.query(StatisticsUser).filter(userid == StatisticsUser.usernameid).first()
    a = itemsbought.totalbtccashrecieved
    totalamt = (Decimal(amount) * int(howmany))
    x = (Decimal(a + totalamt))
    itemsbought.totalbtccashrecieved = x
    db.session.add(itemsbought)
    db.session.commit()


def vendortotalmade_btccash(userid, amount):
    # vendor
    # how much money a user has spent of physical items
    # bitcoin cash
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    a = vendorstats.totalbtccashrecieved
    x = (Decimal(a + amount))
    vendorstats.totalbtccashrecieved = x
    db.session.add(vendorstats)
    db.session.commit()


def vendortotalsent_btccash(userid, amount):
    # vendor
    # how much money a user has spent of physical items
    # bitcoin cash
    vendorstats = db.session.query(StatisticsVendor).filter(userid == StatisticsVendor.vendorid).first()
    a = vendorstats.totalbtccashspent
    x = (Decimal(a + amount))
    vendorstats.totalbtccashspent = x
    db.session.add(vendorstats)
    db.session.commit()
