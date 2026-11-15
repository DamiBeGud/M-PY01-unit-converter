from decimal import Decimal, ROUND_HALF_UP

def convert(kind, value, source, target):
    if not value.is_finite() or abs(value)>Decimal('1000000'):
        raise ValueError('value_out_of_range')
    if kind=='temperature' and source in {'C','F'} and target in {'C','F'}:
        c=value if source=='C' else (value-32)*5/9
        if c<Decimal('-273.15'): raise ValueError('below_absolute_zero')
        result=c if target=='C' else c*9/5+32
    elif kind=='distance' and source in {'m','km'} and target in {'m','km'}:
        if value<0: raise ValueError('negative_distance')
        metres=value if source=='m' else value*1000
        result=metres if target=='m' else metres/1000
    else: raise ValueError('unsupported_units')
    return {'value':format(result.quantize(Decimal('0.000001'),rounding=ROUND_HALF_UP),'f'),'unit':target}
