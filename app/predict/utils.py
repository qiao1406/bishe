import datetime


def parse_date(s):
    s1, s2 = s.split('T')
    i = s2.find(':')
    return s1 + ' ' + s2[:i + 1] + '00:00'


def gen_date_range(sd, ed):
    fmt = '%Y-%m-%d %H:%M:%S'
    sd_obj, ed_obj = datetime.datetime.strptime(sd, fmt), datetime.datetime.strptime(ed, fmt)
    date_range = []
    d = sd_obj
    while d <= ed_obj:
        date_range.append(d.strftime(fmt))
        d += datetime.timedelta(hours=1)
    return date_range
