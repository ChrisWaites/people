any = r'.*'
nonneg_int = r'\d+'
neg_int = r'-\d+'
int = r'-?\d+'
nonneg_float = r'\d*\.?\d+'
neg_float = r'-\d*\.?\d+'
float = r'-?\d*\.?\d+'
float_zero_to_one = r'0(\.\d+)?|1\.0'
url = r'((https?|ftp|file):\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?'
email = r'.+@.+'
phone = r'\+?(\d.*){3,}'
date = r'(0?[1-9]|[12][0-9]|3[01])([ \/\-])(0?[1-9]|1[012])\2([0-9][0-9][0-9][0-9])(([ -])([0-1]?[0-9]|2[0-3]):[0-5]?[0-9]:[0-5]?[0-9])?'
time = r'([01]?[0-9]|2[0-3]):[0-5][0-9]'
iso8601 = r'(?![+-]?\d{4,5}-?(?:\d{2}|W\d{2})T)(?:|(\d{4}|[+-]\d{5})-?(?:|(0\d|1[0-2])(?:|-?([0-2]\d|3[0-1]))|([0-2]\d{2}|3[0-5]\d|36[0-6])|W([0-4]\d|5[0-3])(?:|-?([1-7])))(?:(?!\d)|T(?=\d)))(?:|([01]\d|2[0-4])(?:|:?([0-5]\d)(?:|:?([0-5]\d)(?:|\.(\d{3})))(?:|[zZ]|([+-](?:[01]\d|2[0-4]))(?:|:?([0-5]\d)))))'

def union(*choices):
    return r'({})'.format('|'.join(choices))

def csv(*choices):
    return r'{}'.format(' *, *'.join(choices))

