distance_mi = 4
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = False
if distance_mi == False:
    print("False")
elif distance_mi <= 1 and is_raining == False:
    print("True")
elif distance_mi > 1 and distance_mi <= 6 and has_bike == True :
    print("True")
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print("True")
else:
    print("False")