import hashlib as _hash
from block import Block



class Chain():

    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.blocks=[]
        self.pool=[]
        self.create_orgin_block()

    def proof_of_work(self,block):
        hash=_hash.sha256()
        hash.update(str(block).encode("utf-8"))

        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(),16) < 2**(256-self.difficulty) and block.previous_hash == self.blocks[-1].hash

    def add_to_chain(self,block):
        if self.proof_of_work(block):
            self.blocks.append(block) 

    def add_to_pool(self,data):
        self.pool.append(data)

    def create_orgin_block(self):

        hash=_hash.sha256()
        hash.update(''.encode('utf-8'))
        origin=Block("origin",hash)
        origin.mine(self.difficulty)
        self.blocks.append(origin)


    def mine(self):
        if len(self.pool)>0:
            data=self.pool.pop() 
            block=Block(data,self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block) 

            print("\n\n===================") 
            print("Hash:\t\t",block.hash.hexdigest())
            print("Previous Hash:\t\t",block.previous_hash.hexdigest())
            print("Nonce;\t\t",block.nonce)
            print("Data:",block.data)
            print("\n\n===============")
               