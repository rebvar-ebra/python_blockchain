import hashlib as _hash


class Block():
    def __init__(self,data,previous_hash) -> None:
        self.hash=_hash.sha256()
        self.previous_hash= previous_hash
        self.nonce=0
        self.data=data

    def mine(self,difficulty):
        self.hash.update(str(self).encode('utf-8'))

        while int(self.hash.hexdigest(),16) >2**(256-difficulty):
            self.nonce+=1
            self.hash=_hash.sha256()
            self.hash.update(str(self).encode('UTF-8'))

    def __str__(self):
        return"{}{}{}".format(self.previous_hash.hexdigest(),self.data,self.nonce)
        