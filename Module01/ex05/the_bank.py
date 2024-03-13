# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   the_bank.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2024/03/13 00:42:23 by vafleith          #+#    #+#              #
#   Updated: 2024/03/13 00:42:23 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Account():
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        self.name = name
        Account.ID_COUNT += 1

        if not hasattr(self, "value"):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def is_corrputed(self):
        attributes = list(self.__dict__.keys())
        if len(attributes) % 2 == 0:
            return True
        if (
            "name" not in attributes
            or "id" not in attributes
            or "value" not in attributes
        ):
            return True
        if (
            not isinstance(self.name, str)
            or not isinstance(self.id, int)
            or not isinstance(self.value, (int, float))
        ):
            return True
        no_zip_or_addr = True
        for attr in attributes:
            if attr.startswith("b"):
                return True
            if attr.startswith("zip") or attr.startswith("addr"):
                no_zip_or_addr = False
                break
        return no_zip_or_addr


class Bank():
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if isinstance(new_account, Account):
            if len(self.accounts) == 0:
                self.accounts.append(new_account)
                return True
            for account in self.accounts:
                if account.name == new_account.name:
                    return False
            self.accounts.append(new_account)
            return True
        return False

    def get_account(self, name) -> Account or None:
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def transfer(self, origin, dest, amount):
        """ " Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin_account = self.get_account(origin)
        dest_account = self.get_account(dest)
        if origin_account or dest_account is None:
            return False
        if origin_account.name == dest_account.name:
            return True
        if not origin_account.is_corrputed() and not dest_account.is_corrputed():
            if origin_account.value >= amount > 0:
                origin_account.value -= amount
                dest_account.transfer(amount)
                return True
            return False

    def fix_account(self, name):
        """fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = self.get_account(name)
        if account is None:
            return False
        attributes = list(self.__dict__.keys())
        if "name" not in attributes:
            account.__dict__.update({"name": name})
        if "value" not in attributes:
            account.__dict__.update({"value": 0})
        if "addr" not in attributes:
            account.__dict__.update({"addr": ""})
        if "zip" not in attributes:
            account.__dict__.update({"zip": ""})
        for attr in attributes:
            if attr.startswith("b"):
                del account.__dict__[attr]
        if len(account.__dict__.keys()) % 2 == 0:
            print(account.__dict__.keys())
            return False
        if account.is_corrputed():
            return False
        return True


