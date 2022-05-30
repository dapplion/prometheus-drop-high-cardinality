import re
import sys

# Usage:
# ```
# cat sample_metrics.txt | python prometheus_drop_high_cardinality.py 5
# ```

MAX_VALUES_PER_LABEL = int(sys.argv[1])
input_lines = sys.stdin.readlines()


label_values_by_name = {}
lines_with_label_by_name = {}

for line_num, line in enumerate(input_lines):
  m = re.search("{(.+)}", line)
  if m:
    for label in m.group(1).split(","):
      m2 = re.search("(.+)=\"(.+)\"", label)
      label_name = m2.group(1)
      label_value = m2.group(2)

      if label_name in label_values_by_name:
        label_values_by_name[label_name].add(label_value)
      else:
        label_values_by_name[label_name] = set()
        label_values_by_name[label_name].add(label_value)

      if label_name in lines_with_label_by_name:
        lines_with_label_by_name[label_name].add(line_num)
      else:
        lines_with_label_by_name[label_name] = set()
        lines_with_label_by_name[label_name].add(line_num)

lines_to_drop = set()

for [label_name, label_values] in label_values_by_name.items():
  if len(label_values) > MAX_VALUES_PER_LABEL:
    for line_num in lines_with_label_by_name[label_name]:
      lines_to_drop.add(line_num)

out_lines = []

for x in range(len(input_lines)):
  if x not in lines_to_drop:
    out_lines.append(input_lines[x])

print("".join(out_lines))
