import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_dict = defaultdict()

    def process_item(self, item, spider):
        status = item['status']
        self.status_dict[status] = self.status_dict.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        datetime_format = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{datetime_format}.csv'
        downloads_dir = results_dir / file_name
        with open(downloads_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_MINIMAL)
            count_status_dict = sum(self.status_dict.values())
            writer.writerows(
                [['Статус', 'Количество'],
                 *self.status_dict.items(),
                 ['Total', count_status_dict]]
            )
