import json
import requests 
import creds 
import numpy as np

"""
    Wrapper class to access the API and get Song Details based on ID 
"""

class SongData:

    def __init__(self,CLIENT_ID,CLIENT_SECRET):
        self._CLIENT_ID = CLIENT_ID
        self._CLIENT_SECRET = CLIENT_SECRET

    """
        Get API URL
    """

    @staticmethod
    def getAPIUrl(song_id):
        return 'https://api.spotify.com/v1/audio-features/'+song_id

    def getJSONDetails(self,song_id):

        """
            Set up Authentication
        """

        AUTH_URL = 'https://accounts.spotify.com/api/token'

        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self._CLIENT_ID,
            'client_secret': self._CLIENT_SECRET,
        })

        auth_response_data = auth_response.json()
        self._ACCESS_TOKEN = auth_response_data['access_token']

        """
            Request Bearer Token
        """

        headers = {
            'Authorization': 'Bearer {token}'.format(token=self._ACCESS_TOKEN)
        }


        """
            Get Song Details by calling the API
        """

        url = self.getAPIUrl(song_id)
        return requests.get(url,headers=headers).json() 

    def getSongFeatures(self,song_id):
        
        """
            Get All Features as JSON
        """

        json_dict = self.getJSONDetails(song_id)

        """
            Extract Relevant Features
        """

        features_list = [
            json_dict["danceability"],
            json_dict["energy"],
            json_dict["instrumentalness"],
            json_dict["key"],
            json_dict["liveness"],
            json_dict["speechiness"],
            json_dict["tempo"],
            json_dict["valence"]
        ]

        features_list = [float(x) for x in features_list]

        """
            Reshape the data such that it can be fed into the model
        """

        return np.array(features_list).reshape(1,-1)








