# Prometheus drop high cardinality

Drop metrics that have cardinality above some number:

```
cat sample_metrics.txt | python prometheus_drop_high_cardinality.py 5
```

Input:

```
# HELP metric_name_1 Metric 1
# TYPE metric_name_1 gauge
metric_name_1{label_a="1"} 1
metric_name_1{label_a="2"} 1
metric_name_1{label_a="3"} 1
metric_name_1{label_a="4"} 1
metric_name_1{label_a="5"} 1
metric_name_1{label_a="6"} 1
metric_name_1{label_a="7"} 1
metric_name_1{label_a="8"} 1

# HELP metric_name_2 Metric 2
# TYPE metric_name_2 gauge
metric_name_2{label_b="1"} 1
metric_name_2{label_b="2"} 1
metric_name_2{label_b="3"} 1

# HELP metric_name_3 Metric 3
# TYPE metric_name_3 gauge
metric_name_3{label_a="1",label_c="1"} 1
metric_name_3{label_b="1",label_c="1"} 1
```

Output:

```
# HELP metric_name_1 Metric 1
# TYPE metric_name_1 gauge

# HELP metric_name_2 Metric 2
# TYPE metric_name_2 gauge
metric_name_2{label_b="1"} 1
metric_name_2{label_b="2"} 1
metric_name_2{label_b="3"} 1

# HELP metric_name_3 Metric 3
# TYPE metric_name_3 gauge
metric_name_3{label_b="1",label_c="1"} 1
```
