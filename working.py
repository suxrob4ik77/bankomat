
# from mahsulotlar import tavarlar


class Market:
    def __init__(self, title, balance):
        self.title = title
        self.baza = []
        self.balance = balance


market = Market("Uzum Market",10000)
# market.baza.append(tavarlar)


class History:
    def __init__(self, user, tovar, miqdori, narx):
        self.user = user
        self.tovar = tovar
        self.miqdori = miqdori
        self.narx = narx

class Mahsulotlar:
    def __init__(self, nomi, narx, muddat):
        self.nomi = nomi
        self.narx = narx
        self.muddat = muddat
        self.soni = 100


tavar1 = Mahsulotlar("kartoshka", 9000, "02/02/2025")
tavar2 = Mahsulotlar("fanta", 15000, "02/06/2025")
tavar3 = Mahsulotlar("go`sht", 110000, "02/01/2025")
tavar4 = Mahsulotlar("piyoz", 4500, "09/02/2025")
tavar5 = Mahsulotlar("sabzi", 3000, "02/01/2025")
tavar6 = Mahsulotlar("sok", 12000, "02/07/2025")
tavar7 = Mahsulotlar("cola", 15000, "02/09/2025")
tavar8 = Mahsulotlar("shokalad", 30000, "02/12/2025")
tavar9 = Mahsulotlar("guruch", 25000, "02/01/2026")
tavar10 = Mahsulotlar("shakar", 14000, "02/03/2026")
tavarlar = [tavar1, tavar2, tavar3, tavar4, tavar5, tavar6, tavar7, tavar8, tavar9, tavar10]


class User:
    def __init__(self, phone, card, korzina, is_admin, is_client, password):
        self.phone = phone
        self.card = card
        self.korzina = []
        self.is_admin = is_admin
        self.as_client = is_client
        self.password = password

user_1 = User(+998900199921, 8600130963070000, None, False, True, 4455)
user_2 = User(+998900199922, 8600130963070001, None, False, True, 4456)
user_3 = User(+998900199923, 8600130963070002, None, False, True, 4457)
user_4 = User(+998900199924, 8600130963070003, None, False, True, 4458)
user_5 = User(+998900199925, 8600130963070004, None, True, False, 4459)

users = [user_1, user_2, user_3, user_4, user_5]


# from users import users
# from market import market
# from mahsulotlar import tavarlar
# from history import History


def work():
    while True:
        status = input(f"{market.title}ga xush kelibsiz!"
                       f"\nMahsulotlarni ko`rish: 1 \nKorzinkani ko`rish: 2 \nChiqish: 0 ")
        if status == "0":
            break
        if status == "1":
            for item in tavarlar:
                print(f"Mahsulot nomi: {item.nomi}, narxi: {item.narx}")
            status1 = input("Mahsulot nomini kiriting: ")
            miqdori = int(input("Miqdorini kiriting: "))
            cart=input(f"{users.ca}")
        # if status =="2":




work()
