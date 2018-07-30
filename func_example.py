def get_vat(payment, percent=20):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return 'Сумма НДС: {}'.format(vat)
    except (TypeError, ValueError):
        return 'Неправильные данные'

result = get_vat(212, 20)
print(result)
