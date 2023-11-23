"""
阿里云OSS客户端
"""
import os
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

from common.fs import ensure_dir


class OssClient:
    """阿里云OSS客户端"""

    def __init__(self, endpoint, bucket_name, **kwargs) -> None:
        # 使用环境变量中获取的RAM用户的访问密钥配置访问凭证。
        self.auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())

        # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        self.service = oss2.Service(self.auth, endpoint)

        # 填写Bucket名称，例如examplebucket。
        self.bucket = oss2.Bucket(self.auth, endpoint, bucket_name, **kwargs)

    def list_bucket(self):
        """
        列出所有的Bucket
        """
        return list(oss2.BucketIterator(self.service))

    def object_exists(self, key, **kwargs):
        """
        检查文件是否存在

        #:param key: 文件名
        #:returns 返回值为true表示文件存在，false表示文件不存在。
        """
        exists = self.bucket.object_exists(key, **kwargs)
        return exists

    def list_object(self, prefix="", delimiter="", marker="", max_keys=100):
        """
        列举指定目录下的文件和子目录，通过obj.is_prefix方法判断obj是否为文件夹。

        :param prefix: 只列举匹配该前缀的文件
        :param delimiter: 目录分隔符，'/'：不列举子文件夹下的文件。
        :param marker: 分页符
        :param max_keys: 每次调用 `list_objects` 时的max_keys参数。注意迭代器返回的数目可能会大于该值。
        """
        return list(
            oss2.ObjectIterator(
                self.bucket,
                prefix=prefix,
                delimiter=delimiter,
                marker=marker,
                max_keys=max_keys,
            )
        )

    def delete_object(self, key, **kwargs):
        """
        删除单个文件

        :param str key: 文件名
        :returns 返回状态码，不管文件存在不存在，都返回204
        """
        ret = self.bucket.delete_object(key, **kwargs)
        return ret.status

    def delete_objects(self, key_list, **kwargs):
        """
        删除多个文件

        :param key_list: 文件名列表，不能为空。
        :type key_list: list of str

        :returns 返回状态码，不管文件存在不存在，都返回200
        """
        ret = self.bucket.batch_delete_objects(key_list, **kwargs)
        return ret.status

    def put_object(self, key, data, **kwargs):
        """上传一个普通文件。

        :param key: 上传到OSS的文件名

        :param data: 待上传的内容。
        :type data: bytes，str或file-like object

        :returns 返回状态码
        """
        ret = self.bucket.put_object(key, data, **kwargs)
        return ret.status

    def put_file(self, key, filename, **kwargs):
        """上传一个本地文件到OSS的普通文件。

        :param str key: 上传到OSS的文件名
        :param str filename: 本地文件名，需要有可读权限

        :returns 返回状态码
        """
        ret = self.bucket.put_object_from_file(key, filename, **kwargs)
        return ret.status

    def download_file(self, key, filename, **kwargs):
        """下载一个文件到本地文件。

        :param key: 文件名
        :param filename: 本地文件名。要求父目录已经存在，且有写权限。

        :return: 如果文件不存在，则抛出 :class:`NoSuchKey <oss2.exceptions.NoSuchKey>` ；还可能抛出其他异常
        """
        ensure_dir(os.path.dirname(filename))
        ret = self.bucket.get_object_to_file(key, filename, **kwargs)
        return ret.status

    def copy_object(self, source_bucket_name, source_key, target_key, **kwargs):
        """
        拷贝一个文件到当前Bucket。

        :param str source_bucket_name: 源Bucket名
        :param str source_key: 源文件名
        :param str target_key: 目标文件名
        :param dict params: 请求参数

        :param headers: HTTP头部
        :type headers: 可以是dict，建议是oss2.CaseInsensitiveDict

        :return: :class:`PutObjectResult <oss2.models.PutObjectResult>`
        """

        # # 通过添加存储类型Header，将Object存储类型转换为标准类型。
        # headers = {'x-oss-storage-class': oss2.BUCKET_STORAGE_CLASS_STANDARD}
        # # 通过添加存储类型Header，将Object存储类型转换为低频访问类型。
        # # headers = {'x-oss-storage-class': oss2.BUCKET_STORAGE_CLASS_IA}
        oss2.BUCKET_STORAGE_CLASS_IA

        ret = self.bucket.copy_object(source_bucket_name, source_key, target_key, **kwargs)
        return ret.status

    def archive_object(self, key):
        """
        归档Object

        :param str key: object name
        """
        headers = {"x-oss-storage-class": oss2.BUCKET_STORAGE_CLASS_ARCHIVE}
        ret = self.bucket.copy_object(self.bucket.bucket_name, key, key, headers=headers)
        return ret.status

    def restore_object(self, key, **kwargs):
        """
        解冻归档Object

        :param str key: object name
        """
        ret = self.bucket.restore_object(key, **kwargs)
        return ret.status


# 默认OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), os.getenv("OSS_BUCKET"))
