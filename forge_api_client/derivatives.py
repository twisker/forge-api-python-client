from .utils import get_request, post_request, delete_request

class Derivatives:

    def getFormats(self):

        url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/formats'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def translate(self, data):

        url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/job'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return post_request(url, data, headers)

    def postReferences(self, urn, data):

        url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/references' % urn

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return post_request(url, data, headers)

    def getThumbnail(self, urn, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/thumbnail' % urn

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/thumbnail' % urn

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getManifest(self, urn, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/manifest' % urn

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/manifest' % urn

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def deleteManifest(self, urn, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/manifest' % urn

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/manifest' % urn

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return delete_request(url, headers)

    def getDerivativeManifest(self, urn, derivative_urn, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/manifest/%s' % (urn, derivative_urn)

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/manifest/%s' % (urn, derivative_urn)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getMetadata(self, urn, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/metadata' % urn

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/metadata' % urn

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getModelviewMetadata(self, urn, guid, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/metadata/%s' % (urn, guid)

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/metadata/%s' % (urn, guid)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getModelviewProperties(self, urn, guid, region='US'):

        if region == 'US':

            url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/%s/metadata/%s/properties' % (urn, guid)

        else:

            url = 'https://developer.api.autodesk.com/modelderivative/v2/regions/eu/designdata/%s/metadata/%s/properties' % (urn, guid)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)
