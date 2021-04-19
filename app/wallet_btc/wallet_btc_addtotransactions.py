from app import db
from datetime import datetime
from app.wallet_btc.models import TransactionsBtc

# type 1: wallet withdrawl
# type 2: send bitcoin offsite
# type 4: send coin to escrow
# type 5: send coin to user
# type 6: send coin to agoras profit
# type 7: send coin to holdings
# type 8: send coin from holdings


def addtransaction(category, amount, userid, comment, shard, orderid, balance):
    """
    # this function will move the coin from holdings back to vendor.  This is for vendor verification
    :param category:
    :param amount:
    :param userid:
    :param comment:
    :param shard:
    :param orderid:
    :param balance:
    :return:
    """
    try:
        now = datetime.utcnow()
        comment = str(comment)
        orderid = int(orderid)

        trans = TransactionsBtc(
            category=category,
            userid=userid,
            confirmations=0,
            confirmed=1,
            txid='',
            blockhash='',
            timeoft=0,
            timerecieved=0,
            otheraccount=0,
            address='',
            fee=0,
            created=now,
            commentbtc=comment,
            amount=amount,
            shard=shard,
            orderid=orderid,
            balance=balance,
        )
        db.session.add(trans)
        db.session.commit()

    except Exception as e:
        print(str(e))
