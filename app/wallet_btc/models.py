# coding=utf-8
from flask_login import UserMixin
from app import db


class BtcTransOrphan(db.Model):
    __tablename__ = 'transorphan'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))
    btcaddress = db.Column(db.TEXT)
    txid = db.Column(db.TEXT)


class BtcUnconfirmed(db.Model):
    __tablename__ = 'unconfirmed'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)

    unconfirmed1 = db.Column(db.DECIMAL(20, 8))
    unconfirmed2 = db.Column(db.DECIMAL(20, 8))
    unconfirmed3 = db.Column(db.DECIMAL(20, 8))
    unconfirmed4 = db.Column(db.DECIMAL(20, 8))
    unconfirmed5 = db.Column(db.DECIMAL(20, 8))
    unconfirmed6 = db.Column(db.DECIMAL(20, 8))
    unconfirmed7 = db.Column(db.DECIMAL(20, 8))
    unconfirmed8 = db.Column(db.DECIMAL(20, 8))
    unconfirmed9 = db.Column(db.DECIMAL(20, 8))
    unconfirmed10 = db.Column(db.DECIMAL(20, 8))

    txid1 = db.Column(db.TEXT)
    txid2 = db.Column(db.TEXT)
    txid3 = db.Column(db.TEXT)
    txid4 = db.Column(db.TEXT)
    txid5 = db.Column(db.TEXT)
    txid6 = db.Column(db.TEXT)
    txid7 = db.Column(db.TEXT)
    txid8 = db.Column(db.TEXT)
    txid9 = db.Column(db.TEXT)
    txid10 = db.Column(db.TEXT)


class BtcWallet(db.Model):
    __tablename__ = 'wallet'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    currentbalance = db.Column(db.DECIMAL(20, 8))
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER)
    address2 = db.Column(db.TEXT)
    address2status = db.Column(db.INTEGER)
    address3 = db.Column(db.TEXT)
    address3status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))



class BtcWalletWork(db.Model):
    __tablename__ = 'wallet_work'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.Text)
    comment = db.Column(db.Text)
    created = db.Column(db.DATETIME)
    txtcomment = db.Column(db.Text)
    shard = db.Column(db.INTEGER)


class BtcWalletAddresses(db.Model):
    __tablename__ = 'walletaddresses'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btcaddress = db.Column(db.TEXT)
    shard = db.Column(db.INTEGER)
    userid = db.Column(db.INTEGER)
    status = db.Column(db.INTEGER)


class BtcWalletFee(db.Model):
    __tablename__ = 'walletfee'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))


class TransactionsBtc(db.Model):
    __tablename__ = 'transactions_btc'
    __bind_key__ = 'wallet_btc'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.INTEGER)
    userid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    txid = db.Column(db.Text)
    amount = db.Column(db.DECIMAL(20, 8))
    blockhash = db.Column(db.Text)
    timeoft = db.Column(db.INTEGER)
    timerecieved = db.Column(db.INTEGER)
    commentbtc = db.Column(db.Text)
    otheraccount = db.Column(db.INTEGER)
    address = db.Column(db.Text)
    fee = db.Column(db.DECIMAL(20, 8))
    created = db.Column(db.DATETIME)
    balance = db.Column(db.DECIMAL(20, 8))
    shard = db.Column(db.INTEGER)
    orderid = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    confirmed_fee = db.Column(db.DECIMAL(20, 8))
    digital_currency = db.Column(db.INTEGER)

db.create_all()
db.session.commit()
