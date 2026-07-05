# Learning "file handling" (.txt)


active_members = {
    101 : "Lauren",
    103 : "Sarah",
    105 : "Zack"
}

def check_in_member(member_id):

    try:
        id_number = int(member_id)

        if id_number in active_members:
            active_members[id_number]

            with open("visitors_log.txt", "a") as file:
                file.write(f"ID: {id_number} | name: {active_members[id_number]} has entered. \n")
                return "Access granted! Welcome."
        else:
            return "Access denied: Unknown ID."
    except ValueError:
        return "Error: Only numbers are acceptable!"
    except IOError:
        return "System error: visitor could not be saved!"
