# eth2-tools
Scripts to speed up eth2 testing

## array_to_hex.py
Converts an array of bytes in decimal form to a hex string.

## convert_aggregation_bits.py
Converts all the aggregation bits from an array of bytes in decimal form to hex strings.

## convert_block_body_to_rust.py
Converts a Beacon block body response to Rust object instance (can be used to paste in [Snowbridge merklization tests](https://github.com/Snowfork/snowbridge/blob/main/parachain/pallets/ethereum-beacon-client/src/merkleization.rs#L390)).
