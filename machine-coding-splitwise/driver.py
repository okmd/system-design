import sys
sys.path.append('E:\Danish\Projects\coding-problems\system-design\low-level-machine-coding')
from splitwise.conrollers import UserController, GroupController, BillController
from splitwise.services import BillService, UserService, GroupService

userC = UserController(UserService())
groupC = GroupController(GroupService())
billC = BillController(BillService())

user_rm = userC.add_user(1, 'RM')
user_as = userC.add_user(2, 'AS')
user_sp = userC.add_user(3, 'SP')
user_aj = userC.add_user(4, 'AJ')
user_ds = userC.add_user(5, 'DS')

swe_members = [user_rm, user_as, user_sp, user_aj, user_ds]
group_swe = groupC.add_group(1, "SWE", swe_members)
swe_amount = 1000
swe_equal = swe_amount/len(swe_members)
# swe dept split equally;
equal_contributions = {1: swe_equal, 2: swe_equal,
                       3: swe_equal, 4: swe_equal, 5: swe_equal}
# who actually paid the bills
actual_contributors = {1: 400, 2: 500, 3: 100, 4: 0, 5: 0}
bill1 = billC.add_bill('b1', 1, swe_amount, equal_contributions, actual_contributors)

for user in swe_members:
    user_id = user.get_id()
    name = user.get_name()
    amt = billC.get_user_balance(user_id)
    print(name, f" will pay {-amt}" if amt < 0 else f" will get {amt}")
print("*"*100)

# ############################ KITTY #########################

kitty_party_members = [user_rm, user_as, user_sp, user_aj]
group_kitty_pary = groupC.add_group(2, "Kitty", kitty_party_members)
kitty_amount = 4000
kitty_equal = kitty_amount/len(kitty_party_members)
# swe dept split equally;
equal_contributions = {1: kitty_equal, 2: kitty_equal,
                       3: kitty_equal, 4: kitty_equal}
# who actually paid the bills
actual_contributors = {1: 600, 2: 1000, 3: 2000, 4: 400,}
bill1 = billC.add_bill('b2', 2, kitty_amount, equal_contributions, actual_contributors)

for user in kitty_party_members:
    user_id = user.get_id()
    name = user.get_name()
    amt = billC.get_user_balance(user_id)
    print(name, f" will pay {-amt}" if amt < 0 else f" will get {amt}")


# RM  will get 200.0
# AS  will get 300.0
# SP  will pay 100.0
# AJ  will pay 200.0
# DS  will pay 200.0
# ******************
# RM  will pay 200.0
# AS  will get 300.0
# SP  will get 900.0
# AJ  will pay 800.0

