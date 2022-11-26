import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__name__).absolute().parent


class PepParsePipeline:
    count_peps = {}
    total_count = 0

    @staticmethod
    def get_file():
        filename = ('status_summary_' + str(datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S")) + '.csv')
        result_dir = BASE_DIR / 'results'
        file = result_dir / filename
        return file

    def open_spider(self, spider):
        # тесты требуют, чтоб это было здесь
        pass

    def process_item(self, item, spider):
        self.count_peps[item['status']] = self.count_peps.get(
            item['status'], 0) + 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        file = self.get_file()
        with open(file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.count_peps.items())
            writer.writerow(['Total', self.total_count])
