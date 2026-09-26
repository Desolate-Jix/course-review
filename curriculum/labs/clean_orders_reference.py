"""Reference solution; read after attempting PY03 independently."""
import csv
from pathlib import Path

def clean_orders(rows, user_ids):
    seen = {}
    rejected = []
    duplicates = []
    for line, raw in enumerate(rows, start=2):
        try:
            row = {key: int(raw[key].strip()) for key in ('id', 'user_id', 'amount')}
            row['status'] = raw['status'].strip()
        except (KeyError, AttributeError, ValueError, TypeError):
            rejected.append((line, 'invalid field or integer'))
            continue
        if row['amount'] < 0:
            rejected.append((line, 'negative amount'))
        elif row['user_id'] not in user_ids:
            rejected.append((line, 'unknown user'))
        elif row['status'] not in {'paid', 'pending', 'cancelled'}:
            rejected.append((line, 'invalid status'))
        elif row['id'] in seen:
            if row == seen[row['id']]:
                duplicates.append(line)
            else:
                rejected.append((line, 'conflicting id'))
        else:
            seen[row['id']] = row
    return sorted(seen.values(), key=lambda row: row['id']), rejected, duplicates

if __name__ == '__main__':
    with Path(__file__).with_name('dirty_orders.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    clean, rejected, duplicates = clean_orders(rows, {1,2,3,4})
    print({'input': len(rows), 'clean': len(clean), 'rejected': len(rejected), 'duplicates': len(duplicates)})
    print('ids:', [row['id'] for row in clean])
    print('all_total:', sum(row['amount'] for row in clean))
    print('paid_total:', sum(row['amount'] for row in clean if row['status'] == 'paid'))
    print('reasons:', rejected)
