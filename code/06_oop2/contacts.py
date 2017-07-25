GOMAIL_SERVER = "mx.gomail.com"
YOMAIL_SERVER = "mx.yomail.com"


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class GoogleAccount(Contact):
    synced_contacts = []

    def sync(self):
        print("Syncing {} contact with Server".format(self.name))
        GoogleAccount.synced_contacts.append(self)
        return True

    def __str__(self):
        return "{}, {}".format(self.name, self.email)


class YahooAccount(Contact):
    synced_contacts = []

    def sync(self):
        print("Syncing {} contact with Server".format(self.name))
        YahooAccount.synced_contacts.append(self)
        return True

    def __str__(self):
        return "{}, {}".format(self.name, self.email)


c1 = GoogleAccount("Guido", "guido@python.org.in")
c2 = YahooAccount("Matz", "matz@ruby-lang.org")
c3 = Contact("Peter Norgiv", "peter@Norvig.com")
c4 = Contact("Bjarne", "bjarne@stroustrup.com")
c5 = GoogleAccount("Linus", "torvalds@transmeta.com")
c6 = YahooAccount("Richard Stallman", "rms@gnu.org")
c1.sync()
c2.sync()
print(GoogleAccount.synced_contacts)
c5.sync()
c6.sync()
print(GoogleAccount.synced_contacts)
print(YahooAccount.synced_contacts)
