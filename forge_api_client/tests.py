import unittest
import requests
import urllib
import os
from . import ApiClient


class ForgeTestCase(unittest.TestCase):

    def setUp(self):
        self.client_id = os.environ["AUTODESK_FORGE_CLIENT_ID"]
        self.client_secret = os.environ["AUTODESK_FORGE_CLIENT_SECRET"]

    def test_basic(self):
        fac = ApiClient()
        fac.authClientTwoLegged(self.client_id, self.client_secret, scope="bucket:read bucket:create")
        # test = fac.createBucket("testdwg001")
        # print(test)
        buckets = fac.getBuckets()
        self.assertIn("items", buckets)
        # print(buckets)

    def test_upload_file(self):
        fac = ApiClient()
        scope = "bucket:read bucket:create data:write"
        fac.authClientTwoLegged(self.client_id, self.client_secret, scope=scope)
        put_result = fac.putObject("test02.dwg", "testdwg001", "test02.dwg")
        print(put_result.json())
        re2 = {"bucketKey": "testdwg001", "objectId": "urn:adsk.objects:os.object:testdwg001/test02.dwg",
               "objectKey": "test02.dwg", "sha1": "80b8c70df4b62ef22bbd952bbd49b371c24d98aa", "size": 154709,
               "contentType": "application/octet-stream",
               "location": "https://developer.api.autodesk.com/oss/v2/buckets/testdwg001/objects/test02.dwg"}
        re3 = {"result": "success", "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn",
               "acceptedJobs": {
                   "output": {"destination": {"region": "us"}, "formats": [{"type": "svf", "views": ["2d", "3d"]}]}}}
        kkk = {'type': 'manifest', 'hasThumbnail': 'true', 'status': 'success', 'progress': 'complete', 'region': 'US',
               'urn': 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn', 'version': '1.0',
               'derivatives': [
                   {'name': 'test02.dwg', 'hasThumbnail': 'true', 'status': 'success', 'progress': 'complete',
                    'messages': [{'type': 'warning', 'code': 'AutoCAD-MissingShxFonts', 'message': [
                        'Missing fonts\nSome missing fonts were substituted for the drawing file.\n- Please upload the composite design with the missing font files to see the original fonts in the viewer: {0}',
                        'RS9.shx, sss.shx, sss.shx, sss.shx, HZTXT.shx, hztxt.shx, hztxt10.shx']}], 'outputType': 'svf',
                    'children': [{'guid': 'cb73c076-d3cd-a725-754f-a64cd8c07648', 'type': 'resource',
                                  'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/properties.db',
                                  'role': 'Autodesk.CloudPlatform.PropertyDatabase', 'mime': 'application/autodesk-db',
                                  'status': 'success'},
                                 {'guid': '6882be48-6626-5238-d3df-94e9f0a0019d', 'type': 'geometry', 'role': '2d',
                                  'name': '2D View', 'viewableID': 'Model', 'status': 'success', 'hasThumbnail': 'true',
                                  'progress': 'complete', 'children': [
                                     {'guid': '0e103eba-2c7a-188c-b346-643f12a15521', 'type': 'resource',
                                      'mime': 'image/png', 'resolution': [100, 100], 'role': 'thumbnail',
                                      'status': 'success',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/test02-Model_100.png'},
                                     {'guid': '723878f7-ce4b-9699-a53f-7e326fee632e', 'type': 'resource',
                                      'mime': 'image/png', 'resolution': [200, 200], 'role': 'thumbnail',
                                      'status': 'success',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/test02-Model_200.png'},
                                     {'guid': '391f3a8f-344e-8cb4-8a22-83d67e2d3d91', 'type': 'resource',
                                      'mime': 'image/png', 'resolution': [400, 400], 'role': 'thumbnail',
                                      'status': 'success',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/test02-Model_400.png'},
                                     {'guid': '2bd683d0-6050-155f-b041-705daf32889f', 'type': 'resource',
                                      'mime': 'application/autodesk-f2d', 'role': 'graphics', 'status': 'success',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/7de2e6fb-ea37-02dc-09c8-a55b1a6a6425_f2d/primaryGraphics.f2d'}]},
                                 {'guid': '3bb36b05-6fb7-1fd0-3c58-d83a4e8d4042', 'type': 'geometry', 'role': '3d',
                                  'name': '3D View', 'status': 'success', 'viewableID': 'Model-3D',
                                  'progress': 'complete', 'hasThumbnail': 'true', 'children': [
                                     {'guid': 'e30bd031-d13a-a976-9153-78100829986a', 'type': 'resource',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/dwg.svf',
                                      'role': 'graphics', 'mime': 'application/autodesk-svf', 'status': 'success'},
                                     {'guid': '8d3c7e44-df45-419e-b368-3dd49066ab88', 'type': 'resource',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/dwg.svf.png01_thumb_400x400.png',
                                      'resolution': [400, 400], 'mime': 'image/png', 'role': 'thumbnail'},
                                     {'guid': 'dcfb10c2-e626-4564-a477-b1ad888cd65b', 'type': 'resource',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/dwg.svf.png01_thumb_200x200.png',
                                      'resolution': [200, 200], 'mime': 'image/png', 'role': 'thumbnail'},
                                     {'guid': 'dd49d553-7fed-4c06-b322-70559bfcdee6', 'type': 'resource',
                                      'urn': 'urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6dGVzdGR3ZzAwMS90ZXN0MDIuZHdn/output/dwg.svf.png01_thumb_100x100.png',
                                      'resolution': [100, 100], 'mime': 'image/png', 'role': 'thumbnail'}]}]}]}

        urn = re3["urn"]
        derivative_urn = kkk["direvatives"]["chilldren"][2][0]["urn"]
        out = fac.getDerivativeManifest(urn, urllib.parse.quote(derivative_urn))
