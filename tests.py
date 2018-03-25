import pytest
import Crypto.xor


def test_xor_decode_ok():
    assert Crypto.xor.decyph("'-,","foo") == "ABC"
