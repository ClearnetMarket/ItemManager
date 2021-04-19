from app import db
from app import errorLogger
from datetime import datetime
from app.wallet_btc.wallet_btc_addtotransactions import addtransaction
from app.wallet_btc.wallet_btc_security import checkbalance

# Models
from app.auth.models import \
    User

from app.admin.models import \
    Agoraprofit, \
    Agoraholdings

from app.vendor.models import \
    Orders

from app.wallet_btc.models import \
    BtcWallet, \
    BtcWalletWork, \
    BtcWalletFee
# end models

from decimal import Decimal
from app.common.functions import floating_decimals
from app.notification import notification

# type 1: wallet_btc creation
# type 2: send bitcoin offsite

# type 4: send coin to escrow
# type 5: send coin to user
# type 10: get balance of account


def walletstatus(userid):
    """
    THIS function creates the wallet_btc and puts its first address there
    :param userid:
    :return:
    """
    userwallet = db.session.query(BtcWallet).filter_by(userid=userid).first()
    getuser = db.session.query(User).filter(User.id == userid).first()
    if userwallet:
        try:
            if userwallet.address1status == 0 and userwallet.address2status == 0 and userwallet.address2status == 0:
                createWallet(userid=userid)

            else:
                pass
        except Exception:

            userwallet.address1 = ''
            userwallet.address1status = 0
            userwallet.address2 = ''
            userwallet.address2status = 0
            userwallet.address3 = ''
            userwallet.address3status = 0

            db.session.add(userwallet)
            db.session.commit()
            createWallet(userid == userid)
    else:
        # creates wallet_btc in db
        walletcreate = BtcWallet(userid=userid,
                                 currentbalance=0,
                                 unconfirmed=0,
                                 address1='',
                                 address1status=0,
                                 address2='',
                                 address2status=0,
                                 address3='',
                                 address3status=0,
                                 locked=0,
                                 shard=getuser.shard,
                                 transactioncount=0
                                 )

        db.session.add(walletcreate)
        db.session.commit()

def createWallet(userid):
    """
    THIS function creates the wallet_btc and puts its first address there
    :param userid:
    :return:
    """
    try:
        type_transaction = 1
        user = db.session.query(User).filter(User.id == userid).first()
        timestamp = datetime.utcnow()

        wallet = BtcWalletWork(
            userid=userid,
            type=type_transaction,
            amount=0,
            sendto=0,
            comment=0,
            created=timestamp,
            txtcomment='',
            shard=user.shard
        )
        db.session.add(wallet)
        db.session.commit()

    except Exception as e:
        errorLogger(function='createWallet', error=e, kindoferror=4, user=userid)
        db.session.rollback()


def sendCoin(userid, sendto, amount, comment):
    """
    Withdrawl offsite
    :param userid:
    :param sendto:
    :param amount:
    :param comment:
    :return:
    """
    getwallet = BtcWalletFee.query.filter_by(id=1).first()
    walletfee = getwallet.btc
    a = checkbalance(userid=userid, amount=amount)
    if a == 1:

        strcomment = str(comment)
        type_transaction = 2
        timestamp = datetime.utcnow()
        userswallet = BtcWallet.query.filter_by(userid=userid).first()

        wallet = BtcWalletWork(
            userid=userid,
            type=type_transaction,
            amount=amount,
            sendto=sendto,
            comment=0,
            created=timestamp,
            txtcomment=strcomment,
            shard=userswallet.shard
        )

        db.session.add(wallet)
        db.session.commit()

        # turn sting to a decimal
        amountdecimal = Decimal(amount)
        # make decimal 8th power
        amounttomod = floating_decimals(amountdecimal, 8)
        # gets current balance
        curbalance = floating_decimals(userswallet.currentbalance, 8)
        # gets amount and fee
        amountandfee = floating_decimals(amounttomod + walletfee, 8)
        # subtracts amount and fee from current balance
        y = floating_decimals(curbalance - amountandfee, 8)
        # set balance as new amount
        userswallet.currentbalance = floating_decimals(y, 8)

        db.session.add(userswallet)
        db.session.commit()
    else:
        notification(
            type=34,
            username='',
            userid=userid,
            salenumber=0,
            bitcoin=amount
        )




def sendCointoEscrow(amount, comment, userid):
    """
    #TO Agora Wallet
    ##this function will move the coin to agoras wallet_btc from a user
    :param amount:
    :param comment:
    :param userid:
    :return:
    """
    a = checkbalance(userid=userid, amount=amount)
    if a == 1:
        try:
            type_transaction = 4
            userswallet = BtcWallet.query.filter_by(userid=userid).first()
            curbal = Decimal(userswallet.currentbalance)
            amounttomod = Decimal(amount)
            newbalance = Decimal(curbal) - Decimal(amounttomod)
            userswallet.currentbalance = newbalance
            db.session.add(userswallet)
            db.session.commit()

            oid = int(comment)

            addtransaction(category=type_transaction,
                           amount=amount,
                           userid=userid,
                           comment='Sent Coin To Escrow',
                           shard=userswallet.shard,
                           orderid=oid,
                           balance=newbalance
                           )
        except Exception as e:
            errorLogger(function='sendcointoescrow', error=e, kindoferror=4, user=userid)
            # find order and cancel it
            order = db.session.query(Orders).filter(Orders.id == comment).first()
            # change the order status
            order.disputed_order = 0
            order.cancelled = 1
            order.completed = 1
            order.buyorsell = 1
            order.released = 1
            order.completed_time = datetime.utcnow()
            db.session.add(order)
            db.session.commit()
    else:
        order = db.session.query(Orders).filter(Orders.id == comment).first()
        # change the order status
        # change the order status
        order.disputed_order = 0
        order.cancelled = 1
        order.completed = 1
        order.buyorsell = 1
        order.released = 1
        order.completed_time = datetime.utcnow()
        db.session.add(order)
        db.session.commit()

        notification(
            type=34,
            username='',
            userid=userid,
            salenumber=comment,
            bitcoin=amount
        )



def sendCointoUser(amount, comment, userid):
    """
    # TO User
    # this function will move the coin from agoras wallet_btc to a user
    :param amount:
    :param comment:
    :param userid:
    :return:
    """
    try:
        type_transaction = 5
        oid = int(comment)

        userswallet = BtcWallet.query.filter_by(userid=userid).first()
        curbal = Decimal(userswallet.currentbalance)
        amounttomod = Decimal(amount)
        newbalance = Decimal(curbal) + Decimal(amounttomod)
        userswallet.currentbalance = newbalance
        db.session.add(userswallet)
        db.session.commit()

        addtransaction(category=type_transaction,
                       amount=amount,
                       userid=userid,
                       comment='Transaction',
                       shard=userswallet.shard,
                       orderid=oid,
                       balance=newbalance
                       )
    except Exception as e:
        print(str(e))
        errorLogger(function='sendcointouser', error=e, kindoferror=4, user=userid)

        db.session.rollback()

def sendCointoUser_asAdmin(amount, comment, userid):
    """
    # TO User
    # this function will move the coin from agoras wallet_btc to a user as an admin
    :param amount:
    :param comment:
    :param userid:
    :return:
    """
    try:
        type_transaction = 9

        userswallet = BtcWallet.query.filter_by(userid=userid).first()
        curbal = Decimal(userswallet.currentbalance)
        amounttomod = Decimal(amount)
        newbalance = Decimal(curbal) + Decimal(amounttomod)
        userswallet.currentbalance = newbalance
        db.session.add(userswallet)
        db.session.commit()

        addtransaction(category=type_transaction,
                       amount=amount,
                       userid=userid,
                       comment=comment,
                       shard=userswallet.shard,
                       orderid=0,
                       balance=newbalance
                       )
    except Exception as e:
        print(str(e))
        errorLogger(function='sendcointouser', error=e, kindoferror=4, user=userid)
        db.session.rollback()


def takeCointoUser_asAdmin(amount, comment, userid):
    """
    # TO User
    # this function will move the coin from agoras wallet_btc to a user as an admin
    :param amount:
    :param comment:
    :param userid:
    :return:
    """
    try:
        type_transaction = 10
        a = Decimal(amount)
        userswallet = BtcWallet.query.filter_by(userid=userid).first()
        curbal = Decimal(userswallet.currentbalance)
        amounttomod = Decimal(amount)
        newbalance = Decimal(curbal) - Decimal(amounttomod)
        userswallet.currentbalance = newbalance
        db.session.add(userswallet)
        db.session.commit()

        addtransaction(category=type_transaction,
                       amount=amount,
                       userid=userid,
                       comment=comment,
                       shard=userswallet.shard,
                       orderid=0,
                       balance=newbalance
                       )

        getcurrentprofit = db.session.query(Agoraprofit).order_by(Agoraprofit.id.desc()).first()
        currentamount = floating_decimals(getcurrentprofit.total, 8)
        newamount = floating_decimals(currentamount, 8) + floating_decimals(a, 8)
        prof = Agoraprofit(
            amount=amount,
            timestamp=datetime.utcnow(),
            total=newamount
        )
        db.session.add(prof)
        db.session.commit()

    except Exception as e:
        print(str(e))
        errorLogger(function='sendcointouser', error=e, kindoferror=4, user=userid)
        db.session.rollback()


def sendCointoAgora(amount, comment, shard):
    """
    # TO Agora
    # this function will move the coin from agoras escrow to profit account
    # no balance necessary
    :param amount:
    :param comment:
    :param shard:
    :return:
    """
    try:
        type_transaction = 6
        now = datetime.utcnow()
        oid = int(comment)
        a = Decimal(amount)
        addtransaction(category=type_transaction,
                       amount=amount,
                       userid=1,
                       comment='Sent Coin to Agora profit',
                       shard=shard,
                       orderid=oid,
                       balance=0)

        getcurrentprofit = db.session.query(Agoraprofit).order_by(Agoraprofit.id.desc()).first()
        currentamount = floating_decimals(getcurrentprofit.total, 8)
        newamount = floating_decimals(currentamount, 8) + floating_decimals(a, 8)
        prof = Agoraprofit(
            amount=amount,
            order=oid,
            timestamp=now,
            total=newamount
        )
        db.session.add(prof)
        db.session.commit()
    except Exception as e:
        print(str(e))
        errorLogger(function='sendcointoagora', error=e, kindoferror=4, user=1)
        db.session.rollback()


def sendCointoHoldings(amount, userid, comment):
    """
    # TO Agora
    # this function will move the coin from vendor to agora holdings.  This is for vendor verification
    :param amount:
    :param userid:
    :param comment:
    :return:
    """
    a = checkbalance(userid=userid, amount=amount)
    if a == 1:
        try:
            type_transaction = 7
            now = datetime.utcnow()

            user = db.session.query(User).filter(User.id == userid).first()
            userswallet = BtcWallet.query.filter_by(userid=userid).first()
            curbal = Decimal(userswallet.currentbalance)
            amounttomod = floating_decimals(amount, 8)
            newbalance = floating_decimals(curbal, 8) - floating_decimals(amounttomod, 8)
            userswallet.currentbalance = newbalance
            db.session.add(userswallet)
            db.session.commit()

            c = str(comment)
            a = Decimal(amount)
            commentstring = "Vendor Verification: Level " + c
            addtransaction(category=type_transaction,
                           amount=amount,
                           userid=user.id,
                           comment=commentstring,
                           shard=user.shard,
                           orderid=0,
                           balance=newbalance
                           )

            getcurrentholdings = db.session.query(Agoraholdings).order_by(Agoraholdings.id.desc()).first()
            currentamount = floating_decimals(getcurrentholdings.total, 8)
            newamount = floating_decimals(currentamount, 8) + floating_decimals(a, 8)
            holdingsaccount = Agoraholdings(
                amount=a,
                timestamp=now,
                userid=userid,
                total=newamount
            )
            db.session.add(holdingsaccount)
            db.session.commit()

        except Exception as e:
            print(str(e))
            errorLogger(function='sendcointoholdings', error=e, kindoferror=4, user=userid)
            db.session.rollback()
    else:
        pass


def sendCoinfromHoldings(amount, userid, comment):
    """=
    # TO Agora
    # this function will move the coin from holdings back to vendor.  This is for vendor verification
    :param amount:
    :param userid:
    :param comment:
    :return:
    """
    try:
        type_transaction = 8
        now = datetime.utcnow()
        user = db.session.query(User).filter(User.id == userid).first()
        userswallet = BtcWallet.query.filter_by(userid=userid).first()
        curbal = Decimal(userswallet.currentbalance)
        amounttomod = Decimal(amount)
        newbalance = Decimal(curbal) + Decimal(amounttomod)
        userswallet.currentbalance = newbalance

        db.session.add(userswallet)
        db.session.commit()

        c = str(comment)
        a = Decimal(amount)
        commentstring = "Vendor Verification Refund: Level " + c

        addtransaction(category=type_transaction,
                       amount=amount,
                       userid=user.id,
                       comment=commentstring,
                       shard=user.shard,
                       orderid=0,
                       balance=newbalance
                       )
        getcurrentholdings = db.session.query(Agoraholdings).order_by(Agoraholdings.id.desc()).first()
        currentamount = floating_decimals(getcurrentholdings.total, 8)
        newamount = floating_decimals(currentamount, 8) - floating_decimals(a, 8)

        holdingsaccount = Agoraholdings(
            amount=a,
            timestamp=now,
            userid=userid,
            total=newamount
        )
        db.session.add(holdingsaccount)
        db.session.commit()

    except Exception as e:
        print(str(e))
        errorLogger(function='sendcoinfromholdings', error=e, kindoferror=4, user=userid)
        db.session.rollback()


