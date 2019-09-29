from werkzeug.datastructures import ImmutableMultiDict

imd = ImmutableMultiDict([('address', u'US'), ('address', 'US'), ('address', 'UK')])

print(imd.getlist('address'))
print(list(imd))