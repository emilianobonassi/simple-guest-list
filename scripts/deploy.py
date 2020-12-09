from brownie import SimpleGuestList, accounts, network

def main():
    print(f"You are using the '{network.show_active()}' network")
    dev = accounts.load("dev")
    print(f"You are using: 'dev' [{dev.address}]")

    if input("Deploy SimpleGuestList? y/[N]: ").lower() != "y":
        return

    strategy = SimpleGuestList.deploy({"from": dev})
