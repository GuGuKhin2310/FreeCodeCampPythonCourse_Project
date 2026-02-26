distance_mi = 50
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    if is_raining and not has_bike:
        print(False)
    elif not is_raining and not has_bike:
        print(False)
    else:
        print(True)

else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)