from app import db
from app.achievements.models import UserAchievements, UserAchievements_recent
from datetime import datetime




##customer awards
#id=20
def firstpurchase(userid):
    usera = db.session.query(UserAchievements).filter_by(userid=userid).first()
    now = datetime.utcnow()
    if usera.c2 != 1:
        usera.c2 = 1
        usera.c2_date = now
        db.session.add(usera)
        db.session.commit()
        addit = UserAchievements_recent(
            userid=usera.userid,
            username=usera.username,
            ach_id=20,
            achievement_date=now,
            viewed=0,
        )
        db.session.add(addit)
        db.session.add(usera)
        db.session.commit()
    else:
        pass

##customer awards
#id=19
def firsttrade_customer(userid):
    usera = db.session.query(UserAchievements).filter_by(userid=userid).first()
    now = datetime.utcnow()
    if usera.c3 != 1:
        usera.c3 = 1
        usera.c3_date = now
        addit = UserAchievements_recent(
            userid=usera.userid,
            username=usera.username,
            ach_id=19,
            achievement_date=now,
            viewed=0,
        )
        db.session.add(addit)
        db.session.add(usera)
        db.session.commit()
    else:
        pass



##customer awards
#id=32-35
def howmanytrades_customer(userid, number):
    usera = db.session.query(UserAchievements).filter_by(userid=userid).first()
    now = datetime.utcnow()
    if number >= 10:
        ##ach id 32
        if usera.c9 != 1:
            usera.c9 = 1
            usera.c9_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=32,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass
    if number >= 100:
        ##ach id 33
        if usera.c10 != 1:
            usera.c10 = 1
            usera.c10_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=33,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass
    if number >= 500:
        ##ach id 34
        if usera.c11 != 1:
            usera.c11 = 1
            usera.c11_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=34,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass
    if number >= 1000:
        ##ach id 35
        if usera.c12 != 1:
            usera.c12 = 1
            usera.c12_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=34,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass

##customer awards
#id=21-25
def howmanyitemsbought_customer(userid, number):
    usera = db.session.query(UserAchievements).filter_by(userid=userid).first()
    now = datetime.utcnow()
    if number >= 10:
        ##ach id 32
        if usera.c4 != 1:
            usera.c4 = 1
            usera.c4_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=21,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass
    if number >= 100:
        ##ach id 32
        if usera.c5 != 1:
            usera.c5 = 1
            usera.c5_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=22,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass

    if number >= 1000:
        ##ach id 32
        if usera.c6 != 1:
            usera.c6 = 1
            usera.c6_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=23,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass

    if number >= 2500:
        ##ach id 32
        if usera.c7 != 1:
            usera.c7 = 1
            usera.c7_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=24,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass

    if number >= 5000:
        ##ach id 32
        if usera.c8 != 1:
            usera.c8 = 1
            usera.c8_date = now
            addit = UserAchievements_recent(
                userid=usera.userid,
                username=usera.username,
                ach_id=25,
                achievement_date=now,
                viewed=0,
            )
            db.session.add(addit)
            db.session.add(usera)
            db.session.commit()
        else:
            pass
    else:
        pass