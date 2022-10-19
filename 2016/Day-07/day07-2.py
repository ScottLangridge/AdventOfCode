import re


def main(raw_input):
    ips = raw_input.strip('\n').splitlines()
    tls_ips = [ip for ip in ips if supports_ssl(ip)]
    return len(tls_ips)


def supports_ssl(ip):
    ips, hypers = split_ip(ip)
    abas = []
    for ip in ips:
        abas.extend(find_abas(ip))
    for aba in abas:
        for hyper in hypers:
            if aba[1] + aba[0] + aba[1] in hyper:
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


def find_abas(string):
    abas = []
    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i] != string[i + 1]:
            abas.append((string[i], string[i + 1]))
    return abas


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
