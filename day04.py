import re
import pandas as pd
import numpy as np

file = "input04.txt"
with open(file, 'rt') as f:
    lines = f.readlines()


def lines_to_df(lines: str):
    parsed = []
    for line in lines:
        date, text = split_date_and_text(line)
        id, is_awake = parse_text(text)
        parsed.append([date, id, is_awake])
    return pd.DataFrame(parsed, columns=['date', 'id', 'is_asleep'])

def split_date_and_text(line):
    line = line[1:]  # remove starting [
    return line.split("] ")

def parse_text(text):
    if text.startswith("Guard"):
        res = re.findall(r"\d+", text)
        id = res[0]
        return (id, False)
    if text == "wakes up\n":
        return (None, False)
    if text == "falls asleep\n":
        return (None, True)
    else:
        raise ValueError(f"Parsing error for text: {text}")

def fill_ids(ids):
    first_id = ids[0]
    res = [first_id]
    current_id = first_id
    for i, id in enumerate(ids[1:]):
        if id is None:
            res.append(current_id)
        else:
            current_id = id
            res.append(current_id)
    return res


# split date and time
def split_date(date):
    return date.split(" ")

# create minutes arrays
def time2array(times, states):
    res = np.array([0]*60)
    last_index = 0
    last_state = False
    for t, s in zip(times, states):
        h, m = map(int, t.split(":"))
        if h == 0:
            if last_state:
                for i in range(last_index, m):
                    res[i] = 1
            last_state = s
            last_index = m
        else:
            pass
    return pd.Series(res)


df = lines_to_df(lines)
df = df.sort_values(by='date').reset_index(drop=True)
df['id'] = fill_ids(df['id'].values)
res = list(df['date'].apply(split_date).values)
df_aux = pd.DataFrame(res, columns=['date', 'time'])
df = pd.concat([df_aux, df.drop('date', axis=1)], axis=1)
minutes = df.groupby(['date', 'id']).apply(lambda group: time2array(group['time'].values, group['is_asleep'].values)).reset_index()
per_minute_sum = minutes.drop('date', axis=1).groupby('id').agg(sum)
total_sum = per_minute_sum.apply(sum, axis=1)

# Part 1
guard_id_1 = pd.Series.idxmax(total_sum)
max_minute_guard_1 = pd.Series.idxmax(per_minute_sum.loc[guard_id_1])
print(f"Guard 1 id: {guard_id_1}\n"
      f"Maximal minute for guard 1: {max_minute_guard_1}\n"
      f"Result 1: {int(guard_id_1)*int(max_minute_guard_1)}")

# Part 2
per_minute_sum['idxmax'] = per_minute_sum.apply(lambda x: pd.Series.idxmax(x), axis=1)
per_minute_sum['max'] = per_minute_sum.apply(lambda x: x[x['idxmax']], axis=1)
guard_id_2 = pd.Series.idxmax(per_minute_sum['max'])
max_minute_guard_2 = per_minute_sum.loc[guard_id_2]['idxmax']
print(f"Guard 2 id: {guard_id_2}\n"
      f"Maximal minute for guard 2: {max_minute_guard_2}\n"
      f"Result 2: {int(guard_id_2)*int(max_minute_guard_2)}")
