from alaya.packages.platon_keys.datatypes import PrivateKey
from alaya.packages.platon_keys.utils import address as Address


def private_key_to_address(private_key: str, prefix=None):
    """
    Args:
        private_key: private key hex string
        prefix: expected bech32 address prefix, if none, return hex address
    """
    pk_bytes = bytes.fromhex(private_key)
    Private_Key = PrivateKey(pk_bytes)
    address = Private_Key.public_key.to_address()
    if not prefix:
        return address
    return hex_address_to_bech32_address(address[2:], prefix)


def hex_address_to_bech32_address(address: str, prefix: str):
    """
    Args:
        address: hex address string
        prefix: expected bech32 address prefix
    """
    hex_address = bytes.fromhex(address)
    return Address.address_bytes_to_bech32_address(hex_address, hrp=prefix)


def bech32_address_to_hex_address(address: str):
    """
    Args:
        address: bech32 address string
    """
    prefix = address[0:2]
    print(prefix)
    return Address.bech32_address_to_address_bytes(address, prefix)


if __name__ == '__main__':
    print(private_key_to_address('255674f79fe4f81b21529a6fa8cd4a3baa5f2973a81012a4a207f154ca8c9210'))
    print(private_key_to_address('255674f79fe4f81b21529a6fa8cd4a3baa5f2973a81012a4a207f154ca8c9210', 'lat'))
    print(private_key_to_address('255674f79fe4f81b21529a6fa8cd4a3baa5f2973a81012a4a207f154ca8c9210', 'lax'))
    print(private_key_to_address('255674f79fe4f81b21529a6fa8cd4a3baa5f2973a81012a4a207f154ca8c9210', 'atp'))
    print(private_key_to_address('255674f79fe4f81b21529a6fa8cd4a3baa5f2973a81012a4a207f154ca8c9210', 'atx'))

