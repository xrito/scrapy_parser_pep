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
        file_name = f'status_summary_{now.strftime(DATETIME_FORMAT)}.csv'
        downloads_dir = results_dir / file_name
        count_status_dict = sum(self.status_dict.values())
        with open(downloads_dir, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, summ in self.status_dict.items():
                f.write(f'{status},{summ}\n')
            f.write(f'Total,{count_status_dict}\n')
