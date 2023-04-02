import requests
import hashlib
import sys


def request_api_data(query_char):
    """ Requests query_chara through API"""
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, check the API and try again')
    return res


def get_password_leaks(hashes, hash_to_check):
    """Counts how many matches with the received passwords"""
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """Hashes the password and splits into head and tail"""
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1[:5], sha1[5:]  # Sha1 Hash is 40 chars long, hence the tail is 35 chars.
    response = request_api_data(first5_char)
    return get_password_leaks(response, tail)  # Finds password leak matches


def main(args):
    # Sends passwords from the console one by one to API function
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.. You should probably change your password')
        else:
            print(f'{password} was not found... Carry on')
    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
