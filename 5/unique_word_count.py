import hyperloglog as HLL
import sys

hll = HLL.HyperLogLog(0.01)
actual_count = 0

for line in sys.stdin:

    words = list(map(str, line.split(' ')))
    lower_case_words = list(map(lambda x: x.lower(), words))
    
    for word in lower_case_words:
        hll.add(word)

    approx_count = len(hll)
    actual_count += len(set(lower_case_words))

    print("\n[INFO]. Actual Count     : ", actual_count)
    print("[INFO]. Approx Count     : ", approx_count)
    print("[INFO]. Error Percentage : {}%".format(((actual_count - approx_count) * 100 / actual_count)))