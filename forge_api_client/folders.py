from .utils import get_request, post_request, patch_request

class Folders:

    def getFolder(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)


    def getFolderContents(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/contents' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getFolderParent(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/parent' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getFolderRefs(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/refs' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getFolderRelationshipsLinks(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/relationships/links' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getFolderRelationshipsRefs(self, project_id, folder_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/relationships/refs' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getFolderSearch(self, project_id, folder_id):

        #TODO

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/search' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def patchFolder(self, project_id, folder_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return patch_request(url, data, headers)

    def postFolder(self, project_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    def postFolderRelationshipsRefs(self, project_id, folder_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/folders/%s/relationships/refs' % (folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
