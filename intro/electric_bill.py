import datetime

start_date = datetime.datetime(2025, 9, 17)
end_date = datetime.datetime(2025, 10, 17)

start_meter = 1532
end_meter = 2421

dayfare = 5
kwh = 0.76

days = (end_date - start_date).days
kwh_used = end_meter - start_meter

e_cost = kwh_used * kwh

d_cost = dayfare * days

print((e_cost + d_cost) * 1.25)