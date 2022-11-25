from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


# В проекте должна быть версия scrapy 2.5.1, а не последняя. Из за этого
# первая строка файла не умеет выводить наименования столбцов из словаря,
# чего требует описание задания.
# Строка 'fields': {'number': 'Номер', 'name': 'Название', 'status': 'Статус'}
# не подходит, не проходят тесты. Пришлось колхозить
# Вот 2 ссылки на разные файлы
# https://docs.scrapy.org/en/2.5/topics/exporters.html#scrapy.exporters.BaseItemExporter.fields_to_export
# https://docs.scrapy.org/en/latest/topics/exporters.html#scrapy.exporters.BaseItemExporter.fields_to_export

class CustomCsvItemExporter(CsvItemExporter):
    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                self.fields_to_export = ItemAdapter(item).field_names()
            row = ['Номер', 'Название', 'Статус']
            self.csv_writer.writerow(row)
