import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import number_type, PhoneNumberType
from geopy.geocoders import Nominatim
from colorama import init, Fore, Back, Style
import pyfiglet

init(autoreset=True)
def check_phone_number(country_code, phone_number):
    country_codes = {
        "ID": "Indonesia",
        "RU": "Russia Federation",
        "UK": "United Kingdom"
    }
    if country_code not in country_codes:
        print("Invalid country code. Use ID, RU, or EN.")
        return
    try:
        full_number = f"+{phonenumbers.country_code_for_region(country_code)}{phone_number}"
        parsed_number = phonenumbers.parse(full_number, None)
        location = geocoder.description_for_number(parsed_number, "id")
        geolocator = Nominatim(user_agent="phone_number_checker")
        location_info = geolocator.geocode(location)
        coordinates = f"{location_info.latitude}, {location_info.longitude}" if location_info else "Not available"
        service_provider = carrier.name_for_number(parsed_number, "id")
        time_zone = timezone.time_zones_for_number(parsed_number)
        number_type_result = number_type(parsed_number)
        status = "Active" if number_type_result == PhoneNumberType.MOBILE else "Inactive/Invalid"
        
        print(f"\n{Fore.BLUE + Style.BRIGHT}{'=' * 50}")
        print(f"{Fore.LIGHTBLUE_EX}[+] Phone Number Information")
        print(f"{Fore.BLUE + Style.BRIGHT}{'=' * 50}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Country:{Fore.BLUE} {country_codes[country_code]}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Number:{Fore.BLUE} {full_number}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Location:{Fore.BLUE} {location}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Coordinates:{Fore.BLUE} {coordinates}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Service Provider:{Fore.BLUE} {service_provider}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Time Zone:{Fore.BLUE} {', '.join(time_zone)}")
        print(f"{Fore.LIGHTBLUE_EX}[*] Status:{Fore.BLUE} {status}")
        print(f"{Fore.BLUE + Style.BRIGHT}{'=' * 50}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"\n{Fore.BLUE + Style.BRIGHT}[!] Invalid phone number format.")
    except AttributeError:
        print(f"\n{Fore.BLUE + Style.BRIGHT}[!] Unable to find coordinates for this location.")
if __name__ == "__main__":
    banner = pyfiglet.figlet_format("Phone Tracker", font="slant")
    print(f"{Fore.BLUE + Style.BRIGHT}{banner}")
    print(f"{Fore.LIGHTBLUE_EX}[*] Developed by yadi-dev")
    print(f"{Fore.BLUE + Style.BRIGHT}{'=' * 50}")
    country_code = input(f"{Fore.LIGHTBLUE_EX}[+] Enter country code (ID, RU, or UK): {Fore.BLUE}").upper()
    phone_number = input(f"{Fore.LIGHTBLUE_EX}[+] Enter phone number (without country code): {Fore.BLUE}")
    check_phone_number(country_code, phone_number)
