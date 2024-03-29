from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract, fund_with_link

from brownie import AdvancedCollectible, network, config

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    #We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"), get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from":account},
         publish_source=config["networks"][network.show_active()].get("verify",False)
    )
    fund_with_link(advanced_collectible.address)
    print ({AdvancedCollectible[-1].address})
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print ("New token has been created")
    return advanced_collectible, creating_tx

def main():
    deploy_and_create()