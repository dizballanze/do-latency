# -*- coding: utf-8 -*-

import argparse

from tqdm import tqdm
from terminaltables import AsciiTable
import six

from .ping import do_ping
from .download import do_download


REGIONS = {
    'nyc1': 'speedtest-nyc1.digitalocean.com',
    'nyc2': 'speedtest-nyc2.digitalocean.com',
    'nyc3': 'speedtest-nyc3.digitalocean.com',
    'tor1': 'speedtest-tor1.digitalocean.com',
    'ams2': 'speedtest-ams2.digitalocean.com',
    'ams3': 'speedtest-ams3.digitalocean.com',
    'sfo1': 'speedtest-sfo1.digitalocean.com',
    'sgp1': 'speedtest-sgp1.digitalocean.com',
    'lon1': 'speedtest-lon1.digitalocean.com',
    'fra1': 'speedtest-fra1.digitalocean.com',
    'blr1': 'speedtest-blr1.digitalocean.com'
}
BAR_FORMAT = "{desc}|{bar}|{percentage:3.2f}%"
PADDING_FORMAT = "{:>30}"


def start_test(ping_count=10, file_size="10mb", udp=False):
    results = {key: [] for key in REGIONS}
    # Latency testing
    pbar = tqdm(total=(len(REGIONS) * ping_count), desc=PADDING_FORMAT.format("Latency testing"), bar_format=BAR_FORMAT, leave=True)
    for region, host in six.iteritems(REGIONS):
        pbar.set_description(PADDING_FORMAT.format("Latency testing ({})".format(region)))
        results[region].append(do_ping(host, count=ping_count, udp=udp, hook=lambda: pbar.update(1)))
    pbar.close()
    # Download speed testing
    pbar = tqdm(total=(len(REGIONS) * 100), desc=PADDING_FORMAT.format("Download speed testing"), bar_format=BAR_FORMAT, leave=True, disable=False)
    for region, host in six.iteritems(REGIONS):
        pbar.set_description(PADDING_FORMAT.format("Download speed testing ({})".format(region)))
        url = "http://{}/{}.test".format(host, file_size)
        results[region].append(do_download(url, lambda progress: pbar.update(progress)))
    # Output sorted by latency results as table
    table_data = [[key] + value for key, value in six.iteritems(results)]
    table_data.sort(key=lambda row: float(row[1]))
    table_data.insert(0, ["Region", "Latency (ms)", "Download speed (mbps)"])
    table = AsciiTable(table_data)
    print("\n\n{}\n".format( table.table))


def main():
    parser = argparse.ArgumentParser(description="Digital Ocean regions latency checking tool.")
    parser.add_argument("--ping-count", help='Count of ICMP requests for latency check (default: %(default)s)', type=int, default=10)
    parser.add_argument("--file-size", help='File size for download speed test (default: %(default)s)', type=str, default="10mb", choices=("10mb", "100mb"))
    parser.add_argument('--udp', dest='udp', action='store_true', help="Use UDP not ICMP") 
    args = parser.parse_args()
    start_test(**args.__dict__)


if __name__ == "__main__":
    main()
