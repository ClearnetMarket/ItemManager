# coding=utf-8
from app import db


class proxieslist(db.Model):
    __tablename__ = 'proxies'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    httpstat = db.Column(db.TEXT)
    address = db.Column(db.TEXT)
    port = db.Column(db.INTEGER)


class btcPrices(db.Model):
    __tablename__ = 'prices_btc'
    __bind_key__ = 'coin_prices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.TEXT)
    price = db.Column(db.DECIMAL(50, 2))
    currency_id = db.Column(db.INTEGER)
    percent_change_twentyfour = db.Column(db.DECIMAL(50, 2))


class btc_cash_Prices(db.Model):
    __tablename__ = 'prices_btc_cash'
    __bind_key__ = 'coin_prices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.Text)
    price = db.Column(db.DECIMAL(50, 2))
    currency_id = db.Column(db.INTEGER)
    percent_change_twentyfour = db.Column(db.DECIMAL(50, 2))


class Query_shard(db.Model):
    __tablename__ = 'query_shard'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_requestcancel(db.Model):
    __tablename__ = 'query_requestcancel'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_requestreturn(db.Model):
    __tablename__ = 'query_requestreturn'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_return(db.Model):
    __tablename__ = 'query_return'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_margin(db.Model):
    __tablename__ = 'query_margin'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.DECIMAL(20, 8))
    text = db.Column(db.Text)


class Query_mainsearch(db.Model):
    __tablename__ = 'query_mainsearch'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_websitefeedback(db.Model):
    __tablename__ = 'query_websitefeedback'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Carriers(db.Model):
    __tablename__ = 'query_carriers'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)

class Query_Currencylist(db.Model):
    __tablename__ = 'query_currencylist'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Count_low(db.Model):
    __tablename__ = 'query_count_low'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Physordig(db.Model):
    __tablename__ = 'query_physordig'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Itemorder(db.Model):
    __tablename__ = 'query_itemorder'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Itemcount(db.Model):
    __tablename__ = 'query_itemcount'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Timer(db.Model):
    __tablename__ = 'query_timer'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Itemcondition(db.Model):
    __tablename__ = 'query_itemcondition'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class Query_Continents(db.Model):
    __tablename__ = 'query_continents'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.INTEGER)
    text = db.Column(db.Text)


class currencyList(db.Model):
    __tablename__ = 'currencylist'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    USD = db.Column(db.DECIMAL(20, 8))
    PHP = db.Column(db.DECIMAL(20, 8))
    CHF = db.Column(db.DECIMAL(20, 8))
    CAD = db.Column(db.DECIMAL(20, 8))
    SGD = db.Column(db.DECIMAL(20, 8))
    RUB = db.Column(db.DECIMAL(20, 8))
    DKK = db.Column(db.DECIMAL(20, 8))
    RON = db.Column(db.DECIMAL(20, 8))
    NOK = db.Column(db.DECIMAL(20, 8))
    ILS = db.Column(db.DECIMAL(20, 8))
    SEK = db.Column(db.DECIMAL(20, 8))
    THB = db.Column(db.DECIMAL(20, 8))
    BRL = db.Column(db.DECIMAL(20, 8))
    INR = db.Column(db.DECIMAL(20, 8))
    ZAR = db.Column(db.DECIMAL(20, 8))
    HKD = db.Column(db.DECIMAL(20, 8))
    JPY = db.Column(db.DECIMAL(20, 8))
    HUF = db.Column(db.DECIMAL(20, 8))
    MXN = db.Column(db.DECIMAL(20, 8))
    CNY = db.Column(db.DECIMAL(20, 8))
    AUD = db.Column(db.DECIMAL(20, 8))
    PLN = db.Column(db.DECIMAL(20, 8))
    GBP = db.Column(db.DECIMAL(20, 8))
    TRY = db.Column(db.DECIMAL(20, 8))
    KRW = db.Column(db.DECIMAL(20, 8))
    IDR = db.Column(db.DECIMAL(20, 8))
    NZD = db.Column(db.DECIMAL(20, 8))
    MYR = db.Column(db.DECIMAL(20, 8))
    BGN = db.Column(db.DECIMAL(20, 8))
    EUR = db.Column(db.DECIMAL(20, 8))
    HRK = db.Column(db.DECIMAL(20, 8))
    CZK = db.Column(db.DECIMAL(20, 8))


class Currency(db.Model):
    __tablename__ = 'currency'
    __bind_key__ = 'Agora_Market'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer)
    symbol = db.Column(db.TEXT)












