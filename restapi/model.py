from dao import BespokeDao
import sys


class BespokeModel:

    def __init__(self, collection):
        self._id = str(collection['_id']) if '_id' in collection else None
        self.name = collection['name'] if 'name' in collection else None
        self.sweetness = collection['sweetness'] if 'sweetness' in collection else None

    @staticmethod
    def get_by_id(_id):
        try:
            dao = BespokeDao()
            item = dao.get_by_id(_id)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        item_model = BespokeModel(item) if item else None
        return item_model

    @staticmethod
    def is_existing_name(name):
        try:
            dao = BespokeDao()
            exists = dao.get_by_name(name)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        return True if exists is not None else False

    @staticmethod
    def is_existing_id(_id):
        try:
            dao = BespokeDao()
            exists = dao.check_if_id_exists(_id)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        return True if exists is not None else False

    @staticmethod
    def is_valid(_id):
        return BespokeModel.is_existing_id(_id)

    @staticmethod
    def get_all():
        try:
            dao = BespokeDao()
            items = dao.get_all()
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        model_array = []
        for i in items:
            model_array.append(BespokeModel(i))
        return model_array

    @staticmethod
    def update_item(_id, name, sweetness):
        try:
            dao = BespokeDao()
            preexisting = dao.get_by_name(name)
            if preexisting and str(preexisting['_id']) != str(_id):
                raise ValueError('New update name must be unique')
            item = dao.update_item(_id, name, sweetness)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        item_model = BespokeModel(item) if item else None
        return item_model

    @staticmethod
    def insert_item(name, sweetness):
        try:
            dao = BespokeDao()
            preexisting = dao.get_by_name(name)
            if preexisting:
                raise ValueError('New insert name must be unique')
            item = dao.insert_item(name, sweetness)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        item_model = BespokeModel(item) if item else None
        return item_model

    @staticmethod
    def delete_item(_id):
        try:
            dao = BespokeDao()
            item = dao.delete_item(_id)
        except Exception as e:
            print(e, file=sys.stderr)
            raise
        item_model = BespokeModel(item) if item else None
        return item_model
