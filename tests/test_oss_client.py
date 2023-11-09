import unittest

from common.oss_client import *

endpoint = "https://oss-cn-beijing.aliyuncs.com"
bucket_name = "file-im"


class TestOssClient(unittest.TestCase):
    def test_object_exists(self):
        oss_client = OssClient(endpoint, bucket_name)

        self.assertTrue(oss_client.object_exists("app_res/test/1.png") == True)
        self.assertTrue(oss_client.object_exists("app_res/test/2.png") == False)

    def test_object_list(self):
        oss_client = OssClient(endpoint, bucket_name)

        list = oss_client.list_object(prefix="app_res/")
        print(list)
        self.assertTrue(len(list) > 0)

    def test_delete_object(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.delete_object("app_res/test/imgs")
        self.assertTrue(ret == 204)

    def test_delete_objects(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.delete_objects(
            [
                "app_res/test/imgs/1.png",
                "app_res/test/imgs/1.png",
                "app_res/test/imgs/1.png",
            ]
        )
        self.assertTrue(ret == 200)

    def test_put_object(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.put_object(
            "app_res/test/imgs/2.txt", "D:\\activity_certs\\imgs\\KJ0019.png"
        )
        self.assertTrue(ret == 200)

    def test_put_file(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.put_file(
            "app_res/test/imgs/1.png", "D:\\activity_certs\\imgs\\KJ0019.png"
        )
        self.assertTrue(ret == 200)

    def test_download_file(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.download_file(
            "app_res/test/imgs/1.png", "D:\\activity_certs\\imgs\\2.png"
        )
        self.assertTrue(ret == 200)

    def test_copy_object(self):
        oss_client = OssClient(endpoint, bucket_name)

        headers = {"x-oss-storage-class": oss2.BUCKET_STORAGE_CLASS_STANDARD}
        ret = oss_client.copy_object(
            "file-im",
            "app_res/test/imgs/2.png",
            "app_res/test/imgs/1.png",
            headers=headers,
        )
        self.assertTrue(ret == 200)

    def test_archive_object(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.archive_object("app_res/test/imgs/1.png")
        self.assertTrue(ret == 200)

    def test_restore_object(self):
        oss_client = OssClient(endpoint, bucket_name)

        ret = oss_client.restore_object("app_res/test/imgs/1.png")
        self.assertTrue(ret == 200)
