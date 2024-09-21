from decimal import Decimal
from datetime import datetime, date, timedelta


goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {
            'amount': Decimal('1'),
            'expiration_date': date(2023, 12, 9)
        }
    ],
    'Яйца': [
        {
            'amount': Decimal('2'),
            'expiration_date': date(2023, 12, 12)
        },
        {
            'amount': Decimal('3'),
            'expiration_date': date(2023, 12, 11)
        }
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date is None:
        expiration_date = None
    else:
        expiration_date = datetime.strptime(expiration_date,
                                            DATE_FORMAT).date()
    if title in items:
        list.append(items[title], {'expiration_date': expiration_date,
                                   'amount': amount})
    else:
        items[title] = []
        list.append(items[title], {
                    'expiration_date': expiration_date, 'amount': amount})


add(goods, 'Красное вино', 1, '2024-09-16')


def add_by_note(items, note):
    part = str.split(note)
    if len(part[-1].split('-')) == 3:
        expiration_date = part[-1]
        amount = Decimal(part[-2])
        title = str.join(' ', part[0:-1])
        add(items, title, amount, expiration_date)
    else:
        amount = Decimal(part[-1])
        title = str.join(' ', part[0:-1])
        add(items, title, amount)


add_by_note(goods, 'Сыр моцарелла 0.5 2024-09-16')
add_by_note(goods, 'Ветчина 0.7 2024-09-13')


def find(items, needle):
    results = []
    for item in items:
        lower_item = str.lower(item)
        lower_needle = needle.lower()
        if lower_needle in lower_item:
            list.append(results, item)
    return results


print(find(goods, 'чина'))
find(goods, 'Мо')


def amount(items, needle):
    result = find(items, needle)
    amount = Decimal(0)
    for item in result:
        for value in items[item]:
            amount += value['amount']
    return amount


amount(goods, 'Яйца')
print(amount(goods, 'Красное вино'))


def expire(items, in_advance_days=0):
    check_date = timedelta(days=in_advance_days) + date.today()
    values = {}
    {"помидоры": 5}
    for item in items:
        items[item]
        for others in items[item]:
            others['expiration_date']
            if others['expiration_date'] is None:
                continue
            if check_date >= others['expiration_date']:
                if item in values:
                    values[item] = values[item] + others['amount']
                else:
                    values[item] = others['amount']
    return list(dict.items(values))


print(expire(goods, 3))
print(expire(goods, 6))
