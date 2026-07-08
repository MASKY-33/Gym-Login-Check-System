from gym_management.check_in import check_in_member

while True:
    membership_request = input("Give your Membership-ID here, (or type 'stop' to stop): ")

    if membership_request == "stop":
        print("Thankyou, Bye!")
        break

    membership_result = check_in_member(membership_request)
    print(membership_result)
