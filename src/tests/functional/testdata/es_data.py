import uuid
import datetime

es_data = [{
        'id': str(uuid.uuid4()),
        'imdb_rating': 8.5,
        'genres': [{'id': str(uuid.uuid4()), 'name': 'Action'}],
        'title': 'The Star',
        'description': 'New World',
        'actors_names': 'Ann',
        'writers_names': 'Ben',
        'directors': [
            {'id': str(uuid.uuid4()), 'name': 'Ann'},
            {'id': str(uuid.uuid4()), 'name': 'Bob'}
        ],
        'actors': [
            {'id': str(uuid.uuid4()), 'name': 'Ann'},
            {'id': str(uuid.uuid4()), 'name': 'Bob'}
        ],
        'writers': [
            {'id': str(uuid.uuid4()), 'name': 'Ben'},
            {'id': str(uuid.uuid4()), 'name': 'Howard'}
        ],
        'creation_date': datetime.datetime.now().isoformat(),

        'type': 'type',
        'genres_names': 'genres_names',
        'directors_names': 'directors_names',

    } for _ in range(60)]
