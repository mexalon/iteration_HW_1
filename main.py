import os
from stuff.config import *
import json

sf = source_file_path
tf = target_file_path
wiki_url = target_url


class Countries:
    def __init__(self, from_file: str, to_file: str, to_url, start=None, stop=None):
        self.from_file = from_file
        self.to_file = to_file
        self.idx = -1
        if start:
            self.idx = start

        self.stop = stop
        self.to_url = to_url
        self.one_land = None

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        self.read_country()
        if self.stop:
            if self.idx >= self.stop:
                raise StopIteration

        return self.idx

    def __str__(self):
        return f'{self.one_land}'

    def read_country(self, my_idx=None):
        idx = self.idx
        if my_idx:
            idx = my_idx

        with open(self.from_file, 'r', encoding='UTF-8') as s:
            try:
                self.one_land = json.load(s)[idx]['name']['official']
            except IndexError:
                self.stop = idx

        return self.one_land

    def write_country(self, my_idx=None):
        idx = self.idx
        if my_idx:
            idx = my_idx

        if self.one_land:
            with open(self.to_file, 'a', encoding='UTF-8') as t:
                url = f"[{self.one_land}]({self.to_url + self.one_land.strip().replace(' ', '_')})"
                t.write(f"{idx + 1}. {url}\n")


def del_file(file_name: str):
    """удаляет файл лога"""
    if file_name in os.listdir():
        path = os.path.join(file_name)
        os.remove(path)


if __name__ == '__main__':
    del_file(tf)
    ctf = Countries(sf, tf, wiki_url)
    for country in ctf:
        print(ctf)
        ctf.write_country()
