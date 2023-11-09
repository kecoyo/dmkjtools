import unittest

from common.fs import *


class TestFs(unittest.TestCase):
    def test_create_dir(self):
        dir = "d:/output/test/test_create_dir"
        create_dir(dir)
        self.assertTrue(exists_dir(dir))

    def test_remove_dir(self):
        dir = "d:/output/test/test_remove_dir"
        create_dir(dir)
        remove_dir(dir)
        self.assertFalse(exists_dir(dir))

    def test_move_dir(self):
        src = "d:/output/test/test_move_dir"
        create_dir(src)
        dest = "d:/output/test/test_move_dir2"
        remove_dir(dest)
        move_dir(src, dest)
        self.assertTrue(not exists_dir(src) and exists_dir(dest))

    def test_copy_dir(self):
        src = "d:/output/test/test_copy_dir"
        create_dir(src)
        dest = "d:/output/test/test_copy_dir2"
        copy_dir(src, dest)
        self.assertTrue(exists_dir(src) and exists_dir(dest))

    def test_remove_file(self):
        file = "d:/output/test/test_remove_file.txt"
        content = "hello, yangkk!"
        write_text(file, content)

        remove_file(file)
        self.assertFalse(exists_file(file))

    def test_move_file(self):
        file = "d:/output/test/test_move_file.txt"
        content = "hello, yangkk!"
        write_text(file, content)

        src = "d:/output/test/test_move_file.txt"
        dest = "d:/output/test/test_move_file2.txt"
        move_file(src, dest)
        self.assertTrue(not exists_file(src) and exists_file(dest))

    def test_copy_file(self):
        file = "d:/output/test/test_copy_file.txt"
        content = "hello, yangkk!"
        write_text(file, content)

        src = "d:/output/test/test_copy_file.txt"
        dest = "d:/output/test/test_copy_file2.txt"
        copy_file(src, dest)
        self.assertTrue(exists_file(dest))

    def test_get_file_size(self):
        file = "d:/output/test/test_get_file_size.txt"
        content = "1"
        write_text(file, content)

        size = get_file_size(file)
        print(size)
        self.assertTrue(size == 1)

    def test_get_file_stat(self):
        file = "d:/output/test/test_get_file_stat.txt"
        content = "1"
        write_text(file, content)

        stat = get_file_stat(file)
        print(stat)
        self.assertTrue(stat.st_size == 1)

    def test_readdir(self):
        dir = "d:/output/test/"
        files = readdir(dir)
        print(files)
        self.assertTrue(len(files) > 0)

    def test_readdirp(self):
        dir = "d:/output/test/"
        files = readdirp(dir, "*")
        for file in files:
            print(file)
        self.assertTrue(len(files) > 0)

    def test_read_text(self):
        file = "d:/output/test/test_read_text.txt"
        content = "hello, yangkk!"
        write_text(file, content)

        text = read_text(file)
        self.assertTrue(content == text)

    def test_write_text(self):
        file = "d:/output/test/test_write_text.txt"
        content = "hello, yangkk!"
        write_text(file, content)
        self.assertTrue(read_text(file) == content)

    def test_read_json(self):
        file = "d:/output/test/test_read_json.json"
        data = {"text": "hello, yangkk!"}
        write_json(file, data)

        json = read_json(file)
        self.assertTrue(json["text"] == data["text"])

    def test_write_json(self):
        file = "d:/output/test/test_write_json.json"
        data = {"text": "hello, yangkk!"}
        write_json(file, data)

        self.assertTrue(exists_file(file))

    def test_read_csv(self):
        file = "d:/output/test/test_read_csv.csv"
        data = [
            {"Name": "Alice", "Age": 25},
            {"Name": "Bob", "Age": 30},
            {"Name": "Carol", "Age": 35},
        ]
        write_csv(file, data)

        records = read_csv(file)
        self.assertTrue(len(records) == 3)

    def test_write_csv(self):
        file = "d:/output/test/test_write_csv.csv"
        data = [
            {"Name": "Alice", "Age": 25},
            {"Name": "Bob", "Age": 30},
            {"Name": "Carol", "Age": 35},
        ]
        write_csv(file, data)

        self.assertTrue(exists_file(file))

    def test_read_excel(self):
        file = "d:/output/test/test_read_excel.xlsx"
        data = [
            {"Name": "Alice", "Age": 25},
            {"Name": "Bob", "Age": 30},
            {"Name": "Carol", "Age": 35},
        ]
        write_excel(file, data)

        records = read_excel(file)
        self.assertTrue(len(records) == 3)

    def test_write_excel(self):
        file = "d:/output/test/test_write_excel.xlsx"
        data = [
            {"Name": "Alice", "Age": 25},
            {"Name": "Bob", "Age": 30},
            {"Name": "Carol", "Age": 35},
        ]
        write_excel(file, data)
        self.assertTrue(exists_file(file))
