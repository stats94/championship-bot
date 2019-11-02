from api_service import api_service
import config

class bot:
    api_service = api_service()
    league_id = config.league_id

    def build_table(self):
        # The standings array is wrapped in another array
        table_data = self.api_service.get_table(self.league_id)[0]

        headers = '|Pos|Team|Pl|W|D|L|Form|GD|Pts|\n:-:|:--|:-:|:-:|:-:|:-:|:--|:-:|:-:'

         # Position | Team Name | Played |     Won | Drawn | Lost | Form | GD | Points |
        teams = list(map(lambda team: '{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(team['rank'], team['teamName'], team['all']['matchsPlayed'], team['all']['win'], team['all']['draw'], team['all']['lose'],  team['forme'], team['goalsDiff'], team['points']), table_data))

        return '{}\n{}'.format(headers, '\n'.join(teams))
