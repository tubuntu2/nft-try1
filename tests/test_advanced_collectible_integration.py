
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from brownie import network
import pytest, time
from scripts.AdvancedCollectible.deploy_and_create import deploy_and_create

def test_can_create_simple_collection():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    #Act
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(240)
    #Assert
    assert advanced_collectible.tokenCounter() == 1
    
    