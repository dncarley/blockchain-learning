from blockchain import Blockchain


def test_blockchain():
    blockchain = Blockchain()
    assert blockchain.current_transactions == []