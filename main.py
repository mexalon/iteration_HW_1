import os
import hashlib
from stuff.config import *
import json

sf = source_file_path
tf = target_file_path
hf = hash_file_path
wiki_url = target_url


class Countries:
    def __init__(self, from_file: str):
        self.from_file = from_file
        self.idx = -1
        self.stop = False
        self.to_url = None
        self.to_file = None
        self.one_land = None

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        self.read_country()
        if self.stop:
            self.idx = -1
            self.stop = False
            raise StopIteration

        return self.idx

    def __str__(self):
        return f'{self.idx + 1}: {self.one_land}'

    def read_country(self):
        with open(self.from_file, 'r', encoding='UTF-8') as s:
            try:
                self.one_land = json.load(s)[self.idx]['name']['official']
            except IndexError:
                self.stop = True

        return self.one_land

    def write_country(self, to_file: str, to_url):
        if self.one_land:
            with open(to_file, 'a', encoding='UTF-8') as t:
                url = f"[{self.one_land}]({to_url + self.one_land.strip().replace(' ', '_')})"
                t.write(f"{self.idx + 1}. {url}\n")


def del_file(file_name: str):
    """удаляет файл лога"""
    if file_name in os.listdir():
        path = os.path.join(file_name)
        os.remove(path)


def hw_1(source_filename: str, target_filename: str, url):
    """Первое задание"""
    del_file(target_filename)
    ctf = Countries(source_filename)
    for country in ctf:
        print(ctf)
        ctf.write_country(target_filename, url)


def my_generator(some_file: str):
    """Генератор хэшей"""
    with open(some_file, 'rb') as f:
        line = f.readline()
        while line:
            one_hash = hashlib.md5(line).hexdigest()
            yield one_hash
            line = f.readline()


def hw_2(source_filename: str, target_filename: str):
    """Второе задание"""
    del_file(target_filename)
    for item in my_generator(source_filename):
        print(item)
        with open(target_filename, 'a') as h:
            h.write(f'{item}\n')


if __name__ == '__main__':
    hw_1(sf, tf, wiki_url)
    hw_2(tf, hf)
