import hashlib as _hash


class Consensus():
    def proof_of_work(self,block):
        hash=_hash.sha256()
        hash.update(str(block).encode("utf-8"))

        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(),16) < 2**(256-self.difficulty) and block.previous_hash == self.blocks[-1].hash