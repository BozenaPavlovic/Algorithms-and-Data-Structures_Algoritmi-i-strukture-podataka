def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = len(arr)

    # Određivanje raspona vrednosti u nizu
    min_val = min(arr)
    max_val = max(arr)

    # Izbegavanje deljenja nulom
    range_val = (max_val - min_val) / bucket_count
    if range_val == 0:
        return arr

    # Kreiranje bucket-a
    buckets = [[] for _ in range(bucket_count)]

    # Raspodela elemenata u bucket-e
    for num in arr:
        index = int((num - min_val) / range_val)
        if index == bucket_count:  # ivicni slučaj za max element
            index -= 1
        buckets[index].append(num)

    for i, bucket in enumerate(buckets):
        print(f"Bucket {i}: {bucket}")

    # Sortiranje svakog bucket-a i spajanje
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr
