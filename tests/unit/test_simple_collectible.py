from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network
import pytest
from scripts.AdvancedCollectible.deploy_and_create import deploy_and_create

def test_can_create_simple_collection():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collective = deploy_and_create()
    assert simple_collective.ownerOf(0) == get_account()
    