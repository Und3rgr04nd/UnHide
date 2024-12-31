import requests
import argparse
import json
from colorama import Fore

# Define colors for output
found = Fore.GREEN
error = Fore.RED

banner = r"""
   __  __      __  ___     __   
  / / / /___  / / / (_)___/ /__ 
 / / / / __ \/ /_/ / / __  / _ \
/ /_/ / / / / __  / / /_/ /  __/
\____/_/ /_/_/ /_/_/\__,_/\___/                                 
"""
def fetch_cert(domain, output_file=None):
    url = f"https://crt.sh/json?q={domain}"

    try:
        # Send the request to fetch certificate data
        res = requests.get(url)
        res.raise_for_status()  # Raise an error for bad HTTP responses

        # Parse JSON response
        certificates = res.json()

        # Display each certificate found
        results = []
        for cert in certificates:
            cert_details = {
                "ICA": cert.get('issuer_ca_id'),
                "Issuer Name": cert.get('issuer_name'),
                "Common Name": cert.get('common_name'),
                "Name Value": cert.get('name_value'),
                "ID": cert.get('id'),
                "ET": cert.get('entry_timestamp'),
                "NB": cert.get('not_before'),
                "NA": cert.get('not_after'),
                "SN": cert.get('serial_number')
            }
            results.append(cert_details)
            print(
                f"[{found}FOUND{Fore.RESET}] "
                f"ICA: {cert_details['ICA']} | "
                f"Issuer Name: {cert_details['Issuer Name']} | "
                f"Common Name: {cert_details['Common Name']} | "
                f"Name Value: {cert_details['Name Value']} | "
                f"ID: {cert_details['ID']} | "
                f"ET: {cert_details['ET']} | "
                f"NB: {cert_details['NB']} | "
                f"NA: {cert_details['NA']} | "
                f"SN: {cert_details['SN']}\n"
            )

        # Save the results if save_output is True
        if output_file:
            with open(output_file, "w") as file:
                json.dump(results, file, indent=4)
            print(f"\n[{found}SAVED{Fore.RESET}] Output saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"[{error}ERROR{Fore.RESET}] {e}")
    except json.JSONDecodeError:
        print(f"[{error}ERROR{Fore.RESET}] Failed to decode JSON response.")

def main():
    # Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Fetch certificates from crt.sh")
    parser.add_argument("-d", "--domain", type=str, help="The domain to query (e.g., example.com)")
    parser.add_argument(
        "-s", "--save", type=str, metavar="OUTPUT_FILE",
        help="Save the output to a specified file (optional)"
    )

    args = parser.parse_args()

    fetch_cert(args.domain, args.save)

if __name__ == "__main__":
	print(f"{Fore.MAGENTA}{banner}{Fore.RESET}\nSubdomain Finder Using crt.sh\nCreated by Und3rgr04nd\nGitHub https://github.com/und3rgr04nd\n")
	main()
