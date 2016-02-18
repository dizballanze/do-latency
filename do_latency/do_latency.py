# -*- coding: utf-8 -*-

import argparse

from tqdm import tqdm
from terminaltables import AsciiTable

from ping import do_ping


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
}
TESTS_COUNT = 10
BAR_FORMAT = "{desc}|{bar}|{percentage:3.0f}%"


def start_test(ping_count=TESTS_COUNT):
    results = {key: [] for key in REGIONS}
    pbar = tqdm(total=(len(REGIONS) * ping_count), desc="Latency testing", bar_format=BAR_FORMAT, leave=True)
    for region, host in REGIONS.iteritems():
        pbar.set_description("Latency testing ({})".format(region))
        results[region].append(do_ping(host, count=ping_count, udp=True, hook=lambda: pbar.update(1)))
    pbar.close()
    table_data = [[key] + value for key, value in results.iteritems()]
    table_data.sort(key=lambda row: float(row[1]))
    table_data.insert(0, ["Region", "Latency (ms)"])
    table = AsciiTable(table_data)
    print("\n{}\n".format( table.table))


def main():
    parser = argparse.ArgumentParser(description="Digital Ocean regions latency checking tool.")
    parser.add_argument("--ping-count", help='Count of ICMP requests for latency check', type=int, default=TESTS_COUNT)
    args = parser.parse_args()
    start_test(**args.__dict__)


if __name__ == "__main__":
    main()
