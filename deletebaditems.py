# deletes items that dont have an image and isnt online

from helperfunctions.deleteitem import deletefromdb


def deleteloop():
    """
    This function calls helperfunction to look for deleted items in db and delete
    """
    deletefromdb()


deleteloop()
