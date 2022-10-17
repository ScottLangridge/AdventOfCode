import re
from collections import defaultdict


class RuleSet:
    # self.rules records can take following forms:
    # {rule_id: [['string_val']]}                       - Leaf rule, defines single value.
    # {rule_id: [[rule, rule]]}                         - Pair of child rules.
    # {rule_id: [[rule, rule], [alt_rule, alt_rule]]}   - Pair of child rules or different pair of child rules.

    def __init__(self, rule_dict):
        self.rules = rule_dict
        self.regex_rules = {}

    def get_regex_rule(self, rule_id):
        if rule_id not in self.regex_rules.keys():
            self.generate_regex_rule(rule_id)
        return self.regex_rules[rule_id]

    def generate_regex_rule(self, rule_id):
        rule = self.rules[rule_id]
        regex_pattern = ''

        # If is leaf rule
        if isinstance(rule[0][0], str):
            regex_pattern = rule[0][0]
        else:
            for possible_rule_set in rule:
                for child_rule in possible_rule_set:
                    regex_pattern = regex_pattern + self.get_regex_rule(child_rule)
                regex_pattern = regex_pattern + '|'
            regex_pattern = f'({regex_pattern[:-1]})'

        self.regex_rules[rule_id] = regex_pattern
        return


def main(raw_input):
    rule_dict, messages = parse_input(raw_input)
    rules = RuleSet(rule_dict)
    regex = re.compile(fr'\b{rules.get_regex_rule(0)}\b')

    match_count = 0
    for message in messages:
        if regex.match(message):
            match_count += 1

    return match_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    rules, messages = raw_input.split('\n\n')

    rule_dict = {}
    for rule in rules.splitlines():
        rule_id, rule_val = rule.split(': ')
        sub_rules = []
        for sub_rule in rule_val.split(' | '):
            if sub_rule[0] == '"':
                sub_rules.append([sub_rule.strip('"')])
            else:
                sub_rules.append([int(rule) for rule in sub_rule.split(' ')])

        rule_dict[int(rule_id)] = sub_rules

    messages = messages.splitlines()

    return rule_dict, messages


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
