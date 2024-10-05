import csv

class extractor:
    def __init__(self, path: str, file: str):
        self.path = path
        self.file = file

    def _extract(self) -> tuple[list[str], list[str]]:
        open_file = open(self.path + self.file, 'r')
        data = open_file.read()

        lines = data.strip().split("\n")

        headers = None
        rows = []

        for line in lines:
            columns = line.split()

            if(len(columns) == 0):
                continue

            if len(columns) > 0 and columns[0] == "iter":
                if headers is None:
                    headers = columns
            else:
                if headers and len(columns) - 1 == len(headers):
                    rows.append(columns[0:len(headers)])

        return headers, rows

    def _save_to_csv(self, data: list[str], headers: list, new_path: str, new_file: str) -> str:
        if len(data) == 0:
            return None

        with open(new_path + new_file, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        return new_path + new_file

    def process(self, new_path: str, new_file: str):
        headers, data = self._extract()
        return self._save_to_csv(data, headers, new_path, new_file)