class Market:
    def __init__(self, title, balance):
        self.title = title
        self.baza = []
        self.balance = balance


market = Market("Uzum Market", 10000)


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


tavarlar = [
    Mahsulotlar("kartoshka", 9000, "02/02/2025"),
    Mahsulotlar("fanta", 15000, "02/06/2025"),
    Mahsulotlar("go`sht", 110000, "02/01/2025"),
    Mahsulotlar("piyoz", 4500, "09/02/2025"),
    Mahsulotlar("sabzi", 3000, "02/01/2025"),
    Mahsulotlar("sok", 12000, "02/07/2025"),
    Mahsulotlar("cola", 15000, "02/09/2025"),
    Mahsulotlar("shokalad", 30000, "02/12/2025"),
    Mahsulotlar("guruch", 25000, "02/01/2026"),
    Mahsulotlar("shakar", 14000, "02/03/2026"),
]


class User:
    def __init__(self, phone, card, is_admin, is_client, password):
        self.phone = phone
        self.card = card
        self.korzina = []
        self.is_admin = is_admin
        self.is_client = is_client
        self.password = password


users = [
    User("+998900199921", 8600130963070000, False, True, "4455"),
    User("+998900199922", 8600130963070001, False, True, "4456"),
    User("+998900199923", 8600130963070002, False, True, "4457"),
    User("+998900199924", 8600130963070003, False, True, "4458"),
    User("+998900199925", 8600130963070004, True, False, "4459"),
]


def authenticate():
    phone = input("Telefon raqamingizni kiriting: ")
    password = input("Parolni kiriting: ")
    for user in users:
        if user.phone == phone and user.password == password:
            print("Tizimga muvaffaqiyatli kirdingiz!")
            return user
    print("Telefon yoki parol noto'g'ri!")
    return None


def work():
    user = authenticate()
    if not user:
        return

    while True:
        status = input(f"\n{market.title}ga xush kelibsiz!"
                       f"\n1. Mahsulotlarni ko'rish"
                       f"\n2. Korzinani ko'rish"
                       f"\n0. Chiqish\nTanlang: ")

        if status == "0":
            break
        elif status == "1":
            for idx, item in enumerate(tavarlar, 1):
                print(f"{idx}. Mahsulot: {item.nomi}, Narxi: {item.narx}, Mavjud soni: {item.soni}")

            try:
                choice = int(input("Mahsulot raqamini tanlang: ")) - 1
                if 0 <= choice < len(tavarlar):
                    miqdori = int(input("Miqdorni kiriting: "))
                    selected_item = tavarlar[choice]
                    if selected_item.soni >= miqdori:
                        user.korzina.append((selected_item, miqdori))
                        selected_item.soni -= miqdori
                        print(f"{selected_item.nomi} korzinaga qo'shildi!")
                    else:
                        print("Yetarli miqdor mavjud emas!")
                else:
                    print("Noto'g'ri mahsulot raqami!")
            except ValueError:
                print("Noto'g'ri tanlov!")
        elif status == "2":
            if not user.korzina:
                print("Korzina bo'sh!")
            else:
                print("Korzina:")
                for item, miqdor in user.korzina:
                    print(f"{item.nomi} - {miqdor} dona, Jami narx: {miqdor * item.narx}")
        else:
            print("Noto'g'ri tanlov!")


work()
