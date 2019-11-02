import requests;
import config;

class api_service:
    endpoint = config.endpoint
    api_key = config.api_key

    def get(self, url):
        response = requests.get(url, headers={'X-RapidAPI-Key': self.api_key})
        
        '''
        api element is just a wrapper.
        
        api: {
            results: 0 -> Number of results
            fixtures/standing etc: [] -> array with data
        }
        '''
        json = response.json()
        return json['api']

    def get_table(self, league_id):
        url = '{}/v2/leagueTable/{}'.format(self.endpoint, league_id)
        response = self.get(url)
        return response['standings']
