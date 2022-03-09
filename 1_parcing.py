import csv
import time


def main():

    start = time.time()
    hash_dict = {}
    source_file = input('Input full path to source csv-file: ')
    out_file = input('Input full path to out csv-file: ')

    with open(r'{0}'.format(source_file)) as file_in:
        reader = csv.reader(file_in)
        with open(r'{0}'.format(out_file), 'w', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                object_hash = hash(tuple(row[7:14]))
                hash_dict[object_hash] = hash_dict.get(object_hash, 0) + 1
                if hash_dict[object_hash] == 2:
                    writer.writerow(row[7:14])

    print(f'Script ended in {round(time.time() - start, 4)} sec')


if __name__ == '__main__':
    main()
