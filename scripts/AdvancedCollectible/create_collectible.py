from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract, fund_with_link
from web3 import Web3
from brownie import AdvancedCollectible, network, config

def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount = Web3.toWei(0.1,"ether"))
    create_tx = advanced_collectible.createCollectible({"from": account})
    create_tx.wait(1)
    print ("Collectible created!")
