def get_description():   #下記docstringを参照
    """プロと同じようにランダムな転記を返す"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

 
