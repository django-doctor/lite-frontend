from shared.seed_data.seed_data_classes.seed_class import SeedClass
from shared.seed_data.make_requests import make_request


class SeedCase(SeedClass):
    def assign_case_to_queue(self, case_id=None, queue_id=None):
        self.log("assigning case to queue: ...")
        queue_id = self.context['queue_id'] if queue_id is None else queue_id
        case_id = self.context['case_id'] if case_id is None else case_id
        data = {'queues': [queue_id]}
        make_request("PUT", base_url=self.base_url, url='/cases/' + case_id + '/', headers=self.gov_headers, body=data)

    def assign_test_cases_to_bin(self, bin_queue_id, new_cases_queue_id):
        self.log("assigning cases to bin: ...")
        response = make_request("GET", base_url=self.base_url, url='/queues/' + new_cases_queue_id + '/', headers=self.gov_headers)
        queue = response.json()['queue']
        cases = queue['cases']
        for case in cases:
            data = {'queues': [bin_queue_id]}
            make_request("PUT", base_url=self.base_url, url='/cases/' + case['id'] + '/', headers=self.gov_headers, body=data)

    def add_case_note(self, context, case_id):
        self.log('Creating case note: ...')
        data = self.request_data['case_note']
        context.case_note_text = self.request_data['case_note']['text']
        make_request("POST", base_url=self.base_url, url='/cases/' + case_id + '/case-notes/', headers=self.gov_headers, body=data)  # noqa
