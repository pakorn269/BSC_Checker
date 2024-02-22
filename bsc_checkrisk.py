from web3 import Web3

# Replace with your desired wallet address
wallet_address = "YOUR_WALLET_ADDRESS"

# Replace with the contract address you want to check
contract_address = "CONTRACT_ADDRESS"

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))

# Get contract ABI (Application Binary Interface)
with open("contract_abi.json") as f:
    abi = json.load(f)

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Get token information
token_address = contract.functions["token"]().call()

# Get approval information
approval_data = contract.functions["allowance"](wallet_address, token_address).call()

# Format approval data
allowance = web3.toWei(approval_data, "ether")  # Convert to human-readable format

# Get block timestamp for approval date
block_number = contract.functions["getApprovedBlock"](wallet_address, token_address).call()
approve_date = web3.eth.get_block(block_number)["timestamp"]

# Get transaction details (optional)
tx_hash = contract.functions["approve"](token_address, allowance).call()
tx_details = web3.eth.get_transaction(tx_hash)

# Print results
print(f"Contract: {contract_address}")
print(f"Token: {token_address}")
print(f"Approve Date: {approve_date}")
print(f"TX: {tx_hash}")
print(f"Allowance: {allowance} (BNB)")

# Additional functionality (optional)
# - Display token name and symbol using the token contract
# - Implement error handling for failed function calls
# - Include date formatting for better readability
# - Add logic to handle multiple tokens and contracts

