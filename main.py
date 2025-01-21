import time
import requests
from bs4 import BeautifulSoup
from pypresence import Presence
from datetime import datetime

def time_in_24():
    # Get the current time
    current_time = datetime.now()

    # Format the time as needed
    formatted_time = current_time.strftime("%H:%M:%S")

    # Return the current time
    return str(formatted_time)

def main():
    # My Application ID for Tower Unite
    CLIENT_ID = '1330069852550860810'
    RPC = Presence(CLIENT_ID)
    RPC.connect()
    print("Connected to Discord.")

    url = f"https://steamcommunity.com/miniprofile/{miniprofile_id}"

    while True:
        time.sleep(15)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        game_details = soup.find("span", class_="game_state")
        game_name = soup.find("span", class_="miniprofile_game_name")
        steam_rpc = soup.find("span", class_="rich_presence")

        # if you are not playing anything in your steam
        if game_details == None:
            print(f"[{time_in_24()}]: User isn't playing Tower Unite")
            RPC.update(details="Not Playing Tower Unite")
            continue
        
        # if you are not playng tower unite
        if game_name == None or game_name.text != "Tower Unite":
            print(f"[{time_in_24()}]: User isn't playing Tower Unite")
            RPC.update(details="Not Playing Tower Unit")
            continue

        # if your steam RPC show nothing, usually happen in map swapping
        if steam_rpc == None:
            print(f"[{time_in_24()}]: User is playing Tower Unite")
            RPC.update(details="At Main Menu",
                    large_image="towerunite_main_menu",
                    large_text="At Main Menu")
            continue

        #
        #
        #
        #
        #

        # if steam RPC is available
        print(f"[{time_in_24()}]: User is playing {steam_rpc.text}")

        separated_space = steam_rpc.text.split(' ')
        separated_plaza = steam_rpc.text.split(':')
        separated_game = separated_plaza[0].lower().split('-')
        if separated_space[0] == "Waiting":
            # Waiting
            RPC.update(details=steam_rpc.text,
                large_image="towerunite_game_ports",
                large_text=steam_rpc.text)
        elif separated_plaza[0] == "In the Plaza":
            # Game Ports
            if separated_plaza[1] == " GAME PORTS":
                RPC.update(details=steam_rpc.text,
                    large_image="towerunite_game_ports",
                    large_text=steam_rpc.text)
            # Condo Hub
            elif separated_plaza[1] == " CONDO HUB":
                RPC.update(details=steam_rpc.text,
                    large_image="towerunite_condo_hub",
                    large_text=steam_rpc.text)
            # Plaza
            else:
                RPC.update(details=steam_rpc.text,
                    large_image="towerunite_plaza",
                    large_text=steam_rpc.text)
        elif list(steam_rpc.text)[-1] == "]":
            # Game World
            RPC.update(details=steam_rpc.text,
                large_image=f"towerunite_{separated_game[0]}",
                large_text=steam_rpc.text)
        else:
            # Condo
            separated_condo = steam_rpc.text.split('-')
            if separated_condo[0] == "Condo":
                your_condo = separated_condo[1].lower().split(' ')
                condo_name = ""
                for i in range(len(your_condo)):
                    condo_name += your_condo[i]
                    if your_condo[i] != your_condo[-1]:
                        condo_name += '_'
                RPC.update(details=steam_rpc.text,
                    large_image=f"towerunite_condo_{condo_name}",
                    large_text=steam_rpc.text)
            # Main Menu
            else:
                RPC.update(details=steam_rpc.text,
                    large_image="towerunite_main_menu",
                    large_text=steam_rpc.text)
            

if __name__ == "__main__":
    
    # pip install -r requirements.txt
    # type your information here
    miniprofile_id = #########
    # ////////////////////

    main()