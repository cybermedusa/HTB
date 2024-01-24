import requests

def check_status(subdomain):
    try:
        response = requests.get(f"SCHEMA://{subdomain}.DOMAIN.TLD", timeout=5)
        if response.status_code == 200:
            return subdomain
    except requests.RequestException:
        pass
    return None

def main():
    subdomains_file = "subdomains.txt"
    valid_subdomains = []

    with open(subdomains_file, 'r') as file:
        for line in file:
            subdomain = line.strip()
            if valid_subdomain := check_status(subdomain):
                valid_subdomains.append(valid_subdomain)

    print("Subdomains with 200 status code:")
    for subdomain in valid_subdomains:
        print(subdomain)

if __name__ == "__main__":
    main()
