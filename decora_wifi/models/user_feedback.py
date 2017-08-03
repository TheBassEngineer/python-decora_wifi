# Leviton Cloud Services API model UserFeedback.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class UserFeedback(BaseModel):
    def __init__(self, session, model_id=None):
        super(UserFeedback, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_person_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_change_stream(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/change-stream".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_person_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_person_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_person_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_person_user_feedbacks(self, user_feedback, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_person_user_feedbacks(self, user_feedback, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback)
        return self._session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_person(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/:id/person"
        return session.call_api(api, attribs, 'get')

    def get_person_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def update_all(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/update".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/:id"
        return session.call_api(api, attribs, 'put')

    def update_by_id_person_user_feedbacks(self, user_feedback, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback)
        return self._session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/UserFeedbacks/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')
