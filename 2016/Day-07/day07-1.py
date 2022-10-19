import re


def main(raw_input):
    ips = raw_input.strip('\n').splitlines()
    tls_ips = [ip for ip in ips if supports_tls(ip)]
    return len(tls_ips)


def supports_tls(ip):
    ips, hypers = split_ip(ip)
    for hyper in hypers:
        if contains_abba(hyper):
            return False
    for ip in ips:
        if contains_abba(ip):
            return True
    return False


def split_ip(ip):
    ip += '['
    hyper_ips = ip.split("]")
    ips, hypers = [], []
    for hyper_ip in hyper_ips:
        ip, hyper = hyper_ip.split('[')
        ips.append(ip)
        hypers.append(hyper)
    return ips, hypers


def contains_abba(string):
    for i in range(len(string) - 3):
        if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
            return True
    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
