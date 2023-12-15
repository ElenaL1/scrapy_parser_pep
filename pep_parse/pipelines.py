import datetime
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, DATE_FORMAT,
                                RESULTS_FOLDER, SUMMARY_FILE)


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_FOLDER
        self.results_dir.mkdir(exist_ok=True)

    def close_spider(self, spider):
        now = datetime.datetime.now()
        timestamp = now.strftime(DATE_FORMAT)
        filename = self.results_dir / f'{SUMMARY_FILE}_{timestamp}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.statuses.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{sum(self.statuses.values())}\n')

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
