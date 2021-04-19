from app import db



class Orders(db.Model):
    __tablename__ = 'orders'
    __bind_key__ = 'Agora_Orders'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    type = db.Column(db.INTEGER)
    vendor = db.Column(db.Text)
    vendor_id = db.Column(db.INTEGER)
    customer = db.Column(db.Text)
    customer_id = db.Column(db.INTEGER)
    currency = db.Column(db.INTEGER)
    incart = db.Column(db.INTEGER)
    new_order = db.Column(db.INTEGER)
    accepted_order = db.Column(db.INTEGER)
    waiting_order = db.Column(db.INTEGER)
    disputed_order = db.Column(db.INTEGER)
    disputedtimer = db.Column(db.DATETIME)
    modid = db.Column(db.INTEGER)
    delivered_order = db.Column(db.INTEGER)
    title = db.Column(db.Text)
    price = db.Column(db.DECIMAL(20, 8))
    price_peritem = db.Column(db.DECIMAL(20, 8))
    age = db.Column(db.DATETIME)
    returncancelage = db.Column(db.DATETIME)
    return_by = db.Column(db.DATETIME)
    private_note = db.Column(db.Text)
    escrow = db.Column(db.Text)
    item_id = db.Column(db.INTEGER)
    trade_id = db.Column(db.INTEGER)
    stringauctionid = db.Column(db.Text)
    stringnodeid = db.Column(db.Text)
    imageone = db.Column(db.Text)
    quantity = db.Column(db.INTEGER)
    request_cancel = db.Column(db.INTEGER)
    reason_cancel = db.Column(db.INTEGER)
    cancelled = db.Column(db.INTEGER)
    request_return = db.Column(db.INTEGER)
    shipping_price = db.Column(db.DECIMAL(20, 8))
    shipdescription = db.Column(db.TEXT)
    overallreason = db.Column(db.TEXT)
    return_id = db.Column(db.INTEGER)
    return_quantity = db.Column(db.INTEGER)
    return_amount = db.Column(db.DECIMAL(20, 8))
    feedback = db.Column(db.INTEGER)
    userfeedback = db.Column(db.INTEGER)
    completed = db.Column(db.INTEGER)
    subcategory = db.Column(db.DECIMAL(20, 8))
    perbtc = db.Column(db.DECIMAL(20, 8))
    fee = db.Column(db.DECIMAL(20, 8))
    completed_time = db.Column(db.DATETIME)
    return_allowed = db.Column(db.INTEGER)
    buyorsell = db.Column(db.INTEGER)
    released = db.Column(db.INTEGER)
    digital_currency = db.Column(db.INTEGER)



class notshipping(db.Model):
    __tablename__ = 'notshipping'
    __bind_key__ = 'Agora_Market'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.INTEGER)
    name = db.Column(db.Text)


class vendorVerification(db.Model):
    __tablename__ = 'vendorverification'
    __bind_key__ = 'Agora_Market'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_id = db.Column(db.INTEGER)
    vendor_level = db.Column(db.INTEGER)
    timestamp = db.Column(db.DATETIME)
    amount = db.Column(db.DECIMAL(20, 8))

class Country(db.Model):
    __tablename__ = 'countries'
    __bind_key__ = 'Agora_Market'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ab = db.Column(db.Text)
    name = db.Column(db.Text)
    numericcode = db.Column(db.INTEGER)





class Duration(db.Model):
    __tablename__ = 'durations'
    __bind_key__ = 'Agora_Market'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.Text)
    displaytime = db.Column(db.Text)




db.create_all()
db.session.commit()