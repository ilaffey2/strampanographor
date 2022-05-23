from executionhash import generate_execution_hash
import hashlib



def main():
    hash = hashlib.sha256()
    hash.update(generate_execution_hash().encode("UTF-8"))
    print(hash.digest())
    print(hash.digest())




if '__name__ == __main__':
    main()