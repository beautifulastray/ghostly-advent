import hashlib

def main():
    INPUT = 'yzbqklnj'
    key = INPUT
    i = 0

    while True:
        i +=1
        step = str(i)
        new_key = key + step
        new_key = new_key.encode('utf-8')
        hash_object = hashlib.md5(new_key)
        hash = hash_object.hexdigest()
        s = hash[0:6]
        if s == '000000':
            print('Great Job! We mined some AdventCoins.')
            print(i)
            break

if __name__ == "__main__":
    main()
