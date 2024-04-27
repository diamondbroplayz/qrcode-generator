import qrcode
import validators

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

print(f"- {bcolors.OKGREEN}[1] URL")
print(f"{bcolors.ENDC}- {bcolors.OKGREEN}[2] Data (Text){bcolors.ENDC}")
option = input(f"{bcolors.OKGREEN}Which do you choose?{bcolors.ENDC} {bcolors.BOLD}")

if option == "1":
    while True:
        data = input(f"{bcolors.ENDC}- {bcolors.OKGREEN}What URL would you like to use?{bcolors.ENDC} {bcolors.BOLD}")
        if validators.url(data) == True:
            break
        else:
            print(f"{bcolors.ENDC}- {bcolors.OKGREEN}Invalid URL{bcolors.ENDC}\n")
elif option == "2":
    data = input(f"{bcolors.ENDC}- {bcolors.OKGREEN}What data would you like to use?{bcolors.ENDC} {bcolors.BOLD}")
    if data.startswith("https://"):
        print(f"{bcolors.ENDC}- {bcolors.OKGREEN}Program will continue, however if you are using a URL, you can just select option 1{bcolors.ENDC}\n")


qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="#01A368", back_color="#202020")
img.save("some_file.png")