from app import db
from app.wallet_btc.models import BtcWallet
from decimal import Decimal


def checkbalance(userid, amount):
    # The money requested during the trade
    userwallet = db.session.query(BtcWallet).filter_by(userid=userid).first()
    x = userwallet.currentbalance
    y = Decimal(amount)

    if x >= y:
        return 1
    else:
        return 0
