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
            item_model = BespokeModel(item)
            return item_model  if item else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def is_existing_id(_id):
        try:
            dao = BespokeDao()
            exists = dao.check_if_id_exists(_id)
            return True if exists is not None else False
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def is_valid(_id):
        try:
            return BespokeModel.is_existing_id(_id)
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    #TODO this
    @staticmethod
    def get_all():
        try:
            dao = BespokeDao()
            items = dao.get_all()
            model_array = []
            for i in items:
                model_array.append(BespokeModel(i))
            return model_array
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    # TODO: too much logic here, the model simply tells the dao to update a record and return an instance of itself
    # TODO: the dao will handle how the update needs to happen depending on the data source it is using
    @staticmethod
    def update_item(_id, sweetness):
        try:
            dao = BespokeDao()
            item = dao.update_item(_id, sweetness)
            item_model = BespokeModel(item) if item else None
            return item_model
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    # TODO: too much logic with these "check and do something" methods, simply call the dao to create a new record
    # TODO: and then either return an instance of itself, or None
    @staticmethod
    def insert_item(name, sweetness):
        dao = BespokeDao()
        item = dao.insert_item(name, sweetness)
        item_model = BespokeModel(item) if item else None
        return item_model

    # TODO: too much logic with these "check and do something" methods, simply call the dao to delete a record
    # TODO: and then either return an acknowledgment, or None
    @staticmethod
    def delete_item(name):
        dao = BespokeDao()
        if dao.check_if_exists(name):
            output = dao.delete_item(name)
        else:
            output = {'error': "Cannot perform DELETE request on non-existent entry"}
        return output
