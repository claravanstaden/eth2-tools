# Opening JSON file
import json

f = open('in/input.json')

data = json.load(f)

f.close()


def remove_zero_hash(input):
    return input.replace("0x", "")


resultString = "Body{\n"
resultString += "\trandao_reveal: hex!(\"" + remove_zero_hash(data["body"]["randao_reveal"]) + "\").to_vec(),\n"
resultString += "\teth1_data: Eth1Data{\n"
resultString += "\t\tdeposit_root: hex!(\"" + remove_zero_hash(
    data["body"]["eth1_data"]["deposit_root"]) + "\").into(),\n"
resultString += "\t\tdeposit_count: " + data["body"]["eth1_data"]["deposit_count"] + ",\n"
resultString += "\t\tblock_hash: hex!(\"" + remove_zero_hash(data["body"]["eth1_data"]["block_hash"]) + "\").into(),\n"
resultString += "\t},\n"
resultString += "\tgraffiti: hex!(\"" + remove_zero_hash(data["body"]["graffiti"]) + "\").into(),\n"

resultString += "\tproposer_slashings: vec![\n"
for prop_slash in data["body"]["proposer_slashings"]:
    resultString += "\t\tProposerSlashing{\n"
    resultString += "\t\t\tsigned_header_1: SignedHeader{\n"
    resultString += "\t\t\t\tmessage: BeaconHeader{\n"
    resultString += "\t\t\t\t\tslot: " + prop_slash["signed_header_1"]["message"]["slot"] + ",\n"
    resultString += "\t\t\t\t\tproposer_index: " + prop_slash["signed_header_1"]["message"]["proposer_index"] + ",\n"
    resultString += "\t\t\t\t\tparent_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_1"]["message"]["parent_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tstate_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_1"]["message"]["state_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tbody_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_1"]["message"]["body_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t\tsignature: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_1"]["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t\tsigned_header_2: SignedHeader{\n"
    resultString += "\t\t\t\tmessage: BeaconHeader{\n"
    resultString += "\t\t\t\t\tslot: " + prop_slash["signed_header_2"]["message"]["slot"] + ",\n"
    resultString += "\t\t\t\t\tproposer_index: " + prop_slash["signed_header_2"]["message"]["proposer_index"] + ",\n"
    resultString += "\t\t\t\t\tparent_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_2"]["message"]["parent_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tstate_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_2"]["message"]["state_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tbody_root: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_2"]["message"]["body_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t\tsignature: hex!(\"" + remove_zero_hash(
        prop_slash["signed_header_2"]["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t},\n"
resultString += "\t],\n"

resultString += "\tattester_slashings: vec![\n"
for att_slash in data["body"]["attester_slashings"]:
    resultString += "\t\tAttesterSlashing{\n"
    resultString += "\t\t\tattestation_1: IndexedAttestation{\n"
    resultString += "\t\t\t\tattesting_indices: [\n"
    for indices in att_slash["indices"]:
        resultString += "\t\t\t\t\t" + indices + ",\n"
    resultString += "\t\t\t\t]\n"
    resultString += "\t\t\t\tdata: AttestationData{\n"
    resultString += "\t\t\t\t\tslot: " + att_slash["attestation_1"]["data"]["slot"] + ",\n"
    resultString += "\t\t\t\t\tindex: " + att_slash["attestation_1"]["data"]["index"] + ",\n"
    resultString += "\t\t\t\t\tbeacon_block_root: hex!(\"" + remove_zero_hash(
        att_slash["attestation_1"]["data"]["beacon_block_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tsource: Checkpoint{\n"
    resultString += "\t\t\t\t\t\tepoch: " + att_slash["attestation_1"]["data"]["source"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\t\troot: hex!(\"" + remove_zero_hash(
        att_slash["attestation_1"]["data"]["source"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t\t},\n"
    resultString += "\t\t\t\t\ttarget: Checkpoint{\n"
    resultString += "\t\t\t\t\t\tepoch: " + att_slash["attestation_1"]["data"]["target"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\t\troot: hex!(\"" + remove_zero_hash(
        att_slash["attestation_1"]["data"]["target"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t\t},\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t\tsignature: hex!(\"" + remove_zero_hash(
        att_slash["attestation_1"]["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t\tattestation_2: IndexedAttestation{\n"
    resultString += "\t\t\t\tattesting_indices: [\n"
    for indices in att_slash["indices"]:
        resultString += "\t\t\t\t\t" + indices + ",\n"
    resultString += "\t\t\t\t]\n"
    resultString += "\t\t\t\tdata: AttestationData{\n"
    resultString += "\t\t\t\t\tslot: " + att_slash["attestation_2"]["data"]["slot"] + ",\n"
    resultString += "\t\t\t\t\tindex: " + att_slash["attestation_2"]["data"]["index"] + ",\n"
    resultString += "\t\t\t\t\tbeacon_block_root: hex!(\"" + remove_zero_hash(
        att_slash["attestation_2"]["data"]["beacon_block_root"]) + "\").into(),\n"
    resultString += "\t\t\t\t\tsource: Checkpoint{\n"
    resultString += "\t\t\t\t\t\tepoch: " + att_slash["attestation_2"]["data"]["source"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\t\troot: hex!(\"" + remove_zero_hash(
        att_slash["attestation_2"]["data"]["source"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t\t},\n"
    resultString += "\t\t\t\t\ttarget: Checkpoint{\n"
    resultString += "\t\t\t\t\t\tepoch: " + att_slash["attestation_2"]["data"]["target"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\t\troot: hex!(\"" + remove_zero_hash(
        att_slash["attestation_2"]["data"]["target"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t\t},\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t\tsignature: hex!(\"" + remove_zero_hash(
        att_slash["attestation_2"]["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t}\n"
resultString += "\t],\n"

resultString += "\tattestations: vec![\n"
for attestation in data["body"]["attestations"]:
    resultString += "\t\tAttestation{\n"
    resultString += "\t\t\taggregation_bits: hex!(\"" + remove_zero_hash(
        attestation["aggregation_bits"]) + "\").to_vec(),\n"
    resultString += "\t\t\tdata: AttestationData{\n"
    resultString += "\t\t\t\tslot: " + attestation["data"]["slot"] + ",\n"
    resultString += "\t\t\t\tindex: " + attestation["data"]["index"] + ",\n"
    resultString += "\t\t\t\tbeacon_block_root: hex!(\"" + remove_zero_hash(
        attestation["data"]["beacon_block_root"]) + "\").into(),\n"
    resultString += "\t\t\t\tsource: Checkpoint{\n"
    resultString += "\t\t\t\t\tepoch: " + attestation["data"]["source"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\troot: hex!(\"" + remove_zero_hash(attestation["data"]["source"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t\ttarget: Checkpoint{\n"
    resultString += "\t\t\t\t\tepoch: " + attestation["data"]["target"]["epoch"] + ",\n"
    resultString += "\t\t\t\t\troot: hex!(\"" + remove_zero_hash(attestation["data"]["target"]["root"]) + "\").into()\n"
    resultString += "\t\t\t\t},\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t\tsignature: hex!(\"" + remove_zero_hash(attestation["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t},\n"
resultString += "\t],\n"

resultString += "\tdeposits: vec![\n"
for deposit in data["body"]["deposits"]:
    resultString += "\t\tDeposit{\n"
    resultString += "\t\t\tproof: [\n"
    for proof in deposit["proof"]:
        resultString += "\t\t\t\t" + proof + ",\n"
    resultString += "\t\t\t],\n"
    resultString += "\t\t\tdata: DepositData{\n"
    resultString += "\t\t\t\tpubkey: hex!(\"" + remove_zero_hash(deposit["pubkey"]) + "\").to_vec(),\n"
    resultString += "\t\t\t\twithdrawal_credentials: hex!(\"" + remove_zero_hash(
        deposit["withdrawal_credentials"]) + "\").into(),\n"
    resultString += "\t\t\t\tamount: " + deposit["amount"] + ",\n"
    resultString += "\t\t\t\tsignature: hex!(\"" + remove_zero_hash(deposit["signature"]) + "\").to_vec(),\n"
    resultString += "\t\t\t},\n"
    resultString += "\t\t},\n"
resultString += "\t],\n"

resultString += "\tvoluntary_exits:vec![\n"
for voluntary_exit in data["body"]["voluntary_exits"]:
    resultString += "\t\tVoluntaryExit{\n"
    resultString += "\t\t\tepoch: " + voluntary_exit["epoch"] + ",\n"
    resultString += "\t\t\tvalidator_index: " + voluntary_exit["validator_index"] + ",\n"
    resultString += "\t\t},\n"
resultString += "\t],\n"

resultString += "\tsync_aggregate: SyncAggregate{\n"
resultString += "\t\tsync_committee_bits: hex!(\"" + remove_zero_hash(
    data["body"]["sync_aggregate"]["sync_committee_bits"]) + "\").to_vec(),\n"
resultString += "\t\tsync_committee_signature: hex!(\"" + remove_zero_hash(
    data["body"]["sync_aggregate"]["sync_committee_signature"]) + "\").to_vec(),\n"
resultString += "\t},\n"

resultString += "\texecution_payload: ExecutionPayload{\n"
resultString += "\t\tparent_hash: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["parent_hash"]) + "\").into(),\n"
resultString += "\t\tfee_recipient: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["fee_recipient"]) + "\").to_vec(),\n"
resultString += "\t\tstate_root: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["state_root"]) + "\").into(),\n"
resultString += "\t\treceipts_root: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["receipts_root"]) + "\").into(),\n"
resultString += "\t\tlogs_bloom: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["logs_bloom"]) + "\").to_vec(),\n"
resultString += "\t\tprev_randao: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["prev_randao"]) + "\").into(),\n"
resultString += "\t\tblock_number: " + data["body"]["execution_payload"]["block_number"] + ",\n"
resultString += "\t\tgas_limit: " + data["body"]["execution_payload"]["gas_limit"] + ",\n"
resultString += "\t\tgas_used: " + data["body"]["execution_payload"]["gas_used"] + ",\n"
resultString += "\t\ttimestamp: " + data["body"]["execution_payload"]["timestamp"] + ",\n"
resultString += "\t\textra_data: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["extra_data"]) + "\").into(),\n"
resultString += "\t\tbase_fee_per_gas: U256::from(" + data["body"]["execution_payload"][
    "base_fee_per_gas"] + " as u8),\n"
resultString += "\t\tblock_hash: hex!(\"" + remove_zero_hash(
    data["body"]["execution_payload"]["block_hash"]) + "\").into(),\n"
resultString += "\t\ttransactions_root: hex!(\"7ffe241ea60187fdb0187bfa22de35d1f9bed7ab061d9401fd47e34a54fbede1\").into(),\n"
resultString += "\t}\n"
resultString += "}\n"

text_file = open("out/out.txt", "w")

text_file.write(resultString)

text_file.close()
