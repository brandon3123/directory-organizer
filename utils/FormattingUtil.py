from datetime import datetime

class FormattingUtil:

    @staticmethod
    def year_month_day_from_ct_time(ct_time):
        formatted_date = datetime.strptime(ct_time, "%a %b %d %H:%M:%S %Y")
        formatted_date = formatted_date.strftime('%Y-%m-%d')
        return formatted_date