from web3 import Web3
import json

httpsUrl = "https://sepolia.infura.io/v3/1de33844f96b42a19495503e56672325"
w3 = Web3(Web3.HTTPProvider(httpsUrl))
print(w3.is_connected())

print(w3.eth.block_number)


acc = "0x6Cc713B11BFC80fA7E0e8D7d29Ca29Cc07d1f028"
address = "0xCe4C6339Eca4f53AC6370Ec2747A0749a11C8957"
abi = json.loads(open('abi.json').read())
contract = w3.eth.contract(address=address, abi=abi)

#function
pool = contract.functions
totSupply = pool.totalSupply().call()
print("total Supply:", totSupply)

# Events 
event = contract.events.Approval().get_logs(fromBlock='latest')
print('Events', event)



