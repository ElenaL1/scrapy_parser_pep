import csv
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
        with open(filename, 'w', newline='', encoding='utf-8') as cvsfile:
            writer = csv.DictWriter(
                cvsfile, fieldnames=['Статус', 'Количество'])
            writer.writeheader()
            for status, count in self.statuses.items():
                writer.writerow({'Статус': status, 'Количество': count})
            writer.writerow(
                {'Статус': 'Total', 'Количество': sum(self.statuses.values())})

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
