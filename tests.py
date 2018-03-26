import pytest
import crypto.xor


def test_crypto_xor_decode_ok():
    assert crypto.xor.decyph("'-,", "foo") == "ABC"


def test_crypto_xor_decode_fail():
    assert not crypto.xor.decyph("'-,", "foo") == "ABD"


def test_crypto_xor_main_ok():
    assert crypto.xor.main(["xor.py", "'-,'", "foo"]) == 0
