import sys,pytz,time,pyperclip
from datetime import datetime
FlightNumber = int(sys.argv[1])
AutoCallsign = True if sys.argv[2] == "Y" else False
SameDate = True if sys.argv[3] == "Y" else False
Date = sys.argv[4]

FH_List = {
    "gamerwei_alt": "362922866989072385",
    "sicken_l": "570013631409029120",
    "yojubin23": "663867778523987969",
    "otham1": "256074841789169665",
    "kee_gs": "242105259604836352",
    "sengoplayz": "712636457306816523",
    "robolx_ls": "672633873078681614",
    "hyl_ls": "483361140592869376",
    "ramdoguy3659": "430650178790490114",
    "denipeksen": "705534390310273132",
    "maximtsov": "749214402770894882",
    "kallvins": "755270696329936997",
    "immeralles": "420158829175635968",
    "trulyethane": "756060976444342303",
    "agent_double008": "737631425200783430",
    "a6shiey": "578259013918130207",
    "alt_imeter": "715489622116925480",
    "oppes153": "531466318680162305",
    "violondk": "980710990083665950",
    "avn_ls": "747576555097686037",
    "trulyc3yde": "878017217839656980",
    "j0leg": "738080777253945555",
    "tombad2": "618793147023228928",
    "batbail50": "762713266303926283",
    "trulyymatthew": "750410906919370855",
    "starbucksreserve": "939818316925644800",
    "megashinydiamond123": "782103914648043521",
    "filmboy09": "862987113371795476",
    "trulytraz": "695001201506386040",
    "cameront05092002": "338021233708761090"
}
AirportList = {
    "LHR":"London Heathrow International Airport",
    "LGB":"Long Beach International Airport"
}

StaffAnnounce = "🛫 [<@&474923232294731776> || **__Attendance Logging__**] 🛬\n\nPlease log your attendance for SA {Callsign}.\n\n**[FLIGHT INFORMATION]**\n> **Flight Callsign:** SA {Callsign}\n> **Flight Host:** {FH}\n> **Departure Airport:** {Airport}\n> **Departure Gate:** {Gate}\n> **Aircraft:** {Aircraft}\n> **Arrival Airport:** {Destination}\n\n**[TIME DETAILS]**\n> **Flight Date:** {Flight_Date}\n> **Check-In Time:** {Check_In}\n> **Staff Briefing Time:** {Briefing_Time}\n\n**[FORMAT]**\n> Username - Main Department - Sub Department\n> **Example:** TomBad2 - FD - All\n> **Please use abbreviations for your departments**\n> **Only put your attendance down if you are 100% sure attending.**\n> If something comes up and you have to cancel please edit your attendance to \n> \~\~Username - Main Department - Sub Department\~\~ [Canceled].{Additional_Info}\n\nFor more information, please visit the Flight Calendar or the Trello."
if AutoCallsign == True:
    Callsign = int(input("First Callsign:  "))-1
for i in range(FlightNumber):
    Additional_Info = ""
    Callsign = Callsign + 1 if AutoCallsign == True else int(input("Callsign:  "))
    FH = input("Flight Host:  ").lower()
    FH = f'<@{FH_List[FH]}>' if FH in FH_List else 'HOST NOT FOUND.'
    Flight_Date = input("Flight Date [DD/MM]:  ") if SameDate == False else Date
    Check_In = input("Check-In Time [HH:MM]:  ")
    check_in_datetime_str = f"2024/{Flight_Date} {Check_In}";check_in_datetime = datetime.strptime(check_in_datetime_str, "%Y/%d/%m %H:%M");gmt = pytz.timezone('GMT');check_in_datetime = gmt.localize(check_in_datetime);timestamp = int(check_in_datetime.timestamp())
    Flight_Date = f"<t:{timestamp}:d>"
    Check_In = f"<t:{timestamp}:t>"
    Briefing_Time = f"<t:{timestamp-1800}:t>"
    while True:
        Aircraft = input("Aircraft:  ")
        if "320" in Aircraft:
            Aircraft = "Airbus A320-214"
            break
        elif "330" in Aircraft:
            Aircraft = "Airbus A330-900"
            break
        elif "350" in Aircraft:
            Aircraft = "Airbus A350-900"
            break
        elif "-4" in Aircraft:
            Aircraft = "Boeing 737-400"
            break
        elif "-8" in Aircraft:
            Aircraft = "Boeing 737-800"
            break
        elif "777" in Aircraft:
            Aircraft = "Boeing 777-9X"
            break
        else:
            print("Invalid Aircraft, please retry.")
    Gate = input("Depature Gate:  ")
    Airport = input("Depature Airport [LHR/LGB]:  ").upper()
    Airport = AirportList[Airport] if Airport in AirportList else "Airport Not Found."
    Destination = input("Destination:  ")
    while True:
        Miles = int(input("Miles:  "))
        if Miles >= 1500 and Miles <= 2500:
            break
        else:
            print("Miles must be between 1500 and 2500.")
    if Gate[0].upper() == "B" or Gate.upper() == "A3" or Aircraft == "Airbus A330-900" or Aircraft == "Airbus A350-900" or "KAITAK" in Destination.upper():
        Additional_Info = Additional_Info + "\n\n**[ADDITIONAL INFORMATION]**"
    if Gate[0].upper() == "B":
        Additional_Info = Additional_Info + "\n> This is a Concourse B Flight, <@&698460174842855464> & <@&728064436371325000> are needed."
    if Gate.upper() == "A3":
        Additional_Info = Additional_Info + "\n> This is a gate A3 Flight, <@&698460174842855464> & <@&728064436371325000> are needed."
    if Aircraft == "Airbus A330-900":
        Additional_Info = Additional_Info + "\n> This flight is using the **Airbus A330-900**, a <@&1001135133685985361> Captain is needed."
    if Aircraft == "Airbus A350-900":
        Additional_Info = Additional_Info + "\n> This flight is using the **Airbus A350-900**, a <@&859075016217329665> Captain is needed."
    if "KAITAK" in Destination.upper():
        Additional_Info = Additional_Info + "\n> This is a KaiTak Flight, a <@&1001133811532300298> Captain is needed."
    message = StaffAnnounce.format(Callsign=Callsign,FH=FH,Airport=Airport,Gate=Gate,Aircraft=Aircraft,Destination=Destination,Flight_Date=Flight_Date,Check_In=Check_In,Briefing_Time=Briefing_Time,Additional_Info=Additional_Info)
    pyperclip.copy(message)
    print(message)
    time.sleep(5)