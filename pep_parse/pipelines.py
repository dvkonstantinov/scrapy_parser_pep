from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__name__).absolute().parent


class PepParsePipeline:
    count_peps = {
        'Active': 0,
        'Accepted': 0,
        'Deferred': 0,
        'Final': 0,
        'Provisional': 0,
        'Rejected': 0,
        'Superseded': 0,
        'Withdrawn': 0,
        'Draft': 0,
    }
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
        if item['status'] in self.count_peps:
            self.count_peps[item['status']] += 1
            self.total_count += 1
        return item

    def close_spider(self, spider):
        file = self.get_file()
        with open(file, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for k, v in self.count_peps.items():
                f.write(f'{k},{v}\n')
            f.write(f'Total,{self.total_count}\n')
