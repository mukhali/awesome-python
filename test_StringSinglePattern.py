from StringSinglePattern import StringSinglePattern

class TestStringSinglePattern():
    def setup(self):
        self.a = StringSinglePattern("adaddafkaksaf","ks")

    def test_brute_force(self):
        assert 9 == self.a.brute_force()

    def test_kmp(self):
        assert 9 == self.a.kmp()

    def test_bm(self):
        assert 9 == self.a.bm()

    def test_sunday(self):
        assert 9 == self.a.sunday()

    # def test_get_balance(self):
    #     assert 1000 == self.ba.get_balance()

    # def test_deposit_negative_amount(self):
    #     assert False == self.ba.deposit(-500)

    # def test_deposit_positive_amount(self):
    #     self.ba.deposit(500)
    #     assert 1500 == self.ba.get_balance()

    # def test_withdraw_more_than_balance(self):
    #     assert False == self.ba.withdraw(2500)

    # def test_withdraw_amount_less_than_balance(self):
    #     self.ba.withdraw(600)
    #     assert 400  == self.ba.get_balance()

