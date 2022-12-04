def DataBundles():
    def data_pack(value, data_value, validity):
        def check_Airtime():
            """Check if the airtime balance is greater than or equal to the amount required to activate data bundle"""
            for count in range(3):  # Maximum number of retries customers have
                y = input(f"{data_value} for {validity} at N{value}.\n"
                          f"Choose what happens after your plan finishes?\n"
                          f"1.Continue browsing from airtime / 160mb extra\n"
                          f"2.Stop my data\n"
                          f": ")
                if y == '1':
                    if airtime_balance >= value:
                        print(f"You have successfully activated {data_value} for {validity}\n"
                              "And PAYG is now active after bundle finishes")
                        quit()
                    else:
                        print("Dear Customer, you do not have sufficient airtime to buy this bundle.\n"
                              "Please recharge and try again or Dial *500# to BORROW DATA and pay back Later.")
                        quit()
                elif y == '2':
                    if airtime_balance >= value:
                        print(f"You have successfully activated {data_value} for {validity}\n"
                              "And you will be disconnected once bundle finishes")
                        quit()
                    else:
                        print("Dear Customer, you do not have sufficient airtime to buy this bundle.\n"
                              "Please recharge and try again or Dial *500# to BORROW DATA and pay back Later.")
                        quit()
                else:
                    print("Invalid Entry")
            else:
                print("Too Many Attempts. Code Error")
                quit()

        check_Airtime()

    def data_pack_on(value, data_value, validity):
        def check_Airtime():
            """Check if the airtime balance is greater than or equal to the amount required to activate data bundle"""
            for count in range(3):  # Maximum number of retries customers have
                y = input(f"N{value} / {data_value} / {validity}.\n"
                          f"Choose what happens after your plan finishes?\n"
                          f"1.Continue browsing from airtime / 160mb extra\n"
                          f"2.Stop my data\n"
                          f": ")
                if y == '1':
                    if airtime_balance >= value:
                        print(f"You have successfully activated {data_value} for {validity}\n"
                              "And PAYG is now active after bundle finishes")
                        quit()
                    else:
                        print("Dear Customer, you do not have sufficient airtime to buy this bundle.\n"
                              "Please recharge and try again or Dial *500# to BORROW DATA and pay back Later.")
                        quit()
                elif y == '2':
                    if airtime_balance >= value:
                        print(f"You have successfully activated {data_value} for {validity}\n"
                              "And you will be disconnected once bundle finishes")
                        quit()
                    else:
                        print("Dear Customer, you do not have sufficient airtime to buy this bundle.\n"
                              "Please recharge and try again or Dial *500# to BORROW DATA and pay back Later.")
                        quit()
                else:
                    print("Invalid Entry")
            else:
                print("Too Many Attempts. Code Error")
                quit()

        check_Airtime()

    def daily_weekly():
        d_w = input("1. N50/40MB/DAILY\n"
                    "2. N100/100MB/DAILY\n"
                    "3. N200/200MB/3DAYS\n"
                    "4. N300/350MB/7DAYS\n"
                    "5. N500/750MB/14DAYS\n"
                    "6. N300/1GB/DAILY\n"
                    "7. N500/2GB/DAILY\n"
                    "8. N500/1GB/7DAYS\n"
                    "22.BACK\n"
                    "0. MENU\n: ")
        if d_w == '1':
            data_pack(50, "40MB", "1 DAY")
        elif d_w == '2':
            data_pack(100, "100MB", "1 DAY")
        elif d_w == '3':
            data_pack(200, "200MB", "3 DAYS")
        elif d_w == '4':
            data_pack(300, "350MB", "7 DAYS")
        elif d_w == '5':
            data_pack(500, "750MB", "14 DAYS")
        elif d_w == '6':
            data_pack(300, "1GB", "1 DAY")
        elif d_w == '7':
            data_pack(500, "2GB", "1 DAY")
        elif d_w == '8':
            data_pack(500, "1GB", "7 DAYS")
        elif d_w == '22':
            data_Menu()
        elif d_w == '0':
            selectTrans()
        else:
            daily_weekly()

    def weekly_bundle():
        week = input("Weekly Bundles\n"
                     "1 N500/750MB/14days\n"
                     "2 N500/1GB/7days\n"
                     "3 N1500/6GB/7days\n"
                     "4 N300/350MB/7days\n"
                     "5 N100/All Social/5days\n"
                     "22 Back\n: ")
        if week == '1':
            data_pack(500, "750MB", "14 Days")
        elif week == '2':
            data_pack(500, "1GB", "7 Days")
        elif week == '3':
            data_pack(1500, "6GB", "7 Days")
        elif week == '4':
            data_pack(300, "350MB", "7 Days")
        elif week == '5':
            data_pack(100, "All Social Bundle plan", "5 Days")
        elif week == '22':
            data_Menu()
        else:
            print("invalid entry")
            weekly_bundle()

    def monthly_bundle():
        month = input("Monthy Plans\n"
                      "1 N1000/1.5GB\n"
                      "2 N1200/2GB\n"
                      "3 N1500/3GB\n"
                      "4 N2000/4.5GB\n"
                      "5 N2500/6GB\n"
                      "6 N3000/10GB\n"
                      "7 N4000/11GB\n"
                      "8 N5000/20GB\n"
                      "22 Back\n"
                      "0 Menu\n: ")
        if month == "1":
            data_pack(1000, "1.5GB", "30 Days")
        elif month == "2":
            data_pack(1200, "2GB", "30 days")
        elif month == '3':
            data_pack(1500, "3GB", "30 Days")
        elif month == "4":
            data_pack(2000, "4.5GB", "30 days")
        elif month == '5':
            data_pack(2500, "6GB", "30 Days")
        elif month == "6":
            data_pack(3000, "10GB", "30 days")
        elif month == '7':
            data_pack(4000, "11GB", "30 Days")
        elif month == "8":
            data_pack(5000, "20GB", "30 days")
        elif month == '22':
            data_Menu()
        elif month == "0":
            selectTrans()
        else:
            print("invalid entry")
            monthly_bundle()

    def more_data():
        more = input("1 N500/2.5GB/2days\n"
                     "2 N1000/1.5GB/30days\n"
                     "3 N3000/11GB/30days\n"
                     "4 N4000/15GB/30days\n"
                     "5 N5000/22GB/30days\n"
                     "22 Back\n: ")
        if more == '1':
            data_pack(500, "2.5GB", "2 Days")
        elif more == '2':
            data_pack(1000, "1.5GB", "30 Days")
        elif more == '3':
            data_pack(3000, "11GB", "30 Days")
        elif more == '4':
            data_pack(4000, "15GB", "30 Days")
        elif more == '5':
            data_pack(5000, "22GB", "30 Days")
        elif more == '22':
            data_Menu()
        else:
            print("invalid entry")
            more_data()

    def mega_bundle():
        mega = input("1 N5,000 for 20GB\n"
                     "2 N8,000 for 30GB\n"
                     "3 N10,000 for 40GB\n"
                     "4 N15,000 for 75GB\n"
                     "5 N20,000 for 120GB\n"
                     "22 Back\n"
                     "0 Menu\n: ")
        if mega == "1":
            data_pack(5000, "20GB", "30 Days")
        elif mega == "2":
            data_pack(8000, "30GB", "30 days")
        elif mega == '3':
            data_pack(10000, "40GB", "30 Days")
        elif mega == "4":
            data_pack(15000, "75GB", "30 days")
        elif mega == '5':
            data_pack(20000, "120GB", "30 Days")
        elif mega == '22':
            data_Menu()
        elif mega == "0":
            selectTrans()
        else:
            print("invalid entry")
            mega_bundle()

    def big_data():
        big = input("1 N30,000 for 240GB\n"
                    "2 N36,000 for 280GB\n"
                    "3 N50,000 for 400GB\n"
                    "4 N60,000 for 500GB\n"
                    "5 N100,000 for 1TB\n"
                    "22 Back\n"
                    "0 Menu\n: ")
        if big == "1":
            data_pack(50000, "240GB", "30 Days")
        elif big == "2":
            data_pack(36000, "280GB", "30 days")
        elif big == '3':
            data_pack(50000, "400GB", "90 Days")
        elif big == "4":
            data_pack(60000, "500GB", "120 days")
        elif big == '5':
            data_pack(100000, "1TB", "365 Days")
        elif big == '22':
            data_Menu()
        elif big == "0":
            selectTrans()
        else:
            print("invalid entry")
            big_data()

    def everyday_on():
        every = input("1. N3000/15GB/30 days\n"
                      "2. N6000/45GB/30 days\n"
                      "3. N60/200MB/daily\n"
                      "4. N120/450MB/daily\n"
                      "22.BACK\n"
                      "0. MENU\n: ")
        if every == "1":
            data_pack_on(3000, "500MB everyday", "30 Days")
        elif every == "2":
            data_pack_on(6000, "1.5GB everyday", "30 days")
        elif every == '3':
            data_pack_on(60, "200MB(150MB Night ONLY)", "30 Days")
        elif every == "4":
            data_pack_on(120, "450MB (330MB Night ONLY)", "30 days")
        elif every == '22':
            data_Menu()
        elif every == "0":
            selectTrans()
        else:
            print("invalid entry")
            everyday_on()

    def rechargeFromBank():
        print("You currently do not have access to this service. Contact your bank")

    # Data Bundle Menu
    def data_Menu():
        start = input("1. Daily/Weekly Bundle\n"
                      "2. Weekly Bundles\n"
                      "3. Monthly Bundles\n"
                      "4. More Data (Data++)\n"
                      "5. Mega Bundles\n"
                      "6. Big Data Plans\n"
                      "*. Next\n: ")
        if start == '1':
            daily_weekly()
        elif start == '2':
            weekly_bundle()
        elif start == '3':
            monthly_bundle()
        elif start == '4':
            more_data()
        elif start == '5':
            mega_bundle()
        elif start == '6':
            big_data()
        elif start == '*':
            start = input("7. Everyday On Plan\n"
                          "8. Recharge From Bank\n"
                          "22. Back\n"
                          ": ")
            if start == '7':
                everyday_on()
            elif start == '8':
                rechargeFromBank()
            elif start == '22':
                data_Menu()
            else:
                print("Invalid Entry. FAILED")
                quit()
            data_Menu()

    data_Menu()


# CREATING A SEQUENCE OF RANDOM NUMBERS / WORDS AS DATABASE
import random

plans = ('SmartTrybe', 'smartOPTIMIZER', 'SmartCoonect', 'SmartTalk', 'SmartValue', 'SmartPremier')
num_list = ('0802', '0808', '0701', '0812', '0708', '0902', '0901', '0904', '0907', '0912')
airtel_start = random.choice(num_list)
begin = '234'


def random_end(n):
    rangestart = 10 ** (n - 1)
    rangeend = (10 ** n) - 1
    return random.randint(rangestart, rangeend)


airtel_end = str(random_end(7))

airtel_tariff = random.choice(plans)
phone_number = begin + airtel_start[1:] + airtel_end
alt_phone_number = airtel_start + airtel_end
puk_code = str(random_end(7))
serial_number = str(random_end(23))
data_balance = random_end(3)
airtime_balance = random.randint(0, 1000)


# print(alt_phone_number)

# ME2U
def meYou():
    you = input("Select:\n"
                "1. To Share Data\n"
                "2. To Share Credit\n")
    if you == "1":
        youOne()
    if you == "2":
        youTwo()
# NUMBER INPUT FOR ME2U DATA
def youOne():
        youone = input("Recipient's number\n")
        if len(youone) == 11:
            num = input("How Much data do you want to share?\n")
            print(f"You have Successfully shared {num}mb to {youone}")
        else:
            print("Invalid Number\n")
            youOne()

# NUMBER INPUT FOR ME2U CREDIT
def youTwo():
    youtwo = input("Recipient's number\n")
    if len(youtwo) == 11:
        num = input("How Much Credit do you wanna share?\n")
        print(f"You have Successfully shared N{num} to {youtwo}")
    else:
        print("Invalid Number\n")
        youTwo()



# BORROW ELIGIBILITY
def borrEli():
    eligibility = input("Reply with:\n"
                        "1. For Eligibility\n"
                        "2. For Help\n")
    if eligibility == "1":
        elione = input("You can borrow up to N45 on your Extra Credit Account\n"
                       "1. Go back\n")
        if elione == "1":
            borrEli()
    if eligibility == "2":
        elitwo = input("Help: Remember to pay back your loans within 72 hours\n"
                       "1. Go back\n")
        if elitwo == "1":
            borrEli()


def borrowCred():
    borrow = input("0. Borrow Talk Time/Voice Bundle\n"
                   "1. Eligibity and Help\n"
                   "2. Borrow Credit\n"
                   "3. Borrow Data\n"
                   "4. Repay Loan\n"
                   "Reply with your choice\n")
    if borrow == "0":
        talk = input("You can borrow up to N300(No fee Applies\n"
                     "Select:\n"
                     "3. For N300\n"
                     "4. For N200\n"
                     "5. For N100\n"
                     "6. For N50\n"
                     "7. For N25\n"
                     "9. Go back\n")
        if talk == "3":
            three = input("You have been successfully credited with N300\n"
                          "9. To go back\n")
            if three == "9":
                print("You need to clear up your previous loan in order tp continue\n")
        if talk == "4":
            four = input("You have been successfully credited with N200\n"
                         "9. To go back\n")
            if four == "9":
                print("You need to clear up your previous loan in order to continue\n")
        if talk == "5":
            five = input("You have been successfully credited with N100\n"
                         "9. To go back\n")
            if five == "9":
                print("You need to clear up your previous loan in order to continue\n")
        if talk == "6":
            six = input("You have been successfully credited with N50\n"
                        "9. To go back\n")
            if six == "9":
                print("You need to clear up your previous loan to continue")
        if talk == "7":
            seven = input("You have been successfully credited with N25\n"
                          "9. To go back\n")
            if seven == "9":
                print("You need to clear up your previous loan to continue\n")
        if talk == "9":
            borrowCred()

    if borrow == "1":
        borrEli()

    if borrow == "2":
        serviceborrow = input("You can borrow up to N30(15% Service fee applies\n"
                              "Select:\n"
                              "16. For N30\n"
                              "17. For N25\n")
        if serviceborrow == "16":
            sixteen = input("You have been credited with N30\n"
                            "1. Go back\n")
            if sixteen == "1":
                print("You need to clear your previous loan to continue\n")
        if serviceborrow == "17":
            seventeen = input("You have been credited with N25\n"
                              "1. Go back\n")
            if seventeen == "1":
                print("You need to clear your previous loan to continue\n")
    if borrow == "3":
        print("Kindly Clear Up your existing loan to enable you get another loan on the network\n")

    if borrow == "4":
        repay = input("You have a pending loan balance of N300 and can pay back up to 500\n"
                      "Enter the amount you want to pay back\n")
        if int(repay) < 300:
            print("You still have to settle the loan within 72 hours")
        else:
            print("You have Successfully payed your loan\n")


# Airtel Social Media Handles
def socMed():
    social = input("1. Twitter\n"
                   "2. Email us\n"
                   "3. Facebook\n"
                   "4. Download Airtel Care App\n"
                   "# Previous Menu\n")
    if social == "1":  # Twitter
        print("Airtel Twitter handle is @airtel_care and we are available 24/7 for support\n")
        twitter = input("# Previous Menu\n")
        if twitter == "#":
            socMed()

    if social == "2":  # Email
        print("Send an email to Airtel at customercare@ng.airtel.com\n")
        mail = input("# Previous Menu\n")
        if mail == "#":
            socMed()

    if social == "3":  # Facebook
        print("Follow the Airtel Facebook page www.facebook.com/AirtelNigeria\n")
        mail = input("# Previous Menu\n")
        if mail == "#":
            socMed()

    if social == "4":  # airtel Care App
        print("Our Mobile App (Airtel Care) is available on Google play store and Apple App Store\n"
              "Download it for free. (data charges apply)")
        mail = input("# Previous Menu\n")
        if mail == "#":
            socMed()

    if social == '#':
        selectTrans()


# Billing & Tariff
def billTar():
    trans = input(
        "1. Smart Connect.\n"
        "2. Smart Trybe @11k(After 50 sec)\n"
        "3. Freedom Plan @12k flat rate\n"
        "4. Smart Talk @11k (N7 Access fee)\n"
        "5. Smart Value\n"
        "*. Next\n"
    )

    if trans == "1":  # Smartconnect
        print("Dial *311*2*Phone Number# to add FAF or *311*3*Phone Number# to remove FAF")
        x = input("# Previous Menu\n")
        while x != '#':
            print("Dial *311*2*Phone Number# to add FAF or *311*3*Phone Number# to remove FAF")
            x = input("# Previous Menu\n")
            if x == '#':
                billTar()

    elif trans == "2":  # SmartTrybe
        opt = input("Smart Trybe: 11k/s. 5. 1GB/N500 for 7 days\n"
                    "Press 1 to activate or dial *318#\n")
        if opt == "1":
            print(
                "You are now on Airtel smartTRYBE. Make call to ALL NETWORKS in Nigeria at 11k/sec all day; after 1st 50secs at 25k/sec. Enjoy special data")
        law = input("* next\n")
        if law == "*":
            print("plan of N25 for 250MB (1 night) and N500 for 1GB (7 days). Dial *312# to purchase data plan\n"
                  "Session has ended")
            quit()

    elif trans == "3":  # Freedom Plan
        free = input("Freedom Plan: Flat rate 12k/sec from the 1st sec. N4/SMS\n"
                     "Press 1 to activate or dial *152#\n")
        if free == "1":
            bACK = input("You can only migrate multiple times within 30 days if you have a balance of N100\n"
                         "#. For Previous menu\n")
            if bACK == '#':
                billTar()
            else:
                print('Session Has Ended')
                quit()

    elif trans == "4":  # sMART tALK
        smart = input("Smart Talk: All Networks @11k/s 24/7 Access fee N7\n"
                      "Press 1 to activate or dial *318#\n")
        if smart == "1":
            if airtime_balance < 100:
                print("You can only migrate multiple times within 30 days if you have a balance of N100")
            else:
                print('You  have successfully subscribed to Airtel Smart Talk. Congratulations')

    elif trans == "5":  # sMART vALUE
        value = input("Smart Value: All Networks @15/s 24/7. No Access fee\n"
                      "Press 1 to activate or dial *314#\n")
        if value == "1":
            print("You can only migrate multiple times within 30 days if you have a balance of N100")

    elif trans == "*":
        ast = input("15K flat rate\n"
                    "# Previous Menu\n")
        if ast == "#":
            selectTrans()


# Borrow
def borrCred():
    trans = input(
        "1. Borrow Credit(Welcome to Extra Credit)\n"
        "2. Me2u\n"
        "3. Do not Disturb\n"
        "4. VAS\n"
        "5. Loyalty\n"
        "6. Log a Complaint\n"
        "7. Store Locator\n"
        "# Previous Menu\n"
    )

    if trans == "1":
        print("Dial *500# to borrow Airtime/Data\n"
              "You'll be directed to the borrow credit menu\n")
        borrowCred()

    elif trans == "2":
        print("You will be redirected to the Me2U menu")
        meYou()

    elif trans == "3":  # Do not disturb
        print("SMS STOP to 2442 for full DND\n"
              "SMS HELP to 2442 for partial DND")
        y = input("# Previous Menu\n")
        while y != '#':
            print("SMS STOP to 2442 for full DND\n"
                  "SMS HELP to 2442 for partial DND")
            y = input("# Previous Menu\n")
            if y == '#':
                borrCred()

    elif trans == "4":  # VAS
        print("You will be redirected to the VAS Services menu")

    elif trans == "5":
        print("You will be redirected to the Loyalty Scheme menu")

    elif trans == "6":
        print("Kindly visit this link https://selfcare.ng.airtel.com/LogRequest")

    elif trans == "7":
        print("Kindly visit this link http://www.alwayson.ng/Storelocator")

    else:
        borrCred()


# Manage my account
def manageAcc():
    trans = input(
        "1. My Data Balance\n"
        "2. My Balance\n"
        "3. My Data Plan\n"
        "4. My Number\n"
        "5. My Tariff Plan\n"
        "6. KYC Status\n"
        "7. My PUK\n"
        "8. My Serial Number\n"
        "# Previous menu\n"
    )

    if trans == "1":
        print(f"Dear Customer, your data balance is {data_balance}MB till 20/01/2023.\n")
    elif trans == "2":
        print(f"Your account balance is N{airtime_balance}.")
    elif trans == "3":
        print("You're subscribed to Airtel 2gb Monthly plan, valid for 30 days.")
    elif trans == "4":
        print(f"Your number is {phone_number}.")
    elif trans == "5":
        print(f"Your Tariff plan is {airtel_tariff}.")
    elif trans == "6":
        print("Service Temporarily unavailable.")
    elif trans == "7":
        print(f"Your PUK: {puk_code}.")
    elif trans == "8":
        print(f"Sim serial for the requesting number {alt_phone_number} is {serial_number}.")
    elif trans == '#':
        selectTrans()
    else:
        print('Invalid Code Entered\n"'
              '"start again')
        manageAcc()


# Transaction
def data_Menu():
    pass


def selectTrans():
    trans = input(
        "1. NIN Capture\n"
        "2. Buy bundles & Services\n"
        "3. Manage my Account\n"
        "4. Borrow Credit & other self services\n"
        "5. Billing and Tariff\n"
        "6. Bank Codes\n"
        "7. KYC Update\n"
        "* Next\n: "
    )

    if trans == "1":
        print("Kindly dial *121*1# to submit your Government approved NIN")

        def ninCreat():
            nin = input("Input your National Identification Number (NIN)\n")
            if len(nin) == 11:
                print("Your NIN has been submitted\n"
                      "Thank You!")

            else:
                print("Invalid NIN entry")
                ninCreat()

        ninCreat()

    elif trans == "2":
        print("You'll now be tranferred to the Data Bundles Menu\n")
        DataBundles()


    elif trans == "3":
        manageAcc()

    elif trans == "4":
        borrCred()

    elif trans == "5":
        billTar()

    elif trans == "6":
        print("Service Temporarily Unavailable")

    elif trans == "7":
        print("Service Temporarily Unavailable")

    elif trans == "*":
        contact = input("8. Contact us\n")
        if contact == "8":
            socMed()

    else:
        print('Invalid Entry')
        # selectTrans()
        x = input("Press 1 to try again\n"
                  "Press 2 to Quit\n"
                  )
        if x == '1':
            selectTrans()
        if x == '2':
            print('Seesion Ended')
            quit()


# DIALPAD
def confirmUSSD():
    ussd = input("Enter Code: ")
    if ussd == "*121#":
        print("Enter Transaction")
        selectTrans()

    else:
        print("Connection problem or invalid MMI.")
        confirmUSSD()


confirmUSSD()
