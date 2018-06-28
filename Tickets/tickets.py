# coding: utf-8
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
import requests
from prettytable import PrettyTable
from colorama import Fore
from stations import stations


def cli():
    # """command-line interface"""
    arguments = docopt(__doc__,version='ticket 1.0')
    from_station = stations.get_telecode(arguments.get('<from>'))
    to_station = stations.get_telecode(arguments.get('<to>'))
    date = arguments.get('<date>')
    # print(arguments)
    options = ''.join([key for key,value in arguments.items() if value is True])
    print(options)

    url = ('http://kyfw.12306.cn/otn/leftTickert/query?'
            'leftTicketDTO.train_date={}&'
            'leftTicketDTO.from_station={}&'
            'leftTicketDTO.to_station={}&'
            'purpose_codes=ADULT').format(date,from_station,to_station)
    r = requests.get(url, verify=False)

    raw_trains = r.json()['data']['result']
    pt = PrettyTable()
    pt._set_field_names("车次 车站 时间 经历时 一等座 二等座 软卧 硬卧 硬座 无座".split())
    for raw_trains in raw_trains:
        data_list = raw_trains.split("|")
        train_no = data_list[3]
        initial = train_no[0].lower()

        # print(train_no[0])
        if not options or initial in options:
            from_station_code = data_list[6]
            to_station_code = data_list[7]
            from_station_name = ''
            to_station_name = ''
            start_time = data_list[8]
            arrive_time = data_list[9]
            time_duration = data_list[10]
            first_class_seat = data_list[31] or "--"
            second_class_seat = data_list[30] or "--"
            soft_sleep = data_list[23] or "--"
            hard_sleep = data_list[28] or "--"
            hard_seat = data_list[29] or "--"
            no_seat = data_list[33] or "--"
        pt.add_row([
            train_no,
            '\n'.join([Fore.GREEN + stations.get_name(from_station_code) + Fore.RESET, Fore.RED + stations.get_name(to_station_code) +  Fore.RESET]),
            '\n'.join([Fore.GREEN + start_time + Fore.RESET,Fore.RED + arrive_time +  Fore.RESET]),
            time_duration,
            first_class_seat,
            second_class_seat,
            soft_sleep,
            hard_sleep,
            hard_seat,
            no_seat
        ])
    print(pt)
if __name__ == '__main__':
    cli()
