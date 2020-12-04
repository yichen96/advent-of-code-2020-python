from dataclasses import dataclass
import re

def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split("\n\n")

@dataclass
class Passport:
    byr: str = ""
    iyr: str = ""
    eyr: str = ""
    hgt: str = ""
    hcl: str = ""
    ecl: str = "" 
    pid: str = ""
    cid: str = ""

    def is_byr_valid(self):
        return len(self.byr) == 4 and (1920 <= int(self.byr)<= 2002)
    def is_iyr_valid(self):
        return len(self.iyr) == 4 and (2010 <= int(self.iyr)<= 2020)
    def is_eyr_valid(self):
        return len(self.eyr) == 4 and (2020 <= int(self.eyr)<= 2030)
    def is_hgt_valid(self):
        if self.hgt[-2:] == "cm":
            return 150 <= int(self.hgt[0:-2]) <= 193
        elif self.hgt[-2:] == "in":
            return 59 <= int(self.hgt[0:-2]) <= 76
        else:
            return False
    def is_hcl_valid(self):
        pattern = re.compile("^#(?:[0-9a-f]{6})$")
        return pattern.match(self.hcl) is not None
    def is_ecl_valid(self):
        valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        return self.ecl in valid_colors and len(self.ecl) == 3
    def is_pid_valid(self):
        pattern = re.compile("^(?:[0-9]{9})$")
        return pattern.match(self.pid) is not None

    def is_valid(self):
        return (self.is_byr_valid() and 
                self.is_ecl_valid() and 
                self.is_iyr_valid() and 
                self.is_pid_valid() and 
                self.is_hcl_valid() and 
                self.is_eyr_valid() and 
                self.is_hgt_valid())

def count_valid_passport(passports: list) -> int:
    count = 0

    required_fields = {"byr" ,"iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl","pid"}
    allowed_fields = required_fields | {'cid'}

    for passport in passports:
        info = re.split(' |\n', passport)
        passport_dict = {re.split(':', i)[0]: re.split(':', i)[1] for i in info}
        # dict.keys() returns a set, 
        # the < and > comparison on set is checking the sub set or super set
        if required_fields <= passport_dict.keys() <= allowed_fields:
            count += 1
    return count

def count_valid_passport_class(passports: list) -> int:
    count = 0
    for passport in passports:
        info = re.split(' |\n', passport)
        passport_dict = {re.split(':', i)[0]: re.split(':', i)[1] for i in info}
        passport_class = Passport(**passport_dict)
        if passport_class.is_valid():
            count += 1
    return count

if __name__ == "__main__":
    input_passports = read_input("input.txt")
    print(count_valid_passport_class(input_passports))