from .utils import get_request, post_request
import json

class Buckets:

    def getBuckets(self):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)


    def getBucketDetails(self, bucket_key):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/details' % bucket_key

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def createBucket(self, bucket_key, policy_key="transient", allow=None):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        if allow is not None:
            data = {
                'bucketKey': bucket_key,
                'allow': allow,
                'policyKey': policy_key
            }
        else:
            data = {
                'bucketKey': bucket_key,
                'policyKey': policy_key
            }

        return post_request(url, json.dumps(data), headers)
