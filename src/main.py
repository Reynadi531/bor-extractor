import tabula
import os
from datetime import date
import requests


class Extarctor:
    def __init__(self):
        self.extractor()

    def extractor(self):
        file_path = self.downloader()
        if file_path == None:
            return print("Data still unavailable")
        else:
            self.parser()

    def parser(self):
        tables = tabula.read_pdf(self.filename, pages="all")
        folder_name = "tables"
        counter = 0
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        for i, table in enumerate(tables, start=1):
            table.to_csv(os.path.join(folder_name, f"table_{i}.csv"), index=False)
            counter = i
        return print(f"Done {counter} tables")

    def downloader(self):
        datenow = self.dateparser()
        self.filename = f"BOR-RS-{datenow}.pdf"
        url = f"https://www.kemkes.go.id/downloads/resources/download/Ketersediaan-Tempat-Tidur-RS-Covid19/{self.filename}"
        r = requests.get(url)
        if not r.headers["content-type"] == "application/pdf":
            return None
        else:
            with open(self.filename, 'wb') as f:
                f.write(r.content)  
                return self.filename

        
    def dateparser(self):
        today = date.today()
        datenow = today.strftime("%d") if  "DATE" not in os.environ or len(os.environ["DATE"]) == 0 else os.environ["DATE"].zfill(2)
        monthnow = today.strftime("%m") if "MONTH" not in os.environ or len(os.environ["MONTH"]) == 0 else os.environ["MONTH"].zfill(2)
        yearnow = today.strftime("%Y") if "YEAR" not in os.environ or len(os.environ["YEAR"]) == 0 else os.environ["YEAR"]

        if int(datenow) > 31 or int(datenow) == 0: raise ValueError("Invalid date")
        if int(monthnow) > 12 or int(monthnow) == 0: raise ValueError("Invalid month")
        if int(yearnow) < 2020 or int(monthnow) == 0 : raise ValueError("Invalid year")

        bulan = {
            "01": "Januari",
            "02": "Februari",
            "03": "Maret",
            "04": "April",
            "05": "Mei",
            "06": "Juni",
            "07": "Juli",
            "08": "Agustus",
            "09": "September",
            "10": "Oktober",
            "11": "November",
            "12": "Desember"
        }

        bulannow = bulan[monthnow].upper()
        parseddate = f"{datenow}-{bulannow}-{yearnow}"
        return parseddate

if __name__ == "__main__":
    Extarctor()
