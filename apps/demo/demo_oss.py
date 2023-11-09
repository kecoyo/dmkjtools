import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# 使用环境变量中获取的RAM用户的访问密钥配置访问凭证。
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())

# 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称，例如examplebucket。
bucket = oss2.Bucket(auth, "https://oss-cn-beijing.aliyuncs.com", "file-im")

# 获取Bucket相关信息。
bucket_info = bucket.get_bucket_info()
# 获取Bucket名称。
print("name: " + bucket_info.name)
# 获取Bucket存储类型。
print("storage class: " + bucket_info.storage_class)
# 获取Bucket创建时间。
print("creation date: " + bucket_info.creation_date)
# 获取Bucket内网Endpoint。
print("intranet_endpoint: " + bucket_info.intranet_endpoint)
# 获取Bucket外网Endpoint。
print("extranet_endpoint " + bucket_info.extranet_endpoint)
# 获取拥有者信息。
print("owner: " + bucket_info.owner.id)
# 获取Bucket读写权限ACL。
print("grant: " + bucket_info.acl.grant)
# 获取容灾类型。
print("data_redundancy_type:" + bucket_info.data_redundancy_type)
# 获取Bucket的访问跟踪状态。仅Python SDK 2.16.1及以上版本支持获取访问跟踪状态。
print("access_monitor:" + bucket_info.access_monitor)

# 列举fun文件夹下的所有文件，包括子目录下的文件。
for obj in oss2.ObjectIterator(bucket, prefix="app_res/activity/"):
    print(obj.key)
